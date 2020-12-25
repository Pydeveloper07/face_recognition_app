import json
from BrainOfFront import ReadData, SendData
import base64


def encode_image(filename):
    with open(filename, 'rb') as f:
        img = base64.b64encode(f.read())
    return img.decode()


def send_request(action: str):
    def inner(*args):
        req = {'action': action, 'student_id': args[0]}

        if action == 'login':
            req['password'] = args[1]
        elif action in ('register_enter_time', 'register_exit_time', 'logout'):
            req['course_id'] = args[1]
        elif action in ('face_recognition',):
            req['photo'] = encode_image(args[1])

        SendData(json.dumps(req))
        resp = ReadData()
        return json.loads(resp)

    return inner


login = send_request('login')
face_recognition = send_request('face_recognition')
logout = send_request('logout')
get_subject_list = send_request('get_student_courses')
enter_course = send_request('register_enter_time')
exit_course = send_request('register_exit_time')

if __name__ == '__main__':
    pass
