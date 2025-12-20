"""Библиотека Pandas."""

# +
# импортируем модуль sqlite3 для работы с базой данных SQL
import sqlite3 as sql

import numpy as np
import pandas as pd

# +
# Создание датафрейма
# Способ 1. Создание датафрейма из файла

# функция read_csv() распознает zip-архивы,
# в архиве может содержаться только один файл
csv_zip = pd.read_csv(r"K:\Storage\makarov\train.zip")
csv_zip.head(3)
# -

# импортируем данные в формате Excel, указав номер листа,
# который хотим использовать
excel_data = pd.read_excel(r"K:\Storage\makarov\iris.xlsx", sheet_name=0)
excel_data.head(3)

# +
# Файл в формате html.
# передадим соответствующую ссылку в функцию pd.read_html()
# в параметре match укажем ключевые слова, которые
# помогут найти нужную таблицу
html_data = pd.read_html(
    "https://en.wikipedia.org/wiki/World_population", match="World population"
)

# # мы получили пять результатов
len(html_data)
# -

html_data[0]

# +
# Способ 2. Подключение к базе данных SQL


# создадим соединение с базой данных chinook
conn = sql.connect(r"K:\Storage\makarov\chinook.db")

# выберем все строки из таблицы tracks
sql_data = pd.read_sql("SELECT * FROM tracks;", conn)  # vs. read_sql_query

# посмотрим на результат
sql_data.head(3)

# +
# Способ 3. Создание датафрейма из словаря

# создадим несколько списков и массивов Numpy
# с информацией о семи странах мира
country = np.array(
    [
        "China",
        "Vietnam",
        "United Kingdom",
        "Russia",
        "Argentina",
        "Bolivia",
        "South Africa",
    ]
)
capital = ["Beijing", "Hanoi", "London", "Moscow", "Buenos Aires", "Sucre", "Pretoria"]
population = [1400, 97, 67, 144, 45, 12, 59]  # млн. человек
area = [9.6, 0.3, 0.2, 17.1, 2.8, 1.1, 1.2]  # млн. кв. км.
sea = [1] * 5 + [0, 1]  # выход к морю (в этом списке его нет только у Боливии)

# +
# создадим пустой словарь
countries_dict = {}

# превратим эти списки в значения словаря,
# одновременно снабдив необходимыми ключами
countries_dict["country"] = country
countries_dict["capital"] = capital  # type: ignore[assignment]
countries_dict["population"] = population  # type: ignore[assignment]
countries_dict["area"] = area  # type: ignore[assignment]
countries_dict["sea"] = sea  # type: ignore[assignment]
# -

# посмотрим на результат
countries_dict

# создадим датафрейм
countries = pd.DataFrame(countries_dict)
countries

# +
# Способ 4. Создание датафрейма из 2D массива Numpy

# внешнее измерение будет столбцами, внутренее - строками
arr = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

pd.DataFrame(arr)

# +
# Структура и свойства датафрейма
# Датафрейм библиотеки Pandas состоит из трех основных компонентов:
# строк (index), столбцов (columns) и значений (values).

# выведем столбцы датафрейма countries
countries.columns
# -

# в нашем случае индекс это числовая последовательность
countries.index

# значения выводятся в формате массива Numpy
countries.values

# выведем описание индекса датафрейма через атрибут axes[0]
countries.axes[0]

# axes[1] выводит названия столбцов
countries.axes[1]

countries.ndim, countries.shape, countries.size

# +
# Атрибут dtypes выдает тип данных каждого столбца.

countries.dtypes

# +
# Кроме того, с помощью метода .memory_usage() мы можем посмотреть
# объем занимаемой памяти по столбцам в байтах.

countries.memory_usage()

# +
# Индекс датафрейма
# Присвоение индекса

# создадим список с кодами стран
custom_index = ["CN", "VN", "GB", "RU", "AR", "BO", "ZA"]

# создадим датафрейм из словаря и передадим список через параметр index
countries = pd.DataFrame(countries_dict, index=custom_index)

# посмотрим на результат
countries

