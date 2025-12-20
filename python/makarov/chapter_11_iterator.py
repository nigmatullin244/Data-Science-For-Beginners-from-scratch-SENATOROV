"""Итераторы и генераторы."""

# # Итерируемый объект и итератор

# +
# Основные определения
# Итератор — это объект, который позволяет перебирать элементы коллекции
from collections.abc import Iterator
from itertools import chain, count, cycle

for num in [1, 2, 3]:
    print(num)
# -

# встроенная функция iter() вызывает метод .__iter__(),
# создающий итератор
iter([1, 2, 3])

# +
# Итератор (iterator) позволяет извлекать элементы итерируемого объекта
# за одним отслеживая, какой именно элемент был извлечен на данной
# итерации класс итератора, таким образом, должен включать два метода:
# метод .__iter__(), который возвращает сам этот объект; и
# метод .__next__(), возвращающий следующий элемент последовательности.

iterable_object = [1, 2, 3]

iterator = iter(iterable_object)
print(iterator)
print()

print(next(iterator))
print(next(iterator))
print(next(iterator))

# +
# При использовании цикла итератор создается автоматически.

for item in iterable_object:
    print(item)

# +
# разделение итерируемого объекта и итератора позволяет оставлять
# нетронутыми данные в итерируемом объекте и обращаться к ним столько
# раз, сколько это необходимо с помощью итератора.

iterable_object = [1, 2, 3]

iterator_a = iter(iterable_object)
iterator_b = iter(iterable_object)

print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")
# -

iterable_object

# +
# Функция list() позволяет обойти и вернуть все (оставшиеся) элементы
# конкретного итератора.

result_a = list(iterator_a)
result_b = list(iterator_b)
result_a, result_b
# -

# Используем list для итерации вместо однобуквенной переменной
for item in [1, 2, 3]:
    print(item)

# # Отсутствие «обратного хода»

# +
# Логично, что итератор не позволяет двигаться в обратном направлении
# от последующего элемента к предыдущему.

iterator_c = iter(iterable_object)

for first_item in iterator_c:
    print(first_item)
    break

for next_item in iterator_c:
    print(next_item)
# -

# # Функция zip()

# +
# Помимо функции iter() еще одной функцией, возвращающей итератор
# из итерируемого объекта, является функция zip().

iterator_tuple = zip(iterable_object, iterable_object)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))

# +
# На практике конечно удобнее передать итерируемые объекты в функцию
# zip() и создавать и вызывать метод .__next__() итератора в цикле.

for item_pair in zip(iterable_object, iterable_object):
    print(item_pair)
# -

# # Примеры итераторов

# +
# первый итератор принимает на вход некоторую последовательность чисел
# и возвращает квадрат каждого из них.


class Square:
    """Iterator that returns the square of each element in a sequence."""

    def __init__(self, sequence: list[int]) -> None:
        """Initialize Square iterator with a sequence.

        Args:
            sequence: List of integers to square.
        """
        self._seq = sequence
        self._idx = 0

    def __iter__(self) -> "Square":
        """Return the iterator object itself."""
        return self

    def __next__(self) -> int:
        """Return the next squared element."""
        if self._idx < len(self._seq):
            squared_val = self._seq[self._idx] ** 2
            self._idx += 1
            return squared_val
        raise StopIteration


# -

square_iter = Square([1, 2, 3, 4, 5])
square_iter

for squared_elem in square_iter:
    print(squared_elem)

# +
# Итераторы также могут самостоятельно создавать новые данные.


class Counter:
    """Iterator that generates numbers from start to stop."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Initialize Counter iterator.

        Args:
            start: Starting value (default 3).
            stop: Stopping value (default 9).
        """
        self._current = start - 1
        self._stop = stop

    def __iter__(self) -> "Counter":
        """Return the iterator object itself."""
        return self

    def __next__(self) -> int:
        """Return the next number in the sequence."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


# -

counter = Counter()
counter

print(next(counter))
print(next(counter))

for counter_val in counter:
    print(counter_val)

# +
# Класс Iterator модуля collections.abc


class Counter2(Iterator[int]):
    """Counter iterator inheriting from collections.abc.Iterator."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Initialize Counter2 iterator.

        Args:
            start: Starting value (default 3).
            stop: Stopping value (default 9).
        """
        self._current = start - 1
        self._stop = stop

    def __next__(self) -> int:
        """Return the next number in the sequence."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


