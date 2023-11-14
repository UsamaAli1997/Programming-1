"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that asks for purchase price paid amount and returns change in form of tens fives twos and ones.
"""

def main():
    pp = int(input("Purchase price: "))
    pa = int(input("Paid amount of money: "))

    remains = pa - pp

    ten = remains // 10
    remains = remains % 10

    five = remains // 5
    remains = remains % 5

    two = remains // 2
    remains = remains % 2

    one = remains

    if pp < pa:
        print("Offer change: ")
        if ten != 0:
            print("{} ten-euro notes".format(ten))

        if five != 0:
            print("{} five-euro notes".format(five))

        if two != 0:
            print("{} two-euro coins".format(two))

        if one != 0:
            print("{} one-euro coins".format(one))

    else:
        print("No change")

if __name__ == "__main__":
    main()
