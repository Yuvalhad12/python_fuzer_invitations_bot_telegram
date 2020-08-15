# this one is for running every 30 minutes and make sure we have more than 5 invites.
# if not, we buy 2 more.
# not efficient - we can tie it to "send_email.py", but we like to experiment here.
# also in the future we can coporate all of them into "main" and using threads

import requests, pickle, time
from bs4 import BeautifulSoup
cookies = pickle.load(open("fuzer.pkl", "rb"))
s = requests.session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])

def buy_tickets(securitytoken):
    data = {
        'do':'buyinv',
        'invitations':2,
        'securitytoken':securitytoken
    }

    s.post('https://www.fuzer.me/store.php', data=data)

def main():
    print ('fill_invites is activated')
    while True:
        page = s.get('https://www.fuzer.me/store.php')
        soup = BeautifulSoup(page.content)
        invite_num = soup.find('a', {'class':'w'}).contents[0] #this is how we get the 'a' from inside (a, href) tag
        invite_num = int(invite_num)
        if invite_num < 5:
            print('not enough tickets')
            securitytoken = soup.find('input', {'name':'securitytoken'})['value']
            buy_tickets(securitytoken)
        time.sleep(1800)
