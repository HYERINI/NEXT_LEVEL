import requests
from bs4 import BeautifulSoup

login_html = 'https://ecampus.smu.ac.kr'  #로그인창 주소
crawl_html = 'https://ecampus.smu.ac.kr/login/index.php'  #크롤링할 주소

session_data = requests.session()

params=dict()
params['username'] = '여기에이캠아이디입력'
params['password'] = '여기에이캠비밀번호입력'

login = session_data.post(login_html, data=params)
login.raise_for_status()

# print(login.headers)
# print(session_data.cookies.get_dict())

logins = session_data.get(crawl_html)
soup = BeautifulSoup(logins.content, 'html.parser')
# print(soup)
data = soup.select('#region-main > div > div > div > div.col-loginbox > div:nth-child(1) > div.col-login.col-login-person > form > div.textform')
for item in data : 
    print('아이디와 비번의 html부분 출력')
    print(item)

print('\n문제점: 크롤링할 주소를 아무리 바꿔도 첫 로그인 화면의 html만 크롤링된다')