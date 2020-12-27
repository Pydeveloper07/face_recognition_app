import json
import database as db
import pathlib
import base64
import seeder
import faceRecognition as fr
import os

db_connection = db.connect()


def setup_database():
    db.create_tables(db_connection)
    seeder.seed_users(db_connection)
    seeder.seed_courses(db_connection)
    seeder.seed_takes(db_connection)
    db_connection.commit()


def parse_request(request_text):
    dict_request = json.loads(request_text)


    if dict_request['action'] == 'login':
        result = authenticate_user(dict_request['student_id'], dict_request['password'])
        print(result)


    elif dict_request['action'] == 'register_enter_time':
        result = register_enter_time(dict_request['student_id'], dict_request['course_id'])
    elif dict_request['action'] == 'register_exit_time':
        result = register_exit_time(dict_request['student_id'], dict_request['course_id'])
    elif dict_request['action'] == 'get_student_courses':
        result = get_student_courses(dict_request['student_id'])
    elif dict_request['action'] == 'get_teacher_courses':
        result = get_teacher_courses(dict_request['teacher_id'])
    elif dict_request['action'] == 'get_students_of_course':
        result = get_students_of_course(dict_request['course_id'])
    elif dict_request['action'] == 'face_recognition':
        result = face_recognition(dict_request['student_id'], dict_request['photo'])
    elif dict_request['action'] == 'get_students_enter_exit_times':
        result = get_students_enter_exit_times(dict_request['student_id'], dict_request['course_id'])
    else:
        result = ''
    db_connection.commit()

    return result


def authenticate_user(username, password):

    user = db.get_user_by_id_password(db_connection, username, password)
    dict_output = {}


    if len(user) > 0:
        dict_output['result'] = 'ok'
        dict_output['name'] = user[0][2]
        dict_output['type'] = user[0][3]
    else:
        dict_output['result'] = 'error'
        dict_output['error_text'] = 'User not found'
    print(dict_output)

    return json.dumps(dict_output)


def register_enter_time(student_id, course_id):
    db.register_enter_time(db_connection, student_id, course_id)
    return '{"result": "ok"}'


def register_exit_time(student_id, course_id):
    result = db.register_exit_time(db_connection, student_id, course_id)

    if result.rowcount > 0:
        return '{"result": "ok"}'
    else:
        return '{"result": "error"}'


def get_student_courses(user_id):
    courses = db.get_student_courses(db_connection, user_id)

    result = []

    for course in courses:
        course_structure = {
            'id':  course[0],
            'name': course[1],
            'description': course[2],
            'section': course[3],
            'professor': course[4]
        }
        result.append(course_structure)
    if len(result) > 0:
        return json.dumps({'result': 'ok',
                           'courses': result})
    else:
        return '{"result": "error"}'


def get_teacher_courses(user_id):
    courses = db.get_teacher_courses(db_connection, user_id)

    result = []

    for course in courses:
        course_structure = {
            'id':  course[0],
            'name': course[1],
            'description': course[2],
            'section': course[3],
            'student_count': course[4]
        }
        result.append(course_structure)

    if len(result) > 0:
        return json.dumps({'result': 'ok',
                           'courses': result})
    else:
        return '{"result": "error"}'


def get_students_of_course(course_id):
    students = db.get_students_of_course(db_connection, course_id)

    result = []

    for student in students:
        result.append({'id': student[0],
                       'name': student[1],
                       'first_access_date': student[2],
                       'last_access_date': student[3]})

    if len(result) > 0:
        return json.dumps({'result': 'ok',
                           'students': result})
    else:
        return '{"result": "error"}'


def face_recognition(user_id, file):
    with open(pathlib.Path().absolute() / 'student_image_1.jpg', 'wb') as file_to_save:
        file_to_save.write(base64.b64decode(file))
    pred = fr.face_recognition('student_image_1.jpg')
    os.remove('student_image_1.jpg')
    if pred==user_id:
        return '{"result": "ok"}'
    else:
        return '{"result": "failed"}'

def get_students_enter_exit_times(student_id, course_id):
    enter_exit_times = db.get_students_enter_exit_times(db_connection, student_id, course_id)

    if len(enter_exit_times) > 0:
        student_name = ''
        times_list = []
        for time in enter_exit_times:
            student_name = time[0]
            time_structure = {
                'enter_time': time[1],
                'exit_time': time[2]
            }

            times_list.append(time_structure)

        return json.dumps({
            'result': 'ok',
            'student_name': student_name,
            'times_list': times_list
        })

    else:
        return '{"result": "error"}'
