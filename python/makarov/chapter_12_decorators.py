"""Decorators."""

# +
# Декораторы
# Декораторы - это функции, которые принимают другую
# функцию в качестве аргумента
# расширяют её функциональность без изменения её
# кода и возвращают новую функцию.

# +
# Объекты первого класса
#
# Функции в Питоне представляют собой объекты первого класса
# (first class objects), что означает, что их можно присваивать
# переменной, возвращать из функции или передавать другой
# функции в качестве аргумента.

# +
import functools
import time

# Можно также воспользоваться функцией functools.update_wrapper().
from functools import update_wrapper

# Присвоение функции переменной
from typing import Callable, ParamSpec, TypeVar


def say_hello(name: str) -> None:
    """Print greeting message."""
    print(f"Привет, {name}!")


# -

# присвоим эту функцию переменной (без скобок)
say_hello_function = say_hello
# вызовем функцию из новой переменной
say_hello_function("Алексей")

# +
# Передача функции в качестве аргумента


Rval = TypeVar("Rval")


def calculate_result(
    operation: Callable[[int, int], Rval], first: int, second: int
) -> Rval:
    """Calculate using provided operation."""
    return operation(first, second)


def add(first: int, second: int) -> int:
    """Add two numbers."""
    return first + second


def subtract(first: int, second: int) -> int:
    """Subtract two numbers."""
    return first - second


def multiply(first: int, second: int) -> int:
    """Multiply two numbers."""
    return first * second


def divide(first: int, second: int) -> float:
    """Divide two numbers."""
    return first / second


# +
# Разделим единицу на три.


result = calculate_result(divide, 1, 3)
print(result)  # 0.3333333333333333

# +
# Внутрение функции
# Внутренние (inner) или вложенные (nested) функции
# представляют собой функции, объявленные и вызванные внутри других функций.
# Вызов внутренней функции


def outer() -> None:
    """Call outer and inner functions."""
    print("Вызов внешней функции.")

    # обратите внимание, мы объявляем, а затем
    def inner() -> None:
        """Call inner function."""
        print("Вызов внутренней функции.")

    # вызываем внутреннюю функцию
    inner()


# -

outer()

# +
# Вызвать внутреннюю функцию не получится.

# inner() # Вызвать внутреннюю функцию не получится.

# +
# Возвращение функции из функции
# Функция может возвращать другую функцию. В примере ниже функция
# create_multiplier() создает множитель (factor) для передаваемого во
# внуреннюю функцию multiplier() числа (number).


def create_multiplier(factor: int) -> Callable[[int], int]:
    """Create multiplier function."""

    def multiplier(number: int) -> int:
        """Multiply number by factor."""
        return number * factor

    return multiplier


# +
# Создадим две ссылки на внутреннюю функцию multiplier(),
# передав ей в качестве параметра множитель,
# равный соответственно двум и трем.


double = create_multiplier(factor=2)
triple = create_multiplier(factor=3)

# +
# Умножим число два на каждый из множителей.

result_double: int = double(2)
result_triple: int = triple(2)
print(result_double, result_triple)

# +
# Заметим, что код в примере выше можно сократить с помощью
# lambda-функции.


def create_multiplier_lambda(factor: int) -> Callable[[int], int]:
    """Create multiplier function using lambda."""
    return lambda number: factor * number


# -

triple = create_multiplier_lambda(factor=3)
print(triple(2))

# +
# Замыкание
#
# Замыкание (closure) — это внутренняя функция, которая сохраняет доступ
# к переменным из внешней (окружающей) функции даже после завершения
# выполнения внешней функции.

# +
# Знакомство с декораторами
# Простой декоратор


T = TypeVar("T", bound=Callable[[], None])


def simple_decorator(func: T) -> T:
    """Wrap function with simple decorator."""

    def wrapper() -> None:
        print(f"{func.__name__} called.")
        func()
        print("simple_decorator finished.")

    return wrapper  # type: ignore[return-value]


def say_hello_simple() -> None:
    """Greet user."""
    print("Привет!")


# -

say_hello_simple = simple_decorator(say_hello_simple)

# Вызовем функцию say_hello().
say_hello_simple()

# +
# Таким образом, декоратор — это функция, которая принимает в
# качестве аргумента другую функцию и возвращает ее дополненную версию.

# +
# Конструкция @decorator


