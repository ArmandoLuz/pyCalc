from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from lib.calculator import Calculator


calculator = Calculator()


class ScreenManagement(ScreenManager):
    def go_to(self, screen):
        self.current = screen


class CalculatorScreen(Screen):
    def calculate(self, expression):
        if not expression:
            return

        result = calculator.calculate(expression)
        self.display.text = str(result) if result else 'Operação inválida!'


class HistoryScreen(Screen):
    def on_enter(self):
        self.load_history()

    def load_history(self):
        self.list_view.text = self.get_history()

    def get_history(self):
        history = calculator.history.items()
        result = [f'{item[0]} = {item[1]}' for item in history]
        return '\n'.join(result)

    def clear(self):
        calculator.clear_history()
        self.load_history()


class PyCalc(App):
    def build(self):
        return ScreenManagement()

    
if __name__ == '__main__':
    PyCalc().run()
