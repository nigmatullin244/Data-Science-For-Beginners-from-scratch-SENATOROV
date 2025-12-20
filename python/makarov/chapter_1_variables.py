"""Переменные."""

# # Как объявить переменную в Питоне

# +
# Создание или объявление переменной в Питоне происходит
# в тот момент, когда вы присваиваете ей определенное значение

x_var = 42
print(x_var)
# -

# Кроме того, переменной можно задать строковое (текстовое) значение.
y_var = "Just a string"
print(y_var)

# +
# В Питоне можно записать значения сразу в
# несколько переменных или присвоить одно и
# то же значение нескольким переменным.

a_var, b_var, c_var = 1, 2, 3
print(a_var, b_var, c_var)

# +
# Или задать одно и то же значение нескольким переменным

a_var = b_var = c_var = 10
print(a_var, b_var, c_var)

# +
# Список можно «распаковать» (unpack) в несколько переменных:

numbers = [1, 2, 3]
x_unpack, y_unpack, z_unpack = numbers
print(x_unpack, y_unpack, z_unpack)
# -

# # Типы данных в питоне

# +
# Автоматическое определение типа данных

int_var = 5  # целое число (int)
float_var = 3.14  # число с плавающей точкой (float)
str_var = "Hello"  # строка (str)
d_var = True  # булево значение (bool)
print(type(int_var))  # <class 'int'>
print(type(float_var))  # <class 'float'>
print(type(str_var))  # <class 'str'>
print(type(d_var))  # <class 'bool'>
# -

# Присвоение и преобразование типа данных
e_var = 100  # целое число
print(type(e_var))  # <class 'int'>
f_var = float(e_var)  # преобразование в число с плавающей точкой
print(type(f_var))  # <class 'float'>
g_var = str(e_var)  # преобразование в строку
print(type(g_var))  # <class 'str'>

# преобразуем дробь в целочисленное значение
# обратите внимание, что округления в большую сторону не происходит
a_f_var = float(9.99)
h_var = int(a_f_var)
print(a_f_var, h_var, sep=", ")

# +
# Как можно преобразовать список чисел таким образом,
# чтобы каждый элемент списка превратился в отдельную строку?

# вариант 1: объявить новый список и в цикле
# for помещать туда строковые значения

list_str = []
nums = [1, 2, 3, 4, 5]

for x_var in nums:
    list_str.append(str(x_var))

print(list_str)

# вариант 2: использовать list comprehension
list_str_comp = [str(x_var) for x_var in nums]

print(list_str_comp)

# вариант 3: функции map() и list()
list_str_map = list(map(str, nums))

print(list_str_map)
