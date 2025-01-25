import sqlite3

# Подключение к базе данных (или создание, если её нет)
connection = sqlite3.connect('data142.db')
cursor = connection.cursor()

# Создание таблицы Users, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER  
)
''')

# Создание индекса для поля email, если он не существует
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Вставка данных в таблицу Users
for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i}", f"ex{i}@gmail.xyu", i + 10, 1000))  # Исправлены скобки и добавлен balance

# Обновление данных в таблице Users
cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")
cursor.execute("DELETE FROM Users WHERE age > 15")


# Подключение к базе данных


# Запрос для получения суммы баланса
cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]  # Получаем сумму баланса

# Запрос для получения среднего значения баланса
cursor.execute("SELECT AVG(balance) FROM Users")
average_balance = cursor.fetchone()[0]  # Получаем среднее значение баланса

# Вывод результатов
print(f"Общая сумма баланса: {total_balance}")
print(f"Средний баланс: {average_balance}")

# Закрытие соединения

# Фиксация изменений и закрытие соединения
connection.commit()
connection.close()