@simple_decorator
def say_hi() -> None:
    """Say hi greeting."""
    print("Снова, привет!")


# -

say_hi()

# +
# Функции с аргументами
# Рассмотрим функцию с аргументом и применим к ней simple_decorator().
#
# @simple_decorator
# def say_hello_with_name(name):
#     print(f'Привет, {name}!')
#
# При попытке вызова декорируемой функции произойдет ошибка,
# поскольку внутренняя функция wrapper() не принимает аргументов.

# +
# Исправим это.


def decorate_with_name_arg(func: Callable[[str], None]) -> Callable[[str], None]:
    """Decorate function with name argument."""

    def wrapper(name: str) -> None:
        """Execute wrapped function."""
        print("Текст до вызова функции func().")
        func(name)
        print("Текст после вызова функции func().")

    return wrapper


# -


@decorate_with_name_arg
def say_hello_with_names(name: str) -> None:
    """Say hello with person name."""
    print(f"Привет, {name}!")


say_hello_with_names("Алексей")

# +
# Мы также можем передать во внутреннюю функцию произвольное
# количество позиционных (*args) и именованных (**kwargs) аргументов.

ParamSpecVar = ParamSpec("ParamSpecVar")  # Аргументы функции
ReturnTypeVar = TypeVar("ReturnTypeVar")  # Возвращаемое значение


def decorate_with_args(
    func: Callable[ParamSpecVar, ReturnTypeVar],
) -> Callable[ParamSpecVar, ReturnTypeVar]:
    """Decorate with args."""

    def wrapper(
        *args: ParamSpecVar.args, **kwargs: ParamSpecVar.kwargs
    ) -> ReturnTypeVar:
        print("Текст до вызова функции func().")
        result_dec = func(*args, **kwargs)
        print("Текст после вызова функции func().")
        return result_dec

    return wrapper


# -


@decorate_with_args
def say_hello_with_argument(name: str) -> None:
    """Say hello with argument."""
    print(f"Привет, {name}!")


say_hello_with_argument("Алексей")

# +
# Возвращение значения декорируемой функции
# Объявим функцию return_name_with_decorator и декорируем ее с помощью
# decorate_with_return().

FunctionArgs = ParamSpec("FunctionArgs")  # Аргументы функции
ReturnArgs = TypeVar("ReturnArgs")  # Возвращаемое значение


def decorate_with_return(
    func: Callable[FunctionArgs, ReturnArgs],
) -> Callable[FunctionArgs, ReturnArgs]:
    """Decorate function that returns value."""

    def wrapper(*args: FunctionArgs.args, **kwargs: FunctionArgs.kwargs) -> ReturnArgs:
        """Execute wrapped function."""
        print("Текст внутренней функции.")
        return_value = func(*args, **kwargs)  # Тип выведется автоматически
        return return_value

    return wrapper


# -


@decorate_with_args
def return_name_with_decorator(name: str) -> str:
    """Return provided name."""
    return name


# +
# Посмотрим, какое значение вернула эта функция.


returned_value: str = return_name_with_decorator("Алексей")
# -

print(returned_value)


# +
# Декоратор @functools.wraps
# Питон содержит инструменты для интроспекции (introspection),
# которые позволяют исследовать уже созданный объект
# -


def square(value: int) -> int:
    """Square a number."""
    return value * value


print(square.__name__, square.__doc__)

# +
# При использовании декоратора мы по сути заменяем исходную
# декорируемую функцию на внутреннюю замыкающую функцию.

WrapperArg = ParamSpec("WrapperArg")


