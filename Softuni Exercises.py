# for i in range(1, 11):
#     print(i)

# side = int(input())
# area = side * side
# print(area)

# inch = float(input())
# print(inch * 2.54)

# name = input()
# print("Hello, " + name + "!")

# first_name = str(input("name: "))
# last_name = str(input("surname: "))
# age = int(input("age: "))
# town = str(input("town: "))
#
# print("You are {} {}, a {}-years old person from {}.".format(first_name, last_name, age, town))

# hours_per_project = 3
# architect_name = str(input())
# number_of_projects = int(input())
#
# hours_required = number_of_projects * hours_per_project
# print("The architect " + architect_name + " will need " + str(hours_required) + " hours to complete " + str(number_of_projects) + " project/s.")


# number_of_dogs = int(input())
# number_of_others = int(input())
# dog_food_cost = 2.50 * number_of_dogs
# other_food_cost = 4 * number_of_others
# total = dog_food_cost + other_food_cost
# print(str(total) + " lv.")

# area = float(input())
# price = area * 7.61
# discount = 0.18 * price
#
# print("The final price is: {} lv".format(price - discount))
# print("The discount is: {} lv.".format(discount))

# usd = float(input())
# bgn = usd * 1.79549
# print(bgn)

# import math
#
# from math import floor
#
# rad = float(input())
# print(floor(rad * 180 / math.pi))

# deposited_sum = float(input())
# deposit_time = int(input())
# interest = float(input())
# interest = interest / 100
#
# sum = deposited_sum + deposit_time * ((deposited_sum * interest) / 12)
# print(sum)


# pages = int(input())
# pages_per_hour = int(input())
# days = int(input())
#
# hours_per_day = (pages / pages_per_hour) / days
# print(hours_per_day)

# rent = int(input())
# cake = rent * 0.20
# drinks = cake - (cake * 0.45)
# entertainer = rent / 3
# print(rent + cake + drinks + entertainer)

# days = int(input())
# bakers = int(input())
# cakes = int(input())
# waffles = int(input())
# panckaes = int(input())
#
# print((((cakes * 45 + waffles * 5.80 + panckaes * 3.20)*days)*bakers) - (((cakes * 45 + waffles * 5.80 + panckaes * 3.20)*days)*bakers)/8)

# strawberry_price = float(input())
# bananas = float(input())
# oranges = float(input())
# raspberries = float(input())
# strawberries = float(input())
#
# raspberry_price = strawberry_price / 2
# oranges_price = raspberry_price - (raspberry_price * 0.40)
# bananas_price = raspberry_price - (raspberry_price * 0.8)
#
# price = (strawberry_price * strawberries) + (raspberry_price * raspberries) + (oranges_price * oranges) + (bananas_price * bananas)
# print(price)

# w = int(input())
# l = int(input())
# h = int(input())
# percentage = float(input())
#
# water = (w*l*h)/1000
# final = water - (water*(percentage/100))
# print(final)

# grade = float(input())
# if grade >= 5.50:
#     print("Excellent!")

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# a = int(input())
#
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# a = int(input())
# if a < 100:
#     print("Less than 100")
# elif a >= 100 and a <= 200:
#     print("Between 100 and 200")
# else:
#     print("Greater than 200")

# pwd = input()
# if pwd == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# else:
#     print("Wrong password!")

# from math import pi
#
# shape = input()
# if shape == "square":
#     side = float(input())
#     print(float(round(side*side, 3)))
# if shape == "rectangle":
#     side1 = float(input())
#     side2 = float(input())
#     print(float(round(side1*side2, 3)))
# if shape == "circle":
#     radius = float(input())
#     print(float(round(pi*(radius**2), 3)))
#
# if shape == "triangle":
#     side = float(input())
#     height = float(input())
#     print(float(round(1/2 * side * height, 3)))


# holiday = float(input())
# num_puzzle = int(input())
# num_dolls = int(input())
# num_teddys = int(input())
# num_minions = int(input())
# num_trucks = int(input())
#
# total = num_puzzle * 2.60 + num_dolls * 3 + num_teddys * 4.10 + num_minions * 8.20 + num_trucks * 2
# total = total*0.9
#
# if num_puzzle+num_dolls+num_teddys+num_minions+num_trucks >= 50:
#     total = float(total * 0.75)
#
# remainder = float(total - holiday)
# if remainder >= holiday:
#     print(f"Yes! " + format(remainder, ".2f") + " lv left.")
# else:
#     print("Not enough money! " + format(remainder * -1, ".2f") + " lv needed.")

# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
#
# total_time = time_first + time_second + time_third
# minutes = total_time / 60
# seconds = total_time % 60
#
# minutes = int(minutes)
#
# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')

# number = int(input())
# bonus = 0
#
# if number <= 100:
#     bonus = 5
# elif number > 1000:
#     bonus = 0.1 * number
# else:
#     bonus = 0.2 * number
#
# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2
#
# print(bonus)
# print(bonus + number)


# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# if speed > 10 and speed <= 50:
#     print("average")
# if speed > 50 and speed <= 150:
#     print("fast")
# if speed > 150 and speed <= 1000:
#     print("ultra fast")
# if speed > 1000:
#     print("extremely fast")

# number = float(input())
# from_ = input()
# to_ = input()
#
# if from_ == "m" and to_ == "cm":
#     number = number * 100
# if from_ == "m" and to_ == "mm":
#     number = number * 1000
# if from_ == "cm" and to_ == "m":
#     number = number / 100
# if from_ == "cm" and to_ == "mm":
#     number = number * 10
# if from_ == "mm" and to_ == "cm":
#     number = number / 10
# if from_ == "mm" and to_ == "m":
#     number = number / 1000
#
# print('{0:.3f}'.format(number))

# hours = int(input())
# minutes = int(input())
#
# if minutes + 15 > 59:
#     minutes = int(abs(60 - minutes -15))
#     hours += 1
#     if hours > 23:
#         hours = 0
#     if minutes < 10:
#         print(f'{hours}:0{minutes}')
#     else:
#          print(f'{hours}:{minutes}')
#
# else:
#     print(f'{hours}:{minutes + 15}')

# budget = float(input())
# extras = int(input())
# wardrobe_price = float(input())
#
# decoration = budget * 0.1
# if extras > 150:
#     wardrobe_price = wardrobe_price * 0.9
#
# total_cost = wardrobe_price * extras + decoration
# remainder = budget - total_cost
# if remainder < 0:
#     print("Not enough money!")
#     print("Wingard needs " + format(abs(remainder), ".2f") + " leva more.")
#
# if remainder >= 0:
#     print("Action!")
#     print("Wingard starts filming with " + format(remainder, ".2f") + " leva left.")

# record = float(input())
# distance = float(input())
# sec_per_meter = float(input())
# ivans_time = distance * sec_per_meter
# for i in range(int(distance/15)):
#     ivans_time += 12.5
#
# if ivans_time < record:
#     print(f'Yes, he succeeded! The new world record is {format(ivans_time, ".2f")} seconds.')
# else:
#     print("No, he failed! He was " + format(ivans_time-record, ".2f") + " seconds slower.")


# income = float(input())
# gpa = float(input())
# min_salary = float(input())
# social_scholarship = min_salary*0.35
# honors_scholarship = gpa*25
#
# if income > min_salary and gpa < 5.50:
#     print("You cannot get a scholarship!")
# if income < min_salary and gpa < 5.50:
#     print(f"You get a Social scholarship {int(social_scholarship)} BGN")
# if income >= min_salary and gpa >= 5.50:
#     print(f"You get a scholarship for excellent results {int(honors_scholarship)} BGN")
# if income < min_salary and gpa >= 5.50:
#     if social_scholarship > honors_scholarship:
#         print(f"You get a Social scholarship {int(social_scholarship)} BGN")
#     else:
#         print(f"You get a scholarship for excellent results {int(honors_scholarship)} BGN")
#

##why judge gives error?
# income = float(input())
# gpa = float(input())
# min_salary = float(input())
# social_scholarship = min_salary*0.35
# honors_scholarship = gpa*25
#
# if income >= min_salary and gpa < 5.50:
#     print("You cannot get a scholarship!")
# elif income < min_salary and gpa > 4.50:
#     print(f"You get a Social scholarship {int(social_scholarship)} BGN")
# elif gpa >= 5.50:
#     print(f"You get a scholarship for excellent results {int(honors_scholarship)} BGN")
# elif income < min_salary and gpa >= 5.50:
#     if social_scholarship > honors_scholarship:
#         print(f"You get a Social scholarship {int(social_scholarship)} BGN")
#     else:
#         print(f"You get a scholarship for excellent results {int(honors_scholarship)} BGN")

# day = int(input())
#
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Error")

# input = input()
# week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# weekend = ["Saturday", "Sunday"]
#
# if input in week:
#     print("Working day")
# elif input in weekend:
#     print("Weekend")
# else:
#     print("Error")

# animal = input()
#
# if animal == "dog":
#     print("mammal")
# elif animal in ["crocodile", "tortoise", "snake"]:
#     print("reptile")
# else:
#     print("unknown")

# age = float(input())
# gender = input()
#
# if gender == "m":
#     if age >= 16:
#         print("Mr.")
#     else:
#         print("Master")
# else:
#     if age >= 16:
#         print("Ms.")
#     else:
#         print("Miss")

