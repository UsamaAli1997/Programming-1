"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that asks the user if they're bored, until they are.
"""
def main():
    bored = ""

    while bored != "y":
        bored = input("Bored? (y/n) ")
    else:
        print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()
