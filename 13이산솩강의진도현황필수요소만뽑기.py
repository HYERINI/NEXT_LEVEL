import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'
class1_url = 'https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id=60021'
lecutre_main = 'https://ecampus.smu.ac.kr/course/view.php?id=60021'

user_info = {
    'username':'아이디',
    'password':'비번'
}

with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(class1_url, data = user_info)
    if (request.status_code == 200):
        bs = BeautifulSoup(request2.text, 'html.parser')
        lecture_name = bs.find_all("td", {"class", "text-left"})
        rates = bs.find_all("td", {"class", "text-center"})

    name_lst = []
    for name in lecture_name:
        name_lst.append(name.text.strip())
    name_lst = name_lst[3:]

    rate_list = []
    for rate in rates:
        rate_list.append(str(rate.text))

    a_li = []
    for word in rate_list:
        if '%' in word:
            a_li.append(word)

    size = len(name_lst)
    print("현재까지 업로드 된 강의 수:", size)
    for i in range(0, size): {
        print('강의 제목 : ' + name_lst[i], '-> 강의 진도율 : ' + a_li[i])
    }
