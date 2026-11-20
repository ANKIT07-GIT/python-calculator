import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x % y

def square_root(x):
    if x < 0:
        return "Error: Cannot square root negative number"
    return math.sqrt(x)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Square Root")


    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"{num1} % {num2} = {modulo(num1, num2)}")
        if choice == '7':
            try:
                num1 = float(input("Enter number: "))
                print(f"√{num1} = {square_root(num1)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
            return
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()