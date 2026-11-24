# class Calculator:

#     def add(self, a, b):
#         print("Addition:", a + b)

#     def subtract(self, a, b):

#     def multiply(self, a, b):
#         print("Multiplication:", a * b)

#     def divide(self, a, b):
#         if b == 0:
#             print("Cannot divide by zero!")
#         else:
#             print("Division:", a / b)


# Creating calculator object
# calc = Calculator()

# # Taking input from the user
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# # Asking the user which operation to perform
# operation = input(
#     "Choose operation (add, subtract, multiply, divide): "
# ).lower()

# # Calling the method according to user input
# if operation == "add":
#     calc.add(a, b)

# elif operation == "subtract":
#     calc.subtract(a, b)

# elif operation == "multiply":
#     calc.multiply(a, b)

# elif operation == "divide":
#     calc.divide(a, b)

# else:
#     print("Invalid operation!")

# # Simple bank file handling project

# import json
# import os

# FILE = "accounts.json"

# # File se accounts load karo
# if os.path.exists(FILE):
#     with open(FILE, "r") as f:
#         accounts = json.load(f)
# else:
#     accounts = {}

# while True:
#     print("\n1. Account banao")
#     print("2. Balance dekho")
#     print("3. Paise jama karo")
#     print("4. Paise nikalo")
#     print("5. Exit")

#     choice = input("Option chuno: ")

#     if choice == "1":
#         acc_no = input("Account number: ")
#         name = input("Naam: ")
#         balance = float(input("Shuruaati balance: "))

#         accounts[acc_no] = {"name": name, "balance": balance}

#         with open(FILE, "w") as f:
#             json.dump(accounts, f, indent=4)

#         print("Account ban gaya!")

#     elif choice == "2":
#         acc_no = input("Account number: ")
#         if acc_no in accounts:
#             print("Naam:", accounts[acc_no]["name"])
#             print("Balance: ₹", accounts[acc_no]["balance"])
#         else:
#             print("Account nahi mila.")

#     elif choice == "3":
#         acc_no = input("Account number: ")
#         if acc_no in accounts:
#             amount = float(input("Kitne paise jama karne hain? "))
#             accounts[acc_no]["balance"] += amount
#             with open(FILE, "w") as f:
#                 json.dump(accounts, f, indent=4)
#             print("Paise jama ho gaye.")
#         else:
#             print("Account nahi mila.")

#     elif choice == "4":
#         acc_no = input("Account number: ")
#         if acc_no in accounts:
#             amount = float(input("Kitne paise nikalne hain? "))
#             if amount <= accounts[acc_no]["balance"]:
#                 accounts[acc_no]["balance"] -= amount
#                 with open(FILE, "w") as f:
#                     json.dump(accounts, f, indent=4)
#                 print("Paise nikal gaye.")
#             else:
#                 print("Balance kam hai.")
#         else:
#             print("Account nahi mila.")

#     elif choice == "5":
#         print("Program band.")
#         break

#     else:
#         print("Galat option.")






# import json

# file = "bank.txt"                         


# try:
#     with open(file, "r") as f:
#         accounts = json.load(f)
# except:
#     accounts = {}

# number = input("Account number: ")

# if number not in accounts:
#     accounts[number] = 0  

# amount = float(input("Kitne paise jama karne hain? "))
# accounts[number] += amount


# with open(file, "w") as f:
#     json.dump(accounts, f)

# print("Aapka balance hai:", accounts[number])




# def login_required(func):
#     def wrapper(logged_in):
#         if logged_in:
#             return func()
#         print("Please log in")
#     return wrapper

# @login_required   jhkjk

# def dashboard():
#     print("Welcome!")

# dashboard(False)  # Please log in
# dashboard(True)   # Welcome!



print("Hello, World!")



























































