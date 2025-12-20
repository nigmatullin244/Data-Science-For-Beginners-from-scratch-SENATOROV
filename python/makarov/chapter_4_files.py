"""Работа с файлами в Google Colab."""

# +
# Подгрузка файлов с локального компьютера на сервер Google.
# Способ 1. Вручную через вкладку 'Файлы'
# см. материалы урока на сайте

# +
# Способ 2. Через модуль files библиотеки google.colab
# Только для google.colab

# импортируем модуль os
import os

# импортируем библиотеку
import pandas as pd

# из библиотеки google.colab импортируем класс files
from google.colab import files

# создаем объект этого класса, применяем метод .upload()
uploaded = files.upload()
# Нам будет предложено выбрать файл на жестком диске.

# посмотрим на содержимое словаря uploaded
uploaded

# +
# Чтение файлов
# После загрузки оба файла (train.csv и test.csv)
# оказываются в сессионном хранилище в папке
# под названием /content/.

# Просмотр содержимого в папке /content/
# Модуль os и метод .walk()


# выводим пути к папкам (dirpath) и наименования файлов
# (filenames) и после этого
for dirpath, _, filenames in os.walk("/content/"):

    # во вложенном цикле проходимся по названиям файлов
    for filename in filenames:

        # и соединяем путь до папок и входящие в эти папки файлы
        # с помощью метода path.join()
        print(os.path.join(dirpath, filename))

# +
# Команда !ls

# посмотрим на содержимое папки content
# !ls

# заглянем внутрь sample_data
# !ls /content/sample_data/

# +
# Чтение из переменной uploaded


# посмотрим на тип значений словаря uploaded
type(uploaded["test.csv"])

# bytes

# обратимся к ключу словаря uploaded и применим метод .decode()
uploaded_str = uploaded["test.csv"].decode()

# на выходе получаем обычную строку
print(type(uploaded_str))

# +
# Если разбить строку методом .split() по символам \r
# (возврат к началу строки) и \n (новая строка),
# то на выходе мы получим список.

uploaded_list = uploaded_str.split("\r\n")
type(uploaded_list)  # list
# -

# пройдемся по этому списку, не забыв создать индекс с
# помощью функции enumerate()
for i, line in enumerate(uploaded_list):

    # начнем выводить записи
    print(line)

    # когда дойдем до четвертой строки
    if i == 3:

        # прервемся
        break

# +
# Использование функции open() и конструкции with open()
# Функция open() возвращает объект, который используется
# для чтения и изменения файла. Откроем файл train.csv.


# передадим функции open() адрес файла
with open("/content/train.csv", encoding="utf-8") as f:
    content = f.read()

# +
# Для наших целей метод .read() не очень удобен.
# Будет лучше пройтись по файлу в цикле for.

# снова откроем файл
with open("/content/train.csv", encoding="utf-8") as f1:
    for i, line in enumerate(f1):
        print(line.strip())
        if i == 3:
            break

# +
# Еще один способ — использовать конструкцию with open().
# В этом случае специально закрывать файл не нужно.

# скажем Питону: "открой файл и назови его f3"
with open("/content/test.csv", encoding="utf-8") as f3:

    # "пройдись по строкам без служебных символов"
    for i, line in enumerate(f3):
        print(line.strip())

        # и "прервись на четвертой строке"
        if i == 3:
            break

# +
# Чтение через библиотеку Pandas


# применим функцию read_csv() и посмотрим на первые три записи файла train.csv
train = pd.read_csv("/content/train.csv")
train.head(3)

# +
# Сохранение результата в новом файле на сервере
# Теперь, когда прогноз готов, мы можем сформировать новый файл,
# назовем его result.csv, в котором будет содержаться id
# пассажира и результат, погиб или нет.
# Приведу пример того, что мы хотим получить.

# файл с примером можно загрузить не с локального компьютера, а из Интернета
url = "https://www.dmitrymakarov.ru/wp-content/" + "uploads/2021/11/titanic_example.csv"

# просто поместим его url в функцию read_csv()
example = pd.read_csv(url)
example.head(3)

# +
# создадим новый файл result.csv с помощью функции to_csv(),
# удалив при этом индекс
# result.to_csv("result.csv", index=False)

# файл будет сохранен в 'Сессионном хранилище' и,
# если все пройдет успешно, выведем следующий текст:
# print("Файл успешно сохранился в сессионное хранилище!")
# -

# Скачивание обратно на жесткий диск
# После этого мы можем скачать файл на жесткий диск.
# применим метод .download() объекта files
files.download("/content/result.csv")
