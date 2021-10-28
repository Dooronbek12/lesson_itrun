    # Создайте модуль с двумя функциями, которые вычисляли бы периметр и площадь прямоугольника. Подключите этот модуль к основной программе и вызовите эти функции с аргументами.
# def perimeter(length, width):
#     p = length * 2 + width * 2
#     return(f"Периметр прямоугольника - {p}")


# def area(length, width):
#     a = length * width
#     return(f"Плошадь прямоугольника - {a}")



    # Создайте список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"] с помощью библиотеки random выведите из списка рандомное значение
# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
 
    # Выведите с помощью библиотеки time данное врем
    # сделал



    # У нас есть список lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]. Написать функцию которая переворачивает список.
# lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
# def ls():
#     i = lst[::-1]
#     return(i)
# print(ls())
# print(lst)



# Меню одного из успешных ресторанов представлено в виде словаря 
# menu = {
#     ‘beefstrogonoff’: 350,
#     ‘burger’: 200,
#     ‘meatloaf’: 500,
#     ‘chicken pot pie’: 400,
#     ‘beefshteks’: 650}
# # Доллар очень сильно поднялся, из-за чего владельцы заведения решили поднять цены на 50 сом. Вам необходимо создать новый словарь new_menu, который будет состоять из тех же пар ключ-значений, но с увеличенными на 50 сом ценами. Для решения использовать генератор словарей (dict comprehension) .
# menu = {
#     'beefstrogonoff': 350,
#     'burger': 200,
#     'meatloaf': 500,
#     'chicken pot pie': 400,
#     "beefshteks": 650}
# new_menu = {}
# for key, value in menu.items():
#     new_menu[key] = value + 50
# print(menu)
# print(new_menu)




#  Написать функцию, которая принимает hour(час), min(минуту), sec(секунды).  И вам нужно превратить их в секунды.
h = int(input('Введите часы: '))
m = int(input('Введите минуты: '))
s = int(input('Введите секунды: '))

def hour(h):
 
    second = h * 60 * 60
    return second

def min(m):
    second = m * 60
    return second

def sec(s):
    second = s
    return second

print(f" {h} час будет - {hour(h)} секунда\n {m} минута будет - {min(m)} секунда\n {h} секунда равняется - {sec(s)} секунды\n")