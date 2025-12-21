"""ООП.

Классы и объекты.
"""

# # Классы и объекты в Питоне

# +
# создадим класс CatClass
import numpy as np


class CatClass:
    """Простой класс для демонстрации основ ООП."""

    def __init__(self) -> None:
        """Инициализация объекта класса CatClass."""


# +
# Создание объекта

# создадим объект matroskin класса CatClass
matroskin: CatClass = CatClass()
# -

# проверим тип данных созданной переменной
type(matroskin)

# +
# Атрибуты класса
# Давайте дополним класс CatClass атрибутом типа (type_)
# и атрибутом цвета шерсти (color).


# вновь создадим класс CatClass
class CatClass:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс для представления кошки с атрибутами."""

    def __init__(self, color: str) -> None:
        """Инициализация объекта CatClass с цветом.

        Args:
            color: Цвет шерсти кошки.
        """
        # этот параметр будет записан в переменную атрибута
        self.color: str = color

        # значение атрибута type_ задается внутри класса
        self.type_: str = "cat"


# +
# повторно создадим объект класса CatClass
# передав ему параметр цвета шерсти
matroskin = CatClass("gray")  # type: ignore[call-arg]

# и выведем атрибуты класса
matroskin.color, matroskin.type_  # type: ignore[attr-defined]
# -

# # Методы класса

# +
# Дополним класс возможностью выполнять определенные действия


# перепишем класс CatClass
class CatClass:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс кошки с методами."""

    def __init__(self, color: str) -> None:
        """Инициализация кошки.

        Args:
            color: Цвет шерсти кошки.
        """
        self.color: str = color
        self.type_: str = "cat"

    def meow(self) -> None:
        """Кошка мяукает три раза."""
        for _ in range(3):
            print("Мяу")

    def info(self) -> None:
        """Выводит информацию об объекте."""
        print(self.color, self.type_)


# -

# создадим объект
matroskin = CatClass("gray")  # type: ignore[call-arg]

# применим метод .meow()
matroskin.meow()  # type: ignore[attr-defined]

# и метод .info()
matroskin.info()  # type: ignore[attr-defined]

# # Принципы объектно-ориентированного программирования

# +
# Инкапсуляция

# Инкапсуляция (encapsulation) — это способность класса
# хранить данные и методы внутри себя.

# +
# Публичные и частные атрибуты класса

# Публичные атрибуты — это те атрибуты, к которым можно получить
# доступ за пределами «капсулы» класса.

# +
# Причем не просто получить доступ, но и изменить их.

# изменим атрибут type_ объекта matroskin на dog
matroskin.type_ = "dog"  # type: ignore[attr-defined]

# выведем этот атрибут
matroskin.type_  # type: ignore[attr-defined]

# +
# Способ 1. Один символ подчеркивания указывает на приватный атрибут


class CatClass:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс кошки с защищенным атрибутом."""

    def __init__(self, color: str) -> None:
        """Инициализация кошки.

        Args:
            color: Цвет шерсти кошки.
        """
        self.color: str = color
        # символ подчеркивания указывает на защищенный атрибут
        self._type_: str = "cat"


# +
# Способ 2. Двойное подчеркивание перед названием атрибута


class CatClass:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс кошки с приватным атрибутом."""

    def __init__(self, color: str) -> None:
        """Инициализация кошки.

        Args:
            color: Цвет шерсти кошки.
        """
        self.color: str = color
        # символ двойного подчеркивания предотвратит доступ извне
        self.__type_: str = "cat"  # pylint: disable=unused-private-member


# +
matroskin = CatClass("gray")  # type: ignore[call-arg]

# теперь при вызове этого атрибута Питон выдаст ошибку
# matroskin.__type_

# +
# Наследование
# Наследование — это способность класса наследовать атрибуты
# и методы другого класса.

# +
# создадим класс Animal


class Animal:
    """Базовый класс для животных."""

    def __init__(self, weight: float, length: float) -> None:
        """Инициализация животного.

        Args:
            weight: Вес животного в килограммах.
            length: Длина животного в сантиметрах.
        """
        self.weight: float = weight
        self.length: float = length

    def eat(self) -> None:
        """Животное ест."""
        print("Eating")

    def sleep(self) -> None:
        """Животное спит."""
        print("Sleeping")


# +
# Создадим класс-потомок Bird (птица)


# создадим класс Bird, наследующий от Animal
class Bird(Animal):
    """Класс для представления птиц."""

    def move(self) -> None:
        """Птица летает."""
        print("Flying")


# -

# создадим объект pigeon и передадим ему значения веса и длины
pigeon: Bird = Bird(0.3, 30)

# посмотрим на унаследованные у класса Animal атрибуты
pigeon.weight, pigeon.length

# и методы
pigeon.eat()

# +
# Кроме того, мы можем вызвать метод, свойственный только классу Bird

pigeon.move()

# +
# Функция super()
# Предположим, что в наш класс Bird мы хотим добавить
# атрибут flying_speed (скорость полета).


