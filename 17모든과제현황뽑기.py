import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'
class1_url = 'https://ecampus.smu.ac.kr/mod/assign/index.php?id=60021'
url_lst_assign = []

user_info = {
    'username':'아이디',
    'password':'비번'
}

with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(class1_url, data = user_info)
    request3 = s.post(class2021_url, data = user_info)

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
            # print("현재까지 업로드 된 과제 수:" +  size + '\n')
            for i in range(0, size): 
                print('과제 제목 : ' + assignment_name_lst[i], '\n과제 현황 : ' + assignment_rate_lst[i])
                print('마감 기한 : ' + assignment_close_lst[i] + '\n')
        




