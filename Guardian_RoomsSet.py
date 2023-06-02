# -*- coding: cp1251 -*-
import random
from Dangeon_Guardian import *

def Rooms_RandomSet():

    room_1 = ["Single", 10, 1, 50]
    room_2 = ["Double", 5, 2, 70]
    room_3 = ["Triple", 3, 3, 80]

    room_rnd_1 = random.randint(1,3)
    room_rnd_2 = random.randint(1,3)
    room_rnd_3 = random.randint(1,3)

    match room_rnd_1:
        case 1: room_1 = ["Single", 10, 1, 50]
        case 2: room_1 = ["Double", 5, 2, 70]
        case 3: room_1 = ["Double", 5, 2, 70]

    match room_rnd_2:
        case 1: room_2 = ["Single", 10, 1, 50]
        case 2: room_2 = ["Double", 5, 2, 70]
        case 3: room_2 = ["Double", 5, 2, 70]

    match room_rnd_3:
        case 1: room_3 = ["Single", 10, 1, 50]
        case 2: room_3 = ["Double", 5, 2, 70]
        case 3: room_3 = ["Double", 5, 2, 70]


    return [room_1, room_2, room_3]