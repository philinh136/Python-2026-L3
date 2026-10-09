import gzip
import os
import pickle

ARCHIVE = "students.dat"


def save_data(mgr):
    data = {
        "students": mgr.students,
        "courses": mgr.courses,
        "marks": mgr.marks,
    }
    raw = pickle.dumps(data)
    with gzip.open(ARCHIVE, "wb") as f:
        f.write(raw)


def load_data(mgr):
    if not os.path.exists(ARCHIVE):
        return False
    with gzip.open(ARCHIVE, "rb") as f:
        raw = f.read()
    data = pickle.loads(raw)
    mgr.students = data["students"]
    mgr.courses = data["courses"]
    mgr.marks = data["marks"]
    return True