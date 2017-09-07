import bs4
import requests


class Context:
    def __init__(self, session_cookie):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Oispa kaljaa',
        })
        self.session.cookies.set('_angellist', session_cookie, domain='angel.co')

    def acquire_csrf_token(self):
        resp = requests.get(url='https://angel.co/job_listings/startup_ids')
        csrf_token = bs4.BeautifulSoup(resp.text, 'html.parser').find('meta', {'name': 'csrf-token'})['content']
        self.session.headers['X-CSRF-Token'] = csrf_token
