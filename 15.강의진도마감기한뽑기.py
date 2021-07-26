import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'
assginment_url = 'https://ecampus.smu.ac.kr/mod/assign/index.php?id=60021'
lecutre_main = 'https://ecampus.smu.ac.kr/course/view.php?id=60021'

user_info = {
    'username':'202010869',
    'password':'gusqls96%%!!'
}

with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(lecutre_main, data = user_info)
    if (request.status_code == 200):
        bs = BeautifulSoup(request2.text, 'html.parser')
        deadlines = bs.find_all('span', {'class', 'text-ubstrap'})


deadline_lst = []
for deadline in deadlines:
    deadline_lst.append(deadline.text)

for i in deadline_lst:
    index = i.find('~')
    print(i[index+2:])