import random
from car import Car  

class UnreliableCar(Car):
    """A Car that might not always drive due to reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability."""
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
