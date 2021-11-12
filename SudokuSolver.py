# Main module. Contain a kivy interface
# Kivy 2.0.0

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from layout import SquareLayout
from widget import IntInput

from constructor import sudoku_filler


class BoxApp(App):

    buttons = {}

    def build(self):
        main_layout = RelativeLayout()
        sudoku_space = RelativeLayout(pos_hint={'y': 0.1, 'x': 0.05}, size_hint=(0.9, 0.9))
        button_space = RelativeLayout(pos=(0, 0), size_hint=(1, 0.1))
        sudoku_space.add_widget(self.sudoku_field())
        button_space.add_widget(self.buttons_field())
        main_layout.add_widget(sudoku_space)
        main_layout.add_widget(button_space)
        return main_layout

    def sudoku_field(self):
        sudoku_layout = GridLayout(cols=3, rows=3, spacing=[10, 10], height=70)
        for num in range(1, 10):
            box_layout = SquareLayout(count=num, cols=3, rows=3)
            self.buttons[num] = []
            for _ in range(9):
                cell = IntInput(count=num, multiline=False, halign='center', font_size=40)
                self.buttons[num].append(cell)
                box_layout.add_widget(cell)
            sudoku_layout.add_widget(box_layout)

        return sudoku_layout

    def buttons_field(self):
        buttons_title = ['Solve', 'Clear All']
        buttons_layout = BoxLayout(orientation='horizontal')
        for title in buttons_title:
            button = Button(text=title, font_size=24)
            button.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(button)

        return buttons_layout

    def on_button_press(self, instance):
        if instance.text == 'Solve':
            sudoku_filler(self.buttons)
        elif instance.text == 'Clear All':
            for square in self.buttons.values():
                for cell in square:
                    cell.text = ''


if __name__ == '__main__':
    app = BoxApp()
    app.run()
