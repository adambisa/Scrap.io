from os import getenv
from dotenv import load_dotenv
from notifiers import get_notifier
load_dotenv()
UNAME = getenv('LOGIN')
PWORD = getenv('PASSWORD')


class Url():
    def __init__(self, id, url, price, email, timestamp) -> None:
        self.id = id
        self.url = url
        self.price = price
        self.email = email
        self.timestamp = timestamp

    def inform(self):
        email = get_notifier('email')
        settings = {
            'host': 'ksi2022smtp.iamroot.eu',# change host url
            'port': 587,
            'tls': True,

            'username': UNAME,
            'password': PWORD,

            'to': self.email,
            'from': 'user3763@ksi2022smtp.iamroot.eu',

            'subject': "Some subject",
            'message': f"Something you are interested in buying just got cheaper.{self.url}",
        }
        email.notify(**settings)
print('this works')