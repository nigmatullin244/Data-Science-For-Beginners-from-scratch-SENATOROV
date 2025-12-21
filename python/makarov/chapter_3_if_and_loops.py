"""Условия и циклы.

Продолжение.
"""

from typing import Union

# +
# Еще раз про условия с if
# напишем программу, которая разобьет все числа на малые,
# средние и большие

# запросим число у пользователя и преобразуем в тип int
x_var = int(input())

# и наконец классифицируем число
if x_var < 10:
    print("Small number")
elif x_var < 100:
    print("Medium number")
else:
    print("Large number")

# +
# Несколько условий в одном выражении с операторами and или or

x_var = int(input())

if x_var < 10 or x_var > 100:
    print("Small or large number")
else:
    print("Medium number")

# +
# Проверка вхождения элемента в объект с in / not in

# можно проверить вхождение слова в строку
sentence = "To be, or not to be, that is the question"
word = "question"
if word in sentence:
    print(f"Слово {word} найдено.")
# -

# или отсутствие элемента в списке
my_list = [1, 2, 3, 4, 5]
number = 10
if number not in my_list:
    print(f"Элемент {number} отсутствует в списке.")

# +
# кроме того, можно проверить вхождение ключа и значения в словарь

# возьмем очень простой словарь
d_var = {"apple": 3, "tomato": 6, "carrot": 2}
# вначале поищем яблоки среди ключей словаря
if "apple" in d_var:
    print("Нашлись")
# а затем посмотрим, нет ли числа 6 среди его значений
# с помощью метода .values()
if 6 in d_var.values():
    print("Есть")

# +
# Циклы в питоне
# цикл for

# поочередно выведем элементы списка
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# +
# создадим словарь, значениями которого будут списки из двух элементов
# затем создадим две переменные-контейнера и применим метод .items()

goods_dict: dict[str, list[Union[int, str]]] = {
    "apple": [3, "kg"],
    "tomato": [6, "pcs"],
    "carrot": [2, "kg"],
}

for key, value in goods_dict.items():
    print(key, value)
# -

# возьмем только одну переменную и применим метод .values()
for value in goods_dict.values():
    # значение представляет собой список, выведем его первый
    # элемент с индексом [0]
    print(value[0])

# предположим, что у нас есть следующая база данных клиентов
clients = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}

for i, info in clients.items():
    print(f"clientID: {i}")

    # во втором цикле возьмем информацию об этом клиенте (это тоже словарь)
    for field_name, field_value in info.items():
        # и выведем каждый ключ (название поля) и значение (саму информацию)
        print(f"{field_name}: {field_value}")
    # добавим пустую строку после того, как выведем информацию об одном клиенте
    print()

# создадим последовательность от 0 до 4
for i in range(5):
    print(i)

# и от 0 до 5 с шагом 2 (то есть будем выводить числа через одно)
for i in range(0, 6, 2):
    print(i)

# возьмем месяцы года
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
# и продажи мороженого в тыс. рублей в каждый из месяцев
sales = [120, 150, 170, 130, 160, 180, 200, 210, 190, 220, 230, 250]
# задав последовательность через enumerate,
for i, month in enumerate(months):
    # мы можем вывести каждый из элементов обоих списков в одном цикле
    print(f"{i}: {month}, {sales[i]}")

# выведем числа от 1 до 10, но только четные
for i in range(1, 11):
    # если число четное, выведем его
    if i % 2 == 0:
        print(i)

# +
# Последовательность в обратном порядке
# Способ 1. Функция reversed()

# создадим список
my_list = [1, 2, 3, 4, 5]

# выведем элементы списка в обратном порядке с помощью функции reversed()
for item in reversed(my_list):
    print(item)
# -

# или с помощью range()
for i in reversed(range(5)):
    print(i)

# Способ 2. Указать  −1  в качестве параметра шага
# чтобы вывести 0, вторым параметром нужно указать -1
for i in range(4, -1, -1):
    print(i)

# +
# Способ 3. Функция sorted()

for i in sorted(my_list, reverse=True):
    print(i)

# +
# Функция enumerate()
# пусть дан список с днями недели
# pylint: disable=duplicate-code
days = [
    "Monday",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

# выведем индекс (i) и сами элементы списка (day)
# выведем индекс и элементы списка, но начнем с 1
for i, day in enumerate(days, start=1):
    print(i, day)
# -

# Цикл while
# зададим начальное значение счетчика
counter = 0
# пока счетчик меньше трех
while counter < 3:
    print(f"Текущее значение счетчика: {counter}")
    # увеличим значение счетчика на единицу
    counter += 1
    print(f"Новое значение счетчика: {counter}\n")

# +
# Break, continue
# Оператор break

# создадим константу для выхода из цикла и счетчик
EXIT_NUMBER = 5
counter = 0
# создадим бесконечный цикл
while True:
    # сделаем условие выхода из цикла
    if counter == EXIT_NUMBER:
        break
    counter += 1
    print(counter)

# +
# Оператор continue

# выведем числа от 1 до 10, но только четные c помощью оператора continue
for i in range(1, 11):
    # если число нечетное, пропустим его
    if i % 2 != 0:
        continue
    # если число четное, выведем его
    print(i)
