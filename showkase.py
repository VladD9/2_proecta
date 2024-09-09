from kivy.app import App  
from kivy.uix.label import Label  
from kivy.uix.button import Button  
from kivy.uix.textinput import TextInput  
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager,Screen  
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.image import Image
from kivy.core.window import Window
from random import randint
import datetime

file = open("registration.txt","r",encoding="utf-8")
line = file.readlines()
login = [line[i] for i in range(0, len(line), 2)]
password = [line[i] for i in range(1, len(line), 2)]
file.close()

login_pass = False
password_pass = False
pass1 = False

print(login)
print(password)

now = datetime.datetime.now()
print(now)

treck = '''
Автобуси \n
№1 Мазепи - Франка \n
№2 Шевченка - Тудора \n
№3 Бандери - Незалежності \n
№4 Хіміків - Чорновола \n
№5 Тролейбусна - Івасюка \n
Тролейбуси \n
№6 Тичини - Стуса \n
№7 Коновальця - Довженка \n
№8 Галицька - Хоткевича \n
№9 Вовчинецька - Сагайдачного \n
№10 Січових стрільців - Бельведерська
'''

class One(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = "Вхід", size_hint = (1, 0.3), pos_hint = {'y':0.65}, font_size = 56)
        lab_name = Label(text = "Введіть електронну адресу", size_hint = (0.3, 0.4), pos_hint ={'y':0.35, "x":0.1})
        lab_password = Label(text = 'Введіть пароль', size_hint = (0.2, 0.4), pos_hint = {'y':0.25, 'x':0.1} )
        self.name_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.52, 'x':0.4})
        self.password_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.42, 'x':0.4})
        but_go = Button(text = "Вхід",size_hint = (0.3, 0.1), pos_hint = {'y':0.29, 'x':0.13})
        but_res = Button(text = "Зареєструватись",size_hint = (0.3, 0.1), pos_hint = {'y':0.29, 'x':0.45})

        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)

        line.add_widget(lab_inst)

        line.add_widget(self.name_input)
        line.add_widget(self.password_input)

        line.add_widget(lab_name)
        line.add_widget(lab_password)
        line.add_widget(but_go)
        line.add_widget(but_res)


        self.add_widget(line)

        but_go.on_press = self.check
        but_res.on_press = self.reistr

        self.login_pass = False
        self.password_pass = False
        self.pass1 = False
    
    def check(self):
        self.name_input.text = self.name_input.text + "\n"
        self.password_input.text = self.password_input.text + "\n"
        print( self.name_input.text)
        print(self.password_input.text)
        if self.name_input.text in login:
            self.login_pass = True
        if self.password_input.text in password:
            self.password_pass = True
        if self.login_pass == True and self.password_pass == True:
            self.manager.transition.direction = "up"
            self.manager.current = "two"
    def reistr(self):
        self.manager.transition.direction = "up"
        self.manager.current = "zero"


class Zero(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = "Реєстрація", size_hint = (1, 0.3), pos_hint = {'y':0.65}, font_size = 56)
        lab_name = Label(text = "Введіть електронну адресу", size_hint = (0.3, 0.4), pos_hint ={'y':0.35, "x":0.1})
        lab_password = Label(text = 'Введіть пароль', size_hint = (0.2, 0.4), pos_hint = {'y':0.25, 'x':0.1} )
        lab_password_cor = Label(text = 'Підтведіть пароль', size_hint = (0.2, 0.4), pos_hint = {'y':0.15, 'x':0.11} )

        self.name_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.52, 'x':0.4})
        self.password_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.42, 'x':0.4})
        self.password_cor_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.32, 'x':0.4})

        but_res = Button(text = "Зареєструватись",size_hint = (0.3, 0.1), pos_hint = {'y':0.19, 'x':0.4})

        but_inst = Button(text = "Назад", size_hint = (0.1, 0.1), pos_hint = {'y':0.85, "x":0.01}, font_size = 20)

        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)

        line.add_widget(but_inst)

        line.add_widget(lab_inst)
        line.add_widget(lab_name)
        line.add_widget(lab_password)
        line.add_widget(lab_password_cor)

        line.add_widget(self.name_input)
        line.add_widget(self.password_input)
        line.add_widget(self.password_cor_input)

        line.add_widget(but_res)

        self.add_widget(line)

        but_res.on_press = self.check_in
        but_inst.on_press = self.back

    def check_in(self):
        if self.password_input.text == self.password_cor_input.text:
            self.file = open("registration.txt","a",encoding="utf-8")
            self.file.write(self.name_input.text +"\n")
            self.file.write(self.password_input.text +"\n")
            self.file.close()
    def back(self):
        self.manager.transition.direction = "up"
        self.manager.current = "one"