# снова создадим класс Bird
class Bird(Animal):  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс птицы со скоростью полета."""

    def __init__(self, weight: float, length: float, flying_speed: float) -> None:
        """Инициализация птицы.

        Args:
            weight: Вес птицы в килограммах.
            length: Длина птицы в сантиметрах.
            flying_speed: Скорость полета в км/ч.
        """
        # вызовем метод родительского класса Animal
        super().__init__(weight, length)
        self.flying_speed: float = flying_speed

    def move(self) -> None:
        """Птица летает."""
        print("Flying")


# +
# Без функции super() класс Bird не знал бы откуда брать
# параметры weight и length.


# вновь создадим объект pigeon класса Bird с тремя параметрами
pigeon = Bird(0.3, 30, 100)  # type: ignore[call-arg]
# -

# вызовем как унаследованные, так и собственные атрибуты
pigeon.weight, pigeon.length, pigeon.flying_speed  # type: ignore[attr-defined]

# вызовем унаследованный метод .sleep()
pigeon.sleep()

# и собственный метод .move()
pigeon.move()

# +
# Переопределение класса
# Переопределение — это способность класса-потомка
# изменять поведение унаследованных методов.


# создадим подкласс Flightless для нелетающих птиц
class Flightless(Bird):  # pylint: disable=super-init-not-called
    """Класс для нелетающих птиц."""

    def __init__(self, running_speed: float) -> None:
        """Инициализация нелетающей птицы.

        Args:
            running_speed: Скорость бега в км/ч.
        """
        # у нас остается только один атрибут
        # pylint: disable=super-init-not-called
        self.running_speed: float = running_speed

    def move(self) -> None:
        """Нелетающая птица бежит."""
        print("Running")


# -

# Создадим объект ostrich (страус) класса Flightless
ostrich: Flightless = Flightless(60)

# Посмотрим на значение атрибута скорости
ostrich.running_speed

# Теперь посмотрим, переопределился ли метод .move()
ostrich.move()

# +
# Методы всех родительских классов передаются потомкам.

# применим метод .eat() класса Animal
ostrich.eat()

# +
# Множественное наследование

# Питон позволяет классу наследовать методы двух и более классов.

# Создадим класс SwimmingBird (водоплавающая птица)

# +
# создадим родительский класс Fish


class Fish:
    """Класс для представления рыб."""

    def swim(self) -> None:
        """Рыба плывет."""
        print("Swimming")


# +
# и еще один родительский класс Bird


class Bird:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс для представления птиц."""

    def fly(self) -> None:
        """Птица летает."""
        print("Flying")


# +
# родительские классы перечисляем в скобках через запятую


class SwimmingBird(Fish, Bird):
    """Класс для водоплавающих птиц."""


# +
# Создадим объект duck (утка) класса SwimmingBird

duck: SwimmingBird = SwimmingBird()  # type: ignore[call-arg]
# -

# Утка умеет как летать, так и плавать
duck.fly()  # type: ignore[attr-defined]

duck.swim()

# +
# Полиморфизм
# Полиморфизм — это способность методов с одинаковыми именами
# вести себя по-разному в разных классах.

# для чисел '+' является оператором сложения
2 + 2
# -

# для строк - оператором объединения
"классы" + " и " + "объекты"

# +
# Полиморфизм функций
# Полиморфизм функций — это способность одной функции
# работать с разными типами данных.
# -

len("Программирование на Питоне")

len(["Программирование", "на", "Питоне"])

len({0: "Программирование", 1: "на", 2: "Питоне"})

len(np.array([1, 2, 3]))

# +
# Полиморфизм классов
# Полиморфизм классов — это способность методов с одинаковыми
# именами в разных классах вести себя по-разному.

# +
# создадим класс котов


class CatClass:  # type: ignore[no-redef]  # pylint: disable=function-redefined
    """Класс для представления кошек."""

    def __init__(self, name: str, color: str) -> None:
        """Инициализация кошки.

        Args:
            name: Имя кошки.
            color: Цвет шерсти кошки.
        """
        self.name: str = name
        self._type_: str = "кот"
        self.color: str = color

    def info(self) -> None:
        """Выводит информацию о кошке."""
        print(
            f"Меня зовут {self.name}, я {self._type_}, "
            f"цвет моей шерсти {self.color}"
        )

    def sound(self) -> None:
        """Издает звук кошки."""
        print("Я умею мяукать")


# +
# создадим класс собак


class DogClass:
    """Класс для представления собак."""

    def __init__(self, name: str, color: str) -> None:
        """Инициализация собаки.

        Args:
            name: Имя собаки.
            color: Цвет шерсти собаки.
        """
        self.name: str = name
        self._type_: str = "пес"
        self.color: str = color

    def info(self) -> None:
        """Выводит информацию о собаке."""
        print(
            f"Меня зовут {self.name}, я {self._type_}, "
            f"цвет моей шерсти {self.color}"
        )

    def sound(self) -> None:
        """Издает звук собаки."""
        print("Я умею лаять")


# -

# Создадим объекты этих классов
cat: CatClass = CatClass("Бегемот", "черный")  # type: ignore[call-arg]
dog: DogClass = DogClass("Барбос", "серый")

# +
# Поместим объекты в кортеж и вызовем методы каждого класса

for animal in (cat, dog):
    animal.info()  # type: ignore[union-attr]
    animal.sound()  # type: ignore[union-attr]
    print()

# +
# Решим задачу о среднем росте с помощью класса

patients: list[dict[str, float | str]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# +
# создадим класс для работы с данными DataClass


class DataClass:
    """Класс для работы с данными и расчета средних значений."""

    def __init__(self, data: list[dict[str, float | str]]) -> None:
        """Инициализация класса с данными.

        Args:
            data: Список словарей с данными.
        """
        self.data: list[dict[str, float | str]] = data
        self.metric: str = ""
        self.__total: float = 0.0
        self.__count: int = 0

    def count_average(self, metric: str) -> float:
        """Расчет среднего значения по указанной метрике.

        Args:
            metric: Название метрики для расчета среднего.

        Returns:
            Среднее значение по указанной метрике.
        """
        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0.0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитем общую сумму по указанному в metric значению
            self.__total += float(item[self.metric])

            # и количество таких записей
            self.__count += 1

        # разделим общую сумму показателя на количество записей
        return self.__total / self.__count


# +
# создадим объект класса DataClass и передадим ему данные
data_object: DataClass = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
data_object.count_average("height")
