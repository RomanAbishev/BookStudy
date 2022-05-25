# name = input("Введите имя: ") 
# surname = input("Введите фамилию:")

# print("Hello " + name + " " + surname)
# print ("What do you call a bear with no teeth?\nA gummy bear")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# answer = num1 + num2
# RA = answer * num3
# print("The total is ", RA)

# num1 = int(input("Сколько кусков пиццы было у вас?: "))
# num2 = int(input("Сколько кусков пиццы вы сьели?: "))
# SliceOfPizza = num1 - num2
# print("Поздравляю у Вас осталось:", SliceOfPizza, "кусков пиццы")

# name = input("Введите Ваше имя: ")
# Age = int(input("Введите Ваш возраст: "))
# Age2 = Age + 1
# print(name + " next birhday you will be", Age2)

# sumcheck = int(input("Введите общую сумму счета: "))
# people = int(input("Сколько человек обедали с Вами: "))
# share = sumcheck / people
# print("Для ровного счета каждый должен будет заплатить", share)

# Days = int(input("Введите промежуток времени в днях: "))
# hours = Days * 24
# minute = hours * 60
# seconds = minute * 60
# print(Days, " дней это\n", hours, "часов\n", minute, "минут\n", seconds, "секунд" )

# KG = int(input("Сколько киллограмм вы хотите перевести в фунты?: "))
# Pounds = KG * 2.204
# print(Pounds, "столько фунтов в введенном вами количестве килограмм")

# num1 = int(input("Введите число больше 100: "))
# num2 = int(input("Введите число меньше 10: "))
# answer = num1 // num2
# print("меньшее число в ", answer, "раз меньше большего")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#  print(num2, num1)
# else:
#  print(num1, num2)

# num1 = int(input("Введите число меньше 20: "))
# if num1 >= 20:
#   print("Вы ввели слишком большое число")
# else:
#   print("Спасибо")
 
# num1 = int(input("Введите число от 10 до 20: "))
# if num1 >= 10 and num1 <= 20:
#   print("Спасибо ")
# else:
#   print("Введенное число не из диапазона")

# color = input("Введите любимый цвет: ")
# color = str.lower(color)
# if color == "red" or color == "красный":
#   print("Я тоже люблю " + color + " цвет")
# else:
#   print("Мне не нравится " + color + ", я люблю красный")

# weather = input("Идет ли на улице дождь?")
# weather = str.lower(weather)
# if weather == "yes" or weather == "да":
#   wind = input("Ветренно ли на улице? ")
#   wind = str.lower(wind)
#   if wind == "yes" or wind == "да":
#    print("Слишком ветренно для зонта, оставайтесь дома")
#   else:
#     print("Не забудьте зонтик")
# else:
#   print("Надеюсь день Вам понравится")

# age = int(input("Введите ваш возраст "))
# if age >= 18:
#   print("You can vote")
# elif age == 17:
#  print("You can learn to drive")
# elif age == 16:
#   print("You can buy a lottery ticket")
# else:
#   print("You can go Trick-or-Treating")

# number = int(input("Введите число "))
# if number < 10:
#   print("Too low")
# elif number >= 10 and number <= 20:
#   print("correct")
# else:
#   print("Too high")

# num = int(input("Введите число 1, 2 или 3: "))
# if num == 1:
#   print("Thank you")
# elif num == 2:
#   print("Well done")
# elif num == 3:
#   print("Correct")
# else:
#   print("Error message")

# name = input("Введите ваше имя ")
# print(name.title())
# print("Hello world"[0:3])
  
# name = input("Please rigth you name: ")
# print(len(name))

# name = input("rigth you name ")
# surname = input("rigth you surname ")
# NS = name +" "+surname
# length = len(NS)
# print(NS + "\n", length)

# name = input("rigth you name in lower case ")
# surname = input("rigth you surname in lower case ")
# NS = name + " " + surname
# print(NS.title())

