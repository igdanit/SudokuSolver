# Add a new attributes

from kivy.uix.textinput import TextInput


class IntInput(TextInput):
    def __init__(self, count, **kwargs):
        self.count = count
        self.bind(text=self.on_text)
        super().__init__(**kwargs)
        self.correct_values = '1', '2', '3', '4', '5', '6', '7', '8', '9'

    def on_text(self, substring, value):
        if len(value) != 1 or value not in self.correct_values:
            substring.text = ''