class Two(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        but_inst = Button(text = "Кабінет", size_hint = (0.1, 0.1), pos_hint = {'y':0.85, "x":0.01}, font_size = 20)

        but_bus = Button(text = "Автобус", size_hint = (0.17, 0.17), pos_hint = {'y':0.58, "x":0.28}, font_size = 20)
        but_trol = Button(text = "Тролейбус", size_hint = (0.17, 0.17), pos_hint = {'y':0.58, "x":0.58}, font_size = 20)

        but_back = Button(text = "Назад", size_hint = (0.1, 0.1), pos_hint = {'y':0.85, "x":0.14}, font_size = 20)

        lab_treck = Label(text = treck, size_hint = (0.2, 0.4), pos_hint = {'y':0.28, 'x':0.07}, font_size = 13)

        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)

        line.add_widget(but_inst)
        line.add_widget(but_back)
        line.add_widget(lab_treck)
        line.add_widget(but_trol)
        line.add_widget(but_bus)
        self.add_widget(line)

        but_inst.on_press = self.next
        but_bus.on_press = self.next1
        but_trol.on_press = self.next2
        but_back.on_press = self.back
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = "three"
    def next1(self):
        self.manager.transition.direction = "up"
        self.manager.current = "four"
    def next2(self):
        self.manager.transition.direction = "up"
        self.manager.current = "five"
    def back(self):
        self.manager.transition.direction = "down"
        self.manager.current = "one"

class Three(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = "Кабінет", size_hint = (1, 0.3), pos_hint = {'y':0.65}, font_size = 56)
        lab_name = Label(text = "Введіть номер карти", size_hint = (0.3, 0.4), pos_hint ={'y':0.35, "x":0.1})
        lab_password = Label(text = 'Введіть пароль', size_hint = (0.2, 0.4), pos_hint = {'y':0.25, 'x':0.1268} )
        self.name_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.52, 'x':0.4})
        self.password_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.42, 'x':0.4})
        but_go = Button(text = "Підтвердити та повернутись",size_hint = (0.3, 0.1), pos_hint = {'y':0.297, 'x':0.157})

        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)

        self.add_widget(line)

        line.add_widget(lab_inst)
        line.add_widget(lab_name)
        line.add_widget(lab_password)

        line.add_widget(self.name_input)
        line.add_widget(self.password_input)


        line.add_widget(but_go)

        but_go.on_press = self.next

    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "two"

class Four(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global check


        line = FloatLayout()
        lab_name = Label(text = "Введіть номер автобуса", size_hint = (0.3, 0.4), pos_hint ={'y':0.55, "x":0.1})
        lab_hove = Label(text = "Введіть кількість квитків", size_hint = (0.3, 0.4), pos_hint ={'y':0.45, "x":0.1})

        but_back = Button(text = "Назад", size_hint = (0.1, 0.1), pos_hint = {'y':0.85, "x":0.01}, font_size = 20)

        self.name_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.72, 'x':0.4})
        self.name_hove = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.62, 'x':0.4})
        but_res = Button(text = "Зареєструватись",size_hint = (0.24, 0.1), pos_hint = {'y':0.47, 'x':0.14})
        
        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)

        self.add_widget(line)
        self.add_widget(but_back)
        self.add_widget(lab_name)
        self.add_widget(lab_hove)
        self.add_widget(self.name_input)
        self.add_widget(self.name_hove)
        self.add_widget(but_res)

        but_res.on_press = self.show
        but_back.on_press = self.back

    def show(self):
        global check
        number = randint(1000000,9999999)
        now = datetime.datetime.now()
        print(now)            
        check = 'Номер квитка:',str(number)
        check2 = 'Номер маршруту:', str(self.name_input.text)
        check3 = 'Кількість:',str(self.name_hove.text)
        check4 = 'Час реєстрації:',str(now),'Дійсний проягом 30 хв'
        lab_info = Label(text = str(check), size_hint = (0.3, 0.4), pos_hint ={'y':0.23, "x":0.1})
        lab_info2 = Label(text = str(check2), size_hint = (0.3, 0.4), pos_hint ={'y':0.19, "x":0.078})
        lab_info3 = Label(text = str(check3), size_hint = (0.3, 0.4), pos_hint ={'y':0.15, "x":0.044})
        lab_info4 = Label(text = str(check4), size_hint = (0.3, 0.4), pos_hint ={'y':0.11, "x":0.291})
        self.add_widget(lab_info)
        self.add_widget(lab_info2)
        self.add_widget(lab_info3)
        self.add_widget(lab_info4)
    def back(self):
        self.manager.transition.direction = "down"
        self.manager.current = "two"

