"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This project is for breaking bricks, but it's so difficult.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
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

click_ball = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.x = 0 + j*(brick_width+brick_spacing)
                brick.y = brick_offset + i*(brick_height+brick_spacing)
                self.window.add(brick, x=brick.x, y=brick.y)
                if 0 <= i <= 1:
                    brick.fill_color = 'red'
                elif 2 <= i <= 3:
                    brick.fill_color = 'orange'
                elif 4 <= i <= 5:
                    brick.fill_color = 'yellow'
                elif 6 <= i <= 7:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'

        # count how many bricks in game
        self.total_brick = brick_cols * brick_rows

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.start_ball)
        onmousemoved(self.paddle_move)

    def start_ball(self, event):
        """
        Give the ball speed after clicking.
        """
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def paddle_move(self, mouse):
        """
        move with the mouse.
        """
        if mouse.x > BRICK_COLS*(BRICK_WIDTH+BRICK_SPACING)-BRICK_SPACING-PADDLE_WIDTH:
            self.paddle.x = BRICK_COLS*(BRICK_WIDTH+BRICK_SPACING)-BRICK_SPACING-PADDLE_WIDTH
        elif mouse.x < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x

    def get_dy(self):
        """
        get vertical speed.
        """
        return self.__dy

    def get_dx(self):
        """
        get horizontal speed.
        """
        return self.__dx

    def get_total_brick(self):
        """
        get total brick.
        """
        return self.total_brick

    def reset_ball(self):
        """
        add ball to start point
        """
        self.window.add(self.ball, x=self.window.width / 2 - self.ball.width / 2,
                        y=self.window.height / 2 - self.ball.height / 2)

    def detect_collision(self):
        """
        detect collision.
        """
        # Detect collision with left, right, and top walls
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        elif self.ball.y <= 0:
            self.__dy = -self.__dy

        # Detect if ball falls out of the window
        elif self.ball.y > self.window.height:
            self.__dx = 0
            self.__dy = 0

        # Detect collision with vertex_1
        stuff_top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        if stuff_top_left is not None:
            if stuff_top_left == self.paddle:
                self.__dy = -self.__dy
                self.ball.y = self.paddle.y - self.ball.height - 1  # move the ball back to the top of the board
            else:
                self.window.remove(stuff_top_left)
                self.total_brick -= 1
                self.__dy = -self.__dy
        else:
            # Detect collision with vertex_2
            stuff_top_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            if stuff_top_right is not None:
                if stuff_top_right == self.paddle:
                    self.__dy = -self.__dy
                    self.ball.y = self.paddle.y - self.ball.height - 1
                else:
                    self.window.remove(stuff_top_right)
                    self.total_brick -= 1
                    self.__dy = -self.__dy
            else:
                # Detect collision with vertex_3
                stuff_down_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
                if stuff_down_left is not None:
                    if stuff_down_left == self.paddle:
                        self.__dy = -self.__dy
                        self.ball.y = self.paddle.y - self.ball.height - 1
                    else:
                        self.window.remove(stuff_down_left)
                        self.total_brick -= 1
                        self.__dy = -self.__dy
                else:
                    # Detect collision with vertex_4
                    stuff_down_right = self.window.get_object_at(self.ball.x + self.ball.width,
                                                                 self.ball.y + self.ball.height)

                    if stuff_down_right is not None:
                        if stuff_down_right == self.paddle:
                            self.__dy = -self.__dy
                            self.ball.y = self.paddle.y - self.ball.height - 1
                        else:
                            self.window.remove(stuff_down_right)
                            self.total_brick -= 1
                            self.__dy = -self.__dy
