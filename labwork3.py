###Practical work 3
import curses
import math
import numpy as np


class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, cid, name, credit):
        self.id = cid
        self.name = name
        self.credit = credit


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def find_student(self, sid):
        for s in self.students:
            if s.id == sid:
                return s
        return None

    def find_course(self, cid):
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


def prompt(stdscr, y, text):
    stdscr.addstr(y, 2, text)
    curses.echo()
    val = stdscr.getstr(y, 2 + len(text) + 1).decode()
    curses.noecho()
    return val


def pause(stdscr, y):
    stdscr.addstr(y + 1, 2, "Press any key to continue...")
    stdscr.getch()


def input_students(stdscr, mgr):
    stdscr.clear()
    n = int(prompt(stdscr, 1, "Number of students:"))
    for i in range(n):
        sid = prompt(stdscr, 3 + i * 3, f"[{i+1}] Student id:")
        name = prompt(stdscr, 4 + i * 3, f"[{i+1}] Name:")
        dob = prompt(stdscr, 5 + i * 3, f"[{i+1}] Date of birth:")
        mgr.add_student(sid, name, dob)
    pause(stdscr, 6 + n * 3)


def input_courses(stdscr, mgr):
    stdscr.clear()
    n = int(prompt(stdscr, 1, "Number of courses:"))
    for i in range(n):
        cid = prompt(stdscr, 3 + i * 4, f"[{i+1}] Course id:")
        name = prompt(stdscr, 4 + i * 4, f"[{i+1}] Course name:")
        credit = float(prompt(stdscr, 5 + i * 4, f"[{i+1}] Credit:"))
        mgr.add_course(cid, name, credit)
    pause(stdscr, 6 + n * 4)


def input_marks(stdscr, mgr):
    stdscr.clear()
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(1 + i, 2, f"{c.id} - {c.name}")
    cid = prompt(stdscr, 2 + len(mgr.courses), "Select course id:")
    course = mgr.find_course(cid)
    if not course:
        stdscr.addstr(4 + len(mgr.courses), 2, "Course not found!")
        pause(stdscr, 5 + len(mgr.courses))
        return
    y = 4 + len(mgr.courses)
    for s in mgr.students:
        mark = float(prompt(stdscr, y, f"Mark for {s.name}:"))
        mgr.set_mark(cid, s.id, mark)
        y += 1
    pause(stdscr, y)


def list_courses(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "COURSES", curses.A_BOLD)
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(2 + i, 2, f"{c.id} - {c.name} - {c.credit} credits")
    pause(stdscr, 3 + len(mgr.courses))


def list_students(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "STUDENTS", curses.A_BOLD)
    for i, s in enumerate(mgr.students):
        stdscr.addstr(2 + i, 2, f"{s.id} - {s.name} - {s.dob}")
    pause(stdscr, 3 + len(mgr.students))


def show_marks(stdscr, mgr):
    stdscr.clear()
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(1 + i, 2, f"{c.id} - {c.name}")
    cid = prompt(stdscr, 2 + len(mgr.courses), "Select course id:")
    y = 4 + len(mgr.courses)
    if cid not in mgr.marks:
        stdscr.addstr(y, 2, "No marks for this course!")
        pause(stdscr, y + 1)
        return
    for sid, mark in mgr.marks[cid].items():
        s = mgr.find_student(sid)
        name = s.name if s else "?"
        stdscr.addstr(y, 2, f"{sid} - {name}: {mark}")
        y += 1
    pause(stdscr, y)


def show_gpa_ranking(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "GPA RANKING (descending)", curses.A_BOLD)
    ranked = mgr.students_sorted_by_gpa()
    for i, s in enumerate(ranked):
        stdscr.addstr(2 + i, 2, f"{i+1}. {s.name} ({s.id}) - GPA: {mgr.gpa(s.id):.2f}")
    pause(stdscr, 3 + len(ranked))


def main(stdscr):
    curses.curs_set(1)
    mgr = MarkManager()
    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "STUDENT MARK MANAGEMENT", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(2, 2, "1. Input students")
        stdscr.addstr(3, 2, "2. Input courses")
        stdscr.addstr(4, 2, "3. Input marks")
        stdscr.addstr(5, 2, "4. List courses")
        stdscr.addstr(6, 2, "5. List students")
        stdscr.addstr(7, 2, "6. Show marks for a course")
        stdscr.addstr(8, 2, "7. Show GPA ranking")
        stdscr.addstr(9, 2, "0. Exit")
        choice = prompt(stdscr, 11, "Choose:")

        if choice == "1":
            input_students(stdscr, mgr)
        elif choice == "2":
            input_courses(stdscr, mgr)
        elif choice == "3":
            input_marks(stdscr, mgr)
        elif choice == "4":
            list_courses(stdscr, mgr)
        elif choice == "5":
            list_students(stdscr, mgr)
        elif choice == "6":
            show_marks(stdscr, mgr)
        elif choice == "7":
            show_gpa_ranking(stdscr, mgr)
        elif choice == "0":
            break


if __name__ == "__main__":
    curses.wrapper(main)
###Practical work 4
#main.py
import curses

from domains import MarkManager
from input import input_students, input_courses, input_marks
from output import show_menu, list_courses, list_students, show_marks, show_gpa_ranking


