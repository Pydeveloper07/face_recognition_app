import BrainOfFront
import json


class TeachBoardController:

    def get_teacher_courses(self, teacher_id):
        dictInput = {
            'action': "get_teacher_courses",
            'teacher_id': teacher_id
        }
        return self.serverSender(dictInput)

    def get_students_of_course(self, course_id):
        dictInput = {
            'action': "get_students_of_course",
            'course_id': course_id
        }
        return self.serverSender(dictInput)

    def get_students_enter_exit_times(self, course_id, student_id):
        dictIput = {
            'action': "get_students_enter_exit_times",
            'course_id': course_id,
            'student_id': student_id
        }
        return self.serverSender(dictIput)

    def serverSender(self, dictInput):
        BrainOfFront.SendData(json.dumps(dictInput))
        retValue = BrainOfFront.ReadData()
        dictOutput = json.loads(retValue)
        return dictOutput
