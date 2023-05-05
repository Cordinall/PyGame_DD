# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Player = Dangeon_Room_Action_Player("Олег", "Красивый парень", [(1,  "onehand", "hand", "Потрёпаный меч", "Весьма старый и сильно притупившийся меч из железа", 1)], [(1,  "onehand", "hand", "Руки", "Просто руки", 1)], 100)

Player.BodyAddMelee("Потрёпаный меч")

i = input()