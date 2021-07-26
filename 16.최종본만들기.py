from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'
url_lst_video = []  #강의 진도 현황 있는 페이지
url_lst_assign = []  #과제 제출 현황 있는 페이지

user_info = {
    'username':'202010869',
    'password':'gusqls96%%!!'
}
total_name = []
with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(class2021_url, data = user_info)
    if (request.status_code == 200):
        bs = BeautifulSoup(request2.text, 'html.parser')

        lectures = bs.select('#region-main > div > div > div.course_lists > div > table > tbody > tr > td > div > a')

        class_list = []
        for lecture in lectures:
            class_list.append(str(lecture))
        lst = []
        for i in class_list:
            index = i.find('id')
            lst.append(int(i[index+3:index+8]))
        #print(lst)
        count = len(lst)
        for i in range(count):
            url_lst_video.append('https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id='+str(lst[i]))
            url_lst_assign.append('https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id='+str(lst[i]))

            
    if (request2.status_code == 200):
        for i in range(count):
            request3 = s.post(url_lst_video[i])
            name_lst = []
            bs  = BeautifulSoup(request3.text, 'html.parser')
            lecture_name = bs.select('#ubcompletion-progress-wrapper > div > table.table.table-bordered.user_progress > tbody > tr > td.text-left')
            for name in lecture_name:
                name_lst.append(name.text.strip())
            total_name.append(name_lst)
