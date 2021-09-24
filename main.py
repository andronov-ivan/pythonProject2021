from kivy.app import App


from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import (Color, Rectangle)
from kivy.uix.widget import Widget
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'resizable', '1');
Config.set('graphics', 'width', '720');
Config.set('graphics', 'height', '1280');

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

class FirstApp(App):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    def build(self):
        sl = ScatterLayout()
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', padding = [.05, .05], spacing = 2)
        bl1 = BoxLayout(orientation='horizontal', spacing=0)
        bl2 = BoxLayout(orientation='horizontal', spacing=0)
        bl3 = BoxLayout(orientation='horizontal', spacing=0)
        bl4 = BoxLayout(orientation='horizontal', spacing=0)
        bl5 = BoxLayout(orientation='horizontal', spacing=0)
        bl6 = BoxLayout(orientation='horizontal', spacing=0)
        bl7 = BoxLayout(orientation='horizontal', spacing=0)
        bl8 = BoxLayout(orientation='horizontal', spacing=0)
        bl9 = BoxLayout(orientation='horizontal', spacing=0, size_hint=(1, .5), padding=[0])

        self.lab1 = Label(text='Зона №1')
        self.lab1.bind(size=self._update_rect1, pos=self._update_rect1)
        with self.lab1.canvas.before:
             Color(0,43,230,255)
             self.rect1 = Rectangle(size=self.lab1.size, pos=self.lab1.pos)
        self.bt1 = Button( text = 'Вкл', size_hint=(.2, 1))
        self.bt1.bind(on_press=self.pressing1)

        self.lab2 = Label(text='Зона №2')
        self.lab2.bind(size=self._update_rect2, pos=self._update_rect2)
        with self.lab2.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect2 = Rectangle(size=self.lab2.size, pos=self.lab2.pos)
        self.bt2 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt2.bind(on_press=self.pressing2)

        self.lab3 = Label(text='Зона №3')
        self.lab3.bind(size=self._update_rect3, pos=self._update_rect3)
        with self.lab3.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect3 = Rectangle(size=self.lab3.size, pos=self.lab3.pos)
        self.bt3 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt3.bind(on_press=self.pressing3)

        self.lab4 = Label(text='Зона №4')
        self.lab4.bind(size=self._update_rect4, pos=self._update_rect4)
        with self.lab4.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect4 = Rectangle(size=self.lab4.size, pos=self.lab4.pos)
        self.bt4 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt4.bind(on_press=self.pressing4)

        self.lab5 = Label(text='Зона №5')
        self.lab5.bind(size=self._update_rect5, pos=self._update_rect5)
        with self.lab5.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect5 = Rectangle(size=self.lab5.size, pos=self.lab5.pos)
        self.bt5 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt5.bind(on_press=self.pressing5)

        self.lab6 = Label(text='Зона №6')
        self.lab6.bind(size=self._update_rect6, pos=self._update_rect6)
        with self.lab6.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect6 = Rectangle(size=self.lab6.size, pos=self.lab6.pos)
        self.bt6 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt6.bind(on_press=self.pressing6)

        self.lab7 = Label(text='Зона №7')
        self.lab7.bind(size=self._update_rect7, pos=self._update_rect7)
        with self.lab7.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect7 = Rectangle(size=self.lab7.size, pos=self.lab7.pos)
        self.bt7 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt7.bind(on_press=self.pressing7)

        self.lab8 = Label(text='Зона №8')
        self.lab8.bind(size=self._update_rect8, pos=self._update_rect8)
        with self.lab8.canvas.before:
            Color(0,43,230,255)  # green; colors range from 0-1 not 0-255
            self.rect8 = Rectangle(size=self.lab8.size, pos=self.lab8.pos)
        self.bt8 = Button(text='Вкл', size_hint=(.2, 1))
        self.bt8.bind(on_press=self.pressing8)

        self.lab9 = Label()
        self.bt9 = Button(text='Подключиться', size_hint=(1, 1))
        self.bt9.bind(on_press=self.pressing9)
        self.lab10 = Label()

        sl.add_widget(al)
        al.add_widget(bl)
        bl.add_widget(bl1); bl1.add_widget(self.lab1); bl1.add_widget(self.bt1)
        bl.add_widget(bl2); bl2.add_widget(self.lab2); bl2.add_widget(self.bt2)
        bl.add_widget(bl3); bl3.add_widget(self.lab3); bl3.add_widget(self.bt3)
        bl.add_widget(bl4); bl4.add_widget(self.lab4); bl4.add_widget(self.bt4)
        bl.add_widget(bl5); bl5.add_widget(self.lab5); bl5.add_widget(self.bt5)
        bl.add_widget(bl6); bl6.add_widget(self.lab6); bl6.add_widget(self.bt6)
        bl.add_widget(bl7); bl7.add_widget(self.lab7); bl7.add_widget(self.bt7)
        bl.add_widget(bl8); bl8.add_widget(self.lab8); bl8.add_widget(self.bt8)
        bl.add_widget(bl9); bl9.add_widget(self.lab9); bl9.add_widget(self.bt9); bl9.add_widget(self.lab10)

        self.data1 = '0'
        self.data2 = '0'
        self.data3 = '0'
        self.data4 = '0'
        self.data5 = '0'
        self.data6 = '0'
        self.data7 = '0'
        self.data8 = '0'
        return sl


    def _update_rect1(self, instance, value):
        self.rect1.pos = instance.pos
        self.rect1.size = instance.size

    def _update_rect2(self, instance, value):
         self.rect2.pos = instance.pos
         self.rect2.size = instance.size

    def _update_rect3(self, instance, value):
        self.rect3.pos = instance.pos
        self.rect3.size = instance.size

    def _update_rect4(self, instance, value):
        self.rect4.pos = instance.pos
        self.rect4.size = instance.size

    def _update_rect5(self, instance, value):
        self.rect5.pos = instance.pos
        self.rect5.size = instance.size

    def _update_rect6(self, instance, value):
        self.rect6.pos = instance.pos
        self.rect6.size = instance.size

    def _update_rect7(self, instance, value):
        self.rect7.pos = instance.pos
        self.rect7.size = instance.size

    def _update_rect8(self, instance, value):
        self.rect8.pos = instance.pos
        self.rect8.size = instance.size

    def pressing1(self,btn):
        self.data1 = str(int(self.data1) + 1)
        if int(self.data1) > 1:
            self.data1 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing2(self,ett):
        self.data2 = str(int(self.data2) + 1)
        if int(self.data2) > 1:
            self.data2 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing3(self,ett):
        self.data3 = str(int(self.data3) + 1)
        if int(self.data3) > 1:
            self.data3 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing4(self,ett):
        self.data4 = str(int(self.data4) + 1)
        if int(self.data4) > 1:
            self.data4 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing5(self,ett):
        self.data5 = str(int(self.data5) + 1)
        if int(self.data5) > 1:
            self.data5 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing6(self,ett):
        self.data6 = str(int(self.data6) + 1)
        if int(self.data6) > 1:
            self.data6 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing7(self,ett):
        self.data7 = str(int(self.data7) + 1)
        if int(self.data7) > 1:
            self.data7 = '0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(
            self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(
            self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing8(self,ett):
        self.data8=str(int(self.data8)+1)
        if int(self.data8)>1:
            self.data8='0'
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def pressing9(self,ett):
        search_url = "http://192.168.4.1/,2," + str(self.data1) + "," + str(self.data2) + "," + str(self.data3) + "," + str(self.data4) + "," + str(self.data5) + "," + str(self.data6) + "," + str(self.data7) + "," + str(self.data8) + ","
        self.request = UrlRequest(search_url, self.sms)

    def sms(self,*args):
        msg = (self.request.result)
        x = msg.find(",")
        y = msg.rfind(",")
        msg = msg[x + 1:y + 1]
        print(msg)
        x = msg.find(",")
        self.data1 = msg[0:x]
        msg = msg[x+1:]
        x = msg.find(",")
        self.data2 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data3 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data4 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data5 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data6 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data7 = msg[0:x]
        msg = msg[x + 1:]
        x = msg.find(",")
        self.data8 = msg[0:x]
        msg = msg[x + 1:]
        print('data1=' + self.data1)
        print('data2=' + self.data2)
        print('data3=' + self.data3)
        print('data4=' + self.data4)
        print('data5=' + self.data5)
        print('data6=' + self.data6)
        print('data7=' + self.data7)
        print('data8=' + self.data8)
        self.color_btn()

    def color_btn(self):
        if int(self.data1) == 1:
            self.bt1.text = 'Выкл'
            self.bt1.color = (0, .46, .66, 1)
            self.bt1.background_color = (1, 0, 0, 1)
            self.bt1.size_hint = (1.2, 1)
        else:
            self.bt1.text = 'Вкл'
            self.bt1.color = (0, 0, 0, 1)
            self.bt1.background_color = (0, 1, 0, 1)
            self.bt1.size_hint = (.2, 1)

        if int(self.data2) == 1:
            self.bt2.text = 'Выкл'
            self.bt2.color = (0, .46, .66, 1)
            self.bt2.background_color = (1, 0, 0, 1)
            self.bt2.size_hint = (1.2, 1)
        else:
            self.bt2.text = 'Вкл'
            self.bt2.color = (0, 0, 0, 1)
            self.bt2.background_color = (0, 1, 0, 1)
            self.bt2.size_hint = (.2, 1)

        if int(self.data3) == 1:
            self.bt3.text = 'Выкл'
            self.bt3.color = (0, .46, .66, 1)
            self.bt3.background_color = (1, 0, 0, 1)
            self.bt3.size_hint = (1.2, 1)
        else:
            self.bt3.text = 'Вкл'
            self.bt3.color = (0, 0, 0, 1)
            self.bt3.background_color = (0, 1, 0, 1)
            self.bt3.size_hint = (.2, 1)

        if int(self.data4) == 1:
            self.bt4.text = 'Выкл'
            self.bt4.color = (0, .46, .66, 1)
            self.bt4.background_color = (1, 0, 0, 1)
            self.bt4.size_hint = (1.2, 1)
        else:
            self.bt4.text = 'Вкл'
            self.bt4.color = (0, 0, 0, 1)
            self.bt4.background_color = (0, 1, 0, 1)
            self.bt4.size_hint = (.2, 1)

        if int(self.data5) == 1:
            self.bt5.text = 'Выкл'
            self.bt5.color = (0, .46, .66, 1)
            self.bt5.background_color = (1, 0, 0, 1)
            self.bt5.size_hint = (1.2, 1)
        else:
            self.bt5.text = 'Вкл'
            self.bt5.color = (0, 0, 0, 1)
            self.bt5.background_color = (0, 1, 0, 1)
            self.bt5.size_hint = (.2, 1)

        if int(self.data6) == 1:
            self.bt6.text = 'Выкл'
            self.bt6.color = (0, .46, .66, 1)
            self.bt6.background_color = (1, 0, 0, 1)
            self.bt6.size_hint = (1.2, 1)
        else:
            self.bt6.text = 'Вкл'
            self.bt6.color = (0, 0, 0, 1)
            self.bt6.background_color = (0, 1, 0, 1)
            self.bt6.size_hint = (.2, 1)

        if int(self.data7) == 1:
            self.bt7.text = 'Выкл'
            self.bt7.color = (0, .46, .66, 1)
            self.bt7.background_color = (1, 0, 0, 1)
            self.bt7.size_hint = (1.2, 1)
        else:
            self.bt7.text = 'Вкл'
            self.bt7.color = (0, 0, 0, 1)
            self.bt7.background_color = (0, 1, 0, 1)
            self.bt7.size_hint = (.2, 1)

        if int(self.data8)==1:
            self.bt8.text = 'Выкл'
            self.bt8.color = (0, .46, .66, 1)
            self.bt8.background_color = (1, 0, 0, 1)
            self.bt8.size_hint = (1.2, 1)
        else:
            self.bt8.text = 'Вкл'
            self.bt8.color = (0, 0, 0, 1)
            self.bt8.background_color = (0, 1, 0, 1)
            self.bt8.size_hint = (.2, 1)

if __name__ == "__main__":
    FirstApp().run()