# sofia = {
#     "coffee": 0.50,
#     "water": 0.80,
#     "beer": 1.20,
#     "sweets": 1.45,
#     "peanuts": 1.60
# }
#
# plovdiv = {
#     "coffee": 0.40,
#     "water": 0.70,
#     "beer": 1.15,
#     "sweets": 1.30,
#     "peanuts": 1.50
# }
#
# varna = {
#     "coffee": 0.45,
#     "water": 0.70,
#     "beer": 1.10,
#     "sweets": 1.35,
#     "peanuts": 1.55
# }
#
# product = input()
# city = input()
# quantity = float(input())
#
# if city == "Varna":
#     print(quantity * float(varna.get(product)))
# elif city == "Plovdiv":
#     print(quantity * float(plovdiv.get(product)))
# else:
#     print(quantity * float(sofia.get(product)))

# number = int(input())
#
# if number in range(-100, 101) and number != 0:
#     print("Yes")
# else:
#     print("No")

# hour = int(input())
# day = input()
#
# if hour in range(10,19) and day != "Sunday":
#     print("open")
# else:
#     print("closed")

# price = {
#     "Monday": 12,
#     "Tuesday": 12,
#     "Wednesday": 14,
#     "Thursday": 14,
#     "Friday": 12,
#     "Saturday": 16,
#     "Sunday": 16
# }
#
# day = input()
# print(price.get(day))

# fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
# vegetables = ["tomato", "cucumber", "pepper", "carrot"]
# product = input()
#
# if product in fruit:
#     print("fruit")
# elif product in vegetables:
#     print("vegetable")
# else:
#     print("unknown")

# number = int(input())
# if number not in range(100, 201) and number != 0:
#     print("invalid")

# product = input()
# day = input()
# quantity = float(input())
# valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# weekday = {
#     "banana": 2.50,
#     "apple": 1.20,
#     "orange": 0.85,
#     "grapefruit": 1.45,
#     "kiwi": 2.70,
#     "pineapple": 5.50,
#     "grapes": 3.85
# }
#
# weekend = {
#     "banana": 2.70,
#     "apple": 1.25,
#     "orange": 0.90,
#     "grapefruit": 1.60,
#     "kiwi": 3.00,
#     "pineapple": 5.60,
#     "grapes": 4.20
# }
#
# if day not in valid_days or product not in weekend:
#     print("error")
# elif day in ["Saturday", "Sunday"]:
#     print(f"{format((weekend.get(product) * quantity), '.2f')}")
# else:
#     print(f"{format((weekday.get(product) * quantity), '.2f')}")

# city = input()
# sales = float(input())
#
#
# if city not in ["Sofia", "Varna", "Plovdiv"] or sales < 0:
#     print("error")
# if city == "Sofia":
#     if 0 <= sales <= 500:
#         print(f"{sales * 0.05:.2f}")
#     elif 500 <= sales <= 1000:
#         print(f"{sales * 0.07:.2f}")
#     elif 1000 <= sales <= 10000:
#         print(f"{sales * 0.08:.2f}")
#     elif sales > 10000:
#         print(f"{sales * 0.12:.2f}")
# elif city == "Varna":
#     if 0 <= sales <= 500:
#         print(f"{sales * 0.045:.2f}")
#     elif 500 <= sales <= 1000:
#         print(f"{sales * 0.075:.2f}")
#     elif 1000 <= sales <= 10000:
#         print(f"{sales * 0.1:.2f}")
#     elif sales > 10000:
#         print(f"{sales * 0.13:.2f}")
# elif city == "Plovdiv":
#     if 0 <= sales <= 500:
#         print(f"{sales * 0.055:.2f}")
#     elif 500 <= sales <= 1000:
#         print(f"{sales * 0.08:.2f}")
#     elif 1000 <= sales <= 10000:
#         print(f"{sales * 0.12:.2f}")
#     elif sales > 10000:
#         print(f"{sales * 0.145:.2f}")

# nights = int(input()) - 1
# room = input()
# rating = input()
#
# if room == "apartment":
#     if nights < 10:
#         price = 25 * nights - 25 * nights * 0.30
#     elif 15 > nights >= 10:
#         price = 25 * nights - 25 * nights * 0.35
#     elif nights > 15:
#         price = 25 * nights - 25 * nights * 0.50
# elif room == "president apartment":
#     if nights < 10:
#         price = 35 * nights - 35 * nights * 0.10
#     elif 15 > nights >= 10:
#         price = 35 * nights - 35 * nights * 0.15
#     elif nights > 15:
#         price = 35 * nights - 35 * nights * 0.20
# else:
#     price = 18 * nights
#
# if rating == "positive":
#     price += price*0.25
# else:
#     price -= price*0.1
#
# print(f'{price:.2f}')

# screening_type = input()
# rows = int(input())
# columns = int(input())
#
# if screening_type == "Premiere":
#     income = rows * columns * 12
# elif screening_type == "Normal":
#     income = rows * columns * 7.50
# else:
#     income = rows * columns * 5
#
# print(f"{income:.2f}")

# temperature = int(input())
# time_of_day = input()
#
# if time_of_day == "Morning":
#     if 10 <= temperature <= 18:
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif 18 < temperature <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     else:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
# elif time_of_day == "Afternoon":
#     if 10 <= temperature <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < temperature <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     else:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
# else:
#     if 10 <= temperature <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < temperature <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     else:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# print(f"It's {temperature} degrees, get your {outfit} and {shoes}")

