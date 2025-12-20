"""Функции."""

import matplotlib.pyplot as plt
import numpy as np

# ## Встроенные функции
# В Python есть множество встроенных функций:
# 1. Стандартный функционал (built-in functions)
# 2. Дополнительные библиотеки (library functions)

np.random.seed(42)
height = list(np.round(np.random.normal(180, 10, 1000)))

plt.hist(height, bins=10, edgecolor="black")
plt.title("Распределение роста")
plt.xlabel("Рост (см)")
plt.ylabel("Количество")
plt.show()

# ## Параметры и аргументы функции
# - **Параметр** — это то, что запрашивает функция при вызове (например, `bins`)
# - **Аргумент** — значение этого параметра (например, `10`)

plt.hist(bins=10, x=height)
plt.show()

plt.hist(height)
plt.show()

print("Первая строка")
print()
print("Третья строка")

# ## Функции и методы
# Методы — это функции, которые можно применить только к конкретному объекту.

some_string = "machine learning"
some_string.title()


# ## Собственные функции в Python
# ### Объявление и вызов функции


def double(value: int) -> int:
    """Удваивает переданное значение."""
    return value * 2


double(5)


# ## Пустое тело функции
# Тело функции не может быть пустым. Нужно как минимум указать `return` или `pass`.


def only_pass() -> None:
    """Функция с pass."""
    # pass


only_pass()


# ## Функция print() вместо return
# Результат работы функции можно вывести с помощью `print()`.


def double_print(value: int) -> None:
    """Удваивает значение и выводит результат."""
    res = value * 2
    print(res)


double_print(5)


# ### Различие между return и print
# - **return** возвращает значение функции и прерывает её работу
# - **print()** просто выводит значение и не влияет на дальнейшее исполнение кода

# ## Параметры собственных функций
# Параметры могут быть позиционными и именованными.


def calc_sum(first_num: int, second_num: int) -> int:
    """Возвращает сумму двух чисел."""
    return first_num + second_num


calc_sum(1, second_num=2)


# +
def calc_sum_default(first_num: int = 1, second_num: int = 2) -> int:
    """Возвращает сумму двух чисел с параметрами по умолчанию."""
    return first_num + second_num


calc_sum_default()


# +
def greet() -> None:
    """Выводит приветствие."""
    print("Hello, World!")


greet()


# -

# ## Аннотация функции
# Аннотация позволяет явно прописать тип данных параметров и возвращаемых значений.


def convert_to_int(value: float = 3.5) -> int:
    """Преобразует float в int."""
    return int(value)


convert_to_int.__annotations__

convert_to_int()

# ## Дополнительные возможности функций

result_arithmetic = calc_sum(1, 2) * 2
print(result_arithmetic)

result_logic = calc_sum(1, 2) > 2
print(result_logic)


def first_letter() -> str:
    """Возвращает строку 'Python'."""
    return "Python"


first_char = first_letter()[0]
print(first_char)


def square_from_input() -> int:
    """Запрашивает число и возвращает его квадрат."""
    user_inp = int(input("Введите число: "))
    result_local = user_inp**2
    return result_local


# ## Результат вызова функции
# Функция может возвращать список, кортеж или словарь.


# +
def create_list(count: int) -> list[int]:
    """Создает список чисел от 0 до count-1."""
    numbers = []
    for index in range(count):
        numbers.append(index)
    return numbers


create_list(5)


# -


def get_tuple_values() -> tuple[str, int]:
    """Возвращает кортеж из строки и числа."""
    string_val = "Python"
    number_val = 42
    return string_val, number_val


str_result, num_result = get_tuple_values()
print(str_result, num_result)
print(type(str_result), type(num_result))

tuple_result = get_tuple_values()
print(tuple_result)
print(type(tuple_result))


def is_even_numbers(number: int) -> bool:
    """Проверяет, четное ли число."""
    return number % 2 == 0


is_even_numbers(4)


# ## Использование библиотек
# Внутри функций можно использовать дополнительные библиотеки Python.


def mean_f(data: float | list[float] | np.ndarray) -> float:  # type: ignore[misc]
    """Рассчитает среднее арифметическое и прибавит единицу."""
    return float(np.mean(data)) + 1


data_values = [1, 2, 3]

mean_f([float(x) for x in data_values])