# -

for counter2_val in Counter2():
    print(counter2_val)

# +
# Бесконечный итератор


class FibIterator:
    """Iterator that generates Fibonacci sequence infinitely."""

    def __init__(self) -> None:
        """Initialize Fibonacci iterator."""
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self) -> "FibIterator":
        """Return the iterator object itself."""
        return self

    def __next__(self) -> int:
        """Return the next Fibonacci number."""
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
limit = 10

for fib_num in FibIterator():
    print(fib_num)
    limit -= 1
    if limit == 0:
        break
# -

# # Генераторы

# +
# Простой пример
# Рассмотрим функцию, которая создает последовательность чисел.


def make_sequence(seq_length: int) -> list[int]:
    """Generate a list of integers from 1 to seq_length.

    Args:
        seq_length: The length of the sequence.

    Returns:
        A list of integers from 1 to seq_length.
    """
    res = [elem for elem in range(1, seq_length + 1)]
    return res


# -

make_sequence(5)

# +
# Если использовать ключевое слово yield вместо return, то функция
# вернет не последовательность, а объект-генератор.


def sequence_gen(seq_length: int) -> Iterator[int]:
    """Generate integers from 1 to seq_length using yield.

    Args:
        seq_length: The length of the sequence.

    Yields:
        Integers from 1 to seq_length.
    """
    yield from range(1, seq_length + 1)


# -

sequence_gen(5)

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))

# +
# Все элементы последовательности можно вывести с помощью цикла.


for seq_elem in seq_5:
    print(seq_elem)

# +
# Если вызвать метод .__next__() после того, как генератор выдаст все
# имеющиеся значения, сработает исключение StopIteration.

# next(seq_5)

# +
# Generator comprehension
# Создать объект-генератор можно в одну строчку аналогично
# list comprehension, но с использованием круглых скобок.

gen_obj = (elem for elem in range(1, 5 + 1))
gen_obj

# +
# После этого объект можно превратить в список

list(elem for elem in range(1, 5 + 1))

# +
# или, например, найти сумму элементов

sum(elem for elem in range(1, 5 + 1))
# -

# # Модуль itertools

# +
# Функция count()

natural_numbers = count(start=1, step=0.5)

for num in natural_numbers:
    print(num)
    if num == 2.0:
        break

# +
# На практике функцию count() можно использовать, например,
# для индексирования элементов списка.

str_list = ["A", "B", "C", "D"]
for index_val in zip(count(), str_list):
    print(index_val)

# +
# Кроме этого, совместив count() с map() можно получить
# значения некоторой функции.


def func(val_quad: int) -> int:
    """Calculate quadratic function x^2 + x - 2.

    Args:
        val: Input value.

    Returns:
        Result of x^2 + x - 2.
    """
    return val_quad**2 + val_quad - 2


f_x = map(func, count())
next(f_x)
# -

for func_val in f_x:
    # выполнение продолжится со второго значения итератора
    print(func_val)
    if func_val > 10:
        break

# +
# Функция cycle()

int_list = [1, 2, 3]
cycle_iter = cycle(int_list)

limit = 5
for cycle_item in cycle_iter:
    print(cycle_item)
    limit -= 1
    if limit == 0:
        break

# +
# Строки, как мы помним, также являются итерируемым объектом.

string = "Python"
string_iter = cycle(string)

limit = 10
for cycle_char in string_iter:
    print(cycle_char)
    limit -= 1
    if limit == 0:
        break

# +
# Функция chain()

# Функция chain() объединяет (сцепляет) несколько итерируемых
# объектов в один итератор.

chain_result = chain(["abc", "d", "e", "f"], "abc", [1, 2, 3])
chain_result
# -

list(chain_result)

list(chain.from_iterable(["abc", "def"]))

sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