# flower = input()
# number = int(input())
# budget = int(input())
#
# if flower == "Roses":
#     cost = number * 5
#     if number > 80:
#         cost = cost - cost * 0.1
# if flower == "Dahlias":
#     cost = number * 3.80
#     if number > 90:
#         cost = cost - cost * 0.15
# if flower == "Tulips":
#     cost = number * 2.80
#     if number > 80:
#         cost = cost - cost * 0.15
# if flower == "Narcissus":
#     cost = number * 3
#     if number < 120:
#         cost = cost + cost * 0.15
# if flower == "Gladiolus":
#     cost = number * 2.50
#     if number < 80:
#         cost = cost + cost * 0.20
# cost = round(cost, 2)
#
#
# if cost <= budget:
#     print(f"Hey, you have a great garden with {number} {flower} and {budget-cost:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {cost-budget:.2f} leva more.")

## This doesnt work ???
# budget = int(input())
# season = input()
# headcount = int(input())
#
# if season == "Spring":
#     cost = 3000
# if season == "Summer" or "Autumn":
#     cost = 4200
# if season == "Winter":
#     cost = 2600
#
# if headcount <= 6:
#     cost -= cost * 0.1
# if 6 < headcount <= 11:
#     cost -= cost * 0.15
# if headcount > 11:
#     cost -= cost * 0.25
#
#
# if headcount % 2 == 0 and season != "Autumn":
#     cost -= cost * 0.05
#
#
# if budget >= cost:
#     print(f"Yes! You have {budget - cost:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {cost - budget:.2f} leva.")

# #THIS WORKS :O
# budget = int(input())
# season = input()
# headcount = int(input())
#
# cost = 0
# if season == "Winter":
#     cost = 2600
# elif season == "Spring":
#     cost = 3000
# else:
#     cost = 4200
#
# if headcount <= 6:
#     cost -= cost*0.1
#
# elif 6 < headcount <= 11:
#     cost -= cost*0.15
#
# else:
#     cost -= cost*0.25
#
#
# if headcount % 2 == 0 and season != "Autumn":
#     cost -= cost*0.05
#
#
# if budget >= cost:
#     print(f"Yes! You have {budget - cost:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {cost - budget:.2f} leva.")


# budget = float(input())
# season = input()
#
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         accommodation = "Camp"
#         cost = budget * 0.3
#     else:
#         cost = budget * 0.7
#         accommodation = "Hotel"
#
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         cost = budget * 0.4
#         accommodation = "Camp"
#     else:
#         cost = budget * 0.8
#         accommodation = "Hotel"
#
# else:
#     destination = "Europe"
#     cost = budget * 0.9
#     accommodation = "Hotel"
#
# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {cost:.2f}")

# n1 = int(input())
# n2 = int(input())
# operator = input()
#
# if n2 == 0 and operator in ["/", "%"]:
#     print(f"Cannot divide {n1} by zero")
# elif operator == "+":
#     if (n1 + n2) % 2 == 0:
#         print(f"{n1} + {n2} = {n1 + n2} - even")
#     else:
#         print(f"{n1} + {n2} = {n1 + n2} - odd")
# elif operator == "-":
#     if (n1 - n2) % 2 == 0:
#         print(f"{n1} - {n2} = {n1 - n2} - even")
#     else:
#         print(f"{n1} - {n2} = {n1 - n2} - odd")
# elif operator == "*":
#     if (n1 * n2) % 2 == 0:
#         print(f"{n1} * {n2} = {n1 * n2} - even")
#     else:
#         print(f"{n1} * {n2} = {n1 * n2} - odd")
# elif operator == "/":
#     print(f"{n1} / {n2} = {n1 / n2:.2f}")
# elif operator == "%":
#     print(f"{n1} % {n2} = {n1 % n2}")

# month = input()
# nights = int(input())
#
# if month in ["May", "October"]:
#     cost_ap = nights * 65
#     cost_st = nights * 50
#     if nights > 14:
#         cost_st -= cost_st * 0.30
#         cost_ap -= cost_ap * 0.1
#     elif nights > 7:
#         cost_st -= cost_st * 0.05
# elif month in ["June", "September"]:
#     cost_ap = nights * 68.70
#     cost_st = nights * 75.20
#     if nights > 14:
#         cost_st -= cost_st * 0.2
#         cost_ap -= cost_ap * 0.1
# else:
#     cost_ap = nights * 77
#     cost_st = nights * 76
#     if nights > 14:
#         cost_ap -= cost_ap * 0.1
#
# print(f"Apartment: {cost_ap:.2f} lv.")
# print(f"Studio: {cost_st:.2f} lv.")

