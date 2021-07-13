import requests
from bs4 import BeautifulSoup

login_url = 'https://ecampus.smu.ac.kr/login.aspx'
crawl_url = 'https://ecampus.smu.ac.kr/local/ubion/user\Status.aspx'

login_info = {
    'UserID': '202010904',
    'UserPW': 'lj74973186'
}

with requests.Session() as ss:
    req = ss.post(login_url, data=login_info, verify=False)
    if(req.status_code == 200):
	    soup = BeautifulSoup(req.content, 'html.parser')
	    _FORM = soup.select('p')