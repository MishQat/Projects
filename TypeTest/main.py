import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 0, "Welcome to Mishqat's Typetest!", curses.color_pair(3))
    stdscr.addstr(1, 0,"Press Any key to begin!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

def text_loader():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target, curses.color_pair(3))
    stdscr.addstr(1, 0, f'WPM: {wpm}', curses.color_pair(4))

    for i, char in enumerate(current): # i is the position of the list
        correct_char = target[i]
        if char != correct_char:
            color = curses.color_pair(2)
        else:
            color = curses.color_pair(1)
        stdscr.addstr(0, i, char, color)# so with each caracter typed, the cursor will add 1 to the position and overlay the target text

def wpm_test(stdscr):
    target_text = text_loader()
    current_text = []

    start_time = time.time()
    stdscr.nodelay(True)

    while True:

        time_elapsed = max(time.time() - start_time, 1) # calculates the time passed from start of run to the time of typing
        wpm = round((len(target_text) / (time_elapsed/60)) / 5) # weird formula for calculating wpm

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text: # checks if the current text is equal to the target, the join function joins the elements of the list
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27: # escape key
            break

        if key in ("KEY_BACKSPACE" , '\b' , '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # COLOURSSS!!
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, 'You have completed the test!! press any key to continue...')
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
