import csv
from app.student import Student

class FetchStudentDetails:
    def __init__(self):
        self.student_list = []
        self.headers = []

    def get_data(self, file_name='app/data/student_details.csv'):
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
            self.headers = [header.strip() for header in next(csv_reader)]
            for row in csv_reader:
                row = [value.strip() for value in row]
                student = Student(
                    student_id=int(row[1]),
                    name=row[0],
                    age=int(row[2]),
                    subjects=row[3],
                    grade=row[4],
                    average_score=float(row[5])
                )
                self.student_list.append(student)
        return self.student_list

    def get_super_student(self):
        max_score = -1
        super_student = None
        for student in self.student_list:
            score = student.average_score
            if 'computer science' in student.subjects:
                score += 5
            if 'maths' in student.subjects:
                score += 10
            if student.name.startswith('y'):
                score += 15
            if student.student_id % 2 == 0:
                score += 20
            if student.grade == 'A+':
                score += 25
            if score > max_score:
                max_score = score
                super_student = student
        return super_student

    def get_attendance(self, attendance_file_name='app/data/attendance.csv'):
        with open(attendance_file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                student_id = int(row[0])
                attended = row[1] == 'Y'
                for student in self.student_list:
                    if student.student_id == student_id and attended:
                        student.attendance += 1