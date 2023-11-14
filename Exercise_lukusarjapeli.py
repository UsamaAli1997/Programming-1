"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

Zip Boing
"""

def main():
    try:
        max_numbers = int(input("How many numbers would you like to have? "))
        
        for number in range(1, max_numbers + 1):
            if number % 3 == 0 and number % 7 == 0:
                print("zip boing")
            elif number % 3 == 0:
                print("zip")
            elif number % 7 == 0:
                print("boing")
            else:
                print(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()


