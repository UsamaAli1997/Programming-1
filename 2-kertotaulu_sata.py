"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

A program that prints a multiplication table for a given number until it reaches a result that is more than hundred.
"""

def main():
    
    num = int(input("Choose a number: "))
    # print("Multiplication Table of", num)
    product = num
    i = 1
    while product < 99:
       product = num * i
       print(i, "*", num, "=", product)
       i += 1
    if product < 100:
       print(i, "*", num, "=", num*i)
    
    
    
    
main()


