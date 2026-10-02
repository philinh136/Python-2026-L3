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