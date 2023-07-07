import sqlite3

# подключение к базе данных
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект, который создает запросы и получает их результаты
cursor.execute('''DROP TABLE employes''')   # дроп таблицы
cursor.execute('''CREATE TABLE employes
(id INTEGER PRIMARY KEY, name TEXT, post TEXT, salary INTEGER)''')


# Вставка данных в таблицу
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Vasya', 'CEO', 1000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Nadya', 'Менеджер', 2000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Tolya', 'Сисадмин', 3000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Viktor', 'Девопс', 4000))


cursor.execute("SELECT * FROM employes WHERE post is 'Девопс'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения