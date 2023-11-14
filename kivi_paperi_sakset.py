"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A rock paper and scissors game.
"""

def main ():
    p1 = input("Player 1, enter your choice (R/P/S): ")
    p2 = input("Player 2, enter your choice (R/P/S): ")

    if p1 == "R" and p2 == "P":
        print("Player 2 won!")

    elif p1 == "P" and p2 == "S":
        print("Player 2 won!")

    elif p1 == "P" and p2 == "R":
        print("Player 1 won!")

    elif p1 == "S" and p2 == "R":
        print("Player 2 won!")

    elif p1 == "S" and p2 == "P":
        print("Player 1 won!")

    elif p1 == "R" and p2 == "S":
        print("Player 1 won!")

    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
