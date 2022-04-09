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



            






  






  

  


