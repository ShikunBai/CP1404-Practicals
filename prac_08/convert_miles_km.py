from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Bai Shikun'

UP_VALUE = 1
DOWN_VALUE = 1
MILES_TO_KM = 1.60934

class ConvertMiles(App):
    """ConvertMiles app is a Kivy app for converting miles to kilometres"""
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 230)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * MILES_TO_KM
        except ValueError:
            self.root.ids.output_label.text = str(0.0)
        self.root.ids.output_label.text = str(result)
    def handle_up(self, value):
        """handle up, let miles value + up value"""
        try:
            value = float(value) + UP_VALUE
            self.root.ids.input_number.text = str(int(value))
            self.handle_calculate(value)
        except ValueError:
            value = 0 + UP_VALUE
            self.root.ids.input_number.text = str(int(value))
            self.handle_calculate(value)


    def handle_down(self, value):
        """handle down, let miles value - down value"""
        try:
            value = float(value) - DOWN_VALUE
            self.root.ids.input_number.text = str(int(value))
            self.handle_calculate(value)
        except ValueError:
            value = 0 - DOWN_VALUE
            self.root.ids.input_number.text = str(int(value))
            self.handle_calculate(value)
ConvertMiles().run()