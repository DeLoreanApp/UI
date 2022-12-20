from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from api_calls import APICalls
from kivy.properties import StringProperty
from kivy_garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
import time


Builder.load_file('delorean.kv')
Builder.load_file('game.kv')

global user
main_window_size = Window.size
user = {}


class WelcomeScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    def login(self):
        username = self.ids.email_or_username.text
        password = self.ids.password.text

        try:

            global user
            user = APICalls().login({'email_or_username': username, 'password': password})['user']
            print('user =', user)

        except KeyError:
            print("lol")


class RegisterScreen(Screen):
    def register(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        password_confirm = self.ids.password_confirm.text

        if password == password_confirm:
            global user
            user = APICalls().register({"username": username, "email": email, "password": password})['user']
            print('user =', user)


class HomeScreen(Screen):
    pass


class LeaderboardScreen(Screen):
        def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=2, padding=30, size_hint_y=1)
        self.layout.bind(minimum_height=self.layout.setter("height"))
        self.add_widget(self.layout)

        players_count = [i for i in range(1,11)]

        for i in players_count:
            username = Label(text=f"player")
            rank = Label(text=f"score{random.randint(0,1000)}")
            self.layout.add_widget(username)
            self.layout.add_widget(rank)


class MapScreen(Screen):
    pass


class CameraScreen(Screen):

    def change_window_size(self):
        global main_window_size
        Window.size = (412, 732)

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    def create_button(self):
        play = Button(text="Play Game")
        self.add_button(play)

    pass


class ProfileScreen(Screen):
    username = StringProperty()
    email = StringProperty()
    def get_user(self):
        self.username = f"@{user['username']}"
        self.email = f"{user['email']}"




class FriendsList(Screen):
    pass


class MyVisits(Screen):
    pass


class SettingsScreen(Screen):
    pass

class GameHomePage(Screen):
    pass

class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass


class GameFinalPage(Screen):
    def reset_window_size(self):
        global main_window_size
        Window.size = main_window_size
    pass

class ChangeMail(Screen):
    pass

class ChangePass(Screen):
    pass

class ChangeLanguge(Screen):
    pass


class DeLoreanApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='homescreen'))
        sm.add_widget(LeaderboardScreen(name='leaderboard'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(ProfileScreen(name='profile'))

        sm.add_widget(FriendsList(name='friends'))
        sm.add_widget(MyVisits(name='myvisits'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ChangeMail(name='changemail'))
        sm.add_widget(ChangePass(name='changpass'))
        sm.add_widget(ChangeLanguge(name='changlang'))

        sm.add_widget(GameHomePage(name="game_home"))
        sm.add_widget(Q1(name="q1"))
        sm.add_widget(Q2(name="q2"))
        sm.add_widget(Q3(name="q3"))
        sm.add_widget(GameFinalPage(name="game_final"))

        return sm


if __name__ == '__main__':
    DeLoreanApp().run()
