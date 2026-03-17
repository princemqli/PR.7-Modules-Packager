from datetime import datetime
import time

def show_current_datetime():
    print("Current Date and Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def date_difference():
    d1 = input("Enter the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")
    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.strptime(d2, "%Y-%m-%d")
    diff = abs((date2 - date1).days)
    print("Difference:", diff, "days")

def format_date():
    d = input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(d, "%Y-%m-%d")
    print("Formatted Date:", date.strftime("%d-%m-%Y"))

def stopwatch():
    seconds = int(input("Enter seconds: "))
    for i in range(seconds):
        print(i+1)
        time.sleep(1)

def countdown():
    seconds = int(input("Enter seconds: "))
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)