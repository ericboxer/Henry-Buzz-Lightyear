import neopixel
import time
from colors import COLOR


class Heartbeat:
    def __init__(self, npPin, step=5) -> None:
        self.stepCountMillis = step * 0.1
        self.lastCout = 0
        self.heartbeatLED = neopixel.NeoPixel(npPin, 1)
        self.colorStep = 0

    def tick(self):

        self.heartbeatLED.brightness = 0.01
        if self.colorStep > 5:
            self.colorStep = 0

        if self.colorStep == 0:
            self.heartbeatLED.fill(COLOR.RED)
        if self.colorStep == 1:
            self.heartbeatLED.fill(COLOR.YELLOW)
        if self.colorStep == 2:
            self.heartbeatLED.fill(COLOR.GREEN)
        if self.colorStep == 3:
            self.heartbeatLED.fill(COLOR.CYAN)
        if self.colorStep == 4:
            self.heartbeatLED.fill(COLOR.BLUE)
        if self.colorStep == 5:
            self.heartbeatLED.fill(COLOR.PINK)

        now = time.monotonic()

        # print(now)
        if now - self.lastCout >= self.stepCountMillis:
            self.colorStep += 1
            self.lastCout = now
