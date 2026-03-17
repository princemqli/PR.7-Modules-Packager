import math

def factorial():
    n = int(input("Enter a number: "))
    print("Factorial:", math.factorial(n))

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): "))
    ci = p * (1 + r/100) ** t
    print("Compound Interest:", round(ci, 2))

def trigonometry():
    x = float(input("Enter angle in degrees: "))
    rad = math.radians(x)
    print("sin:", math.sin(rad))
    print("cos:", math.cos(rad))
    print("tan:", math.tan(rad))

def area():
    r = float(input("Enter radius of circle: "))
    print("Area:", math.pi * r * r)