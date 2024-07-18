# dict = {
#     "danish": 200,
#     "fahad": 400,
#     "shoaib": 600,
#     "books": ["1", "2", "3"]
# }

# print(dict.keys())
# print(dict.values())
# print(dict.items())

# dict["books"] = ["1", "2", "3", "4", "5"]
# print(dict)

# new_dict = {
#     "books": ["1", "2", "3", "4", "5","6"]
# }
# dict.update(new_dict)
# print(dict)


# arr = [100, 200, 300, 400, 500, 600]

# for i in range(len(arr)):
#     print(i, arr[i])
    
# for i, val in enumerate(arr):
#     print(i, val)

# students = ["alice", "bob", "charlie"]
# score = [80, 90, 100]

# dict = {
#     "students": [],
#     "score": []
# }

# for i,  val in enumerate(students):
#     dict["students"].append(students[i])
#     dict["score"].append(score[i])
# print(dict)

# zip function: loop over multiple list

# for i,  val in enumerate(students):
#     dict["students"].append(val)
#     dict["score"].append(val)
# print(dict)


# x = 1
# while x > 0 and x <= 10:
#     x += 1
#     print("Hello World")



# x = 10
# while x > 0:
#     x -= 1
#     print("Hello World")


# num = int(input("Enter the number: "))
# while num >= 0:
#     print(num)
#     num = int(input("Enter the number: "))
    

# while True:
#     num = int(input("Enter the number: "))
#     if  num < 0:
#         break
#     print(num)


# list1 = [10,20, 30]
# list2 = [40, 50, 60, 30, 80]

# # for i in lis1:
# #     if i in list2:
# #         print(i)

# for i in list1:
#     for j in list2:
#         if i == j:
#             print(i)
        




# order_1_destination = "China"

# location = ["New York", "California", "Chine"]

# shipment_price = 0

# for loc in location:
#     if loc == order_1_destination:
#         shipment_price = 10
#     elif loc == order_1_destination:
#         shipment_price = 20
#     elif loc == order_1_destination:
#         shipment_price = 30
# print(shipment_price)


# def get_shipping_price():
#     for loc in location:
#         if loc == order_1_destination:
#             shipment_price = 10
#         elif loc == order_1_destination:
#             shipment_price = 20
#         elif loc == order_1_destination:
#             shipment_price = 30
            
# get_shipping_price()

# def multiply():
#     # global x
#     print("Hello, world!")
#     x = 100
#     print(x)
    
# x = 2
# y = 5

# print(x)

# multiply()

# print(x)


# x = "hello"

# def modify_string(xx):
#     print(xx)
#     xx = xx + " World"
#     print(xx)
#     return xx
    
# x = modify_string(x)
# print(x)


# def get_shippment_price(order_1_destination):
#     if "New York" == order_1_destination:
#         shipment_price = 10
#     elif "California" == order_1_destination:
#         shipment_price = 20
#     elif "China" == order_1_destination:
#         shipment_price = 30
#     print(shipment_price)
#     return shipment_price

# shipment_price = get_shippment_price("China")


# def sum(x, y, a):
#     z = x + y + a
#     return z
# sum = sum(3,5,6)
# print(sum)

# def do_sum(*args):
#     total = sum(args)
#     return total
# result = do_sum(3,5,6)
# print(result)
