"""This file is to be run seperately by cron job every week, 
AND NOT BY A SERVICE OR AS A PART OF THIS PROJECT

BIG CREDIT to @avramit and his package "FXaPi" as parts of it are present in this code.

THIS CODE IS NOT WRITTEN EFFICIENTLY, but than again, it runs once a week and its main objective is to teach OOP and not efficency.
"""


import requests, hashlib, re
BASE_URL = 'https://www.fxp.co.il'

USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.md5pass = hashlib.md5(self.password.encode()).hexdigest() #Translates the password into md5 password


        self.s = requests.session()
        self.s.post(BASE_URL + '/login.php', params={ ###logs into fxp
			'web_fast_fxp': 1
		}, data={
			'vb_login_username': USERNAME,
			'vb_login_password': '',
			'securitytoken': 'guest',
			'do': 'login',
			'cookieuser': 1,
			'vb_login_md5password': self.md5pass,
			'vb_login_md5password_utf': self.md5pass
            }) 

        self.userid = self.s.cookies.get('bb_userid')

        home_req = self.s.get(BASE_URL + '/login.php', params={
			'web_fast_fxp': 1})

        self.securitytoken = re.search(r'SECURITYTOKEN = "(.+?)";', home_req.text).group(1)

    def post(self, thread_id, content):
        r = self.s.post(BASE_URL +'/newreply.php', params={
            't': thread_id
            }, data={
                'do': 'postreply',
                'securitytoken':self.securitytoken,
                'ajax': 1,
                'message_backup': content,
                'message': content,
                'wysiwyg': 1,
                'signature': 1,
                'fromquickreply': 1,
                'specifiedpost': 1,
                'parseurl': 1,
                'loggedinuser': self.userid
            })





user = User(USERNAME,PASSWORD)

string= """
***הקפצה***
פעולה זו נעשתה באופן אוטומטי, והיא תיעשה כל שבוע וחצי על מנת למנוע ספאם מיותר;
שימו לב: אם עבר יותר משבוע וחצי מאז ההקפצה הקודמת, אז הפוסט הזה אינו רלוונטי יותר.
כמו כן, מאחר ופעולה זו נעשתה באופן אוטומטי - כל מיני תגובות על הפוסט או הודעות בפרטי לא ייענו, אך אם יש שאלות \ בקשות כלשהן - ניתן להשיג אותי באימייל שפורסם בפוסט עצמו.
"""

user.post("POSTID", string)




