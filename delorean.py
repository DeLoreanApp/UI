from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('delorean.kv')


class WelcomeScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass

class HomeScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass

class EditProfile(Screen):
    pass

class FriendsList(Screen):
    pass

class MyVisits(Screen):
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
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(EditProfile(name='editprofile'))
        sm.add_widget(FriendsList(name='friends'))
        sm.add_widget(MyVisits(name='myvisits'))

        return sm


if __name__ == '__main__':
    MyApp().run()
