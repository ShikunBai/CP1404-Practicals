from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """A simple Kivy app that dynamically adds labels for each name in a list."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        """Load the layout and dynamically add labels for each name."""
        self.root = Builder.load_file("dynamic_labels.kv")
        main_box = self.root.ids.main
        for name in self.name_list:
            label = Label(text=name, font_size=32)
            main_box.add_widget(label)
        return self.root

if __name__ == "__main__":
    DynamicLabelsApp().run()
