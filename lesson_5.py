# Для чего нужны исключения(try, except)?
# try ловить ошибки except исключает ошибки


# Словите ошибку ZeroDivisionError  и выведите “Делить на ноль нельзя! Ты чо вася”
# Словите ошибку TypeError и выведите “Ошибка типов данных! Иди читай notion”
try:
    a = 5
    b = 0
    c = a / b
    d = "asas" + 12
except ZeroDivisionError:
    print("Делить на ноль нельзя! Ты чо вася")
except TypeError:
    print("Ошибка типов данных! Иди читай notion")
