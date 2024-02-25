from enum import IntEnum

class ControllerMode(IntEnum):
    Run = 0
    Program = 1
    Faulted = 2
    Test = 3

class RequestedControllerMode(IntEnum):
    Run = 0
    Program = 1
    Test = 2