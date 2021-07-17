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


