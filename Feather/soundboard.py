from time import time
import busio
import board
import digitalio
import time


class SoundBoard:
    def __init__(self, uart, resetPin) -> None:
        print("SB Initi")
        self.writing = False

        self.uart = uart
        self.resetPin = digitalio.DigitalInOut(resetPin)

    def reset(self):
        print("resetting")
        self.resetPin.direction = digitalio.Direction.OUTPUT
        self.resetPin.value = False
        self.resetPin.direction = digitalio.Direction.OUTPUT
        time.sleep(0.01)
        self.resetPin.direction = digitalio.Direction.INPUT
        time.sleep(1)

        self.readLine()
        self.readLine()
        time.sleep(1)
        self.readLine()
        self.readLine()

    def readLine(self):

        data = self.uart.read(64)
        if data is not None:
            datastring = "".join([chr(b) for b in data])
            print(datastring)

    def send(self, data):
        print(f"sending {data}")
        newData = data + "\r\n"
        self.uart.write(str(newData).encode("utf_8"))
        self.readLine()

    def playTrack(self, trackname):
        pTrack = f"P{trackname.upper()}OGG"
        self.send(pTrack)
        self.readLine()