def repeat_twice_no_meta(
    func: Callable[WrapperArg, None],
) -> Callable[WrapperArg, None]:
    """Repeat function execution twice."""

    def wrapper(*args: WrapperArg.args, **kwargs: WrapperArg.kwargs) -> None:
        """Execute wrapped function."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


# -


@repeat_twice_no_meta
def square_repeated(value: int) -> None:
    """Square a number."""
    print(value * value)


square_repeated(3)

# Как следствие, инструменты интроспекции не видят
# декорируемой функции.
print(square_repeated.__name__, square_repeated.__doc__)

# +
# Декоратор @functools.wraps модуля functools позволяет
# сохранить метаданные декорируемого объекта.


RTVar = TypeVar("RTVar")
Params = ParamSpec("Params")


def repeat_twice(
    func: Callable[Params, RTVar],
) -> Callable[Params, RTVar]:
    """Repeat function execution twice."""

    @functools.wraps(func)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> RTVar:
        """Execute wrapped function."""
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


# -


@repeat_twice
def square_with_metadata(value: int) -> None:
    """Square a number."""
    print(value * value)


print(square_with_metadata.__name__, square_with_metadata.__doc__)

# +
# Атрибут __wrapped__ ссылается на исходную функцию
# до применения декоратора.

# print(square_with_metadata.__wrapped__)
# <function square_with_metadata at 0x...>

# +
# Можно также воспользоваться функцией functools.update_wrapper().


ParamUpdateVar = ParamSpec("ParamUpdateVar")


def repeat_twice_update_wrapper(
    func: Callable[ParamUpdateVar, None],
) -> Callable[ParamUpdateVar, None]:
    """Repeat function execution twice using update_wrapper."""

    def wrapper(*args: ParamUpdateVar.args, **kwargs: ParamUpdateVar.kwargs) -> None:
        """Execute wrapped function."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    update_wrapper(wrapper, func)
    return wrapper


# -


@repeat_twice_update_wrapper
def power(base: int, exponent: int) -> None:
    """Raise value to a power."""
    print(base**exponent)


power(2, 3)

print(power.__doc__)

# +
# Примеры декораторов
# Декоратор можно использовать для выведения (и записи)
# информации о вызове функции (логирования).


ParamLogVar = ParamSpec("ParamLogVar")
ReturnLog = TypeVar("ReturnLog")  # Для возвращаемого значения


def logging_decorator(
    func: Callable[ParamLogVar, ReturnLog],
) -> Callable[ParamLogVar, ReturnLog]:
    """Decorate function for logging function calls."""

    @functools.wraps(func)
    def wrapper(*args: ParamLogVar.args, **kwargs: ParamLogVar.kwargs) -> ReturnLog:
        """Execute wrapped function."""
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result_log = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result_log}")
        return result_log

    return wrapper


# +
@logging_decorator
def power_logged(base: int, exponent: int) -> int:
    """Calculate power."""
    return int(base**exponent)


print(power_logged(5, 3))

# +
ParamTimeVar = ParamSpec("ParamTimeVar")
ReturnTimeLog = TypeVar("ReturnTimeLog")


def timer_decorator(
    func: Callable[ParamTimeVar, ReturnTimeLog],
) -> Callable[ParamTimeVar, ReturnTimeLog]:
    """Decorate timer."""

    @functools.wraps(func)
    def wrapper(
        *args: ParamTimeVar.args, **kwargs: ParamTimeVar.kwargs
    ) -> ReturnTimeLog:
        start_time = time.time()
        result_time: ReturnTimeLog = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result_time

    return wrapper


# +
@timer_decorator
def delayed_function(timer: float) -> str:
    """Delay function."""
    time.sleep(timer)
    return "execution completed"


delayed_function(2)

# +
# Типы методов
# Методы экземпляра


class CatClass:
    """A simple cat class."""

    def __init__(self, color: str) -> None:
        """Initialize cat instance."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Print cat info."""
        print(self.color, self.type_, sep=", ")


# -

cat = CatClass(color="black")
cat.info()

# +
# При этом поскольку это атрибуты и методы экземляра класса,
# применить их к самому классу мы не можем.
#
# CatClass.info() # будет ошибка

# +
# Переменные класса (class variable) и методы класса
# (class method) позволяют обратиться к
# самому классу без создания экземпляра.


class CatClassWithSpecies:
    """Cat class with species class method."""

    species: str = "кошка"  # переменная класса доступна всем экземлярам

    def __init__(self, color: str) -> None:
        """Initialize cat instance."""
        self.color = color

    def info(self) -> None:
        """Print cat color."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Get species of the cat."""
        print(cls.species)


# -

print(CatClassWithSpecies.species)

CatClassWithSpecies.get_species()

# +
# Статические методы (static method) не имеют доступа
# ни к атрибутам экземпляра, ни к атрибутам класса.
#
# Чаще всего статические методы — это служебные методы,
# логически связанные с функционалом создаваемого класса.
# В нашем примере создадим статический метод для
# преобразования веса кошки из килограммов в фунты.


