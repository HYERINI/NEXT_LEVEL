import requests
from bs4 import BeautifulSoup as bs #beautifulsoup대신 bs 사용하겠다는 뜻
import openpyxl

#사용자의 아이디와 비번을 data에 추출
data = {
    'username' : '아이디입력',
    'password' : '비번입력'
}

with requests.Session() as s:
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)
    result = s.get('https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id=60021', data=data)
    source2 = result.text
    soup = bs(source2,'html.parser')
    # print(soup)
    # items = soup.find("table", {"class", "table table-bordered user_progress"})
data = soup.select('#ubcompletion-progress-wrapper > div > table > tbody > tr > td.text-center')
for i in data :
    print(i)


#엑셀로 저장하기 세팅
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "이산수학강의진도현황"
ws1.append(["제목", "현황"])

#한 페이지 내에 있는 기사 제목, url, 신문사 이름 스크래핑
for article in data:
    a_tag = article.select_one('td > tl')

    title = a_tag
    how = a_tag
    
#엑셀에 title, url, comp를 저장하기
    ws1.append([title, how])


wb.save(filename='네이버 기사 스크래핑.xlsx')