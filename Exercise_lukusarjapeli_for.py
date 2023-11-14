"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

Zip Boing For Loop
"""

def zip_boing_game(max_numbers):
    """
    Play the Zip Boing game for a specified number of iterations.
    
    Args:
        max_numbers (int): The maximum number of iterations for the game.

    This function plays the Zip Boing game for the given number of iterations.
    It prints numbers, "zip" for numbers divisible by 3, "boing" for numbers divisible by 7,
    and "zip boing" for numbers divisible by both 3 and 7.
    """
    for number in range(1, max_numbers + 1):
        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")
        elif number % 3 == 0:
            print("zip")
        elif number % 7 == 0:
            print("boing")
        else:
            print(number)

def main():
    """
    Main function to interact with the user and play the Zip Boing game.

    This function prompts the user for the number of iterations and then calls the
    zip_boing_game function to play the game.
    """
    try:
        max_numbers = int(input("How many numbers would you like to have? "))
        zip_boing_game(max_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()



