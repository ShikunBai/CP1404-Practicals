from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    second = Guitar("Second guitar", 2013, 16035.4)
    print(gibson)
    print(second)
    print(gibson.get_age())
    print(second.get_age())
    print(gibson.is_vintage())
    print(second.is_vintage())


if __name__ == '__main__':
    main()