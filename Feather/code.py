import board
import digitalio
import busio
import time
from heartbeat import Heartbeat
from soundboard import SoundBoard
from colors import COLOR
import neopixel
from wings import Wings


pewPewTimer = 3
pewPewLastTime = 0

chestLedlastTime = 0
chestLEDStep = 0

armButton = digitalio.DigitalInOut(board.D13)
chestButton = digitalio.DigitalInOut(board.D12)

buzzWings = Wings(board.D10, board.D9)

armLED = neopixel.NeoPixel(board.D6, 1, brightness=1)
chestLEDS = neopixel.NeoPixel(board.D11, 3, brightness=0.5)

clipIndex = 0

clips = [
    "APPROACH",
    "COMPEACE",
    "IAMBUZZ1",
    "LASERPOW",
    "NOTDZURG",
    "PEWPEWPW",
    "SCANPERM",
    "SECRETMI",
    "SLNGSHOT",
    "SPBUZZ01",
    "STARCMND",
    "TOIFININ",
    "TORESCUE",
    "WHOGOES1",
]

buttons = [armButton, chestButton]

for btn in buttons:
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN


hb = Heartbeat(board.NEOPIXEL)

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0.05)

player = SoundBoard(uart, board.D5)
player.reset()

player.playTrack("TOIFININ")
while True:

    now = time.monotonic()
    hb.tick()
    buzzWings.tick()
    if armButton.value == True:
        armLED.fill(COLOR.RED)
        player.playTrack("PEWPEWPW")
        pewPewTimer = now

    if now - pewPewLastTime >= pewPewTimer:
        armLED.fill(COLOR.BLACK)

    if chestButton.value == True:
        player.playTrack(clips[clipIndex])
        clipIndex += 1
        if clipIndex > len(clips) - 1:
            clipIndex = 0
    print(clipIndex)

    if now - 1.34 >= chestLedlastTime:
        chestLedlastTime = now
        chestLEDStep += 1
        if chestLEDStep > 2:
            chestLEDStep = 0

    if chestLEDStep == 0:
        chestLEDS[0] = COLOR.RED
        chestLEDS[1] = COLOR.GREEN
        chestLEDS[2] = COLOR.BLUE
    if chestLEDStep == 1:
        chestLEDS[0] = COLOR.GREEN
        chestLEDS[1] = COLOR.BLUE
        chestLEDS[2] = COLOR.RED
    if chestLEDStep == 2:
        chestLEDS[0] = COLOR.BLUE
        chestLEDS[1] = COLOR.RED
        chestLEDS[2] = COLOR.GREEN
