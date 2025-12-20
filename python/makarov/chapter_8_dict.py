"""Словарь."""

# # Понятие словаря в Питоне

# +
# пустой словарь можно создать с помощью {} или функции dict()
# Способ 3. Класс Counter модуля collections
from collections import Counter

# Небольшое отступление от темы. Сложные структуры данных бывает
# удобно вывести с помощью функции pprint() одноименного модуля.
from pprint import pprint

import numpy as np

empty_dict1: dict[str, int] = {}
empty_dict2: dict[str, int] = {}
print(empty_dict1)  # {}
print(empty_dict2)  # {}
# -

# словарь можно сразу заполнить ключами и значениями
person1: dict[str, str | int] = {"name": "Alice", "age": 30, "city": "New York"}
person1

# словарь можно создать из вложенных кортежей
nested_list: list[tuple[str, int]] = [("a", 1), ("b", 2), ("c", 3)]
dict_from_nested_list: dict[str, int] = dict(nested_list)
dict_from_nested_list

# если поместить ключи в кортеж и задать значение
keys1: tuple[str, ...] = ("name", "age", "city")
value: int = 0
person2: dict[str, int] = dict.fromkeys(keys1, value)
person2

# # Ключи и значения словаря

# +
# Ключами словаря могут быть только неизменяемые типы данных.
# Например, строки, числа, кортежи или логические значения
# (Boolean). Кроме того, ключи должны быть уникальными и
# соответственно не могут повторяться.

# Значения словаря, наоборот, могут состоять из чисел, строк,
# пропущенных (NaN) и логических значений, значения типа None,
# списков, массивов Numpy и вложенных словарей.
# -

# приведем пример того, какими могут быть значения словаря
value_types: dict[str, object] = {
    "k1": 123,
    "k2": "string",
    "k3": np.nan,  # тип "Пропущенное значение"
    "k4": True,  # логическое значение
    "k5": None,
    "k6": [1, 2, 3],
    "k7": np.array([1, 2, 3]),
    "k8": {1: "v1", 2: "v2", 3: "v3"},
}
value_types

# # Методы .keys(), .values() и .items()

# создадим несложный словарь с информацией о сотруднике
person: dict[str, str | int] = {
    "name": "John Doe",
    "age": 28,
    "position": "Software Engineer",
    "department": "IT",
}
person

# посмотрим на ключи словаря
person.keys()

# значения
person.values()

# а также на пары ключ-значение в виде списка из кортежей
person.items()

# # Использование цикла for

# Ключи и значения словаря удобно просматривать с помощью
# цикла for и метода .items().
for key, person_value in person.items():
    print(f"Key: {key}, Value: {person_value}")

# Доступ по ключу и метод .get()
# Конкретное значение в словаре можно получить, введя название
# словаря и затем название ключа в квадратных скобках.
person["name"]

# Если такого ключа нет, Питон выдаст ошибку.
# Для того чтобы этого не произошло, можно использовать метод
# .get(). Он также выводит значение по ключу.
person.get("name")

# Если ключа в словаре нет, метод .get() возвращает значение
# None.
print(person.get("salary"))  # ключа "salary" нет в словаре

# # Проверка наличия ключа и значения в словаре

# С помощью оператора in мы можем проверить наличие
# определенного ключа в словаре.
print("age" in person)  # True
print("salary" in person)  # False

# Метод .items() поможет проверить наличие пары ключ : значение.
# Обратите внимание, эту пару мы записываем в форме кортежа.
print(("age", 28) in person.items())  # True

# # Операции со словарями

# Добавление и изменение элементов
# Добавить элемент можно, передав новому ключу новое значение.
person["salary"] = 70000
person

# Изменить элемент можно передав существующему ключу новое
# значение.
person["age"] = 29
person

# Метод .update() позволяет соединить два словаря.
additional_info: dict[str, str] = {"email": "john.doe@example.com"}

# и присоединим его к существующему словарю с помощью метода
# .update()
person.update(additional_info)

person

