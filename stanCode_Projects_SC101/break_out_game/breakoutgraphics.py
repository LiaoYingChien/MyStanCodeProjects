"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.is_first_click = True
        self.process = 0
        self.brick_num = brick_cols * brick_rows

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.action)
        onmousemoved(self.change_paddle_position)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'RED'
                elif j < 4:
                    self.brick.fill_color = 'ORANGE'
                elif j < 6:
                    self.brick.fill_color = 'YELLOW'
                elif j < 8:
                    self.brick.fill_color = 'GREEN'
                elif j < brick_rows:
                    self.brick.fill_color = 'BLUE'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing),
                                y=brick_offset+j*(brick_height+brick_spacing))

    def change_paddle_position(self, event):
        if (event.x - PADDLE_WIDTH/2) <= 0:
            self.paddle.x = 0
        elif (event.x + PADDLE_WIDTH/2) >= self.window.width:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        else:
            self.paddle.x = event.x - PADDLE_WIDTH/2

    def action(self, click):
        if self.is_first_click is True:
            self.process += 1
            self.set_ball_speed()
            self.is_first_click = False

    def set_ball_speed(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def bunch_obj(self, x, y):
        for point_x in [x, x+2*BALL_RADIUS]:
            for point_y in [y, y+2*BALL_RADIUS]:
                bunch_obj = self.window.get_object_at(point_x, point_y)
                if bunch_obj is not None:
                    if bunch_obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                    else:
                        self.__dy = -self.__dy
                        self.window.remove(bunch_obj)
                        self.brick_num -= 1
                    return

    def new_start(self):
        self.is_first_click = True
        self.window.add(self.ball, x=self.window.width / 2 - BALL_RADIUS, y=self.window.height / 2 - BALL_RADIUS)

    def creat_label(self, text):
        label = GLabel(text)
        label.font = 'roboto-50'
        self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height+label.height)/2)
