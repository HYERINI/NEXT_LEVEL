import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'
class1_url = 'https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id=60021'

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

name_lst = []
for name in lecture_name:
    name_lst.append(name.text.strip())
print(name_lst[3:])


with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(class1_url, data = user_info)
    if (request.status_code == 200):
        bs = BeautifulSoup(request2.text, 'html.parser')

rates = bs.find_all("td", {"class", "text-center"})

rate_list = []
for rate in rates:
    rate_list.append(str(rate.text))

a_li = []
for word in rate_list:
    if '%' in word:
        a_li.append(word)
print(a_li)