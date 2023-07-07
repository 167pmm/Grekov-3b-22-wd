import sqlite3

# подключение к базе данных
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект, который создает запросы и получает их результаты
cursor.execute('''DROP TABLE films''')   # дроп таблицы
cursor.execute('''CREATE TABLE films
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating INTEGER)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Васаби', 'боевик', 9.7))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Копы в юбках', 'комедия', 8.6))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Девичник в Вегасе', 'романтика', 8.9))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Берегись автомобиля', 'криминал', 7.6))


cursor.execute("SELECT * FROM films WHERE genre is 'комедия'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения