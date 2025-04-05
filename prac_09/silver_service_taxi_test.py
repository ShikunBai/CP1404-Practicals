from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, fanciness=2)
    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print(f"Fare: ${fare:.2f}")

    assert fare == 48.78, f"Expected fare $48.78, got ${fare:.2f}"


if __name__ == "__main__":
    main()
