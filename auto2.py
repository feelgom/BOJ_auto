import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {"login_user_id":"ysji86", "login_password":"eepel0524"}
boj_url = "https://www.acmicpc.net/"
LANG = {"C++14":88, "Python 3":28}

problem_id = 2839
language = "Python 3"
with open("2839.py", 'r') as f:
    code = f.read()

with requests.Session() as sess:
    login_req = sess.post(boj_url+'signin',data=LOGIN_INFO)
    # if login_req.status_code != 200:
    #     raise Exception('로그인이 되지 않았어요! 아이디와 비밀번호를 다시한번 확인해 주세요.')
    # else:
    #     print("로그인 성공")
    soup = bs(sess.get(boj_url).text, 'html.parser')
    if soup.find('a', {'class': 'username'}) is None:
        print("invalid login info")
        exit(1)
    else:
        print("Login Success")

    soup = bs(sess.get(boj_url + 'submit/' + str(problem_id)).text, 'html.parser')

    try:
        key = soup.find('input', {'name': 'csrf_key'})['value']
    except TypeError:
        print("Wrong problem number")
        exit(1)

    if language not in LANG:
        print("Invalid language")
        exit(1)

    data = {
        'problem_id': problem_id,
        'source': code,
        'language': LANG[language],
        'code_open': 'onlyaccepted',
        'csrf_key': key
    }

    sess.post(boj_url + '/submit/' + str(problem_id), data=data)

    while True:
        url = boj_url + '/status?from_mine=1&problem_id=' + str(problem_id) + '&user_id' + LOGIN_INFO["login_user_id"]
        soup = bs(sess.get(url).text, 'html.parser')
        status = soup.find('span', {'class': 'result-text'}).find('span').string.strip()
        result = soup.find('span', {'class': 'result-ac'})
        print('\r                      ',end='')
        print('\r%s' % status, end='')
        if result is not None:
            break
    
    print()