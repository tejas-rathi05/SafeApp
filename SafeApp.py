from kivymd.uix.snackbar import Snackbar
import mysql.connector
from kivy.core.window import Window     #Core class for creating the default Kivy window.
from kivy.lang import Builder   #calling kivy language jo samajh sake kivy language
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp    #The App class is the base for creating Kivy applications
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp     #display pixels
import pyperclip
import string
import random

# UIX = UI/UX (User interface and user experience)

# Window.size = (1920, 1080)

KV = '''
#:import gch kivy.utils.get_color_from_hex
#:import Snackbar kivymd.uix.snackbar.Snackbar

ScreenManager:
    Manager:
    Generator:
    View:

<Manager>
    id: "manager"
    name: 'manager'
    MDCard:     #MDCard is like a template on the screen.
        size: self.size
        pos: self.pos
        md_bg_color: gch('#111111')

    MDCard:
        size_hint: (0.25, 1)
        md_bg_color: gch('#171626')
        elevation: 50

    FloatLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                pos: 90, 530
                size: 487/2.5, 512/2.5
                source: 'Images/Logo2.png'

    MDFillRoundFlatButton:
        id: manager_btn
        pos_hint: {'center_x': 0.125, 'center_y': 0.5}
        size_hint: (0.2, 0.2)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "MANAGER"
        color: 'white'
        font_size: 25
        font_name: "Poppins-SemiBold"
    
    MDFillRoundFlatButton:
        id: generator_btn
        pos_hint: {'center_x': 0.125, 'center_y': 0.3}
        size_hint: (0.2, 0.1)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "GENERATOR"
        color: 'white'
        font_size: 25
        font_name: "Poppins-SemiBold"
        on_release:
            root.manager.current = "generator"
            root.manager.transition.direction = "up"

    MDLabel:
        text: 'PASSWORD MANAGER'
        font_size: 60
        font_name: "Poppins-Bold"
        color: 'white'
        pos_hint: {'center_x': 0.9, 'center_y': 0.8}

    MDLabel:
        text: 'Enter your details to add the password'
        font_size: 15
        font_name: "Poppins-Italic"
        color: 'white'
        pos_hint: {'center_x': 0.63, 'center_y': 0.75}
        halign: 'center'

    MDTextFieldRound:
        id: username
        hint_text: 'Enter Username'
        color_active: gch('#111111')
        normal_color: gch('#111111')
        hint_text_color: 1,1,1, 0.1
        line_color: 255/255, 76/255, 41/255, 1
        foreground_color: 255/255, 76/255, 41/255, 1
        cursor_color: 255/255, 76/255, 41/255, 1
        pos_hint: {'center_x': 0.65, 'center_y': 0.6}
        size_hint: (0.35, 0.07)
        font_size: 18

    MDTextFieldRound:
        id: email
        hint_text: 'example@gmail.com'
        color_active: gch('#111111')
        normal_color: gch('#111111')
        hint_text_color: 1,1,1, 0.1
        line_color: 255/255, 76/255, 41/255, 1
        foreground_color: 255/255, 76/255, 41/255, 1
        cursor_color: 255/255, 76/255, 41/255, 1
        pos_hint: {'center_x': 0.65, 'center_y': 0.45}
        size_hint: (0.35, 0.07)
        font_size: 18

    MDTextFieldRound:
        id: password
        hint_text: '****************'
        color_active: gch('#111111')
        normal_color: gch('#111111')
        hint_text_color: 1,1,1, 0.1
        line_color: 255/255, 76/255, 41/255, 1
        foreground_color: 255/255, 76/255, 41/255, 1
        cursor_color: 255/255, 76/255, 41/255, 1
        pos_hint: {'center_x': 0.65, 'center_y': 0.3}
        size_hint: (0.35, 0.07)
        font_size: 18
        

    BoxLayout:
        pos_hint: {'center_x': 0.9, 'center_y': 0.6}
        MDIcon:
            icon: "account-circle-outline"
            font_size: '50'
            color: 255/255, 76/255, 41/255, 0.5

    BoxLayout:
        pos_hint: {'center_x': 0.9, 'center_y': 0.45}
        MDIcon:
            icon: "email-outline"
            font_size: '50'
            color: 255/255, 76/255, 41/255, 0.5

    BoxLayout:
        pos_hint: {'center_x': 0.9, 'center_y': 0.3}
        MDIcon:
            icon: "key-outline"
            font_size: '50'
            color: 255/255, 76/255, 41/255, 0.5

    MDRoundFlatButton:
        id: submit_btn
        pos_hint: {'center_x': 0.65, 'center_y': 0.15}
        md_bg_color: gch('#111111')
        line_color: 255/255, 76/255, 41/255, 1
        text_color: 255/255, 76/255, 41/255, 1
        text: "Submit"
        color: 'white'
        font_size: 20
        font_name: "Poppins-Regular"
        on_release: 
            app.submit(username.text, email.text, password.text)

    MDFillRoundFlatButton:
        id: view_btn
        pos_hint: {'center_x': 0.77, 'center_y': 0.15}
        md_bg_color: 82/255, 5/255, 123/255, 0.5
        text: "      View Passwords      "
        color: 'white'
        halign: "center"
        font_size: 20
        user_font_size: 25
        font_name: "Poppins-Regular"
        on_release:
            root.manager.current = "view"
            root.manager.transition.direction = "left"

<Generator>
    name: "generator"
    MDCard:
        size: self.size
        pos: self.pos
        md_bg_color: gch('#111111')

    MDCard:
        size_hint: (0.25, 1)
        #pos: self.pos
        #pos_center_y: 0.5
        md_bg_color: gch('#171626')
        elevation: 50

    FloatLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                pos: 90, 530
                size: 487/2.5, 512/2.5
                source: 'Images/Logo2.png'

    MDLabel:
        text: 'PASSWORD GENERATOR'
        font_size: 60
        font_name: "Poppins-Bold"
        color: 'white'
        pos_hint: {'center_x': 0.9, 'center_y': 0.8}

    MDFillRoundFlatButton:
        id: manager_btn
        pos_hint: {'center_x': 0.125, 'center_y': 0.5}
        size_hint: (0.2, 0.1)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "MANAGER"
        color: 'white'
        halign: "center"
        font_size: 25
        user_font_size: 25
        font_name: "Poppins-Bold"
        on_release:
            app.clear_fields()
            root.manager.current = "manager"
            root.manager.transition.direction = "down"

    MDFillRoundFlatButton:
        id: generator_btn
        pos_hint: {'center_x': 0.125, 'center_y': 0.3}
        size_hint: (0.2, 0.2)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "GENERATOR"
        color: 'white'
        font_size: 25
        font_name: "Poppins-Bold"

    MDLabel:
        text: 'Choose the length of the password'
        font_size: 15
        font_name: "Poppins-Italic"
        color: 'white'
        pos_hint: {'center_x': 0.65, 'center_y': 0.75}
        halign: 'center'

    MDTextFieldRound:
        id: length
        hint_text: 'Enter the length of password'
        color_active: gch('#111111')
        normal_color: gch('#111111')
        hint_text_color: 1,1,1, 0.1
        line_color: 255/255, 76/255, 41/255, 1
        foreground_color: 255/255, 76/255, 41/255, 1
        cursor_color: 255/255, 76/255, 41/255, 1
        pos_hint: {'center_x': 0.57, 'center_y': 0.5}
        size_hint: (0.33, 0.07)
        font_size: 18
    
    MDTextFieldRound:
        id: generated_pwd
        hint_text: 'Generated Password'
        color_active: gch('#111111')
        normal_color: gch('#111111')
        hint_text_color: 1,1,1, 0.1
        line_color: 255/255, 76/255, 41/255, 1
        foreground_color: 255/255, 76/255, 41/255, 1
        cursor_color: 255/255, 76/255, 41/255, 1
        pos_hint: {'center_x': 0.57, 'center_y': 0.4}
        size_hint: (0.33, 0.07)
        font_size: 18

    MDRoundFlatButton:
        id: generate_btn
        pos_hint: {'center_x': 0.81, 'center_y': 0.5}
        md_bg_color: gch('#111111')
        line_color: 255/255, 76/255, 41/255, 1
        text_color: 255/255, 76/255, 41/255, 1
        text: "Generate"
        color: 'white'
        font_size: 20
        font_name: "Poppins-Regular"
        on_release: 
            app.generate(length.text)
            app.show_pwd()
    
    MDIconButton:
        id: copy_btn
        icon: "content-copy"
        pos_hint: {'center_x': 0.81, 'center_y': 0.4}
        md_bg_color: gch('#171626')
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        user_font_size: 30
        on_release: 
            app.copy_pwd()

    MDFillRoundFlatButton:
        id: clear_fields
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        md_bg_color: 82/255, 5/255, 123/255, 1
        text: "              Clear              "
        color: 'white'
        halign: "center"
        font_size: 20
        user_font_size: 25
        font_name: "Poppins-Regular"
        on_release: 
            app.clear_fields()

<View>
    name: "view"
    MDCard:
        size: self.size
        pos: self.pos
        md_bg_color: gch('#111111')

    MDCard:
        size_hint: (0.25, 1)
        md_bg_color: gch('#171626')
        elevation: 50

    MDFillRoundFlatButton:
        id: back_btn
        pos_hint: {'center_x': 0.125, 'center_y': 0.7}
        size_hint: (0.2, 0.1)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "BACK"
        color: 'white'
        halign: "center"
        font_size: 25
        font_name: "Poppins-SemiBold"
        on_release: 
            app.hide_table()
            root.manager.current = "manager"
            root.manager.transition.direction = "right"

    MDFillRoundFlatButton:
        id: view_table
        pos_hint: {'center_x': 0.125, 'center_y': 0.4}
        size_hint: (0.2, 0.2)
        radius: [20]
        md_bg_color: 82/255, 5/255, 123/255, 1
        elevation: 20
        text: "VIEW"
        color: 'white'
        halign: "center"
        font_size: 25
        user_font_size: 25
        font_name: "Poppins-SemiBold"
        on_release: app.view_table()

'''

