from enum import Enum


class Mode(Enum):
    off = 1
    flight = 2
    hover = 3
    collision_avoidance = 4


class Flight_Status(Enum):
    off = 1
    flying = 2
    taking_off = 3
    landing = 4

class Altitude_Hold(Enum):
    on = 1
    off = 2