# poem = input("enter the first line of the poem ")
# print(len(poem))
# gap = int(input("enter first number"))
# gap1 = int(input("enter last number of the gap "))
# print(poem[gap:gap1])

# name = input("введите имя ")
# print(name.upper())

# name = input("enter you name ")
# name1 = len(name)

# if name1 < 5:
#   surname = input("enter surname ")
#   NS = name + surname
#   print(NS.upper())
# elif name1 >= 5:
#   name = str(name)
#   print(name.lower())

# word = input("Please enter a word: ")
# first = word[0]
# length = len(word)
# rest = word[1:length]
# if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
#  newword = rest + first + "ay"
# else:
#  newword = word + "way"
# print(newword.lower())

# import math

# number = float(input("ввести число с большим количеством знаков в дробной части "))
# rezults = number * 2
# print(round(rezults, 2))

# num_pi = math.pi
# print(round(num_pi, 5))

# num = float(input("Введите число больше 500 "))
# if num >= 500:
#   rez = math.sqrt(num)
#   print("Корень из ", num, " равен" , round(rez, 2))
# else:
#   print("Не похоже, что это число больше 500")

# radius = float(input("Ввеите радиус круга "))
# sq = math.pi * (radius**2)
# print("Радиус круга", round(sq, 2))

# radius = int(input("Введите радиус цилиндра "))
# higth = int(input("Введите высоту цилиндра "))
# sq = math.pi * (radius**2)
# v_sq = sq * higth
# print("Объем цилинда", round(v_sq, 3))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# rez = num1//num2
# rez1 = num1%num2
# if num1 > num2:
#   print("You enter", num1, "and", num2, "if", num1, "divide on", num2, "rezults  was", rez, "with remains ", rez1 )
# else:
#   print("Ввеите первое число больше второго")

# shape = int(input("Выберите фигуру для расчета:\n 1) Квадрат\n 2) Треугольник\n расчета введите 1 или 2 "))
# if shape == 1:
#   sq = int(input("Введите длину стороны квадрата "))
#   s_sq = sq**2
#   print("Площадь квадрата равна ", s_sq)
# elif shape == 2:
#   tr = int(input("Введите длину стороны треугольника "))
#   higth_tr = int(input("Введите высоту треугольника проведенную к этой стороне "))
#   s_tr = (tr*higth_tr)*0.5
#   print("Прощадь треугольника равна ", s_tr)
# else:
#   print("Не похоже что вы ввели 1 или 2 ")

# name = input("enter you name ")
# count = int(input("enter number "))

# for i in range(1, (count+1)):
#   print(name)

# name = input("enter you name ")
# count = int(input("enter number "))
# for x in range(0, count):
#   for i in name:
#     print(i)

# num = int(input("enter a number between 1 and 12 "))
# if num >= 1 and num <= 12:
#   for i in range(1,11):
#     answer = i * num
#     print(i, "x", num, "=", answer)
# else:
#   print("Не похоже, что вы ввесли числа из заданного промежутка")

# num = int(input("enter number between 0 and 50 "))
# for i in range(50, num-1, -1):
#   print(i)

# name = input("enter you name ")
# num = int(input("enter number "))
# if num < 10:
#   for i in range(0, num):
#     print(name)
# else:
#   for x in range(0,3):
#     print("Too high")

# total = 0

# for i in range(0,5):
#   num = int(input("enter 5 number in order\n lets stars\n enter first number "))
#   answer = input("Добавлять ли данноу число в суммирование?\n yes or no ")
#   if answer == "y":
#     total = num + total
# print(total)

# road = int(input("В каком направлении вы хотите вести отчет?\n 1)в прямом или 2)обратном "))
# if road == 1:
#   num1 = int(input("enter number "))
#   for i in range(1, num1+1):
#     print(i)
# elif road == 2:
#   num = int(input("enter number less 20 "))
#   if num <= 20:
#     for x in range(20, num + 1, -1):
#       print(x)
#   else:
#     print("Looks like you enter number more 20")
# else:
#   print("i don`t understand")

