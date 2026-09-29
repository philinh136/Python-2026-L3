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