#  ''' tewutbwutbbtuwekbgkr ''' ----> is a docstring

class Manager(Screen):
    pass

class Generator(Screen):
    pass

class View(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Manager(name = "manager"))
sm.add_widget(Generator(name = "generator"))
sm.add_widget(View(name = "view"))

class SafeApp(MDApp):
    def build(self):
        # initialising the screen.
        # loading the kivy docstring.
        # adding the widgets.
        # connecting MySQL.

        screen = Screen()

        self.kv = Builder.load_string(KV)
        screen.add_widget(self.kv)

        db = mysql.connector.connect(
            host = 'localhost', 
            user = 'root', 
            passwd = "Tejas###1",
            database = "PasswordManager",
        )
        cursor = db.cursor()

        # created a database.
        # cursor.execute("CREATE DATABASE IF NOT EXISTS PasswordManager")

        cursor.execute("""CREATE TABLE if not exists manager(
        id int AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(50),
        mail_address VARCHAR(50),
        password TEXT NOT NULL);
        """)
        db.commit()     # to save the changes
        db.close()
        return screen

    def view_table(self):
        db = mysql.connector.connect(
            host = 'localhost', 
            user = 'root', 
            passwd = "Tejas###1",
            database = "PasswordManager",
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM manager")
        records = cursor.fetchall()
        # records = [(1, 'John', 'john123@gmail.com', 'AGU?|xJ>b0')]
        # fetchall() = This method fetches all (or all remaining) rows of a query result set and returns a list of tuples.

        data = []
        for record in records:
            data.append(record)

        self.table = MDDataTable(
            size_hint = (None, None),
            width = 900,
            height = 700,
            check = True,
            rows_num = len(data),
            pos_hint = {"center_x": 0.63, "center_y": 0.5},
            column_data = [
                ("Id", dp(20)),     #display pixels(dp)
                ("User Name", dp(45)),
                ("Email Address", dp(65)),
                ("Password", dp(45))
            ],
            row_data = data
        )
        self.root.add_widget(self.table)
        self.table.bind(on_check_press = self.check_press)

    def hide_table(self):
        self.table.opacity = 0

    def check_press(self, instance_table, current_row):
        pyperclip.copy(current_row[3])
        Snackbar(
            text = "Password Copied",
            snackbar_x="650",
            snackbar_y="10",
            size_hint_x=( Window.width - (dp(500) * 2)) / Window.width,
            radius = [10],
            ).open()

    def submit(self, username, email, password):
        Snackbar(
            text = "Submited",
            snackbar_x="650",
            snackbar_y="10",
            size_hint_x=( Window.width - (dp(500) * 2)) / Window.width,
            radius = [10],
            ).open()
        self.kv.get_screen('manager').ids.username.text = ''
        self.kv.get_screen('manager').ids.password.text = ''
        self.kv.get_screen('manager').ids.email.text = ''
        
        db = mysql.connector.connect(
            host = 'localhost', 
            user = 'root', 
            passwd = "Tejas###1",
            database = "PasswordManager",
        )
        cursor = db.cursor()

        sql_command = "INSERT INTO manager (user_name, mail_address, password) VALUES (%s, %s, %s)"
        
        values = (username, email, password)
        cursor.execute(sql_command, values)

        db.commit()
        db.close()
    
    def generate(self, length):
        global generated_pwd
        s1=string.ascii_lowercase   # ascii_lowercase is a string constant
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        s= []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        generated_pwd = "".join(s[0:int(length)])
        self.kv.get_screen('generator').ids.copy_btn.icon = "content-copy"
        self.kv.get_screen("generator").ids.copy_btn.md_bg_color = (23/255, 22/255, 38/255, 1)

    def show_pwd(self):
        self.kv.get_screen('generator').ids.generated_pwd.text = generated_pwd

    def copy_pwd(self):
        self.kv.get_screen('generator').ids.copy_btn.icon = "check-bold"
        Snackbar(
            text = "Password Copied!", 
            snackbar_x="650",
            snackbar_y="10",
            size_hint_x=( Window.width - (dp(500) * 2)) / Window.width,
            radius = [10],
            ).open()
        pyperclip.copy(generated_pwd)
        
        self.kv.get_screen("generator").ids.copy_btn.md_bg_color = (124/255, 252/255, 0/255, 0.8)
    
    def clear_fields(self):
        self.kv.get_screen('generator').ids.length.text = ''
        self.kv.get_screen('generator').ids.generated_pwd.text = ''
        self.kv.get_screen("generator").ids.copy_btn.md_bg_color = (23/255, 22/255, 38/255, 1)
        self.kv.get_screen('generator').ids.copy_btn.icon = "content-copy"


if __name__ == '__main__':
    SafeApp().run()



    '''
    **********************************************************************************************************************
    *****************************************************NOTES************************************************************
    **********************************************************************************************************************

    Class = Template
    Object = Instance of the class
    self = instance of the object


    '''