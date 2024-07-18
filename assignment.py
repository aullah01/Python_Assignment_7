# Problem # 1:
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

# Solution:

# l = [100, 200, 300, 400]

# for i in range(len(l)):
#     print(i, l[i])


# Problem # 2:
# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

# Solution:

# def find_common_count(list1,list2):
    
#     common_counts = {}
    
#     for item in list1:
#         if item in common_counts:
#             common_counts[item] += 1
#         else:
#             common_counts[item] = 1  
            
#     for item in list2:
#         if item in common_counts:
#             common_counts[item] += 1
#         else:
#             common_counts[item] = 1
#     return common_counts
# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']

# result  = find_common_count(l1, l2)

# print(result)

# Problem # 3:
# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

# Solution:

# x = 2783
# counter = 0

# while x != 0:
#     counter += 1
#     x //= 10
# print("Total number of digits: ", counter)


# Problem # 4:

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

# Solution:

# user_input = int(input("Enter a number: "))

# while user_input != 0:
#     print(user_input)
#     user_input = int(input("Enter a number: "))


# Problem # 5:

# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

# Solution:

# numbers = []
# count = 0
# sum = 0
# while count < 5:
#     num = int(input("Enter a number: "))
#     numbers.append(num)
#     count += 1
#     sum += num
    
# print("5 input numbers are: ",numbers)
# print("Sum of 5 input numbers: ", sum)


# Problem 6:

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# Solution:

# names = []

# while True:
#     name = input("Enter a name (or END to quit): ").upper()
#     if name == "END":
#         break
#     names.append(name)
# print("Names: ",names)
# print("I am done")

# Problem # 7:

# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

# Solution:

# l1 = [11, 33, 50]
# result = ""
# for num in l1:
#     result += str(num)
# print(result)

# Problem # 8:


# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

# Solution:

# words = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# result_words = []

# for word in words:
#     if len(word) > 5:
#         result_words.append(word)

# print("Words longer than 5 characters:", result_words)

# Problem # 8:

# Diamond Shape:

# rows = 7

# Number of rows for the upper part of the diamond
# rows = int(input("Enter the number of rows: "))

# # Generate the upper part of the diamond
# for i in range(0, rows):
#     for j in range(0, rows - i - 1):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print()

# # Generate the lower part of the diamond
# for i in range(0, rows - 1):
#     for j in range(0, i + 1):
#         print(" ", end="")
#     for j in range(0, rows -i - 1):
#         print("* ", end="")
#     print()



# Problem # 9:

# Sqaure Shape:

# rows = int(input("Enter the number of rows: "))

# for i in range(0, rows):
#     for j in range(0, rows):
#         if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# Problem # 10:

# Left Triangle:

# Solution:

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(i + 1):
#         print("*", end="")
#     print()


# Problem # 11:

# Pyramid Shape:

# Solution:

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()

# Problem # 12:

# Rectangle Shape:

# Solution:

# rows = 4

# for i in range(rows):
#     for j in range(rows+1):
#         print("*", end="")
#     print()


# Problem # 13:

# Right Triangle:

# Solution:

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(i + 1):
#         print("*", end=" ")
#     print()
        
        
# Problem # 14:

# Upside down left trianlge:

# Solution:

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows-i):
#         print("*", end=" ")
#     print()
    
    
# Problem # 15:

# Write a program to create a function that takes two arguments, name and age. print them inside function.

# Solution:

# def name_age(name, age):
#     print(name)
#     print(age)
# name_age("Ameen", 24)


# Problem # 16:


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# Solution: 

# def show_employee(name, salary=9000):
#     print("Name:", name)
#     print("Salary:", salary)
# show_employee("Ameen")
# show_employee("Ameen", 50000)

# Problem # 17:

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

# Solution:

# list = []

# def create_list(a, b, c, d):
#     list.append(a)
#     list.append(b)
#     list.append(c)
#     list.append(d)
#     return list
# create_list(4,8,10,12)
# print(list)

# Problem # 18:

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

# Solution:

# def km_to_miles(km):
#     miles = km * 0.621371
#     return miles
# print(km_to_miles(5))


# Problem # 19:

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

# Solution:

# def is_divisible_by_11(num):
#     return (num % 11 == 0)
# result = is_divisible_by_11(44)
# print(result)
        
        
# Problem # 20:

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

# Solution:

# def get_highest(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# print(get_highest(5, 10))
# print(get_highest(7, 3))


# problem # 21:

# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.

# Solution:

# def fuel_cost(distance, fuel_per_liter=280):
#     cost = distance * fuel_per_liter
#     return cost

# print(fuel_cost(100))


# Problem # 22:


# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false    

# def is_valid_email(email):
#     if len(email) > 256:
#         return False
#     if not email[0].isalnum() and email[0]!= '_':
#         return False
#     if '@' not in email:
#         return False
#     before_at, after_at = email.split('@')
#     if not before_at.isalnum() and before_at!= '_':
#         return False
#     if after_at.count('.')!= 1:
#         return False
#     before_period, after_period = after_at.split('.')
#     if len(before_period) < 1 or len(after_period) < 1:
#         return False
#     return True

# print(is_valid_email("ameen@gmail.com"))
# print(is_valid_email("ameen@.com"))


# Problem # 23:

"""
Take a variable store i.e
Store = {“name”: “my store”, “inventory”: [], “orders”: []}

Add 5 items in the inventory using a function “add_item”
id, name, price and quantity

Take user input unless it says “done”
Display user updated inventory items every time
Ask user to type id of the item to purchase or type “done” to checkout
Each time only 1 quantity will by subtracted from the item

Functions: add_item_in_inventory, add_item_in_basket(), checkout()
On checkout, print “{quantity} {item} sold in {store}”
"""

# Solution:
# store = {
#     "name": "my store",
#     "inventory": [],
#     "orders": []
# }

# def add_item_to_inventory(store, item_id, name, price, quantity):
#     item = {
#         "id": item_id,
#         "name": name,
#         "price": price,
#         "quantity": quantity
#     }
#     store['inventory'].append(item)

# def display_inventory(store):
#     print("\nUpdated Inventory:")
#     for item in store['inventory']:
#         print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

# def add_item_to_basket(store, item_id, basket):
#     for item in store['inventory']:
#         if item['id'] == item_id and item['quantity'] > 0:
#             basket.append(item)
#             item['quantity'] -= 1 
#             print(f"Added {item['name']} to basket.")
#             return
#     print("Item not available or out of stock.")

# def checkout(store, basket):
#     for item in basket:
#         print(f"{1} {item['name']} sold in {store['name']}")

# add_item_to_inventory(store, 1, "Apple", 0.5, 10)
# add_item_to_inventory(store, 2, "Banana", 0.3, 15)
# add_item_to_inventory(store, 3, "Orange", 0.4, 5)
# add_item_to_inventory(store, 4, "Grapes", 1.0, 7)
# add_item_to_inventory(store, 5, "Mango", 1.2, 8)

# basket = []
# while True:
#     display_inventory(store)
#     user_input = input("Type the ID of the item to purchase or type 'done' to checkout: ").strip()
    
#     if user_input.lower() == 'done':
#         break
    
#     try:
#         item_id = int(user_input)
#         add_item_to_basket(store, item_id, basket)
#     except ValueError:
#         print("Please enter a valid item ID or 'done'.")

# checkout(store, basket)


        


