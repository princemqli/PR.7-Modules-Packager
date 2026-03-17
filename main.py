import datetime_module as dt
import math_module as mm
import random_module as rm
import uuid_module as um

from custom_modules import file_operations as fo
import math

def explore_module():
    module = input("Enter module name to explore: ")
    if module == "math":
        print("Available Attributes in math module:")
        print(dir(math))

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            dt.show_current_datetime()
        elif ch == "2":
            dt.date_difference()
        elif ch == "3":
            dt.format_date()
        elif ch == "4":
            dt.stopwatch()
        elif ch == "5":
            dt.countdown()
        elif ch == "6":
            break

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            mm.factorial()
        elif ch == "2":
            mm.compound_interest()
        elif ch == "3":
            mm.trigonometry()
        elif ch == "4":
            mm.area()
        elif ch == "5":
            break

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            rm.random_number()
        elif ch == "2":
            rm.random_list()
        elif ch == "3":
            rm.random_password()
        elif ch == "4":
            rm.random_otp()
        elif ch == "5":
            break

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            fo.create_file()
        elif ch == "2":
            fo.write_file()
        elif ch == "3":
            fo.read_file()
        elif ch == "4":
            fo.append_file()
        elif ch == "5":
            break

def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            um.generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break

if __name__ == "__main__":
    main()