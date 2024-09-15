# --------------------------------------------------------
# Lab 2: Getting Started with Python
# CIS 103: Building a Simple Calculator
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/7/2024
from secrets import choice

#Defining the four functions (addition, subtraction, multiplication, and division) of a calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."

#Implementing a loop that will prompt the user to perform multiple calculations

def main():
    while True:
        print("Select the following options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting!")
            break

        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
