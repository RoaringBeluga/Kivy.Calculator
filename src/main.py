import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from cpu2 import CalcCPU2


class MainScreen(GridLayout):

    cpu = CalcCPU2()
    started_input = True

    def poing(self):
        self.ids.pogo.text = "POGO! Poing, poing, POING!"

    def unpoing(self):
        self.ids.pogo.text = "Pogo sticks!"

    def press(self, symbol):
        if self.started_input:
            self.ids.display.text = ''
            self.started_input = False
        print(symbol)
        if symbol == '.':
            if '.' not in self.ids.display.text:
                self.ids.display.text += '.'
        else:
            self.ids.display.text += symbol

    def calculate(self, command):
        print(command)
        self.started_input = True
        self.cpu.input(float(self.ids.display.text))
        self.ids.display.text = '0'
        self.cpu.calc(command)
        if command == '=':
            self.ids.display.text = str(self.cpu.display)

    def clear_input(self):
        self.ids.display.text = '0'

    def reset_calc(self):
        self.cpu = CalcCPU2()
        self.clear_input()

class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()