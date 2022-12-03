"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 50
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE)
count = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)
    oval.filled = True
    window.add(oval, x=START_X, y=START_Y)


def bouncing_ball(event):
    global count
    maybe_obj = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
    if maybe_obj is not None and (count <= 3):
        vy = 0
        while oval.x <= window.width:
            oval.move(VX, vy)
            vy += GRAVITY

            if oval.y >= window.height and vy > 0:
                vy = -vy
                vy = vy * REDUCE
            pause(DELAY)
        window.add(oval, x=START_X, y=START_Y)
        count += 1


if __name__ == "__main__":
    main()