# +
# Этот индекс можно сбросить с помощью метода .reset_index().

# при этом параметр inplace = True сделает изменения постоянными
countries.reset_index(inplace=True)
countries

# +
# Как мы видим, прошлый индекс стал отдельным столбцом.
# Снова сделаем этот столбец индексом
# с помощью метода .set_index().

# передадим методу название столбца, который хотим сделать индексом
countries.set_index("index", inplace=True)
countries

# +
# Еще раз сбросим индекс, но на этот раз не будем делать его отдельным
# столбцом. Для этого передадим методу .reset_index() параметр drop = True.

countries.reset_index(drop=True, inplace=True)
countries

# +
# Собственный индекс можно создать, просто поместив
# новые значения в атрибут index.


countries.index = custom_index  # type: ignore[assignment]
countries

# +
# Многоуровневый индекс

# Многоуровневый (MultiIndex) или иерархический (hierarchical) индекс
# позволяет задать несколько уровней (levels) для индексации строк или столбцов

# создадим список из кортежей с названием континента и кодом страны
rows = [
    ("Asia", "CN"),
    ("Asia", "VN"),
    ("Europe", "GB"),
    ("Europe", "RU"),
    ("S. America", "AR"),
    ("S. America", "BO"),
    ("Africa", "ZA"),
]

# +
# в столбцах название страны и столицы мы объединим в категорию names
# а размер населения, площадь и выход к морю в data

cols = [
    ("names", "country"),
    ("names", "capital"),
    ("data", "population"),
    ("data", "area"),
    ("data", "sea"),
]

# +
# Теперь создадим иерархический индекс для строк и столбцов
# с помощью функции pd.MultiIndex.from_tuples().

# создадим многоуровневый индекс для строк
# индексам присвоим названия через names = ['region', 'code']
custom_multindex = pd.MultiIndex.from_tuples(rows, names=["region", "code"])

# сделаем то же самое для столбцов
custom_multicols = pd.MultiIndex.from_tuples(cols)

# +
countries.index = custom_multindex
countries.columns = custom_multicols

countries

# +
# вернемся к обычному индексу и названиям столбцов
custom_cols = ["country", "capital", "population", "area", "sea"]

countries.index = custom_index  # type: ignore[assignment]
countries.columns = custom_cols  # type: ignore[assignment]

countries

# +
# Преобразование в другие форматы
# Получившийся датафрейм можно преобразовать в словарь с помощью метода .to_dict().

print(countries.to_dict())

# +
# Аналогично, метод .to_numpy() преобразовывает данные в массив Numpy.

countries.to_numpy()
# -

# по умолчанию, индекс также станет частью .csv файла
# параметр index = False позволит этого избежать
countries.to_csv("countries.csv", index=False)

# +
# Метод .to_list() позволяет преобразовать объект Series
# (столбец датафрейма) в список.

print(countries.country.to_list())
# -

# Создание Series
country_list = [
    "China",
    "South Africa",
    "United Kingdom",
    "Russia",
    "Argentina",
    "Vietnam",
    "Australia",
]

country_series = pd.Series(country_list)
country_series

# например, выведем первый элемент
country_series[0]

# +
# Создание Series из словаря

country_dict = {
    "CN": "China",
    "ZA": "South Africa",
    "GB": "United Kingdom",
    "RU": "Russia",
    "AR": "Argentina",
    "VN": "Vietnam",
    "AU": "Australia",
}
# -

country_series = pd.Series(country_dict)
country_series

country_series["AU"]

# +
# Доступ к строкам, столбцам и элементам
# Циклы в датафрейме
# Цикл for позволяет получить доступ к названиям столбцов датафрейма.

for column in countries:
    print(column)

# +
# Метод .iterrows() возвращает индекс строки и ее содержимое в формате Series.

# прервем цикл после первой итерации с помощью break
for index, row in countries.iterrows():
    print(index)
    print(row)
    print("...")
    print(type(row))
    break

# +
# Получить доступ к элементам одной строки можно
# по индексу объекта Series
# (то есть по названиям столбцов исходного датафрейма).

