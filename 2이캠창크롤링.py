import requests
from bs4 import BeautifulSoup as bs 

data = {
    'username' : '아이디',
    'password' : '비번'
}

with requests.Session() as s:
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)

print(request.text)

print("로그인하고 그 다음페이지 html까지 크롤링된듯")