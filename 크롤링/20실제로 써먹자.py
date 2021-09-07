import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'  #로그인 창 주소
class2021_url = 'https://ecampus.smu.ac.kr/'  #강의 인덱스 가져오기 위한 주소
url_lst = []
url_lst_assign = []

user_info = {
    'username':'202010904',
    'password':'lj74973186@@@'
}

with requests.Session() as s:
    #필요한 주소들 & selecter들 미리 설정
    request = s.post(login_url, data = user_info)
    request3 = s.post(class2021_url, data = user_info)
    source = request3.text
    soup = BeautifulSoup(source,'html.parser')
    items = soup.find_all("div", {"class", "course-title"})

    #강의 제목 끌어오기
    class_name_lst = []
    for name in items:
        arrange = name.get_text()
        class_name_lst.append(arrange)     

    #url에 있는 강의가 갖고 있는 id코드 크롤링하기
    if (request.status_code == 200):
        bs = BeautifulSoup(request3.text, 'html.parser')

        lectures = bs.find_all("a", {"class", "course_link"})
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

        print("--------------------------------강의 진도 현황-------------------------------------------\n")

        #강의진도현황크롤링하기
        if (request3.status_code == 200):
            value_lst = []
            for i in range(count):
                request3 = s.post(url_lst[i])
                name_lst = []
                rate_list = []
                a_li = []
                bs  = BeautifulSoup(request3.text, 'html.parser')
                lecture_name = bs.find_all("td", {"class", "text-left"})
                rates = bs.find_all("td", {"class", "text-center"})

                for name in lecture_name:
                    name_lst.append(name.text.strip())
                name_lst = name_lst[3:]

                for rate in rates:
                    rate_list.append(str(rate.text))

                for word in rate_list:
                    if '%' in word:
                        a_li.append(word)
                    if '-' in word:
                        a_li.append(word)
                

                size = len(a_li)

                i += 1
                absent_lst = []
                value = ''
                for i in range(0, size - 1, 1):
                    if '%' in a_li:
                        if float(a_li[i][:-1]) < 100:
                            string = name_lst[i] + '-> 진도율 : ' + a_li[i]
                            absent_lst.append(string)
                    if '-' in a_li:
                        string = name_lst[i] + ' -> 진도율 : 0% '
                        absent_lst.append(string)

                if len(absent_lst) == 0:
                    value_lst.append("모든 강의를 100% 출석하였습니다. 아주 훌륭해요!!")
                else:
                    for i in absent_lst:
                        value += (i + '\n')
                    value_lst.append(value)

                print(value_lst)
                print('-----------------------------------------------------------------------------------------\n')
 
   

    # #과제제출현황크롤링하기
    # print("--------------------------------과제 제출 현황-------------------------------------------\n")

    # if (request.status_code == 200):
    #     for i in range(count):
    #         request4 = s.post(url_lst_assign[i])

    #         bs = BeautifulSoup(request4.text, 'html.parser')
    #         assignment_name = bs.find_all("td", {"class", "cell c1"})
    #         assignment_rates = bs.find_all("td", {"class", "cell c3"})
    #         assignment_close = bs.find_all("td", {"class", "cell c2"})

    #         assignment_name_lst = []
    #         for name in assignment_name:
    #             assignment_name_lst.append(name.text.strip())

    #         assignment_rate_lst = []
    #         for rate in assignment_rates:
    #             assignment_rate_lst.append(rate.text.strip())

    #         assignment_close_lst = []
    #         for close in assignment_close:
    #             assignment_close_lst.append(close.text.strip())

    #         size = len(assignment_name_lst)
    #         print('-----------------------------------------------------------------------------------------\n')
    #         print(class_name_lst[i] + '\n')
    #         i += 1
    #         for i in range(0, size):
    #             print('과제 제목 : ' + assignment_name_lst[i], '\n과제 현황 : ' + assignment_rate_lst[i])
    #             print('마감 기한 : ' + assignment_close_lst[i] + '\n')
        

