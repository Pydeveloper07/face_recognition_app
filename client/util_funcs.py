import json
from BrainOfFront import ReadData, SendData


def send_request(action: str):
    def inner(*args):
        req = {'action': action, 'username': args[0]}

        if action == 'set_start_time':
            req['start_time'] = args[1]
        elif action == 'set_end_time':
            req['end_time'] = args[1]

        SendData(json.dumps(req))
        return ReadData()

    return inner


# send_credentials = send_request('send_credentials')
# send_photo = send_request('send_photo')

send_start_time = send_request('send_start_time')
send_end_time = send_request('send_end_time')
logout = send_request('logout')


if __name__ == '__main__':
    pass