def main(stdscr):
    curses.curs_set(1)
    mgr = MarkManager()
    while True:
        choice = show_menu(stdscr)

        if choice == "1":
            input_students(stdscr, mgr)
        elif choice == "2":
            input_courses(stdscr, mgr)
        elif choice == "3":
            input_marks(stdscr, mgr)
        elif choice == "4":
            list_courses(stdscr, mgr)
        elif choice == "5":
            list_students(stdscr, mgr)
        elif choice == "6":
            show_marks(stdscr, mgr)
        elif choice == "7":
            show_gpa_ranking(stdscr, mgr)
        elif choice == "0":
            break


if __name__ == "__main__":
    curses.wrapper(main)

#input.py
import curses

from output import prompt, pause


def input_students(stdscr, mgr):
    stdscr.clear()
    n = int(prompt(stdscr, 1, "Number of students:"))
    for i in range(n):
        sid = prompt(stdscr, 3 + i * 3, f"[{i+1}] Student id:")
        name = prompt(stdscr, 4 + i * 3, f"[{i+1}] Name:")
        dob = prompt(stdscr, 5 + i * 3, f"[{i+1}] Date of birth:")
        mgr.add_student(sid, name, dob)
    pause(stdscr, 6 + n * 3)


def input_courses(stdscr, mgr):
    stdscr.clear()
    n = int(prompt(stdscr, 1, "Number of courses:"))
    for i in range(n):
        cid = prompt(stdscr, 3 + i * 4, f"[{i+1}] Course id:")
        name = prompt(stdscr, 4 + i * 4, f"[{i+1}] Course name:")
        credit = float(prompt(stdscr, 5 + i * 4, f"[{i+1}] Credit:"))
        mgr.add_course(cid, name, credit)
    pause(stdscr, 6 + n * 4)


def input_marks(stdscr, mgr):
    stdscr.clear()
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(1 + i, 2, f"{c.id} - {c.name}")
    cid = prompt(stdscr, 2 + len(mgr.courses), "Select course id:")
    course = mgr.find_course(cid)
    if not course:
        stdscr.addstr(4 + len(mgr.courses), 2, "Course not found!")
        pause(stdscr, 5 + len(mgr.courses))
        return
    y = 4 + len(mgr.courses)
    for s in mgr.students:
        mark = float(prompt(stdscr, y, f"Mark for {s.name}:"))
        mgr.set_mark(cid, s.id, mark)
        y += 1
    pause(stdscr, y)

#output.py
import curses


def prompt(stdscr, y, text):
    stdscr.addstr(y, 2, text)
    curses.echo()
    val = stdscr.getstr(y, 2 + len(text) + 1).decode()
    curses.noecho()
    return val


def pause(stdscr, y):
    stdscr.addstr(y + 1, 2, "Press any key to continue...")
    stdscr.getch()


def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "STUDENT MARK MANAGEMENT", curses.A_BOLD | curses.A_UNDERLINE)
    stdscr.addstr(2, 2, "1. Input students")
    stdscr.addstr(3, 2, "2. Input courses")
    stdscr.addstr(4, 2, "3. Input marks")
    stdscr.addstr(5, 2, "4. List courses")
    stdscr.addstr(6, 2, "5. List students")
    stdscr.addstr(7, 2, "6. Show marks for a course")
    stdscr.addstr(8, 2, "7. Show GPA ranking")
    stdscr.addstr(9, 2, "0. Exit")
    return prompt(stdscr, 11, "Choose:")


def list_courses(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "COURSES", curses.A_BOLD)
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(2 + i, 2, f"{c.id} - {c.name} - {c.credit} credits")
    pause(stdscr, 3 + len(mgr.courses))


def list_students(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "STUDENTS", curses.A_BOLD)
    for i, s in enumerate(mgr.students):
        stdscr.addstr(2 + i, 2, f"{s.id} - {s.name} - {s.dob}")
    pause(stdscr, 3 + len(mgr.students))


def show_marks(stdscr, mgr):
    stdscr.clear()
    for i, c in enumerate(mgr.courses):
        stdscr.addstr(1 + i, 2, f"{c.id} - {c.name}")
    cid = prompt(stdscr, 2 + len(mgr.courses), "Select course id:")
    y = 4 + len(mgr.courses)
    if cid not in mgr.marks:
        stdscr.addstr(y, 2, "No marks for this course!")
        pause(stdscr, y + 1)
        return
    for sid, mark in mgr.marks[cid].items():
        s = mgr.find_student(sid)
        name = s.name if s else "?"
        stdscr.addstr(y, 2, f"{sid} - {name}: {mark}")
        y += 1
    pause(stdscr, y)


def show_gpa_ranking(stdscr, mgr):
    stdscr.clear()
    stdscr.addstr(0, 2, "GPA RANKING (descending)", curses.A_BOLD)
    ranked = mgr.students_sorted_by_gpa()
    for i, s in enumerate(ranked):
        stdscr.addstr(2 + i, 2, f"{i+1}. {s.name} ({s.id}) - GPA: {mgr.gpa(s.id):.2f}")
    pause(stdscr, 3 + len(ranked))

#init.py
from domains.student import Student
from domains.course import Course
from domains.mark_manager import MarkManager

#student.py
class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

#course.py
class Course:
    def __init__(self, cid, name, credit):
        self.id = cid
        self.name = name
        self.credit = credit

#Mark_manager.py
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
        for s in self.students:
            if s.id == sid:
                return s
        return None

    def find_course(self, cid):
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