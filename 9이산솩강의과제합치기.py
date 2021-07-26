import requests
from bs4 import BeautifulSoup as bs #beautifulsoup대신 bs 사용하겠다는 뜻

#사용자의 아이디와 비번을 data에 추출
data = {
    'username' : '202010904',
    'password' : 'lj74973186@@'
}

#이산수학 강의 현황 출력
with requests.Session() as s:
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)
    result = s.get('https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id=60021', data=data)
    source2 = result.text
    soup = bs(source2,'html.parser')
    items = soup.find_all("table", {"class", "table table-bordered user_progress"})
for a in items : 
        arrange = a.get_text()
print(arrange)

#이산수학 과제 현황 출력
with requests.Session() as s:
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)
    result = s.get('https://ecampus.smu.ac.kr/mod/assign/index.php?id=60021', data=data)
    source2 = result.text
    soup = bs(source2,'html.parser')
data = soup.select("#region-main > div > table")
for i in data :
    arrange = i.get_text()
print(arrange)