# name = "John Smith"
# age = "20"
# new_patient = True
# inpw
#
# def printer():
#     if new_patient:
#         print(name + " is new patient  and " + age + " years old man")
#         print("He is born in ", 2019-int(age))
#     else:
#         print("his name is " + name + "and he is " + age + " years old man but not new patient" )
# printer()
#
# print("what is your weight?")
# m =int(input(" what is your weight in pounds? "))
# print("u r ",end="")
# print(m*0.453592)


# name = "Sejong university is one of the most expensive universities"
# print(len(name))
# up=name.upper()
# print(up)
# print(name.lower())
# print(name.split())
# print(name.capitalize())
# print(name.splitlines())
# print(name.replace("expensive","cheap"))
# print("one" in name)

#is_hot = False
# is_cold = False
# if is_hot:
#     print("it is a hot day\n Drink plent of water")
# elif is_cold:
#     print("It is a cold day\n Wear warm clothes")
# else:
#     print("it is a lovely day")
# price = 1000000
# is_good = False
# if is_good:
#     print(int(price/100*10))
# else:
#     print(format(int(price/100*20),',d'))
#
# secret_number = 9
# trials = 0
# last_num = 3
# while trials < last_num:
#     if int(input("Guess the secret number...")) == secret_number:
#         print("You won");
#         break;
#     trials += 1
# st = "start"
# sp = "stop"
# qt = "quit"
# print("start - to start the car")
# print("stop - to stop the car")
# print("quit - to exit")
# while True:
#     choice = input(">").lower()
#     if st == choice:
#         print("Car started...Ready to go!")
#     elif sp == choice:
#         print("Car stopped")
#     elif qt == choice:
#         break;
#     else:
#         print("I don't understand that...")

#
# prices = [10,20,30]
# total = 0
# for item in prices:
#     total += item
# print(total)


# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5,2,5,2,2]
# for item in numbers:
#     print("X "*item)
#
# names = ["Mike", "John","Sarah" ,"Nur","Bob","Harry"]
# print(names[2:-2])

# nums = [123,343,23,4,5,23,66,12324,4234]
# largest = nums[0]
# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)

# for item in range(5,10,2):
#     print(item)

# list = [123,33,222,222,33,4,5,3,23,4]
# unique = []
# for num in list:
#     if num not in unique:
#         unique.append(num)
# print(unique)
# dict = {1 : "one", 2 : "two", 3 : "three", 4: "four",5 : "five", 6 : "six", 7 : "seven", 8: "eight", 9:  "nine"}
# m = input("Phone: ")
# for m in dict:
#      nw =m.replace()
#         print(m.)


# def greet_user():
#     print("Hi There")
#     print("welcome aboard")
#
# print("Long time no see")
# greet_user()
# print("my buddy")

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# import random
# members = "mike", "Sarah", "Sejun", "Sahadat"
# leader = random.choice(members)
# print(leader)
# import random
# class roll:
#     def dice(self):
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         return x,y
#
# print(roll().dice())



#Now Lets move om exercises

# name = input("What is your name ? > ")
# # age = int(input("What is your age? > "))
# # print(name + " you will be 100 years old in " + str(2119-age) + " Insha Allah")

# def odd_or_even():
#     num = int(input("> "))
#     if num % 2 == 1:
#         print("odd")
#     elif num % 4 == 0:
#         print("multiple of 41")
#     else:
#         print("even")
# odd_or_even()

# def list():
#     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     free = []
#     for i in a:
#         if i < 5:
#             free.append(i)
#     print(free)
# list()
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # # #print("")
# # # print(list(filter(lambda x: (x <= 5) , a)))


def divisors():
    div_list = []
    div = int(input("> "))
    for i in range(1,div):
        if div % i == 0:
            div_list.append(i)
    print(div_list)
divisors()
