import math
import numpy as np
from domains.student import Student
from domains.course import Course

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def find_student(self, sid):
        #return next((s for s in self.students if s.id == sid), None)
        for s in self.students:
            if s.id == sid:
                return s
        return None

    def find_course(self, cid):
        #return next((c for c in self.courses if c.id == cid), None)
        for c in self.courses:
            if c.id == cid:
                return c
        return None

    def add_student(self, sid, name, dob):
        self.students.append(Student(sid, name, dob))

    def add_course(self, cid, name, credit):
        self.courses.append(Course(cid, name, credit))

    def set_mark(self, cid, sid, mark):
        mark = math.floor(mark * 10) / 10
        self.marks.setdefault(cid, {})
        self.marks[cid][sid] = mark

    def gpa(self, sid):
        marks_list = []
        credits_list = []
        for c in self.courses:
            if c.id in self.marks and sid in self.marks[c.id]:
                marks_list.append(self.marks[c.id][sid])
                credits_list.append(c.credit)
        if not credits_list:
            return 0.0
        marks_arr = np.array(marks_list)
        credits_arr = np.array(credits_list)
        return float(np.sum(marks_arr * credits_arr) / np.sum(credits_arr))

    def students_sorted_by_gpa(self):
        return sorted(self.students, key=lambda s: self.gpa(s.id), reverse=True)