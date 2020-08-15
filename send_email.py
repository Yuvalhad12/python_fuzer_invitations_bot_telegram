# this one is for sending an invitation to desired email
# code is not efficient. We can do it without functions and I am sure there are more things we can do here

import requests, pickle
from bs4 import BeautifulSoup
cookies = pickle.load(open("fuzer.pkl", "rb"))
s = requests.session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])

def get_tokens():
    page = s.get('https://www.fuzer.me/profile.php?do=invitation')
    soup = BeautifulSoup(page.content)
    token = soup.find('input', {'name':'token'})['value']
    securitytoken = soup.find('input', {'name':'securitytoken'})['value']

    return (token, securitytoken)

def send_email(email):
    print('send_email is activated')
    token, securitytoken = get_tokens()
    data = {
        'do':'invitation',
        'email':email,
        'token':token,
        'securitytoken': securitytoken
    }

    s.post('https://www.fuzer.me/profile.php?do=invitation', data=data)
