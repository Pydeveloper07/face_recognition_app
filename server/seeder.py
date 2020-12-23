import database as db


def seed_users(connection):
    if len(db.get_user_by_id(connection, 'admin')) == 0:
        db.add_user(connection, 'admin', 'admin', 'admin', 2)

    if len(db.get_user_by_id(connection, 'u1810087')) == 0:
        db.add_user(connection, 'u1810087', 'forker123', 'Fazliddin Akhmedov', 0)

    if len(db.get_user_by_id(connection, 'u1810075')) == 0:
        db.add_user(connection, 'u1810075', 'forker123', 'Javokhir Rajabov', 0)

    if len(db.get_user_by_id(connection, 'u1810171')) == 0:
        db.add_user(connection, 'u1810171', 'forker123', 'Tukhtamurod Isroilov', 0)

    if len(db.get_user_by_id(connection, 'u1810184')) == 0:
        db.add_user(connection, 'u1810184', 'forker123', 'Farrukh Koraev', 0)

    if len(db.get_user_by_id(connection, 'u1810197')) == 0:
        db.add_user(connection, 'u1810197', 'forker123', 'Mirshodjon Mirjonov', 0)

    if len(db.get_user_by_id(connection, 'u1810036')) == 0:
        db.add_user(connection, 'u1810036', 'forker123', 'Kamronbek Rustamov', 0)

    if len(db.get_user_by_id(connection, 't1810001')) == 0:
        db.add_user(connection, 't1810001', 'forker123', 'Tongzon Jose', 1)
    if len(db.get_user_by_id(connection, 't1810002')) == 0:
        db.add_user(connection, 't1810002', 'forker123', 'Abdul Rahim Naseer', 1)
    if len(db.get_user_by_id(connection, 't1810003')) == 0:
        db.add_user(connection, 't1810003', 'forker123', 'Agostini Alessandro', 1)
    if len(db.get_user_by_id(connection, 't1810004')) == 0:
        db.add_user(connection, 't1810004', 'forker123', 'Seth Ashish', 1)
    if len(db.get_user_by_id(connection, 't1810005')) == 0:
        db.add_user(connection, 't1810005', 'forker123', 'Dragunov Andrei', 1)


def seed_courses(connection):
    if len(db.get_course_by_id(connection, 0)) == 0:
        connection.execute(db.INSERT_INITIAL_COURSES, (0, "Operating System",
                                                       'An operating system (OS) is system software that manages '
                                                       'computer hardware, software resources, '
                                                       'and provides common services for computer programs. Time-sharing '
                                                       'operating systems schedule '
                                                       'tasks for efficient use of the system and may also include '
                                                       'accounting software for cost '
                                                       'allocation of processor time, mass storage, printing, and other '
                                                       'resources. For hardware functions '
                                                       'such as input and output and memory allocation, the operating '
                                                       'system acts as an intermediary '
                                                       'between programs and the computer hardware'))
    if len(db.get_course_by_id(connection, 4)) == 0:
        connection.execute(db.INSERT_INITIAL_COURSES, (4, "System Programming",
                                                       'An System Programming lorem ipsum'))

    if len(db.get_course_by_id(connection, 1)) == 0:
        connection.execute(db.INSERT_INITIAL_COURSES, (1, "Database",
                                                       'DBMS software primarily functions as an interface between the end user and the database, '
                                                       'simultaneously managing the data, the database engine, and the database schema in order to '
                                                       'facilitate the organization and manipulation of data. Though functions of DBMS vary greatly, '
                                                       'general-purpose DBMS features and capabilities should include: a user accessible catalog '
                                                       'describing metadata, DBMS library management system, data abstraction and independence, data '
                                                       'security, logging and auditing of activity, support for concurrency and transactions, support for '
                                                       'authorization of access, access support from remote locations, DBMS data recovery support in the '
                                                       'event of damage, and enforcement of constraints to ensure the data follows certain rules.'))
    if len(db.get_course_by_id(connection, 2)) == 0:
        connection.execute(db.INSERT_INITIAL_COURSES, (2, "Computer Algorithm",
                                                    'Consider how you use a computer in a typical day. For example, you start working on a report, '
                                                    'and once you have completed a paragraph, you perform a spell check. You open up a spreadsheet '
                                                    'application to do some financial projections to see if you can afford a new car loan. You use a '
                                                    'web browser to search online for a kind of car you want to buy. You may not think about this very '
                                                    'consciously, but all of these operations performed by your computer consist of algorithms. An '
                                                    'algorithm is a well-defined procedure that allows a computer to solve a problem. Another way to '
                                                    'describe an algorithm is a sequence of unambiguous instructions.'))

    if len(db.get_course_by_id(connection, 3)) == 0:
        connection.execute(db.INSERT_INITIAL_COURSES, (3, "System Analysis",
                                                    'System analysis is conducted for the purpose of studying a system or its parts in order to '
                                                    'identify its objectives. It is a problem solving technique that improves the system and ensures '
                                                    'that all the components of the system work efficiently to accomplish their purpose.'))


def seed_takes(connection):
    if len(db.get_takes_by_id(connection, 't1810001', 0)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('t1810001', 0, 1))
    if len(db.get_takes_by_id(connection, 't1810001', 4)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('t1810001', 4, 1))
    if len(db.get_takes_by_id(connection, 't1810002', 1)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('t1810002', 1, 1))
    if len(db.get_takes_by_id(connection, 't1810003', 2)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('t1810003', 2, 1))
    if len(db.get_takes_by_id(connection, 't1810004', 3)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('t1810004', 3, 1))
    if len(db.get_takes_by_id(connection, 'u1810087', 0)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810087', 0, 1))
    if len(db.get_takes_by_id(connection, 'u1810036', 0)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810036', 0, 1))
    if len(db.get_takes_by_id(connection, 'u1810075', 1)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810075', 1, 1))
    if len(db.get_takes_by_id(connection, 'u1810087', 1)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810087', 1, 1))
    if len(db.get_takes_by_id(connection, 'u1810036', 2)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810036', 2, 1))
    if len(db.get_takes_by_id(connection, 'u1810075', 2)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810075', 2, 1))
    if len(db.get_takes_by_id(connection, 'u1810197', 3)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810197', 3, 1))
    if len(db.get_takes_by_id(connection, 'u1810184', 3)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810184', 3, 1))
    if len(db.get_takes_by_id(connection, 'u1810197', 0)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810197', 0, 1))
    if len(db.get_takes_by_id(connection, 'u1810184', 0)) == 0:
        connection.execute(db.INSERT_INITIAL_TAKES, ('u1810184', 0, 1))
