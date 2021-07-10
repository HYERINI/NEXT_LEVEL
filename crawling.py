from typing import no_type_check
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#세션 만들기
session=requests.session()

#로그인 하는 페이지의 general-requestURL에서 url 가져옴
url="https://ecampus.smu.ac.kr/login/index.php"

#가져오고 싶은 데이터 (Form data)
data = {
    "username" : "아이디",
    "password" : "비밀번호"
}
response=session.post(url, data=data)
response.raise_for_status()

#나의강좌 접근
url="https://ecampus.smu.ac.kr/local/ubion/user/"
response=session.get(url)
response.raise_for_status()
#쉬바 모르겠어