
from kivy.uix.gridlayout import GridLayout


class SquareLayout(GridLayout):
    def __init__(self, count, **kwargs):
        self.count = count
        super().__init__(**kwargs)
