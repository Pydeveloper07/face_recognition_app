import json
from BrainOfFront import ReadData, SendData
import base64


def send_request(action: str):
    def inner(*args):
        req = {'action': action, 'user_id': args[0]}

        if action == 'login':
            req['password'] = args[1]
        elif action in ('enter_course', 'exit_course', 'logout'):
            req['course_id'] = args[1]

        SendData(json.dumps(req))
        resp = ReadData()
        return json.loads(resp)

    return inner


login = send_request('login')
# send_photo = send_request('send_photo')
logout = send_request('logout')
get_subject_list = send_request('get_subjects')
enter_course = send_request('enter_course')
exit_course = send_request('exit_course')

if __name__ == '__main__':
    pass
