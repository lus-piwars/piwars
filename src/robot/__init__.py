from typing import Tuple
from gpiozero import Motor  # type: ignore


class Robot:
    """
    Controls communication between the robot and the peripherals (the motors, camera, etc) and other programs.
    """

    def __init__(
        self,
        front_left: Tuple[int, int, int],
        front_right: Tuple[int, int, int],
        back_left: Tuple[int, int, int],
        back_right: Tuple[int, int, int],
    ):
        self.front_left = Motor(*front_left)
        self.front_right = Motor(*front_right)
        self.back_left = Motor(*back_left)
        self.back_right = Motor(*back_right)

    def move(self, speed: float, direction: float):
        """
        Moves the robot in the specified direction at the specified speed.
        :param speed: The speed (between zero and one) that the robot should move at.
        :param direction: The direction in which the robot should move
        (an angle in degrees). This angle specified is used to set the motor speeds.
        A positive value will cause the robot to veer to the right. A negative value
        will cause the robot to veer to the left.
        TODO: Once we've worked out how the robot is going to be designed, we'll fill
              this method in with some concrete implementation details.
        :return: None
        """
        pass

    def stop_moving(self):
        """
        Stops the robot from moving.
        :return: None
        """
        pass