# guests = int(input("how many guests you wont to invute? "))
# if guests < 10:
#   for i in range(0, guests):
#     name = input("Введите имя приглашенного человека ")
#     print(name + " has been invited")
# elif guests >= 10:
#   print("too many people")

# total = 0 
# while total <= 50: 
#  num = int(input("Enter a number 50 or less: ")) 
#  total = total + num 
# print("The total is ", total)

# num = int(input("Enter a number "))
# while num < 5:
#   num = int(input("enter number again "))
# print("the last number was a ", num)


# num = int(input("Enter a first number "))
# total = num 
# again = "y"
# while again == "y":
#   num2 = int(input("enter number again "))
#   total = total + num2
#   again = input("Do you want to add another number, y/n? ")
    
# print("The summ is ", total)


# guest = 0
# again = "y"
# while again == "y":
#   name2 = input("enter new name ")
#   print(name2 + " has been invited")
#   guest = guest + 1
#   again = input("Хотите еще кого-то пригласить, y/n? ")
# print("вы пригласили", guest, "гостей")

# compnum = 50
# guess = int(input("Can you guess the number I am thinking of? "))
# attempts = 1
# while guess != 50:
#   if guess < 50:
#     print("too low")
#   else:
#     print("too high")
#   attempts = attempts +1
#   guess = int(input("Have another guess "))
# print("Well done, you took", attempts, "attempts")


# num1 = int(input("enter number between 10 and 20 "))
# while num1 < 10 or num1 > 20:
#   if num1 < 10:
#     print("too low")
#   else:
#     print("too high")
#   num1 = int(input("try one more time "))
# print("thank you")

# num = 10
# while num > 0:
#   print("There are ", num, " green bottles hanging on the wall.")
#   print( num, " green bottles hanging on the wall.")
#   print("And if 1 green bottle should accidentally fall,")
#   num = num - 1
#   answer = int(input("How many bottles will be handing on the wall? "))
#   if answer == num:
#     print("There will be ", num, "green bottels handing on the wall. ")
#   else:
#     while answer != num:
#       answer = int(input("No, try again: "))
# print("There are no more bottles handing on the wall")

# import random
# num = random.randint(0, 100)
# print(num)

# colour = random.choice(["Яблоко", "Груша", "Манго", "Банан", "Киви"])
# print(colour)

# guess = random.choice(["h", "t"])
# answer = input("guess heads or tails, h/t? ")
# if guess == answer:
#   print("Well done, you win")
# else:
#   print("Bad luck ")
# if guess == "h":
#   print("It was heads ")
# else:
#   print("It was tails")

# import random
# num = random.randint(1, 5)
# answer = int(input("enter number 1 - 5 "))
# if answer == num:
#   print("Well done")
# elif answer < num:
#   print("Вы ввели число меньше загаданного ")
#   answer = int(input("I give you one more try "))
#   if answer == num:
#     print("Correct")
#   else:
#     print("you lose")
# elif answer > num:
#   print("Вы ввели число больше загаданного")
#   answer = int(input("I give you one more try "))
#   if answer == num:
#     print("Correct")
#   else:
#     print("you lose")
# print("rigth answer was", num)

# import random
# num = random.randint(1, 10)
# correct = False
# while correct == False:
#   answer = int(input("Enter you guess "))
#   if answer == num:
#     correct = True
#   elif answer > num:
#     print("too high")
#   else:
#     print("too low")
# print("well done, rigth answer is ", num)

# import random
# score = 0
# for i in range(1, 6):
#   num1 = random.randint(1, 50)
#   num2 = random.randint(1, 50)
#   correct = num1 + num2
#   print(num1, "+", num2, "= ?")
#   answer = int(input("Your answer: "))
#   print()
#   if answer == correct:
#     score = score + 1
# print("You scored ", score, " out of 5")

