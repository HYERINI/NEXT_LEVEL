import requests
from bs4 import BeautifulSoup as bs #beautifulsoup대신 bs 사용하겠다는 뜻

#사용자의 아이디와 비번을 data에 추출
data = {
    'username' : '아이디입력',
    'password' : '비번입력'
}

with requests.Session() as s:
    request = s.post('https://ecampus.smu.ac.kr/login/index.php', data=data)
    source = request.text
    soup = bs(source,'html.parser')

top_list = soup.select("#region-main > div > div.progress_courses > div.course_lists > ul > li > div > a > div.course-name > div.course-title > h3")

# print(top_list[0].text) ---> 해당 selector에서의 강의 제목부분이 top_list[0]임
print("❤당신이 듣고 있는 강의들입니다❤\n")
for top in top_list:
	print(top.text)


