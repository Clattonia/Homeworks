# crud_functions.py
import sqlite3

# Функция для инициализации базы данных и создания таблицы Products
def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Создание таблицы Products, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    
    connection.commit()
    connection.close()

# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    connection = sqlite3.connect('db144.db')
    cursor = connection.cursor()
    
    # Выборка всех записей из таблицы Products
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    
    connection.close()
    return products