# print("Hello World")
# print("jashan")


# class Shop:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, cash):
#         self.__balance += cash
#         print("Deposited:", cash)

#     def withdraw(self, cash):
#         if cash <= self.__balance:
#             self.__balance -= cash
#             print("Withdraw:", cash)
#         else:
#             print("Shop mein paise kam hain!")

#     def show_balance(self):
#         print("Current Balance:", self.__balance)


# s1 = Shop(1000)

# s1.deposit(500)
# s1.withdraw(200)
# s1.show_balance()




# # 1. Remove all occurrences of a number using a for loop
# numbers = [2, 5, 2, 7, 2, 9]
# target = 2

# remaining = []
# for number in numbers:
#     if number != target:
#         remaining.append(number)

# print(remaining)  # [5, 7, 9]


# # 2. Update or add a student-score pair
# scores = {"Ava": 88, "Noah": 92}
# scores["Mia"] = 95  # Adds Mia; assigning an existing name updates its score
# scores["Ava"] = 90
# print(scores)  # {'Ava': 90, 'Noah': 92, 'Mia': 95}


# # 3. Sum all values in a dictionary
# prices = {"apple": 2, "banana": 3, "orange": 4}
# total = sum(prices.values())
# print(total)  # 9


# # 4. Convert a tuple to a list, add a number, then convert back
# values = (10, 20, 30)
# values_list = list(values)
# values_list.append(40)
# values = tuple(values_list)
# print(values)  # (10, 20, 30, 40)


# # 5. Remove the minimum and maximum values from a set
# numbers_set = {4, 1, 8, 3, 6}
# numbers_set.remove(min(numbers_set))
# numbers_set.remove(max(numbers_set))
# print(numbers_set)  # {3, 4, 6}#