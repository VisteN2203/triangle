# -Сделать ввод длины массива;
# -Сделать наполнение массива таким, чтобы пользователь сам наполнял массив числами;
# -Выбрать три числа, которые являются длинами отрезков, из которых состоит треугольник с максимально возможной площадью;
# -Вывести площадь и три числа, из которых составлен треугольник;
# -Обработать все возможные исключения;
import random
import math

array = []
larray = int(input('Введите длинну массива '))

if larray < 3:
    print("Пошёл нахуй,ПЁС")

for i in range(larray):
    array.append(random.randint(1,100))

array.sort(reverse=True)

for i in range(larray - 2):
    a = array[i]
    b = array[i +1]
    c = array[i + 2]

    if b + c > a:
        p=(a+b+c)/2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(s, a, b, c)
        break