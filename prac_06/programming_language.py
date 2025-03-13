class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a Car instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def is_dynamic(self):
        """Determine if a Car instance is dynamic."""
        return self.typing == "Dynamic"
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"