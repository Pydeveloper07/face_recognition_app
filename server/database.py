import sqlite3

# user type = 0 - for student; 1 - for teacher; 2 - for admin
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, password TEXT, name TEXT, type INTEGER);"

CREATE_COURSES_TABLE = """
    CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT);
"""

CREATE_TAKES_TABLE = """
    CREATE TABLE IF NOT EXISTS takes (user_id TEXT, course_id INTEGER , section INTEGER, 
                                        PRIMARY KEY (user_id, course_id),
                                        FOREIGN KEY (user_id) REFERENCES users (id) ON UPDATE SET NULL,
                                        FOREIGN KEY (course_id) REFERENCES courses (id) ON UPDATE SET NULL);
"""

CREATE_TIME_TRACKER_TABLE = """
    CREATE TABLE IF NOT EXISTS time_tracker (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            student_id TEXT, 
                                            course_id INTEGER,
                                            enter_time TEXT,
                                            exit_time TEXT,
                                            FOREIGN KEY (student_id) REFERENCES users (id) ON UPDATE SET NULL,
                                            FOREIGN KEY (course_id) REFERENCES courses (id) ON UPDATE SET NULL);
"""

REGISTER_ENTER_TIME = "INSERT INTO time_tracker (student_id, course_id, enter_time) VALUES (?,?, datetime('now', 'localtime'));"
REGISTER_EXIT_TIME = """
    UPDATE time_tracker
    SET exit_time = datetime('now', 'localtime')
    WHERE
        (student_id, course_id) = (?,?) AND exit_time IS NULL 
"""

INSERT_INITIAL_USERS = "INSERT INTO users(id, password, name, type) VALUES (?,?,?,?);"
INSERT_INITIAL_COURSES = "INSERT INTO courses(id, name, description) VALUES (?,?,?);"
INSERT_INITIAL_TAKES = "INSERT INTO takes(user_id, course_id , section) VALUES (?,?,?);"

GET_USER_BY_ID = "SELECT * FROM users WHERE id = ?;"
GET_COURSE_BY_ID = "SELECT * FROM courses WHERE id = ?;"
GET_TAKES_BY_ID = "SELECT * FROM takes WHERE (user_id,course_id) = (?,?);"

GET_USER_BY_ID_PASSWORD = "SELECT * FROM users WHERE (id, password) = (?, ?);"
GET_TEACHER_COURSES = """
    SELECT C.id, C.name, C.description, T.section, IFNULL(student_count, 0) as student_count
    FROM users as U
    INNER JOIN takes as T on U.id = T.user_id
    INNER JOIN courses as C on T.course_id = C.id
    LEFT JOIN (SELECT takes.course_id as course_id, takes.section as section, COUNT(DISTINCT takes.user_id) as student_count 
               FROM takes 
               INNER JOIN users ON takes.user_id = users.id
               WHERE users.type = 0
               GROUP BY takes.course_id, takes.section) AS Q ON T.course_id = Q.course_id AND T.section = Q.section
    WHERE U.id = ? AND U.type = 1
    ORDER BY C.name
"""

GET_STUDENT_COURSES = """
    SELECT C.id, C.name, C.description, T.section, S.teacher_name
    FROM users as U
    INNER JOIN takes as T on U.id = T.user_id
    INNER JOIN courses as C on T.course_id = C.id
    LEFT JOIN (SELECT T.section as section, T.course_id as course_id, T.user_id as user_id, U.name as teacher_name 
                FROM takes as T 
                INNER JOIN users as U on T.user_id  = U.id
                WHERE U.type = 1) as S on T.section = S.section and T.course_id = S.course_id
    WHERE U.id = ? AND U.type = 0
    ORDER BY C.name
"""

GET_STUDENTS_OF_COURSE = """
    SELECT U.id, U.name, 
    IFNULL(MM.first_access_time, DATETIME("0000-01-01 00:00:00")) as first_access_time,
    IFNULL(MM.last_access_time, DATETIME("0000-01-01 00:00:00")) as last_access_time
    FROM users as U
    INNER JOIN takes as T on U.id = T.user_id
    LEFT JOIN (SELECT MIN(DATETIME(enter_time)) as first_access_time, MAX(DATETIME(exit_time)) as last_access_time, student_id, course_id
               FROM time_tracker
               GROUP BY student_id, course_id) AS MM ON T.user_id = MM.student_id AND T.course_id = MM.course_id 
    WHERE U.type = 0 AND T.course_id = ?
    ORDER BY U.name     
"""

GET_STUDENTS_ENTER_EXIT_TIMES = """
    SELECT U.name, T.enter_time, T.exit_time
    FROM time_tracker AS T INNER JOIN users AS U on T.student_id = U.id
    WHERE (U.id, T.course_id) = (?,?)
"""


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_COURSES_TABLE)
        connection.execute(CREATE_TAKES_TABLE)
        connection.execute(CREATE_TIME_TRACKER_TABLE)


def add_user(connection, user_id, password, name, user_type):
    connection.execute(INSERT_INITIAL_USERS, (user_id, password, name, user_type,))


def add_student(connection, user_id, password, name):
    add_user(connection, user_id, password, name, 1)


def register_enter_time(connection, student_id, course_id):
    connection.execute(REGISTER_ENTER_TIME, (student_id, course_id))


def register_exit_time(connection, student_id, course_id):
    return connection.execute(REGISTER_EXIT_TIME, (student_id, course_id))


def get_user_by_id(connection, user_id):
    return connection.execute(GET_USER_BY_ID, (user_id,)).fetchall()


def get_user_by_id_password(connection, user_id, password):
    return connection.execute(GET_USER_BY_ID_PASSWORD, (user_id, password)).fetchall()


def get_student_courses(connection, user_id):
    return connection.execute(GET_STUDENT_COURSES, (user_id,)).fetchall()


def get_teacher_courses(connection, user_id):
    return connection.execute(GET_TEACHER_COURSES, (user_id,)).fetchall()


def get_students_of_course(connection, course_id):
    return connection.execute(GET_STUDENTS_OF_COURSE, (course_id,)).fetchall()


def get_course_by_id(connection, course_id):
    return connection.execute(GET_COURSE_BY_ID, (course_id,)).fetchall()


def get_takes_by_id(connection, user_id, course_id):
    return connection.execute(GET_TAKES_BY_ID, (user_id, course_id)).fetchall()


def get_students_enter_exit_times(connection, student_id, course_id):
    return connection.execute(GET_STUDENTS_ENTER_EXIT_TIMES, (student_id, course_id)).fetchall()