# import random
# colour = random.choice(["red","blue","green","white", "pink"])
# print("sekect from red, blue, green, white or pink")
# tryagain = True
# while tryagain == True:
#   theirchoice = input("Выберете цвет ")
#   theirchoice = theirchoice.lower()
#   if colour == theirchoice:
#     print("Well done")
#     tryagain = False
#   else:
#     if colour == "red":
#       print("I bet are seeing RED right now!")
#     elif colour == "blue":
#       print("Don`t feel BLUE")
#     elif colour == "green":
#       print("I bet you are GREEN with envy right now ")
#     elif colour == "white":
#       print("Are you White as a sheet, as you didn`t guess correctly?")
#     elif colour == "pink":
#       print("Some of you are not feeling in the PINK, as got it wrong!")

# country_tuple = ("Russia", "USA", "Ukrain", "England", "France")
# print(country_tuple)
# country = input("Enter one of these countries ")
# print(country, " has index number ", country_tuple.index(country))
# num = int(input("Enter a number between 0 and 4: "))
# print(country_tuple[num])  

# sports = ["Basketball", "Football"]
# sports.append(input("Enter you favourite sport: "))
# print(sorted(sports))

# subject_list = ["Math", "Geo", "Fiz", "Chem", "Informath", "Hisory"]
# print(subject_list)
# correct = True
# while correct == True:
#   dislike = input("Which of thesee subjects do you dislike? ")
#   subject_list.remove(dislike)
#   print("selected subject is deleted ")
#   dislike1 = input("Do you want remove once more subject? y/n ")
#   if dislike1 == "n":
#     print("you subject list is ", subject_list)
#     correct = False
#   elif dislike1 == "y":
#     correct = True
#   else:
#     print("I don`t understand you, bye ")
#     correct = False
      
# subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
# print(subject_list)
# dislike = input("Which of these subjects do you dislike? ")
# getrid = subject_list.index(dislike)
# del subject_list[getrid]
# print(subject_list)  
  

# food_dictionary = {}
# food1 = input("Enter a food you like: ")
# food_dictionary[1] = food1
# food2 = input("Enter another food you like: ")
# food_dictionary[2] = food2
# food3 = input("Enter a third food you like: ")
# food_dictionary[3] = food3
# food4 = input("Enter one last food you like: ")
# food_dictionary[4] = food4
# print(food_dictionary)
# dislike = int(input("Which of these do you want to get rid of? "))
# del food_dictionary[dislike]
# print(sorted(food_dictionary.values()))


# colours = ["blue", "white", "red", "green", "yellow", "sky", "pink", "purple", "black", "orange"]
# print(colours)
# num1 = int(input("enter first number between 0 and 4 "))
# num2 = int(input("enter second number between 5 and 9 "))
# print(colours[num1:num2])

# numbers = [123, 375, 282, 777]
# for i in numbers:
#   print(i)
# you_number = int(input("enter number of the list "))
# if you_number in numbers:
#   print(you_number, " is in the list on ", numbers.index(you_number), "position")
# else:
#   print("number ", you_number, " is not in the list")


# guest1 = input("enter first guest ")
# guest2 = input("enter first guest ")
# guest3 = input("enter first guest ")
# names = [guest1, guest2, guest3]
# mg = True
# while mg == True:
#   again = input("do you want invite more guests? y/n ")
#   if again == "n":
#     mg = False
#   elif again == "y":
#     new_guest = names.append(input("enter one more guest "))
#     mg = True
#   else:
#     print("pardn I don`t understand you ")
#     mg = True
# print("You have", len(names), " people coming to your party")
# print(names)
# mg1 = True
# while mg1 == True:
#   selection = input("enter one of the names: ")
#   print(selection, "is in position ", names.index(selection), " in the list")
#   stillcome = input("Do yoy still want them to come? y/n ")
#   if stillcome == "n":
#     names.remove(selection)
#     print(names)
#     mg1 = True
#   else:
#     mg1 = False
# print(names)
  
# name = input("Введите ваше имя ")
# print(len(name))
# surname = input("Введите фамилию ")
# print(len(surname))
# print(name + " " + surname)
# fullname = name + " " + surname
# print(len(fullname))

