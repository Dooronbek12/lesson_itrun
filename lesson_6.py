# 1)Создать функцию calc(a, b, operation). Описание входных параметров:
# Первое число
# Второе число
# Действие над ними:
#    1) + Сложить
#    2) - Вычесть
#    3) * Умножить
#    4) / Разделить
#    5) В остальных случаях функция должна возвращать "Операция не поддерживается"

def calc(a, b, operation):
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print