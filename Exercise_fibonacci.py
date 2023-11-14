"""
COMP.CS.100
Creator: Usama Ali
Student id number: 151265163

Exercise fibonacci
"""

def main():
    try:
        num = int(input("How many Fibonacci numbers do you want? "))
        fib_sequence = [1, 1]

        for i in range(2, num):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)

        for i, num in enumerate(fib_sequence):
            print(f"{i+1}. {num}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()


