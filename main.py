#!/usr/bin/env python3

import curses
import subprocess
import os
import pathlib
import sys


def run_command(command, stdscr):
    """Runs a shell command. If prefixed with '$', it runs in the foreground."""
    try:
        if command.strip().startswith("$"):
            command = command[1:]  # Remove the '$' prefix
            curses.endwin()  # Temporarily exit ncurses to display command output
            os.system(command)
            input("\nPress Enter to continue...")  # Wait for user input
            curses.doupdate()  # Redraw the screen
            return "OK"
        else:
            # Run in background, suppress output
            with open(os.devnull, "wb") as devnull:
                subprocess.Popen(
                    command,
                    shell=True,
                    stdin=devnull,
                    stdout=devnull,
                    stderr=devnull,
                    close_fds=True,
                    preexec_fn=os.setsid,
                )
            os.system(f"notify-send 'running: {command}'")
            return "OK"
    except Exception as e:
        return f"Error: {e}"


def display_menu(stdscr, menu, last_command, last_status):
    """Displays the menu and the status of the last command in a centered box."""
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Determine box dimensions
    box_width = max(len(item) for item in menu) + 7  # Width based on longest menu item
    box_height = (
        len(menu) + 5
    )  # Height based on number of menu items and additional lines for status and spacing
    box_width = min(
        box_width, width - 2
    )  # Ensure box width doesn't exceed screen width
    box_width = max(60, box_width)
    box_height = min(
        box_height, height - 2
    )  # Ensure box height doesn't exceed screen height

    # Calculate position to center the box
    start_y = (height - box_height) // 2
    start_x = (width - box_width) // 2

    # Create a new window for the box and draw a border
    box = curses.newwin(box_height, box_width, start_y, start_x)
    box.box()

    box.addstr(0, 2, " Command Menu ")
    # Add menu items to the box
    for i, item in enumerate(menu):
        item_name = item
        if len(item_name) > box_width - 9:
            item_name = item_name[: box_width - 10] + "..."

        if i > ord("z") - ord("a"):
            display_char = chr(ord("A") + (i - ord("z") + ord("a") - 1))
        else:
            display_char = chr(ord("a") + i)
        box.addstr(i + 2, 2, f"{display_char}) {item_name}")

    # Add quit instruction and status message
    box.addstr(i + 3, 2, "esc) quit")
    if last_status:
        box.addstr(
            box_height - 1,
            2,
            f" Last Command [{last_command[:10]}] Status: {last_status} ",
        )
    else:
        box.addstr(box_height - 1, 2, f" Last Command Status: ")

    # Refresh the box
    stdscr.refresh()
    box.refresh()


def main(stdscr):
    # get list of commands from $HOME/commands.txt
    commands_file = pathlib.Path.home() / "commands.txt"
    if len(sys.argv) > 1:
        commands_file = pathlib.Path.home() / sys.argv[1]

    menu = [
        x
        for x in commands_file.read_text().split("\n")
        if x.strip() and x.strip()[0] != "#"
    ]

    last_status = None
    last_command = None
    curses.curs_set(0)
    curses.use_default_colors()
    while True:
        display_menu(stdscr, menu, last_command, last_status)
        c = stdscr.getch()

        if c == 10:  # 10 is enter key
            break
        elif c == 27:  # 27 is escape key
            break
        elif 97 <= c < 97 + len(menu):  # lower case
            item = menu[c - 97]
            last_command = item
            last_status = run_command(item, stdscr)
        elif 65 <= c < 65 + len(menu):  # upper case
            item = menu[c - 65 + 26]
            last_command = item
            last_status = run_command(item, stdscr)


curses.wrapper(main)
