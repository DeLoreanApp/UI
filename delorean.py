from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from api_calls import APICalls
from kivy.properties import StringProperty

Builder.load_file('delorean.kv')

global user
user = {}


class WelcomeScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    def login(self):
        username = self.ids.email_or_username.text
        password = self.ids.password.text

        global user
        user = APICalls().login({'email_or_username': username, 'password': password})['data']['user']
        print('user =', user)


class RegisterScreen(Screen):
    def register(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        password_confirm = self.ids.password_confirm.text

        if password == password_confirm:
            global user
            user = APICalls().register({"username": username, "email": email, "password": password})['data']['user']
            print('user =', user)


class HomeScreen(Screen):
    pass


class LeaderboardScreen(Screen):
    pass


class MapScreen(Screen):
    pass


class CameraScreen(Screen):
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


class MyApp(App):
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

        return sm


if __name__ == '__main__':
    MyApp().run()
