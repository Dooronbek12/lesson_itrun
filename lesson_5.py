# Для чего нужны исключения(try, except)?
# try ловить ошибки except исключает ошибки


# Словите ошибку ZeroDivisionError  и выведите “Делить на ноль нельзя! Ты чо вася”
# Словите ошибку TypeError и выведите “Ошибка типов данных! Иди читай notion”
# try:
#     a = 5
#     b = 0
#     c = a / b
#     d = "asas" + 12
# except ZeroDivisionError:
#     print("Делить на ноль нельзя! Ты чо вася")
# except TypeError:
#     print("Ошибка типов данных! Иди читай notion")


# 4 Задание
# age = int(input("Возраст: ")) 
# d = "Доступ разрешен" if age >= 18 and age <= 50 else "Вы уже старый"  if age > 50 else "Иди домой"
# print(d)


# 5 Задание
# my_passwords = ["qwerty", "12345678"] 
# user_input = input("Введите пароль: ") 
# password = "Пароль верный" if user_input in my_passwords else "Неверный пароль"
# print(password)


# 6 Задание
# number = int(input("Пожалуйста введите цифру: ")) 
# types = 'четным' if number % 2 == 0 else 'нечетным'
# print(f'Ваша цифра {number} является {types} .')


# 7 Задание
# boolean = True
# a = (f'{boolean} является истиной') if boolean else (f'{boolean} является ложью') 
# print(a)


# 8 Задание
# name = input("Ваша имя: ")
# names = ["Mark", "Kate", "Anna", "Smit"]
# a = (f"{name} в нашем классе") if name in names else (f"{name} не в нашем классе")
# print(a)


# 9 Задание
# lst = [] 
# for i in range(10): 
#     lst.append(i) 
# print(lst) 

# lst = []
# a = for i range(10)

# 10 Задание
# lst = [] 
# for i in range(10): 
#     if i % 2 == 0: 
#     lst.append(i) 
# print(lst) 


# 11 Задание
# cars = ["Bmw", "Mersedes", "Lexus", "Kia", "Lada"] 
# new_cars = [] 
# for x in cars: 
#     if "a" in x: 
#         new_cars.append(x) 
# print(new_cars) 

# # 12 Задание
# squares = [] 
# for i in range(10): 
#     squares.append(i ** 2) 
# print(squares) 
