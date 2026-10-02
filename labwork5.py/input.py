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