import server_utils as utils
import json

utils.setup_database()
# print(utils.parse_request(
#     json.dumps({
#         "action": "login",
#         "username": "t1810002",
#         "password": "forker123"})
# ))
# print(utils.parse_request(
#     json.dumps({
#         "action": "register_enter_time",
#         "student_id": "u1810036",
#         "course_id": 3})
# ))

print(utils.parse_request(
    json.dumps({
        "action": "get_students_of_course",
        "course_id": '0'
    })
))

# print(utils.parse_request(
#     json.dumps({
#         "action": "register_enter_time",
#         "student_id": "u1810087",
#         "course_id": 1})
# ))
#
# print(utils.parse_request(
#     json.dumps({
#         "action": "register_exit_time",
#         "student_id": "u1810087",
#         "course_id": 1})
# ))

#
# print(utils.parse_request(
#     json.dumps({
#         "action": "get_teacher_courses",
#         "teacher_id": "t1810002"})
# ))

print(utils.parse_request(
    json.dumps({
        "action": "get_students_enter_exit_times",
        "course_id": 0,
        "student_id": 'u1810087'
    })
))
