from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more fancy Taxi that charges more per km and adds a flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, Taxi.price_per_km * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        """Return the fare including flagfall."""
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 2)

    def __str__(self):
        """Return a string with fare rate and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
