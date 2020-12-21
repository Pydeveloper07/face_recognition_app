import json
import datetime
import database as db
from client.models import subject_list

isOff = False
user = {
    'user_id': 'u1810184',
    'password': '19990111'
}


def is_stop():
    return isOff


def login_handler(connection, req):
    # resp = {'status': 'Error'}
    #
    #
    # if req['user_id'] == user['user_id'] \
    #         and req['password'] == user['password']:
    #     resp['status'] = 'ok'
    # print(resp)

    # need to make request to database
    print(req)
    return {'status': 'ok'}


def logout_handler(connection, req):
    # need to make request to database
    print(req)

    global isOff
    isOff = True
    return {'status': 'ok'}


def get_subjects_handler(connection, req):
    # need to make request to database

    # resp = {'status': 'ok',
    #         'subjects': subject_list[0:3]}
    print(req)
    return {'status': 'ok'}


def enter_course_handler(connection, req):
    # need to make request to database
    print(req)
    cur_time = datetime.datetime.now()
    print(f'User entered course {req["course_id"]} at {cur_time} ')

    return {'status': 'ok'}


def exit_course_handler(connection, req):
    # need to make request to database
    print(req)
    cur_time = datetime.datetime.now()
    print(f'User left course {req["course_id"]} at {cur_time} ')

    return {'status': 'ok'}


handler_dict = {
    'login': login_handler,
    'logout': logout_handler,
    'get_subjects': get_subjects_handler,
    'enter_course': enter_course_handler,
    'exit_course': exit_course_handler,
}


def handle_request(connection, req):
    if len(req) == 0:
        return None
    req = json.loads(req)
    handler = req.get('action')
    if handler is None or handler not in handler_dict:
        return {'response': 'Error', 'reason': 'Unknown action'}
    else:
        result = handler_dict[handler](connection, req)
        return json.dumps(result)
