"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 10

# Global variable
window = GWindow()
click_cnt = 1
pre_click = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(mouse_click)


def mouse_click(event):
    global click_cnt
    global pre_click
    click = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
    if click_cnt % 2 != 0:
        click.filled = False
        window.add(click)
    else:
        pre_object = window.get_object_at(int(pre_click.x+SIZE/2), int(pre_click.y+SIZE/2))
        window.remove(pre_object)
        line = GLine(pre_click.x, pre_click.y, click.x, click.y)
        window.add(line)

    click_cnt += 1
    pre_click = click


if __name__ == "__main__":
    main()
