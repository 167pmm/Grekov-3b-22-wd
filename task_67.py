import sqlite3

# подключение к базе данных
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект, который создает запросы и получает их результаты
cursor.execute('''DROP TABLE books''')   # дроп таблицы
cursor.execute('''CREATE TABLE books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, realise DATE)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Гарри Поттер', 'Дж.Роулинг', '2003-09-07'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Закон трех отрицаний', 'Александра Маринина', '2003-11-07'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Персональный ангел', 'Татьяна Устинова', '1999-01-01'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Там, где нас нет', 'Татьяна Устинова', '1998-01-01'))


cursor.execute("SELECT * FROM books WHERE realise >= '2000-01-01'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения