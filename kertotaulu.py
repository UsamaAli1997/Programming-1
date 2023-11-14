"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that prints a multiplication table for an entered number just like in school, using steps of one to ten.
"""

def main():
    
    num = int(input("Choose a number: "))
    # print("Multiplication Table of", num)
    for i in range(1, 11):
        print(i,"*",num,"=",num * i)
    
    
    
main()

