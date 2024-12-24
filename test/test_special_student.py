import pytest

from app.fetch_student_details import FetchStudentDetails
from app.student import Student


class TestSuperStudent:
    def test_get_super_student(self):
        fetch_student = FetchStudentDetails()
        fetch_student.get_data()
        super_student = fetch_student.get_super_student()

        assert type(super_student) == Student
        assert super_student.name == "yohan doe"