# exam_hr = int(input())
# exam_m = int(input())
# arrival_hr = int(input())
# arrival_m = int(input())
#
# exam = exam_hr * 60 + exam_m
# arrival = arrival_hr * 60 + arrival_m
#
# remainder = arrival - exam
#
#
# if remainder > 0:
#     print("late")
#     if remainder > 59:
#         if remainder % 60 < 10:
#             print(f"{int(remainder/60)}:0{remainder % 60} hours after the start")
#         if remainder % 60 > 9:
#             print(f"{int(remainder / 60)}:{remainder % 60} hours after the start")
#     else:
#         print(f"{remainder} minutes after the start")
# elif remainder < -30:
#     print("early")
#     remainder = remainder * -1
#     if remainder > 59:
#         if remainder % 60 <10:
#             print(f"{int(remainder / 60)}:0{remainder % 60} hours before the start")
#         if remainder % 60 > 9:
#             print(f"{int(remainder / 60)}:{remainder % 60} hours before the start")
#     else:
#         print(f"{remainder} minutes before the start")
# elif 0 > remainder >= -30:
#     print("on time")
#     remainder = remainder * -1
#
#     print(f"{remainder} minutes before the start")
# else:
#     print("on time")

# year = input()
# holidays = int(input())
# at_home = int(input())
# weekends = (48 - at_home) * 3/4
# holidays = holidays * 2/3
# if year == "leap":
#     total = holidays + weekends + at_home
#     total += total * 0.15
# else:
#     total = holidays + weekends + at_home
#
# print(int(total))

# n = int(input())
# for i in range(1, n+1, 3):
#     print(i)


# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# n = input()
# for i in n:
#     print(i)

# n = input()
# vowels = {
#     "a": 1,
#     "e": 2,
#     "i": 3,
#     "o": 4,
#     "u": 5
# }
# score = 0
# for i in n:
#     if i in list(vowels.keys()):
#         score += vowels.get(i)
# print(score)

# total = 0
# n = int(input())
# for i in range(n):
#     number = int(input())
#     total += number
#
# print(total)

# n = int(input())
# for i in range(0, n+1):
#     if i % 2 == 0:
#         print(2**i)

# numbers = []
# n = int(input())
#
# for i in range(n):
#     value = int(input())
#     numbers.append(value)
#
# print(f"Max number: {max(numbers)}")
# print(f"Min number: {min(numbers)}")

# n = int(input())
# n = 2*n
# numbers = []
# for i in range(n):
#     value = int(input())
#     numbers.append(value)
#
# left = sum(numbers[0:int(n/2)])
# right = sum(numbers[int(n/2):])
#
# if left == right:
#     print(f"Yes, sum = {left}")
# else:
#     print(f"No, diff = {int(abs(left - right))}")

# n = int(input())
# numbers = []
# for i in range(n):
#     value = int(input())
#     numbers.append(value)
#
# sum1 = sum(numbers[0:n:2])
# sum2 = sum(numbers[1:n:2])
#
# if sum1 == sum2:
#     print("Yes")
#     print(f"Sum = {sum1}")
# else:
#     print("No")
#     print(f"Diff = {int(abs(sum1-sum2))}")

# age = int(input()) + 1
# cost = float(input())
# toy_price = int(input())
# savings = 0
#
# for i in range(1, age):
#     if i % 2 == 0:
#         savings += (i/2)*10
#         savings -= 1
#     else:
#         savings += toy_price
#
# if savings >= cost:
#     print(f"Yes! {savings - cost:.2f}")
# else:
#     print(f"No! {cost-savings:.2f}")

# #trolled them noobs with generator expression :D
# x = (i for i in range(1, 1001) if i % 10 == 7)
# for i in x:
#     print(i)
# #noob version that Judge accepts:
# for i in range(1, 1001):
#     if i % 10 == 7:
#         print(i)

# n = int(input())
# numbers = []
# for i in range(n):
#     value = int(input())
#     numbers.append(value)
#
# if max(numbers) == sum(numbers) - max(numbers):
#     print("Yes")
#     print(f"Sum = {max(numbers)}")
# else:
#     print("No")
#     print(f"Diff = {int(abs(max(numbers) - (sum(numbers) - max(numbers))))}")

# n = int(input())
# numbers = []
# odd_nums = []
# even_nums = []
#
# for i in range(n):
#     value = float(input())
#     numbers.append(value)
#
# for i in range(1, len(numbers)+1):
#     if i % 2 != 0:
#         odd_nums.append(numbers[i-1])
#     else:
#         even_nums.append(numbers[i-1])
#
# if n == 0:
#     print("OddSum=0.00,")
#     print("OddMin=No,")
#     print("OddMax=No,")
#     print("EvenSum=0.00,")
#     print("EvenMin=No,")
#     print("EvenMax=No")
#
# else:
#     print(f"OddSum={sum(odd_nums):.2f},")
#     print(f"OddMin={min(odd_nums):.2f},")
#     print(f"OddMax={max(odd_nums):.2f},")
#     if len(even_nums) > 0:
#         print(f"EvenSum={sum(even_nums):.2f},")
#         print(f"EvenMin={min(even_nums):.2f},")
#         print(f"EvenMax={max(even_nums):.2f}")
#     else:
#         print("EvenSum=0.00,")
#         print("EvenMin=No,")
#         print("EvenMax=No")

