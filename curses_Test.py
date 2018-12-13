# Import curses module
import curses, time
from select import select
stdscr = curses.initscr()

def theClock():

     # Define global colour scheme
     curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

     # Get the screen size
     max_y, max_x = stdscr.getmaxyx()

     # Calculate the clock position relative to the screen size
     clock_x = max_x - 28

     # Draw the clock
     clockWindow = curses.newwin(3, 26, 1, clock_x)
     clockWindow.bkgd(' ', curses.color_pair(1))
     clockWindow.box()
     clockWindow.refresh()

     # If 'q' is pressed, exit
     finished = 0
     while not finished:    # finished = 0 until the 'q' key is pressed
         if select([0], [], [], 1)[0]:
             c = stdscr.getch()
             if c == ord('q'):
                 curses.beep()
                 finished = 1
                 break

         t = time.asctime()
         clockWindow.addstr(1, 1, t)
         clockWindow.refresh()


def main(stdscr):

     # Bring up the clock function

     theClock()

if __name__ == '__main__':
     curses.wrapper(main)
