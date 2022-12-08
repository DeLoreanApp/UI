from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from api_calls import APICalls
from kivy.properties import StringProperty
from kivy_garden.mapview import MapView
from kivy.app import App


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
    pass


class MapScreen(Screen):
    pass


class CameraScreen(Screen):

    def change_window_size(self):
        global main_window_size
        Window.size = (412, 732)

    pass


class ProfileScreen(Screen):
    username = StringProperty()
    email = StringProperty()
    def get_user(self):
        self.username = f"@{user['username']}"
        self.email = f"{user['email']}"


class EditProfile(Screen):
    pass


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
        sm.add_widget(EditProfile(name='editprofile'))
        sm.add_widget(FriendsList(name='friends'))
        sm.add_widget(MyVisits(name='myvisits'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GameHomePage(name="game_home"))
        sm.add_widget(Q1(name="q1"))
        sm.add_widget(Q2(name="q2"))
        sm.add_widget(Q3(name="q3"))
        sm.add_widget(GameFinalPage(name="game_final"))

        return sm


if __name__ == '__main__':
    DeLoreanApp().run()
