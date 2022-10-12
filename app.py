import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from lib.calculator import Calculator


calculator = Calculator()


class ScreenManagement(ScreenManager):
    def go_to(self, screen):
        self.current = screen


class CalculatorScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class CalculatorUI(GridLayout):
    def calculate(self, expression):
        if not expression:
            return

        result = calculator.calculate(expression)
        self.display.text = str(result) if result else 'Operação inválida!'


class HistoryUI(GridLayout):
    def load_history(self):
        history = calculator.history.items()
        # result = '\n'.join(list(map(lambda item: f'{item[0]} = {item[1]}', history)))
        result = [f'{item[0]} = {item[1]}' for item in history]
        print(calculator.history.items())
        return 'kdskdks'
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     # self.cols = 1
    #     # self.rows = 2

    #     self._scrollview = ScrollView()

    #     for expression, value in calculator.history.items():
    #         print(f'{expression} = {value}')
    #         self._scrollview.add_widget(Button(text=f'{expression} = {value}'))

    #     self.add_widget(self._scrollview)

        # self._clear_button = Button(text='Limpar Histórico')

    def clear(self):
        calculator.clear_history()


class PyCalc(App):
    def build(self):
        return ScreenManagement()
        # return CalculatorUI()

    
if __name__ == '__main__':
    PyCalc().run()