# ## Глобальные и локальные переменные
# Переменные существуют либо только внутри функции (локальные), либо во всей программе (глобальные).

# +
global_name = "Петр"


def show_name() -> None:
    """Выводит глобальное имя."""
    print(global_name)


# -

show_name()


def show_local_name() -> None:
    """Выводит локальное имя."""
    local_name_var = "Алена"
    print(local_name_var)


show_local_name()

# +
global_local_name: str


def make_global() -> str:  # возвращаем str
    """Создает имя."""
    return "Алена"


global_local_name = make_global()  # присваиваем
print(global_local_name)
# -

make_global()

print(global_local_name)

# +
global_number = 5


def print_number() -> None:
    """Выводит локальное число."""
    local_number = 10
    print("Local number:", local_number)


# -

print_number()

print("Global number:", global_number)


# ## Анонимные или lambda-функции
# Функции можно создавать с помощью слова lambda без названия.


# +
def multiply_numbers(first: int, second: int) -> int:
    """Перемножает два числа."""
    return first * second


multiply_numbers(2, 3)

# +
# Структура lambda-функции:
# lambda [параметры]: [выражение]
# - ключевое слово lambda
# - передаваемые параметры
# - через двоеточие пишется исполняемое выражение

print("Lambda-функции удобны для кратких операций")
# -

# ### Lambda-функция внутри функции filter()
# Lambda-функции удобно использовать с встроенными функциями.

# +
lambda_nums = [15, 27, 9, 18, 3, 1, 4]

filtered_nums = list(filter(lambda num: num > 10, lambda_nums))
print(filtered_nums)


# -


def is_greater_than_ten(number: int) -> bool:
    """Проверяет, больше ли число 10."""
    return number > 10


test_nums = [15, 27, 9, 18, 3, 1, 4]
result = list(filter(is_greater_than_ten, test_nums))
print(result)  # [15, 27, 18]

# ### Lambda-функция внутри функции sorted()

# +
indices_distances = [
    (901, 0.0),
    (1002, 0.22982440568634488),
    (442, 0.25401128310081567),
]

sorted(indices_distances, key=lambda item: item[1], reverse=False)
# -

# ## Немедленно вызываемые функции
# Lambda-функции можно вызвать немедленно после определения.

# Lambda-функции рекомендуется использовать только с filter, map и sorted
# Присваивание lambda в переменную не рекомендуется
# Вместо этого используйте def для определения функций
print("Используйте def для определения функций вместо lambda")


# ## *args и **kwargs
# Они позволяют передавать функции различное количество позиционных или именованных аргументов.

# ### *args
# *args позволяет передавать переменное количество позиционных аргументов.


def calculate_mean(*numbers: int) -> float:
    """Возвращает среднее арифметическое произвольного количества чисел."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers) if numbers else 0.0


print(calculate_mean(1, 2, 3, 4))

# +
# Главным элементом является оператор распаковки * (unpacking operator)
# Он принимает все передаваемые в функцию числа и формирует из них кортеж

# Если захотим передать функции список, можем это сделать
numbers_list = [1, 2, 3, 4]
calculate_mean(*numbers_list)


# -


def test_type(*numbers: int) -> None:
    """Выводит тип переданных аргументов."""
    print(numbers, type(numbers))


test_type(1, 2, 3, 4)

# +
nums_a = [1, 2, 3]
nums_b = [*nums_a, 4, 5, 6]

print(nums_b)


# -

# ### **kwargs
# **kwargs преобразует именованные параметры в словарь.


# +
def get_kwargs_items(**kwargs: int) -> dict[str, int]:
    """Возвращает элементы словаря."""
    return kwargs


get_kwargs_items(param_a=1, param_b=2)


# -


def simple_stats(*nums: float, **params: bool) -> None:
    """Выводит статистику по числам на основе флагов в params."""
    # Если ключ 'mean' есть в словаре params и его значение == True
    if params.get("mean", False):
        # Рассчитаем среднее арифметическое кортежа nums и округлим
        print(f"mean:\t{np.round(np.mean(nums), 3)}")

    # Если ключ 'std' есть в словаре params и его значение == True
    if params.get("std", False):
        # Рассчитаем СКО кортежа nums и округлим
        print(f"std:\t{np.round(np.std(nums), 3)}")


simple_stats(5, 10, 15, 20, mean=True, std=True)