# n = int(input())
# numbers = []
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
# for i in range(n):
#     value = int(input())
#     numbers.append(value)
#
# for number in numbers:
#     if number < 200:
#         p1 += 1
#     elif 200 <= number < 400:
#         p2 += 1
#     elif 400 <= number < 600:
#         p3 += 1
#     elif 600 <= number < 800:
#         p4 += 1
#     else:
#         p5 += 1
#
# print(f"{p1/n * 100:.2f}%")
# print(f"{p2/n * 100:.2f}%")
# print(f"{p3/n * 100:.2f}%")
# print(f"{p4/n * 100:.2f}%")
# print(f"{p5/n * 100:.2f}%")

# n = int(input())
# salary = int(input())
#
# for i in range(n):
#     site = input()
#     if site == "Facebook":
#         salary -= 150
#     if site == "Instagram":
#         salary -= 100
#     if site == "Reddit":
#         salary -= 50
#
# if salary > 0:
#     print(salary)
# else:
#     print("You have lost your salary.")


# while True:
#     word = input()
#     if word == "Stop":
#         break
#     else:
#         print(word)

# user = input()
# print(f"Welcome {user}!")
# pwd = input()
# data = input()
# while data != pwd:
#     data = input()

# n = int(input())
# total = []
# while n>0:
#     n2 = int(input())
#     n -= n2
#     total.append(n2)
# print(sum(total))

# n = int(input())
# a = 1
# while a <= n:
#     print(a)
#     a = a*2+1

##This solutions works perfect in Pycharm and gives expectedoutput but idiot Judge finds an unexpected EOF instead of proper output
# balance = 0
# while True:
#     increase = input()
#     if increase == "NoMoreMoney":
#         print(f"Total: {balance:.2f}")
#         break
#
#     if balance + float(increase) < 0:
#         print("Invalid operation!")
#         print(f"Total: {balance:.2f}")
#         break
#     balance += float(increase)
#     print(f"Increase: {float(increase):.2f}")
#

##Trash softuni version
# balance = 0
# increase = input()
# while increase != "NoMoreMoney":
#     amount = float(increase)
#     if amount < 0:
#         print("Invalid operation!")
#         break
#     balance += amount
#     print(f"Increase: {float(increase):.2f}")
#     increase = input()
# print(f"Total: {balance:.2f}")

# numbers = []
#
# while True:
#     value = input()
#     if value == "Stop":
#         break
#     numbers.append(int(value))
#
# print(max(numbers))

# name = input()
# sum_score = 0
# grade = 0
# exams_failed = 0
#
# while grade < 12 and exams_failed < 2:
#     score = float(input())
#     if score < 4.00:
#         exams_failed += 1
#         if exams_failed == 2:
#             break
#     grade += 1
#     sum_score += score
#
# if grade == 12:
#     average = sum_score / 12
#     print(f"{name} graduated. Average grade: {average:.2f}")
#
# if exams_failed == 2:
#     print(f"{name} has been excluded at {grade} grade")

# width = int(input())
# length = int(input())
# height = int(input())
# total_m3 = width * length * height
#
# while total_m3 >= 0:
#     boxes = input()
#     if boxes == "Done":
#         print(f"{total_m3} Cubic meters left.")
#         break
#     total_m3 -= int(boxes)
# else:
#     print(f"No more free space! You need {total_m3 * -1} Cubic meters more.")

# book_name = input()
# checked = 0
# found = False
# while not found:
#     current = input()
#     if current == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {checked} books.")
#         break
#     if current == book_name:
#         print(f"You checked {checked} books and found it.")
#         found = True
#     checked += 1

# allowed_fails = int(input())
# solved = 0
# failed = 0
# total_score = 0
# last_exercise = ""
# while True:
#     exercise = input()
#     if exercise == "Enough":
#         print(f"Average score: {total_score/(solved+failed):.2f}")
#         print(f"Number of problems: {solved+failed}")
#         print(f"Last problem: {last_exercise}")
#         break
#     last_exercise = exercise
#
#     score = int(input())
#     total_score += score
#     if score <= 4.00:
#         failed += 1
#     else:
#         solved += 1
#
#     if failed == allowed_fails:
#         print(f"You need a break, {failed} poor grades.")
#         break

# trip_cost = float(input())
# budget = float(input())
# spending_spree = 0
# days = 0
# while budget < trip_cost and spending_spree < 5:
#     operation = input()
#     amount = float(input())
#     days += 1
#     if operation == "save":
#         budget += amount
#         spending_spree = 0
#     else:
#         budget -= amount
#         spending_spree += 1
#         if budget < 0:
#             budget = 0
#
#
# if spending_spree == 5:
#     print("You can't save the money.")
#     print(days)
# if budget >= trip_cost:
#     print(f"You saved the money for {days} days.")