# Метод .setdefault() не изменяет значение, если указанный ключ
# уже содержится в словаре.
person.setdefault("age", 35)  # ключ "age" уже есть в словаре
person

# Если такого ключа нет, ключ и соответствующее значение будут
# добавлены в словарь.
person.setdefault("phone", "123-456-7890")
person

# Удаление элементов
# Метод .pop() удаляет элемент по ключу и выводит удаляемое
# значение.
removed_value: str | int = person.pop("salary")
print(f"Removed value: {removed_value}")

# Убедимся, что этой пары ключа и значения больше нет в
# словаре.
person

# Ключевое слово del также удаляет элемент по ключу.
del person["phone"]
person

# Метод .popitem() удаляет и выводит последний добавленный в
# словарь элемент.
removed_item: tuple[str, str | int] = person.popitem()
print(f"Removed item: {removed_item}")

# Метод .clear() удаляет все ключи и значения и возвращает
# пустой словарь.
person.clear()
person

# +
# удалим весь словарь
del person

# если попытаться вновь вызвать эту переменную, Питон выдаст
# ошибку
# -

# # Сортировка словарей

# Для сортировки словарей можно использовать функцию sorted().
# возьмем несложный словарь
dict_to_sort: dict[str, int] = {
    "banana": 3,
    "apple": 5,
    "orange": 2,
}

# Отсортируем ключи этого словаря.
sorted(dict_to_sort)

# Теперь отсортируем значения с помощью метода .values().
sorted(dict_to_sort.values())

# Если мы хотим отсортировать пары «ключ : значение» по ключу
# или по значению, вначале воспользуемся методом .items() для
# извлечения этих пар (кортежей) из словаря.
dict_to_sort.items()

# для их сортировки по ключу (индекс [0]) воспользуемся методом
# .items() и lambda-функцией
sorted(dict_to_sort.items(), key=lambda item: item[0])

# сортировка по значению выполняется так же, однако
# lambda-функции мы передаем индекс [1]
sorted(dict_to_sort.items(), key=lambda item: item[1])

# # Копирование словарей

# создадим исходный словарь с количеством студентов на курсах
students_per_course: dict[str, int] = {
    "Course 1": 120,
    "Course 2": 95,
    "Course 3": 150,
}

# создадим копию исходного словаря с помощью метода .copy()
students_per_course_copy: dict[str, int] = students_per_course.copy()
students_per_course_copy

# добавим информацию о четвертом курсе в новый словарь
students_per_course_copy["Course 4"] = 80
students_per_course_copy

# выведем исходный и новый словари
print(f"Original dictionary: {students_per_course}")
print(f"New dictionary: {students_per_course_copy}")

# +
# Копирование через оператор присваивания = (так делать не стоит!)
# передадим исходный словарь в новую переменную
students_per_course_assigned: dict[str, int] = students_per_course

# удалим элементы нового словаря
students_per_course_assigned.clear()

# выведем исходный и новый словари
print(f"Original dictionary after clear: {students_per_course}")
print(f"Assigned dictionary after clear: {students_per_course_assigned}")
# -

# # Функция dir()

# функция dir() возвращает все методы передаваемого ей объекта
some_dict: dict[str, int] = {"a": 1, "b": 2}
dir(some_dict)

# +
# Вначале всегда идут так называемые специальные методы.
# Они начинаются и заканчиваются символом двойного подчеркивания
# __.

# Например, когда мы вызываем функцию print() и передаем ей
# словарь.
print(some_dict)
# -

# На самом деле мы применяем к словарю метод __str__().
str(some_dict)

# В большинстве случаев нас будут интересовать методы без
# символов двойного подчеркивания. Выведем последние 11
# элементов списка
dict_methods: list[str] = dir(some_dict)[-11:]
dict_methods

# # Dict comprehension

# +
# Dictionary comprehension, как и в случае со списками,
# позволяет превратить один словарь в другой. В процессе этого
# превращения, элементы исходного словаря могут быть изменены
# или отобраны на основе какого-либо условия.

# создадим еще один словарь
source_dict: dict[str, int] = {"k1": 2, "k2": 4, "k3": 6}
# -

