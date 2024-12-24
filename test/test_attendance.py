import pytest
from app.fetch_student_details import FetchStudentDetails

class TestAttendance:
    def test_attendance_attr(self):
        fetch_student = FetchStudentDetails()
        result = fetch_student.get_data()
        fetch_student.get_attendance()

        assert hasattr(result[0], "attendance")

    def test_attendance_simple(self):
        fetch_student = FetchStudentDetails()
        result = fetch_student.get_data()
        fetch_student.get_attendance()

        assert result[0].attendance == 13