import os


def running_on_raspberry_pi() -> bool:
    return os.uname()[4].startswith("arm")