class Five(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global check


        line = FloatLayout()
        lab_name = Label(text = "Введіть номер тролейбуса", size_hint = (0.3, 0.4), pos_hint ={'y':0.55, "x":0.1})
        lab_hove = Label(text = "Введіть кількість квитків", size_hint = (0.3, 0.4), pos_hint ={'y':0.45, "x":0.1})

        but_back = Button(text = "Назад", size_hint = (0.1, 0.1), pos_hint = {'y':0.85, "x":0.01}, font_size = 20)

        self.name_input = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.72, 'x':0.4})
        self.name_hove = TextInput(multiline = False, size_hint = (0.3, 0.05), pos_hint = {'y':0.62, 'x':0.4})
        but_res = Button(text = "Зареєструватись",size_hint = (0.24, 0.1), pos_hint = {'y':0.47, 'x':0.14})

        img = Image(source='fon.png',size_hint = (1.27, 1),pos_hint = {'y':0.0001, 'x':0.00001})
        logo= Image(source='logo.png',size_hint = (0.1,0.1),pos_hint = {'y':0.88, 'x':0.9})

        line.add_widget(img)
        line.add_widget(logo)
        
        self.add_widget(line)
        self.add_widget(but_back)
        self.add_widget(lab_name)
        self.add_widget(lab_hove)
        self.add_widget(self.name_input)
        self.add_widget(self.name_hove)
        self.add_widget(but_res)

        but_res.on_press = self.show
        but_back.on_press = self.back

    def show(self):
        global check
        number = randint(1000000,9999999)
        now = datetime.datetime.now()
        print(now)            
        check = 'Номер квитка:',str(number)
        check2 = 'Номер маршруту:', str(self.name_input.text)
        check3 = 'Кількість:',str(self.name_hove.text)
        check4 = 'Час реєстрації:',str(now),'Дійсний проягом 30 хв'
        lab_info = Label(text = str(check), size_hint = (0.3, 0.4), pos_hint ={'y':0.23, "x":0.1})
        lab_info2 = Label(text = str(check2), size_hint = (0.3, 0.4), pos_hint ={'y':0.19, "x":0.078})
        lab_info3 = Label(text = str(check3), size_hint = (0.3, 0.4), pos_hint ={'y':0.15, "x":0.044})
        lab_info4 = Label(text = str(check4), size_hint = (0.3, 0.4), pos_hint ={'y':0.11, "x":0.291})
        self.add_widget(lab_info)
        self.add_widget(lab_info2)
        self.add_widget(lab_info3)
        self.add_widget(lab_info4)
    
    def back(self):
        self.manager.transition.direction = "down"
        self.manager.current = "two"









           



        

            


        



class MyApp(App):
    def build(self):
        main_screen = ScreenManager()
        main_screen.add_widget(One(name= 'one'))
        main_screen.add_widget(Zero(name= 'zero'))
        main_screen.add_widget(Two(name= 'two'))
        main_screen.add_widget(Three(name= 'three'))
        main_screen.add_widget(Four(name= 'four'))
        main_screen.add_widget(Five(name= 'five'))

        return main_screen
    
app = MyApp()
app.run()

