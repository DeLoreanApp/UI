import requests


class APICalls:
    def __init__(self):
        # self.URL = "https://delorian-api.herokuapp.com{}"
        self.URL = "http://127.0.0.1:8000{}"
    def register(self, params):
        r = requests.post(self.URL.format("/register"), json=params)
        return r.json()

    def login(self, params):
        r = requests.post(self.URL.format('/login'), json=params)
        return r.json()

    def get_user(self, id):
        r = requests.get(self.URL.format(f'/user/{id}'))
        return r.json()

    def get_leaderboard(self):
        r = requests.get(self.URL.format('/leaderboard'))
        return r.json()