# target = 10000
# achieved = 0
# while achieved < 10000:
#     steps = input()
#     if steps == "Going home":
#         steps = int(input())
#         achieved += steps
#         break
#     achieved += (int(steps))
#
# if achieved >= target:
#     print("Goal reached! Good job!")
#     print(f"{achieved-target} steps over the goal!")
# else:
#     print(f"{target-achieved} more steps to reach goal.")

# number = float(input())
# number = int(number * 100)
#
# coins = {
#     200: 0,
#     100: 0,
#     50: 0,
#     20: 0,
#     10: 0,
#     5: 0,
#     2: 0,
#     1: 0
# }
#
# while number > 0:
#     for coin_value in coins:
#         if number >= coin_value:
#             # we subtract the coin from the number
#             number -= coin_value
#             # we increment the count of the coin
#             coins[coin_value] += 1
#             break
#
# print(sum(coins.values()))


# len = int(input())
# wid = int(input())
# total = len*wid
# while total >= 0:
#     inpt = input()
#     if inpt == "STOP":
#         print(f"{total} pieces are left.")
#         break
#     total -= int(inpt)
# else:
#     print(f"No more cake left! You need {total * -1} pieces more.")

# for i in range(24):
#     for j in range(60):
#         print(f"{i}:{j}")

# for i in range(1, 11):
#     for j in range(1,11):
#         k = i * j
#         print(f"{i} * {j} = {k}")

# n = int(input())
# combos = 0
# for x1 in range(0, n+1):
#     for x2 in range(0,n+1):
#         for x3 in range(0,n+10):
#             if x1+x2+x3 == n:
#                 combos += 1
# print(combos)

# start_num = int(input())
# end_num = int(input())
# magic_number = int(input())
# combos = 0
#
# found = False
#
# for i in range(start_num,end_num +1):
#     for j in range(start_num,end_num+1):
#         combos += 1
#         if i + j == magic_number:
#             found = True
#             break
#     if found:
#         break
#
# if found:
#     print(f"Combination N:{combos} ({i} + {j} = {magic_number})")
# else:
#     print(f"{combos} combinations - neither equals {magic_number}")

# #shorthand
# while True:
#     destination = input()
#     if destination == "End":
#         break
#     needed = float(input())
#     while needed > 0:
#         needed -= float(input())
#     print(f"Going to {destination}!")
# 
# #Softuni judge is bugged again, this works though
# #Descriptive version
# while True:
#     destination = input()
#     if destination == "End":
#         break
#     needed = int(input())
#     budget = 0
#     while budget < needed:
#         saved = int(input())
#         budget += saved
#         if budget >= needed:
#             print(f"Going to {destination}!")
#             break

# floors = int(input())
# units = int(input())
# for i in range(floors, 0, -1):
#     for j in range(0, units):
#         if i == floors:
#             if i > 99 and j < 10:
#                 print(f"L{i}0{j}", end=" " if j < units - 1 else "\n")
#             else:
#                 print(f"L{i}{j}", end=" " if j < units-1 else "\n")
#         elif i % 2 == 0:
#             if i > 99 and j < 10:
#                 print(f"O{i}0{j}", end=" " if j < units - 1 else "\n")
#             else:
#                 print(f"O{i}{j}", end=" " if j < units-1 else "\n")
#         else:
#             if i > 99 and j < 10:
#                 print(f"A{i}0{j}", end=" " if j < units - 1 else "\n")
#             else:
#                 print(f"A{i}{j}", end=" " if j < units-1 else "\n")
# #Another students version seems much shorter:
# floors = int(input())
# rooms = int(input())
# 
# for f in range(floors, 0, -1):
#     for r in range(rooms):
#         if f == floors:
#             print(f'L{f}{r}', end=' ')
#         elif f % 2 == 0:
#             print(f'O{f}{r}', end=' ')
#         else:
#             print(f'A{f}{r}', end=' ')
#     print()



##extracurricular
# per_line = int(input("How many numbers per line would you like: "))
#
# for number in range(1, 1000):
#     print(number, end = " " if number % per_line else "\n")


