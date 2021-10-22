# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# second =input("+,-,*,/")

# if second == "+":
#     print(a + b)

# elif second == "-":
#     print(a - b)

# elif second == "*":
#     print(a * b)

# elif second == "/":
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print("Не возможно делить на ноль!")

# else:
#     print("Ошибка!")
# try:
#     print(5+"txt")
# except TypeError:
#     print("Ошибка TypeError")
# a =input("Первое число:")
# b = input("Второе число:")
# if a > b:
#     print("a больше b")
# elif a < b:
#     print("b больше a")
# else:
#     print("Числ о равен")
# a,b,c = 25,10,115
# max = a if a > b and a > c else b
# print(max)

# a, b = 21,45
# print('python') if a > b else print("javascript")
# name = "Marty"
# age = 30.5
# age_sotka = 100
# asd = "Privet  Shef {0}, Mne karoche {1} lgod" .format(name, age) 
# print(len(asd)
# def PositiveChislo(x):
#     if x <=0:
#         return True
#     else:
#         return False

# p = []
# for a in range(-1000,1000):
#     if PositiveChislo(a):
#         p.append(a)
# print(p)

def main():
    operation = input('\nВыберите действие(+,-,*,/')

    if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Пжл, введите нормальное число")
    else:
        while True:
            try:
                var1 = float(input('Введите первое число: '))
                var1 = float(input('Введите второе число: '))
            except ValueError:
                print("Пжл только цифры")
                continue
            else:
                break
            print("Ответ: ")
            if operation == "+":
                print(var1+var2)
            if operation == "-":
                print(var1-var2)
            if operation == "*":
                print(var1*var2)
            if operation == "/":
                try:
                    print(var1/var2)
                except ZeroDivisionError:
                    print("На нолб желить нельзя")
while True:
    main()               


            