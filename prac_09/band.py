class Band:
    """Represent a band, which is a collection of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string representation of the Band and its Musicians."""
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Return a string of each musician performing."""
        performance = []
        for musician in self.musicians:
            if musician.instruments:
                performance.append(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                performance.append(f"{musician.name} needs an instrument!")
        return "\n".join(performance)
