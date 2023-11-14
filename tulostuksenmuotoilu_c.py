"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

Fixing field width
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            # Use f-strings to format the output with a width of 4 characters
            if j < 10:
                print(f"{result:4}", end="")
            else:
                print(f"{result:4}")
                
if __name__ == "__main__":
    main()

