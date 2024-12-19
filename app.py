import sqlite3
from flask import Flask, render_template

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS presents")

# creating table
presents = """ CREATE TABLE presents(
            name CHAR(50) NOT NULL,
            present CHAR(25) NOT NULL,
            cost INT,
            status CHAR(50)
        ); """
cursor.execute(presents)
# INSERT records
cursor.execute('''INSERT INTO presents VALUES 
    ('Иванов Иван Иванович', 'Утенок', 3000, 'Куплен'),
    ('Петров Иван Иванович', 'Медвежонок', 5000, 'Не куплен'),
    ('Коростылёва Ольга Олеговна', 'Утенок', 3000, 'Не куплен'),
    ('Жданов Михаил Александрович', 'Машинка', 3000, 'Куплен'),
    ('Петухов Анатолий Александрович', 'Утенок', 3000, 'Куплен'),
    ('Мягков Дмитрий Петрович', 'Лошадка', 3000, 'Куплен'),
    ('Коростылева Лариса Григорьевна', 'Утенок', 3000, 'Куплен'),
    ('Куц Павел Андреевич', 'Утенок', 2000, 'Куплен'),
    ('Петрова Лариса Ивановна', 'Ваза', 3000, 'Куплен'),
    ('Петров Василий Иванович', 'Утенок', 3000, 'Куплен')
''')

connection.commit()
rows = cursor.execute('''SELECT * FROM presents''').fetchall()
connection.close()

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', items=rows)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)