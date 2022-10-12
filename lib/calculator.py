class Calculator:
    def __init__(self):
        self._history = {}

    @property
    def history(self):
        return self._history

    def clear_history(self):
        self._history = {}

    def calculate(self, expression):
        try:
            result = eval(self._normalize(expression))
            self._history[expression] = result
            return result
        except:
            return None

    def _normalize(self, expression):
        return str(expression).replace('^', '**')
    