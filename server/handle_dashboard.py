import json
import database as db


def logout(connection, req):
    return {'response': 'OK'}


def set_start_time(connection, req):
    return {'response': 'OK'}


def set_end_time(connection, req):
    return {'response': 'OK'}


action_dict = {
    'send_start_time': set_start_time,
    'send_end_time': set_end_time,
    'logout': logout
}


def handle_request(connection, req):
    req = json.loads(req)
    action = req.get('action')
    if action is None:
        return None
    else:
        result = action_dict[action](connection, req)
        return 'Yes' if result.get('response') == 'OK' else 'No'