# В первом примере умножим каждое значение на два.
new_dict: dict[str, int] = {key: value * 2 for key, value in source_dict.items()}
new_dict

# Во втором примере сделаем символы всех ключей заглавными
# с помощью метода .upper().
new_dict_upper: dict[str, int] = {
    key.upper(): value for key, value in source_dict.items()
}
new_dict_upper

# Теперь предположим, мы хотим отсортировать те пары, в которых
# значение больше двух, но меньше шести.
filtered_dict: dict[str, int] = {
    key: value for key, value in source_dict.items() if 2 < value < 6
}
filtered_dict

# +
# Если бы мы выполняли эту задачу с помощью цикла for, то
# использовали бы оператор И.
new_dict_loop: dict[str, int] = {}

for key, value in source_dict.items():
    if 2 < value < 6:
        # если условия верны, записываем ключ и значение в новый
        # словарь
        new_dict_loop[key] = value

new_dict_loop
# -

# условие с if-else ставится в самом начале схемы dict
# comprehension заменим значение на слово even, если оно четное,
# и odd, если нечетное
filtered_dict_parity: dict[str, str] = {
    key: ("even" if value % 2 == 0 else "odd") for key, value in source_dict.items()
}
filtered_dict_parity

# Dict comprehension можно использовать вместо метода .fromkeys().
# создадим кортеж из ключей
keys2: tuple[str, ...] = ("k1", "k2", "k3")

# передадим словарю ключи из кортежа keys2 и зададим значение 0
# каждому из них
new_dict_fromkeys: dict[str, int] = {key: 0 for key in keys2}
new_dict_fromkeys

# # lambda-функция, функции map() и zip()

# Возьмем список фруктов.
fruits: list[str] = ["apple", "banana", "cherry"]

# создадим lambda-функцию, которая посчитает длину передаваемого
# ей слова с помощью функции map() применим lambda-функцию к
# каждому элементу списка words и поместим длины слов в новый
# список length с помощью функции list()
length: list[int] = list(map(len, fruits))
length

# с помощью функции zip() поэлементно соединим оба списка и
# преобразуем в словарь
fruit_length_dict: dict[str, int] = dict(zip(fruits, length))
fruit_length_dict

# то же самое можно сделать с помощью функции zip() и
# list comprehension
fruit_length_dict_comp: dict[str, int] = {fruit: len(fruit) for fruit in fruits}
fruit_length_dict_comp

# Пример со словарем
# Теперь поработаем со словарями. Предположим, что мы продолжаем
# спрашивать людей об их росте, и у нас есть несколько
# американцев, которые сообщили свой рост в футах.
height_feet: dict[str, float] = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}

# Наша задача — создать точно такой же словарь, но чтобы футы
# были преобразованы в метры. Вначале создадим список с данными
# о росте в метрах. Один фут равен 0,3048 метра
height_meters: list[float] = list(
    map(lambda height: height * 0.3048, height_feet.values())
)
height_meters

# с помощью функции zip() соединим ключи исходного словаря с
# элементами списка metres
height_meters_rounded: dict[str, object] = dict(
    zip(height_feet.keys(), np.round(height_meters, 2))
)
height_meters_rounded

# Как и в предыдущем примере, эту задачу можно решить с помощью
# dict comprehension.
height_meters_comp: dict[str, object] = {
    key: np.round(value * 0.3048, 2) for key, value in height_feet.items()
}
height_meters_comp

# # Вложенные словари

# возьмем словарь, ключами которого будут id сотрудников
employees: dict[str, dict[str, str | int | float]] = {
    "id1": {
        "first name": "Александр",
        "last name": "Иванов",
        "age": 30,
        "job": "программист",
    },
    "id2": {
        "first name": "Ольга",
        "last name": "Петрова",
        "age": 35,
        "job": "ML-engineer",
    },
}

# В данном случае ключами словаря выступают id сотрудников, а
# значениями — вложенные словари с информацией о них.
for emp_id, info in employees.items():
    print(f"ID: {emp_id}, Info: {info}")

