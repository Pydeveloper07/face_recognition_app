import sqlite3

CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, password TEXT, name TEXT, type INTEGER);"
INSERT_INITIAL_USERS = "INSERT INTO users(id, password, name, type) VALUES (?,?,?,?);"
GET_USER_BY_ID = "SELECT * FROM users WHERE id = ?;"
GET_USER_BY_ID_PASSWORD = "SELECT * FROM users WHERE (id, password) = (?, ?);"


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)


def add_user(connection, user_id, password, name, user_type):
    connection.execute(INSERT_INITIAL_USERS, (user_id, password, name, user_type,))


def add_student(connection, user_id, password, name):
    add_user(connection, user_id, password, name, 1)


def get_user_by_id(connection, user_id):
    return connection.execute(GET_USER_BY_ID, (user_id,)).fetchall()


def get_user_by_id_password(connection, user_id, password):
    connection = connect()
    return connection.execute(GET_USER_BY_ID_PASSWORD, (user_id, password),).fetchall()


def seed_users(connection):
    if len(get_user_by_id(connection, 'u1810087')) == 0:
        add_user(connection, 'u1810087', 'forker123', 'Fazliddin Akhmedov', 0)

    if len(get_user_by_id(connection, 'u1810075')) == 0:
        add_user(connection, 'u1810075', 'forker123', 'Javokhir Rajabov', 0)

    if len(get_user_by_id(connection, 'u1810171')) == 0:
        add_user(connection, 'u1810171', 'forker123', 'Tukhtamurod Isroilov', 0)

    if len(get_user_by_id(connection, 'u1810184')) == 0:
        add_user(connection, 'u1810184', 'forker123', 'Farrukh Koraev', 0)

    if len(get_user_by_id(connection, 'u1810197')) == 0:
        add_user(connection, 'u1810197', 'forker123', 'Mirshodjon Mirjonov', 0)

    if len(get_user_by_id(connection, 'u1810036')) == 0:
        add_user(connection, 'u1810036', 'forker123', 'Kamronbek Rustamov', 0)