for _, row in countries.iterrows():
    # например, сформируем вот такое предложение
    print(row["capital"] + " is the capital of " + row["country"])
    break

# +
# Доступ к столбцам

# выведем столбец capital датафрейма countries
countries["capital"]
# -

# однако в этом случае название не должно содержать пробелов
countries.capital

# Как уже было сказано, отдельные столбцы в датафрейме имеют тип данных Series.
type(countries.capital)

# +
# Для того чтобы получить доступ к столбцам и
# при этом на выходе сформировать датафрейм,
# необходимо использовать двойные скобки.

# логика здесь в том, что внутрениие скобки - это список,
# внешние - оператор индексации
countries[["capital"]]
# -

countries[["capital", "area"]]

# +
# Доступ к столбцам можно также получить с помощью метода
# .filter(), передав параметру items список с
# необходимыми нам столбцами.

countries.filter(items=["capital", "population"])

# +
# Доступ к строкам

# выведем строки со второй по пятую (не включительно)
countries[1:5]

# +
# Методы .loc[] и .iloc[]
# Метод .loc[] позволяет получить доступ к строкам и столбцам через
# их названия (label-based location)
# -

# для этого передадим методу .loc[] два списка:
# с индексами строк и названиями столбцов
countries.loc[["CN", "RU", "VN"], ["capital", "population", "area"]]

# +
# Через двоеточие, как и в Numpy, мы можем вывести
# все строки или все столбцы датафрейма


# например, выведем все строки датафрейма
countries.loc[:, ["capital", "population", "area"]]

# +
# Метод .loc[] также поддерживает значения Boolean


# например, выведем все строки и только последний столбец,
# передав список соответствующих логических значений
countries.loc[:, [False, False, False, False, True]]

# +
# Метод .get_loc() позволяет узнать порядковый номер
# (начиная с нуля) строки или столбца по их индексу
# и названию соответственно.

# выведем номер строки с индексом RU
countries.index.get_loc("RU")
# -

countries.columns.get_loc("country")

# +
# Метод .iloc[]
# Метод .iloc[] действует примерно также, как и .loc[],
# с тем отличием, что он основывается на числовом индексе
# (integer-based location).

# теперь в списки мы передаем номера строк и столбцов,
# нумерация начинается с нуля
countries.iloc[[0, 3, 5], [0, 1, 2]]
# -

# выведем первые три строки и последние два столбца
countries.iloc[:3, -2:]

# +
# К столбцам удобно обращаться по их названиям, к строкам —
# по порядковому номеру (числовому индексу).

# вначале передадим названия столбцов в двойных скобках,
# затем номера строк через метод .iloc[]
countries[["population", "area"]].iloc[[0, 3]]

# +
# Многоуровневый индекс и методы .loc[] и .iloc[]
# вновь создадим датафрейм с многоуровневым индексом по строкам и столбцам
countries.index = custom_multindex
countries.columns = custom_multicols

countries

# +
# Для доступа к первой строке передадим методу
# .loc[] соответствующий двойной индекс.

countries.loc["Asia", "CN"]
# -

# выведем первую строку и столбцы с числовыми данными
countries.loc[
    ("Asia", "CN"), [("data", "population"), ("data", "area"), ("data", "sea")]
]

# +
# Доступ к строкам можно получить, указав внутри кортежа
# название региона и список с кодами стран.

countries.loc[("Asia", ["CN", "VN"]), :]

# +
# Внутри кортежа можно указать только регион. В этом случае
# мы получим все находящиеся в нем страны.

countries.loc[("Asia"), :]

# +
# Аналогичным образом мы можем получить доступ к столбцам.

countries.loc[:, [("names", "country"), ("data", "population")]]

# +
# Метод .iloc[], при этом, игнорирует структуру иерархического индекса
# и использует простой числовой индекс.

# получим доступ к четвертой строке и третьему, четвертому и пятому столбцам
countries.iloc[3, [2, 3, 4]]

# +
# Метод .xs()
# Метод .xs() (от англ. cross-section, срез) позволяет получить доступ
# к определенному уровню иерархического индекса. Начнем со строк.

