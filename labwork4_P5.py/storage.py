import os
import zipfile

# Constants for file names
ARCHIVE = "students.dat"
STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"
MARKS_FILE = "marks.txt"

def write_students(mgr):
    with open(STUDENTS_FILE, "w") as f:
        for s in mgr.students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

def write_courses(mgr):
    with open(COURSES_FILE, "w") as f:
        for c in mgr.courses:
            f.write(f"{c.id},{c.name},{c.credit}\n")

def write_marks(mgr):
    with open(MARKS_FILE, "w") as f:
        for cid, student_marks in mgr.marks.items():
            for sid, mark in student_marks.items():
                f.write(f"{cid},{sid},{mark}\n")

def compress_files():
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in (STUDENTS_FILE, COURSES_FILE, MARKS_FILE):
            if os.path.exists(fname):
                zf.write(fname)

def decompress_files():
    if not os.path.exists(ARCHIVE):
        return False
    with zipfile.ZipFile(ARCHIVE, "r") as zf:
        zf.extractall()
    return True

def load_data(mgr):
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                sid, name, dob = line.split(",")
                mgr.add_student(sid, name, dob)

    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                cid, name, credit = line.split(",")
                mgr.add_course(cid, name, float(credit))

    if os.path.exists(MARKS_FILE):
        with open(MARKS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                cid, sid, mark = line.split(",")
                mgr.marks.setdefault(cid, {})
                mgr.marks[cid][sid] = float(mark)