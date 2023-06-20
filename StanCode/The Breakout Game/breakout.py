"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Kevin! Let's break bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    break bricks game.
    """
    global NUM_LIVES
    graphics = BreakoutGraphics()

    while True:
        # If the ball completely leaves the window, the life value will be deducted by 1.
        if graphics.ball.y > graphics.window.height:
            NUM_LIVES -= 1
            graphics.reset_ball()
            if NUM_LIVES == 0:
                break
        # If no brick ,Game Over.
        if graphics.total_brick == 0:
            graphics.reset_ball()
            break

        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.detect_collision()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
