import requests
from bs4 import BeautifulSoup

login_html = 'https://ecampus.smu.ac.kr/local/ubion/user/'
crawl_html = 'https://ecampus.smu.ac.kr/local/ubion/user/'

session_data = requests.session()

params=dict()
params['username'] = '202010904'
params['password'] = 'lj74973186'

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