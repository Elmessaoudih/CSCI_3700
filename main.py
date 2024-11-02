from flask import Flask, render_template
import util

app = Flask(__name__)

# Database connection details
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

@app.route('/')
def index():
    return "Welcome to the Fruit Basket API!"

@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    if cursor is None or connection is None:
        return "Error connecting to the database."

    sql_command = "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');"
    result = util.run_and_fetch_sql(cursor, sql_command)
    if result == -1:
        message = "Error with the SQL command."
    else:
        connection.commit()
        message = "Success!"

    util.disconnect_from_db(connection, cursor)
    return message

@app.route('/api/unique')
def unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    if cursor is None or connection is None:
        return "Error connecting to the database."

    sql_command_a = "SELECT DISTINCT fruit_a FROM basket_a;"
    sql_command_b = "SELECT DISTINCT fruit_b FROM basket_b;"

    record_a = util.run_and_fetch_sql(cursor, sql_command_a)
    record_b = util.run_and_fetch_sql(cursor, sql_command_b)

    if record_a == -1 or record_b == -1:
        log = []
        col_names = []
    else:
        col_names = ["Unique Fruits in Basket A", "Unique Fruits in Basket B"]
        max_length = max(len(record_a), len(record_b))
        log = [(record_a[i][0] if i < len(record_a) else None,
                record_b[i][0] if i < len(record_b) else None)
               for i in range(max_length)]

    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', sql_table=log, table_title=col_names)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')

