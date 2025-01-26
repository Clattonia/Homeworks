import sqlite3
from crud_functions145 import initiate_db

# Указываем имя базы данных
db_name = 'db145.db'

# Инициализация базы данных и создание таблиц
initiate_db(db_name)

# Подключение к базе данных
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Данные для вставки
products = [
    ("Product1", "Описание продукта 1", 100),
    ("Product2", "Описание продукта 2", 200),
    ("Product3", "Описание продукта 3", 300),
    ("Product4", "Описание продукта 4", 400),
]

# Вставка данных
cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products)

# Фиксация изменений и закрытие соединения
connection.commit()
connection.close()