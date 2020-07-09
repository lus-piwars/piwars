from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from robot import Robot


class Challenge:
    """
    Base class for all challenges. Other challenges should "subclass" this class.
    For example:

    ```python
    class SomeChallenge(Challenge):
        def __init__(self, robot):
            # construct super class
            super(SomeChallenge, self).__init__()
            # store a copy of robot somewhere for later use
            self.robot = robot
        def __call__(self):
            pass
    ```
    """

    def __init__(self, robot: Robot):
        raise NotImplementedError("The `Challenge` class shouldn't be used directly.")

    def __call__(self):
        raise NotImplementedError("The `Challenge` class shouldn't be used directly.")
