# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

def Rand_Room_shell():
    a = random.randint(1,3)
    b = random.randint(1,3)

    return a,b

Inv = []

Room_shell_1 = Dangeon_Room_NonAction(1,3)
Room_shell_1.VisualGeneration()
Room_chest_1 = Dangeon_Room_Action_Chest(1,1,1)
Room_chest_1.VisualGeneraton()

Inv.append(Room_chest_1.ItemGeneration())

print(Inv)