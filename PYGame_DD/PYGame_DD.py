# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Inventory_bag = []
Inventory_body = []

Current_difficuty = 0

Enemy_max_dmg = Current_difficuty + 2
Enemy_min_dmg = Current_difficuty + 1
Enemy_max_hp = Current_difficuty + 5
Enemy_min_hp = Current_difficuty + 1
Chest_treasure_max_dmg = Current_difficuty + 3
Chest_treasure_min_dmg = Current_difficuty + 1

ExitDangeon = 0
while ExitDangeon == 0:


    Entity_Room_size = random.randint(1,3)
    Entity_Room_biome = random.randint(1,3)
    Entity_Room = Dangeon_Room_NonAction(Entity_Room_size, Entity_Room_biome)

    Entity_Room.VisualGeneration()

    doPlayer = input("========================================================\nВыберете действие: 1. Осмотреться 2. Вывести список объектов 3. Подойти к *объект*")

    

    Entity_Enemy_name = random.randint(1,1)
    Entity_Enemy_dmg = random.randint(1,1)
    Entity_Enemy_hp = random.randint(1,1)