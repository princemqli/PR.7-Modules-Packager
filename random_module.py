import random
import string

def random_number():
    print("Random Number:", random.randint(1, 100))

def random_list():
    print("Random List:", [random.randint(1, 50) for _ in range(5)])

def random_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

def random_otp():
    print("OTP:", random.randint(1000, 9999))