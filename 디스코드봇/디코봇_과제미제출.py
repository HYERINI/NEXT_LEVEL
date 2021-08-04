import asyncio
import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

token = '해당봇의 토큰'

# 봇 로그인
@client.event
async def on_ready():
    print('다음으로 로그인합니다.')
    print(client.user.name)
    print(client.user.id)
    print('=======================')

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == '!안녕':
        channel = message.channel
        await channel.send('안녕하세요!')
    if message.content == '!설명':
        if message.author.dm_channel:
            await message.author.dm_channel.send('DM 채널이 있어서 보내봤어요')
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            await channel.send('DM 채널이 없어서 만들고 보냈어요')
    if message.content.startswith('!료그인'):
        channel = message.channel

        smu_id = message.content[5:14]
        smu_pw = message.content[15:]

        login_url = 'https://ecampus.smu.ac.kr/login/index.php'  #로그인 창 주소
        class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'  #강의 인덱스 가져오기 위한 주소
        url_lst = []
        url_lst_assign = []

        user_info = {}

        user_info['username'] = smu_id
        user_info['password'] = smu_pw

        with requests.Session() as s:
            #필요한 주소들 & selecter들 미리 설정
            request = s.post(login_url, data = user_info)
            request3 = s.post(class2021_url, data = user_info)
            source = request3.text
            soup = BeautifulSoup(source,'html.parser')
            items = soup.find_all("a", {"class", "coursefullname"})

            #강의 제목 끌어오기
            class_name_lst = []
            for name in items:
                arrange = name.get_text()
                class_name_lst.append(arrange)     

            #url에 있는 강의가 갖고 있는 id코드 크롤링하기
            if (request.status_code == 200):
                bs = BeautifulSoup(request3.text, 'html.parser')

                lectures = bs.select('#region-main > div > div > div.course_lists > div > table > tbody > tr > td > div > a')

                class_list = []
                for lecture in lectures:
                    class_list.append(str(lecture))
                lst = []
                for i in class_list:
                    index = i.find('id')
                    lst.append(int(i[index+3:index+8]))
                count = len(lst)
                for i in range(count):
                    url_lst_assign.append('https://ecampus.smu.ac.kr/mod/assign/index.php?id='+str(lst[i]))
                    url_lst.append('https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id='+str(lst[i]))


            print("--------------------미제출과제현황----------------------\n")

            if (request.status_code == 200):
                for i in range(count):
                    request4 = s.post(url_lst_assign[i])

                    bs = BeautifulSoup(request4.text, 'html.parser')
                    assignment_name = bs.find_all("td", {"class", "cell c1"})
                    assignment_rates = bs.find_all("td", {"class", "cell c3"})
                    assignment_close = bs.find_all("td", {"class", "cell c2"})

                    assignment_name_lst = []
                    for name in assignment_name:
                        assignment_name_lst.append(name.text.strip())

                    assignment_rate_lst = []
                    for rate in assignment_rates:
                        assignment_rate_lst.append(rate.text.strip())

                    assignment_close_lst = []
                    for close in assignment_close:
                        assignment_close_lst.append(close.text.strip())
                    size = len(assignment_name_lst)

                    await channel.send('-----------------------------------------------------------------------------------------\n')
                    await channel.send(class_name_lst[i] + '\n')
                    i += 1


                    absent = '미제출'
                    
                    if absent not in assignment_rate_lst:
                        await channel.send('모두 완료')
                        
                    for i in range(0, size):
                        if absent in assignment_rate_lst[i]:
                            await channel.send('과제 제목 : ' + assignment_name_lst[i])
                            await channel.send('과제 현황 : ' + assignment_rate_lst[i])
                            await channel.send('마감 기한 : ' + assignment_close_lst[i])
client.run(token)