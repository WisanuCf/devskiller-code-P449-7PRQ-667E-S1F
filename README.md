# Student Details Application

This task evaluates the candidate's skills in `Python 3`.

## Introduction

The idea of this project is to keep student details in a file and 
fetch details from it. 

## Problem Statement

- Please do *NOT* modify any tests unless specifically told to do so.
- Make tests pass by implementing missing features in the production code. The application is dependency-free.

### Task 1

Implement the `get_data` method in the `FetchStudentDetails` class. It should read student records from a given CSV file, map them to the `Student` class and add them to the `self.student_list`. First row is the headers, which means that you need to assign them to `self.headers` variable. Please note that the order of students on a list should be the same as in the CSV file.

### Task 2

Implement the `get_super_student` method in the `FetchStudentDetails` class. It should return the *super student*, i.e. a student who has scored the highest `average_score`. When looking for such students, the average score is modified according to the following rules.

 * add _5_ points if the student is studying `computer science`,
 * add _10_ points if the student is studying `maths`,
 * add _15_ points if their name starts with the letter `y` (case-sensitive),
 * add _20_ points if their `id` is divisible by 2,
 * add _25_ points if the student has a `A+` grade.

### Task 3

Implement the `get_attendance` method in the`FetchStudentDetails` class. It should read data from a CSV file, specified by the `attendance_file_name` argument, and use it to calculate the attendance for every student.

The input CSV file has two columns:

 * student ID,
 * information if the student attended a class:
    * `Y` means that the student attended a class, so you should increase the `Student.attendance` attribute.
    * `N` means that the student did not attend a class - the `Student.attendance` attribute stays the same.

### Hint

 * Take into account that the list of students could be extremely large and adjust your solution accordingly.
 * Take the time complexity into account.

## Environment setup

To execute the unit tests, use:

```
pip install -q -e . && python3 setup.py pytest
```
