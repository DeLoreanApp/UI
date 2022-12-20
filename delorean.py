from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from api_calls import APICalls
from kivy.properties import StringProperty
from kivy_garden.mapview import MapView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
import time
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Builder.load_file('delorean.kv')
Builder.load_file('game.kv')

global user
main_window_size = Window.size
user = {}
sm = ScreenManager()


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
            response = APICalls().login({'email_or_username': username, 'password': password})  # Get the whole response
            if response['status'] == 'success':
                user = response['user']
                print('user =', user)
                sm.switch_to(sm.get_screen(name='homescreen'))
            else:  # Error handling from the API (status = 'fail')

                self.show_error_popup(response['error'])

        except KeyError:
            # Display an error message if the 'user' key is not found in the response from the API
            self.show_error_popup("Invalid username or password")
        except ConnectionError:
            # Display an error message if there is a problem connecting to the API
            self.show_error_popup("Could not connect to server")
        except Exception as e:
            # Catch any other exceptions and display a generic error message
            self.show_error_popup("An error occurred: {}".format(e))

    def show_error_popup(self, error_message):
        popup = Popup(title="Error", content=Label(text=error_message), size_hint=(None, None), size=(400, 400))
        popup.open()


class RegisterScreen(Screen):
    def register(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        password_confirm = self.ids.password_confirm.text

        if password == password_confirm:
            try:
                global user
                response = APICalls().register({"username": username, "email": email, "password": password})
                if response['status'] == 'success':
                    user = response['user']
                    print('user =', user)
                else:  # Error handling from the API (status == 'fail')
                    self.show_error_popup(response['error'])
            except KeyError:
                # Display an error message if the 'user' key is not found in the response from the API
                self.show_error_popup("Error creating account")
            except ConnectionError:
                # Display an error message if there is a problem connecting to the API
                self.show_error_popup("Could not connect to server")
            except Exception as e:
                # Catch any other exceptions and display a generic error message
                self.show_error_popup("An error occurred: {}".format(e))
        else:
            # Display an error message if the passwords do not match
            self.show_error_popup("Passwords do not match")

    def show_error_popup(self, error_message):
        popup = Popup(title="Error", content=Label(text=error_message), size_hint=(None, None), size=(400, 400))
        popup.open()

class HomeScreen(Screen):
    pass


class LeaderboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation='vertical', padding=20)
        self.add_widget(boxlayout)
        label = Label(text='Leaderboard', bold=True, size_hint_y=0.05, font_size=40)
        boxlayout.add_widget(label)
        layout = GridLayout(cols=3,padding=30, size_hint_y=0.95)
        boxlayout.add_widget(layout)

        leaders = APICalls().get_leaderboard()

        rank = 1
        user = leaders['leaderboard']
        for user in leaders['leaderboard']:
            if rank > 10:
                break
            username = Label(text=f"{user['username']}")
            score = Label(text=f"{user['score']}")
            layout.add_widget(Label(text=str(rank)))
            layout.add_widget(username)
            layout.add_widget(score)
            rank += 1


class MapScreen(Screen):
    pass


class CameraScreen(Screen):

    def change_window_size(self):
        global main_window_size
        Window.size = (412, 732)

    def capture(self):
        """
        Function to capture the images and give them the names
        according to their captured time and date.
        """
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


class ChangeMail(Screen):
    def change_email(self):
        current_email = self.ids.current_email.text
        new_email = self.ids.new_email.text
        check_email = self.ids.new_repeat_email.text
        global user
        user_id = user['user_id']
        old_email = user['email']
        if current_email == old_email and new_email == check_email:
            user = APICalls().change_email(user_id, {'new_email': new_email})['user']


class ChangePass(Screen):
    def change_password(self):
        new_password = self.ids.new_pass.text
        new_password_confirm = self.ids.new_repeat_pass.text
        if new_password == new_password_confirm:
            APICalls().change_password(user['user_id'], {'password': new_password})


class ChangeLanguage(Screen):
    pass


class DeLoreanApp(App):
    def build(self):
        # Create the screen manager
        # sm = ScreenManager()
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
        sm.add_widget(ChangeMail(name='changemail'))
        sm.add_widget(ChangePass(name='changpass'))
        sm.add_widget(ChangeLanguage(name='changlang'))

        sm.add_widget(GameHomePage(name="game_home"))
        sm.add_widget(Q1(name="q1"))
        sm.add_widget(Q2(name="q2"))
        sm.add_widget(Q3(name="q3"))
        sm.add_widget(GameFinalPage(name="game_final"))

        return sm


if __name__ == '__main__':
    DeLoreanApp().run()