# Базовые операции
# первый ключ - нужный нам сотрудник, второй - элемент с
# информацией о нем
employees["id1"]["first name"]  # Александр

# +
# Функция pprint() расшифровывается как pretty print («красивая
# печать») и в некоторых случаях справляется со своей задачей
# лучше обычной функции print().
# -

# добавим информацию о новом сотруднике
employees["id3"] = {
    "first name": "Дарья",
    "last name": "Некрасова",
    "age": 27,
    "job": "веб-дизайнер",
}

# и выведем обновленный словарь с помощью функции pprint()
pprint(employees)

# +
# Циклы for
# Посмотрим, как можно использовать цикл for со вложенными
# словарями. Давайте заменим тип данных с информацией о возрасте
# сотрудника с int на float.

# для этого вначале пройдемся по вложенным словарям, т.е. по
# значениям info внешнего словаря employees затем по ключам и
# значениям вложенного словаря info если ключ совпадет со словом
# 'age' преобразуем значение в тип float
for info in employees.values():
    for emp_key, emp_value in info.items():
        if emp_key == "age" and isinstance(emp_value, int):
            info[emp_key] = float(emp_value)

pprint(employees)
# -

# Вложенные словари и dict comprehension
# преобразуем обратно из float в int, но уже через dict
# comprehension для начала просто выведем словарь employees без
# изменений
pprint({emp_id: info for emp_id, info in employees.items()})

# а затем заменим значение внешнего словаря info (т.е.
# вложенный словарь) на еще один dict comprehension с условием
# if-else
pprint(
    {
        emp_id: {
            emp_key: (
                int(emp_value)
                if emp_key == "age" and isinstance(emp_value, float)
                else emp_value
            )
            for emp_key, emp_value in info.items()
        }
        for emp_id, info in employees.items()
    }
)

# # Частота слов в тексте

# Напоследок разберем очень несложный пример подсчета частоты
# слов в тексте. Это уже знакомый нам мешок слов (Bag of Words,
# BoW). В качестве примера возьмем уже известный нам текст про
# Париж, музеи и искусство.
corpus: str = (
    "When we were in Paris we visited a lot of museums. We first "
    "went to the Louvre, the largest art museum in the world. I "
    "have always been interested in art so I spent many hours "
    "there. The museum is enormous, so a week there would not "
    "be enough."
)

# Предварительная обработка текста
# Превратим строку в список слов.
words: list[str] = corpus.split()
print(words)

# Применим list comprehension, чтобы избавиться от точек и
# запятых. Помимо этого, переведем все слова в нижний регистр.
words = [word.strip(".,").lower() for word in words]
print(words)

# +
# Мы готовы создавать мешки слов разными способами.
# Способ 1. Условие if-else
# создадим пустой словарь для мешка слов bow
bow_1: dict[str, int] = {}

# пройдемся по словам текста
for word in words:
    # если нам встретилось слово, которое уже есть в словаре
    if word in bow_1:
        # увеличим его значение (частоту) на 1
        bow_1[word] = bow_1[word] + 1
    # в противном случае, если слово встречается впервые
    else:
        # зададим ему значение 1
        bow_1[word] = 1

# отсортируем словарь по значению в убывающем порядке
# (reverse = True) и выведем шесть наиболее частотных слов
top_words_1: list[tuple[str, int]] = sorted(
    bow_1.items(), key=lambda word_item: word_item[1], reverse=True
)[:6]
top_words_1

# +
# Способ 2. Метод .get()
bow_2: dict[str, int] = {}

for word in words:
    bow_2[word] = bow_2.get(word, 0) + 1

top_words_2: list[tuple[str, int]] = sorted(
    bow_2.items(), key=lambda word_item: word_item[1], reverse=True
)[:6]
top_words_2

# +
# создадим объект этого класса, передав ему список слов
bow_3: Counter[str] = Counter(words)

# выведем шесть наиболее часто встречающихся слов с помощью
# метода .most_common()
bow_3.most_common(6)
