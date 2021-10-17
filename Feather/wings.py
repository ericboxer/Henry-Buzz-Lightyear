import neopixel
import time
from colors import COLOR


class Wings:
    def __init__(self, leftLED, rightLED, step=1) -> None:
        self.stepCountMillis = step
        self.lastCout = 0
        # self.leftLED = leftLED
        # self.rightLED = rightLED
        self.wingLeft = neopixel.NeoPixel(leftLED, 2)
        self.wingright = neopixel.NeoPixel(rightLED, 2)
        self.state = False

    def tick(self):
        now = time.monotonic()

        if now - self.lastCout >= self.stepCountMillis:
            self.state = not self.state
            self.lastCout = now

        if self.state:
            self.wingLeft.fill(COLOR.RED)
            self.wingright.fill(COLOR.BLACK)
        else:
            self.wingLeft.fill(COLOR.BLACK)
            self.wingright.fill(COLOR.GREEN)