class CatClassWithStatic:
    """Cat class with static method."""

    species: str = "кошка"

    def __init__(self, color: str) -> None:
        """Initialize cat instance."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Print cat info."""
        print(self.color, self.type_)

    @classmethod
    def get_species(cls) -> None:
        """Get species."""
        print(cls.species)

    @staticmethod
    def convert_to_pounds(kilograms: float) -> None:
        """Convert kilograms to pounds."""
        pounds: float = kilograms * 2.205
        print(f"{kilograms} kg is approximately {pounds} pounds")


# +
# Статические методы можно вызвать как из самого класса,
# так и из экземпляра класса.


CatClassWithStatic.convert_to_pounds(4)
# -

cat_instance: CatClassWithStatic = CatClassWithStatic("gray")
cat_instance.convert_to_pounds(5)

# +
# Декорирование класса
# Помимо встроенных декораторов @classmethod и @staticmethod
# мы можем расширять функционал класса с помощью
# собственных декораторов.


@timer_decorator
class CatClassDecorated:
    """Cat class decorated with timer."""

    def __init__(self, color: str) -> None:
        """Initialize cat instance."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Print cat info."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


# +
cat_decorated = CatClassDecorated("gray")

# Как мы видим, декоратор «сработал» только при создании
# экземпляра класса.
# -

cat_decorated.info()

# +
# Теперь рассмотрим функцию setattr(), которая позволяет
# добавить к экземпляру класса атрибут и соответствующее
# значение атрибута.

setattr(cat_decorated, "weight", 5)

# +
# Получить значение атрибута можно, обратившись к атрибуту
# напрямую или через функцию getattr().

weight_value = getattr(cat_decorated, "weight")
print(weight_value, weight_value)

# +
# Функцию setattr() можно использовать в декораторе и,
# таким образом, добавить переменную класса.


SetVar = TypeVar("SetVar", bound=type)


def add_attribute(
    attribute_name: str, attribute_value: object
) -> Callable[[type], type]:
    """Decorate class to add attribute."""

    def wrapper(cls: type) -> type:
        """Execute decorator."""
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


# -


@add_attribute("species", "кошка")
class CatClassWithAttribute:
    """Cat class with species attribute."""

    def __init__(self, color: str) -> None:
        """Initialize cat instance."""
        self.color = color
        self.type_ = "cat"


# +
# Несколько декораторов
# Ничто не мешает использовать несколько декораторов.


@logging_decorator
@timer_decorator
def delayed_function_decorated(delay_time: float) -> str:
    """Execute after delay with logging and timer."""
    time.sleep(delay_time)
    return "execution completed"


# -

print(delayed_function_decorated(2))

# +
# Вместо синтаксического сахара можно записать функцию в
# переменную, последовательно применив сначала один декоратор,
# а затем второй.


# не забудем заново объявить функцию без декораторов
def delayed_function_manual(delay_time: float) -> str:
    """Execute after delay."""
    time.sleep(delay_time)
    return "execution completed"


# -

delayed_function_manual = logging_decorator(timer_decorator(delayed_function_manual))
print(delayed_function_manual(2))

# +
# Декораторы с аргументами
# Иногда бывает полезно передать декоратору некоторый аргумент.
# Например, модифицируем декоратор @repeat_twice
# таким образом, чтобы он вызывал декорируемую функцию
# заданное параметром количество раз.

# +
ParamRepeatVar = ParamSpec("ParamRepeatVar")
ReturnRepeatLog = TypeVar("ReturnRepeatLog")


def repeat(
    n_times: int,
) -> Callable[
    [Callable[ParamRepeatVar, ReturnRepeatLog]],
    Callable[ParamRepeatVar, ReturnRepeatLog],
]:
    """Decorate function factory for repeating function calls."""

    def inner_decorator(
        func: Callable[ParamRepeatVar, ReturnRepeatLog],
    ) -> Callable[ParamRepeatVar, ReturnRepeatLog]:
        """Inner decorator function."""

        @functools.wraps(func)
        def wrapper(
            *args: ParamRepeatVar.args, **kwargs: ParamRepeatVar.kwargs
        ) -> ReturnRepeatLog:
            """Execute wrapped function."""
            for _ in range(n_times):
                func(*args, **kwargs)
            return func(*args, **kwargs)  # возвращаем последний результат

        return wrapper

    return inner_decorator


# -


@repeat(n_times=3)
def say_hello_repeated(name: str) -> None:
    """Say hello with repeating."""
    print(f"Привет, {name}!")


say_hello_repeated("Алексей")
