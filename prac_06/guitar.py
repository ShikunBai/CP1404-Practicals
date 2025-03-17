"""
Guitar
Estimate time: 70 minutes
Actual time: 50 minutes
"""
CURRENT_YEAR = 2022

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Return a formatted string of the Guitar."""
        return f"{self.name} ({self.year} : ${self.cost:,.2f})"

    def get_age(self):
        """Return the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar age is vintage."""
        return self.get_age() >= 50

