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
        """Build the Kivy app from the kv file"""
        Window.size = (500, 230)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_calculate(self, value):
        """
        Convert miles to kilometres and display the result.
        Uses error-checked value.
        """
        number = self.parse_float(value)
        result = number * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_up(self, value):
        """
        Increase the miles value by UP_VALUE and update result.
        """
        number = self.parse_float(value) + UP_VALUE
        self.root.ids.input_number.text = str(int(number))
        self.handle_calculate(number)

    def handle_down(self, value):
        """
        Decrease the miles value by DOWN_VALUE and update result.
        """
        number = self.parse_float(value) - DOWN_VALUE
        self.root.ids.input_number.text = str(int(number))
        self.handle_calculate(number)

     def parse_float(self, value):
        """
        Try to convert value to float.
        Return 0.0 if conversion fails.
        """
        try:
            return float(value)
        except ValueError:
            return 0.0

ConvertMiles().run()
