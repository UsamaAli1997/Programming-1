"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that asks the user if they're bored part 2.
"""

def main():
    while True:
        bored = input("Answer Y or N: ")
        if bored.lower() in ["y", "n"]:
            print("You answered", bored)
            break
        else:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()

