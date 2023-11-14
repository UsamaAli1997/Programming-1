"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that asks the user how they feel on scale 1-10 and then proposes a suitable emoticon to describe the mood.
if-elif-else-statements.
"""
def main():
    string = input("How do you feel? (1-10) ")
    emotions = float(string)

    if emotions >= 1 and emotions <= 10:

        if emotions <= 7 and emotions >= 4:
            print("A suitable smiley would be :-|")

        elif emotions >= 8 and emotions < 10:
            print("A suitable smiley would be :-)")

        elif emotions < 4 and emotions > 1:
            print("A suitable smiley would be :-(")

        elif emotions == 1:
            print("A suitable smiley would be :'(")

        elif emotions == 10:
            print("A suitable smiley would be :-D")

    else:
        print("Bad input!")



if __name__ == "__main__":
    main()
