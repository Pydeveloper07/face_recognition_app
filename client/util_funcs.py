from BrainOfFront import SendFile, SendData, ReadData
import json


def send_request(action: str):
    def inner(*args):
        req = {'action': action, 'username': args[0]}

        if action == 'check_credentials':
            req['password'] = args[1]
        elif action == 'set_time_spent':
            req['time_spent'] = args[1]

        print(json.dumps(req))
        SendData(json.dumps(req))
        return ReadData()

    return inner


def check_photo(photo):
    SendFile(photo)


check_credentials = send_request('check_credentials')
logout = send_request('logout')
set_time_spent = send_request('set_time_spent')