# subject = input("Введите любимый школьный предмет ")
# for letter in subject:
#   print(letter, end="-")


# poem = "Мороз и солнце день чудесный"
# print(poem)
# fnum = int(input("Выберите начальную позицию "))
# snum = int(input("Выберите конечную позицию "))
# print(poem[fnum:snum])

# f_attempt = input("Придумайте пароль ")
# s_attempt = input("Введите пароль еще раз ")
# if f_attempt == s_attempt:
#   print("Thank you")
  
# elif f_attempt.lower() == s_attempt:
#   print("Пароли должны бытиь в одном регистре ")
# else:
#     print("Введенные пароли не совпадают, попробуйте еще раз ")

# postcode = input("Введите почтовый индекс ")
# start = postcode[0:2]
# print(start.upper())

# name = input("Введите ваше имя ")
# count = 0
# for x in name:
#   if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#     count = count + 1
# print("Volwes = ", count)

# word = input("Enter a word ")
# length = len(word)
# num = 1
# for x in word:
#   position = length - num
#   letter = word[position]
#   print(letter)
#   num = num + 1
  
# from array import *

# newArray = array ('i', [])
# more = int(input("How many items: "))
# for y in range(0,more):
#  newValue=int(input("Enter num: "))
#  newArray.append(newValue)
# print(newArray)
# print(newArray.count(13))

# nums = array ('i', [])

# for y in range(0, 5):
#   newValue = int(input("Enter a number "))
#   nums.append(newValue)
  
# nums = sorted(nums)
# nums.reverse()
# print(nums)

# nums = array('i', [])
# for i in range (0, 5):
#   num = random.randint(1, 100)
#   nums.append(num)
#   nums = sorted(nums)
# for i in nums:
#   print(i)

# nums = array ('i', [])

# while len(nums) < 5:
#   num = int(input("Enter a number between 10 and 20 "))
#   if num >=10 and num <= 20:
#     nums.append(num)
#   else:
#     print("Outside the range")
# nums = sorted(nums)
# for i in nums:
#   print(i)

# nums = array('i', [1, 2, 15, 2, 15])
# for i in nums:
#   print(i)
  
# num = int(input("Enter a number from array "))
# if nums.count(num) == 1:
#   print(num, "is in the list once")
# else:
#   print(num, "is in the list ", nums.count(num), " times")

  
# from array import *

# newArray = array ('i', [])
# more = int(input("How many items: "))
# for y in range(0,more):
#  newValue=int(input("Enter num: "))
#  newArray.append(newValue)
# print(newArray)
# print(newArray.count(13))

# nums = array ('i', [])

# for y in range(0, 5):
#   newValue = int(input("Enter a number "))
#   nums.append(newValue)
  
# nums = sorted(nums)
# nums.reverse()
# print(nums)

# nums = array('i', [])
# for i in range (0, 5):
#   num = random.randint(1, 100)
#   nums.append(num)
#   nums = sorted(nums)
# for i in nums:
#   print(i)

# nums = array ('i', [])

# while len(nums) < 5:
#   num = int(input("Enter a number between 10 and 20 "))
#   if num >=10 and num <= 20:
#     nums.append(num)
#   else:
#     print("Outside the range")
# nums = sorted(nums)
# for i in nums:
#   print(i)

# nums = array('i', [1, 2, 15, 2, 15])
# for i in nums:
#   print(i)
  
# num = int(input("Enter a number from array "))
# if nums.count(num) == 1:
#   print(num, "is in the list once")
# else:
#   print(num, "is in the list ", nums.count(num), " times")

from array import *
import random

farray = array('i', [])
for y in range(0, 3):
 newValue = int(input("Enter a number "))
 farray.append(newValue)

sarray = array('i', [])
for i in range(0, 5):
  num = random.randint(1, 100)
  sarray.append(num)
farray.extend(sarray)
farray = sorted(farray)

for a in farray:
  print(a)
  
  
  



  




    





  
  
  
  







            






  






  

  