# movies_list = []
# capacity_list = []
# tickets_sold_list = []
# student_ticket_total = 0
# standard_ticket_total = 0
# kid_ticket_total = 0
# while True:
#     movie = input()
#     if movie == "Finish":
#         break
#     movies_list.append(movie)
#     capacity = int(input())
#     capacity_list.append(capacity)
#     student = 0
#     standard = 0
#     kid = 0
#     total = 0
#     while total < capacity:#capacity limiter
#         ticket_type = input()
#
#         if ticket_type == "student":
#             student += 1
#             student_ticket_total += 1
#         if ticket_type == "standard":
#             standard += 1
#             standard_ticket_total += 1
#         if ticket_type == "kid":
#             kid += 1
#             kid_ticket_total += 1
#         total = student + standard + kid
#         if ticket_type == "End" or total>= capacity:
#             break
#     tickets_sold_list.append(total)
#
# for index, movie in enumerate(movies_list):
#     print(f"{movie} - {tickets_sold_list[index]/capacity_list[index]*100:.2f}% full.")
# print("Total tickets:", sum(tickets_sold_list))
# print(f"{student_ticket_total/sum(tickets_sold_list)*100:.2f}% student tickets.")
# print(f"{standard_ticket_total/sum(tickets_sold_list)*100:.2f}% standard tickets.")
# print(f"{kid_ticket_total/sum(tickets_sold_list)*100:.2f}% kids tickets.")


# bigger_than_n = False
# current = 1
# n = int(input())
# for row in range(1, n+1):
#     for col in range(1, row+1):
#         if current > n:
#             bigger_than_n = True
#             break
#         print(str(current) + ' ', end="")
#         current += 1
#     if bigger_than_n:
#         break
#     print()

##SOFTUNI TRASH VERSION DOESNT
# num1 = int(input())
# num2 = int(input())
# even_sum = 0
# odd_sum = 0
# for number in range(num1, num2+1):
#     number_to_str = str(number)
#     for index, digit in enumerate(number_to_str):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#
#     if even_sum == odd_sum:
#         print(number, end=" ")

# #MY VERSION WORKS
# num1 = int(input())
# num2 = int(input())
# for number in range(num1, num2+1):
#     string = str(number)
#     even_sum = 0
#     odd_sum = 0
#     for index in range(len(string)):
#         if index % 2 == 0:
#             even_sum += int(string[index])
#         else:
#             odd_sum += int(string[index])
#
#     if even_sum == odd_sum:
#         print(number, end = " ")

# import math
# primes_sum = 0
# non_primes_sum = 0
# while True:
#     n = input()
#     if str(n) == "stop":
#         break
#     elif int(n) < 0:
#         print("Number is negative.")
#     elif int(n) == 0:
#         pass
#     elif int(n) in [2, 3, 5, 7]:
#         primes_sum += int(n)
#     elif int(n) > 2 and int(n) % 2 == 0:
#         non_primes_sum += int(n)
#     else:
#         max_divisor = int(math.sqrt(int(n)))
#         for i in range(3, 1 + max_divisor, 2):
#             if int(n) % i != 0:
#                 primes_sum += int(n)
#                 break
#             else:
#                 non_primes_sum += int(n)
#                 break
#
# print(f"Sum of all prime numbers is: {primes_sum}")
# print(f"Sum of all non prime numbers is: {non_primes_sum}")


# primes_sum = 0
# non_primes_sum = 0
# while True:
#     n = input()
#     if str(n) == "stop":
#         break
#     elif int(n) < 0:
#         print("Number is negative.")
#     elif int(n) == 0:
#         pass
#     elif int(n) > 2 and int(n) % 2 == 0:
#         non_primes_sum += int(n)
#     else:
#         if int(n) == 3:
#             primes_sum += int(n)
#         max_divisor = int(int(n)/2)
#         for i in range(3, 1 + max_divisor, 2):
#             if int(n) % i != 0:
#                 primes_sum += int(n)
#                 break
#             else:
#                 non_primes_sum += int(n)
#                 break
#
# print(f"Sum of all prime numbers is: {primes_sum}")
# print(f"Sum of all non prime numbers is: {non_primes_sum}")

# master_data = {}
# jury_count = int(input())
# while True:
#     discipline = input()
#     if discipline == "Finish":
#         break
#     master_data[discipline] = []
#     for i in range(jury_count):
#         score = float(input())
#         master_data[discipline].append(score)
#
# overall_average = []
#
# for discipline in master_data:
#     discipline_average = sum(master_data.get(discipline)) / len(master_data.get(discipline))
#     print(f"{discipline} - {discipline_average:.2f}.")
#     overall_average.append(discipline_average)
#
# print(f"Student's final assessment is {sum(overall_average)/len(overall_average):.2f}.")


# n = int(input())
# l = int(input())
# starter = "a" #counting from 0 for letters so no need to add 1 below in ord()
# for i in range(1, n):
#     for j in range(1, n):
#         for x in range(l):
#             for y in range(l):
#                 for k in range(1,n+1):
#                     if k > i and k > j:
#                         print(f"{i}{j}{chr(ord(starter) + x)}{chr(ord(starter) + y)}{k}", end=" ")


# n = int(input())
#
# for num1 in range(1,10):
#     for num2 in range(1,10):
#         for num3 in range(1,10):
#             for num4 in range(1,10):
#                 if n % num1 == 0 and n % num2 == 0 and n % num3 == 0 and n % num4 == 0:
#                     print(f"{num1}{num2}{num3}{num4}", end=" ")


