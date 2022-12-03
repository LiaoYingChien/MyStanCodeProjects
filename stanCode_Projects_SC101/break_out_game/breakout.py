"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while True:
        if graphics.is_first_click is not True:
            # Update
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.bunch_obj(graphics.ball.x, graphics.ball.y)
            # Check
            if graphics.brick_num == 0:
                graphics.creat_label('You Win')
                # print('Game over')
                break
            if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width-graphics.ball.width:
                dx = graphics.get_dx()
                dx = -dx
                graphics.set_dx(dx)
            if graphics.ball.y < 0:
                dy = graphics.get_dy()
                dy = -dy
                graphics.set_dy(dy)
            if graphics.ball.y > graphics.window.height:
                if graphics.process < NUM_LIVES:
                    graphics.new_start()
                else:
                    graphics.creat_label('Game Over')
                    # print('Game over')
                    break

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
