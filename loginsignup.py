import random

def login():
    a = input("Enter your name:")
    b = input("Enter your role:")
    c = input("Create your username:")
    e = input("Create password:")
    f = input("Confirm password:")
    if e == f:
        print("Welcome!", a)
        print("You are successfully logged in.")
    else:
        print("Password doesn't match.")
        print("Please try again.")
        return login()  # Recursively call login function if password doesn't match

def signup():
    s = input("Enter your Username:")
    generated_otp = otp()
    print("Your OTP for signup is:", generated_otp, "please don't share this with anyone.")
    t = int(input("Enter the OTP:"))
    if t == generated_otp:
        print("Welcome!", s)
    else:
        print("Your OTP doesn't match!")
        print("Please try again.")
        return signup()  # Recursively call signup function if OTP doesn't match

def otp(length=4):
    digits = "0123456789"
    generated_otp = " "
    for _ in range(length):
        generated_otp += random.choice(digits)
    return int(generated_otp)

try:
    n = input("Are you a member of this community:")
    if n.lower() == "yes":
        signup()
    elif n.lower() == "no":
        login()
    else:
        raise ValueError
except ValueError:
    print("Please reply in yes or no")
