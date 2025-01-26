# populate_db.py
import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('db144.db')
cursor = connection.cursor()

# Добавление записей в таблицу Products
products = [
    ("Product1", "Описание продукта 1", 100),
    ("Product2", "Описание продукта 2", 200),
    ("Product3", "Описание продукта 3", 300),
    ("Product4", "Описание продукта 4", 400),
]

cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products)

# Фиксация изменений и закрытие соединения
connection.commit()
connection.close()