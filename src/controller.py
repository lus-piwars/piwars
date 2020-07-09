"""
This file is very much in progress.
"""

from robot import Robot
from utils import running_on_raspberry_pi

# only do this on the raspberry pi (can't run it on other platforms)

if running_on_raspberry_pi():
    import evdev  # type: ignore

# emulates a gamepad for local testing
class GamepadEmulator:
    pass


class Controller:
    def __init__(self):
        self.robot = Robot
        if running_on_raspberry_pi():
            self.gamepad = evdev.InputDevice("/dev/input/event3")
        else:
            self.gamepad = GamepadEmulator()

    async def __call__(self, *args, **kwargs):
        for event in self.gamepad.read_loop():  # type: ignore
            pass
