import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {"login_user_id":"ysji86", "login_password":"eepel0524"}
boj_url = "https://www.acmicpc.net/"

with requests.Session() as sess:
    login_req = sess.post(boj_url+'signin',data=LOGIN_INFO)
    print(login_req.status_code)
    # soup = bs(sess.get(boj_url).text, 'html.parser')
    # if soup.find('a', {'class': 'username'}) is None:
    #     print("invalid login info")
    #     exit(1)
    # else:
    #     print("Login Success")