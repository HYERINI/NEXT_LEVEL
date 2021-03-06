import requests
from bs4 import BeautifulSoup as bs #beautifulsoup대신 bs 사용하겠다는 뜻

#사용자의 아이디와 비번을 data에 추출
data = {
    'username' : '아이디',
    'password' : '비번'
}

with requests.Session() as s: 
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)
    result = s.post('https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10', data=data)
    source2 = result.text
    soup = bs(source2,'html.parser')
    # print(soup)
    items = soup.find_all("a", {"class", "coursefullname"})

for i in items:
    arrange = i.get_text()
    print(arrange)
