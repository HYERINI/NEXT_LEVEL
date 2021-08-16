from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login/index.php'
class2021_url = 'https://ecampus.smu.ac.kr/local/ubion/user/?year=2021&semester=10'

user_info = {
    'username':'202010904',
    'password':'lj74973186@@@'
}

with requests.Session() as s:
    request = s.post(login_url, data = user_info)
    request2 = s.post(class2021_url, data = user_info)
    if (request.status_code == 200):
        bs = BeautifulSoup(request2.text, 'html.parser')

lectures = bs.select('#region-main > div > div > div.course_lists > div > table > tbody > tr > td > div > a')

class_list = []
for lecture in lectures:
    class_list.append(str(lecture))
lst = []
for i in class_list:
    index = i.find('id')
    lst.append(int(i[index+3:index+8]))
print(lst)