# выберем Европу из уровня region
# axis = 0 указывает, что мы берем строки
countries.xs("Europe", level="region", axis=0)
# -

# levels указывает, на каких уровнях искать названия столбцов
# параметр axis = 1 говорит о том, что мы имеем дело со столбцами
countries.xs(("names", "country"), axis=1)

# +
# Кроме того, мы можем соединить два метода .xs() и одновременно
# получить доступ и к строкам, и к столбцам.

# в данном случае мы можем не указывать level, потому что
# Europe и names находятся во внешних индексах,
# которые в level указаны по умолчанию
countries_xs = countries.xs("Europe", axis=0).loc[:, "names"]
countries_xs

# +
# Вернем датафрейму одноуровневый индекс.

# обновим атрибуты index и columns
countries.index = custom_index  # type: ignore[assignment]
countries.columns = custom_cols  # type: ignore[assignment]

# посмотрим на исходный датафрейм
countries

# +
# Метод .at[]
# Метод .at[] подходит для извлечения или записи одного значения датафрейма.

countries.at["CN", "capital"]
# -

# Фильтры
# создадим логическую маску для стран с населением больше миллиарда человек
countries.population > 1000

# применим логическую маску к исходному датафрейму
countries[countries.population > 1000]

# отфильтруем датафрейм по критериям численности населения и площади
countries[(countries.population > 50) & (countries.area < 2)]

# +
# вначале создаем нужные нам маски
population_mask = countries.population > 70
area_mask = countries.population < 50

# затем объединяем их по необходимым условиям (в данном случае ИЛИ)
mask = population_mask | area_mask
# и применяем маску к исходному датафрейму
countries[mask]

# +
# Метод .query()
# Метод .query() позволяет задавать условие фильтрации «своими словами».

# например, выберем страны с населением более 50 млн. человек И
# площадью менее двух млн. кв. километров
countries.query("population > 50 and area < 2")
# -

# выведем данные по Великобритании
countries.query("country == 'United Kingdom'")

# +
# С помощью метода .isin() мы можем проверить наличие нескольких значений
# в определенном столбце, а затем использовать результат
# в качестве логической маски.

# найдем строки, в которых в столбце capital присутствуют следующие значения
keyword_list = ["Beijing", "Moscow", "Hanoi"]

countries_print = countries[countries.capital.isin(keyword_list)]
print(countries_print)
# -

# Похожим образом можно использовать метод .startswith().
# например, для нахождения стран, НЕ начинающихся с буквы "A"
countries_start = countries[~countries.country.str.startswith("A")]
countries_start

# например, возьмем три строки с наибольшими значением по столбцу population
countries.nlargest(3, "population")

# +
# Метод .argmax() выводит индекс строки, в которой в
# определенном столбце содержится наибольшее значение.

# например, предположим, что мы хотим найти индекс страны с наибольшей площадью
countries_max = countries.area.argmax()
countries_max

# +
# Посмотрим, какой стране соответствует этот индекс.

# напомню, что двойные скобки позволяют вывести DataFrame, а не Series
countries_area = countries.iloc[[countries.area.argmax()]]
countries_area

# +
# Вспомним, что в метод .loc[] можно передать тип данных Boolean.
# Используем это свойство для создания фильтра.

# выведем страны с населением более 90 млн. человек
countries.loc[countries.population > 90, :]

# +
# Метод .filter(), если использовать параметр like,
# ищет совпадения с искомой фразой в индексе
# (если axis = 0) или названии столбцов (если axis = 1).

# найдем строки, в которых в индексе есть буквосочетание "ZA"
countries.filter(like="ZA", axis=0)
# -

# Сортировка
# выполним сортировку по столбцу population, не сохраняя изменений,
# в возрастающем порядке (значение по умолчанию)
countries.sort_values(by="population", inplace=False, ascending=True)

# теперь отсортируем по двум столбцам в нисходящем порядке
countries.sort_values(by=["area", "population"], inplace=False, ascending=False)

# +
# Кроме того, можно отсортировать строки по индексу с помощью метода .sort_index().

countries.sort_index()
