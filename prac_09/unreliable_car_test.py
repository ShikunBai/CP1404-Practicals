from unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("Unreliable Car", 100, 30.0)

    drive_attempts = 100
    successful_drives = 0
    total_distance = 0

    for _ in range(drive_attempts):
        result = unreliable_car.drive(1)  # 尝试每次开1公里
        if result > 0:
            successful_drives += 1
            total_distance += result

    print(f"Tried to drive {drive_attempts} times.")
    print(f"Successful drives: {successful_drives}")
    print(f"Total distance driven: {total_distance}")
    print(f"Remaining fuel: {unreliable_car.fuel}")

if __name__ == "__main__":
    main()
