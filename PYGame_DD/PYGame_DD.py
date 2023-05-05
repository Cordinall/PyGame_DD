# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Room_objects = []
Inventory_bag = []
Inventory_body = [(1,  "onehand", "hand", "Потрёпаный меч", "Весьма старый и сильно притупившийся меч из железа", 1)]

Current_difficuty = 0

Enemy_max_dmg = Current_difficuty + 2
Enemy_min_dmg = Current_difficuty + 1
Enemy_max_hp = Current_difficuty + 5
Enemy_min_hp = Current_difficuty + 1
Chest_treasure_max_dmg = Current_difficuty + 3
Chest_treasure_min_dmg = Current_difficuty + 1

ExitDangeon = 0
while ExitDangeon == 0:

    Visual_Room_size = random.randint(1,3)
    Visual_Room_biome = random.randint(1,3)
    Visual_Room = Dangeon_Room_NonAction(Visual_Room_size, Visual_Room_biome)

    Visual_Room.VisualGeneration()

    doPlayer = int(input("========================================================\nВыберете действие: 1. Осмотреться 2. Вывести список объектов 3. Взаимодествовать с *объект* 4. Осмотреть персонажа\n"))

    if doPlayer == 1:

        Entity_Enemy_name = random.randint(1,1)
        Entity_Enemy_dmg = random.randint(Enemy_min_dmg,Enemy_max_dmg)
        Entity_Enemy_hp = random.randint(Enemy_min_hp,Enemy_max_hp)

        Entity_Enemy = Dangeon_Room_Action_Enemy(Entity_Enemy_name, Entity_Enemy_dmg, Entity_Enemy_hp)

        Entity_Enemy.VisualGeneraton()

        ExitBattle = 0
        while ExitBattle == 0:

            if Entity_Enemy.HpVis() <= 0:

                Entity_Enemy.VisualDeath()
                ExitBattle = 1
                continue

            doPlayer = int(input("========================================================\nВыберете действие: 1. Атака 2. Смена обмундирования 3. Уклонение 4. Применить предмет\n"))

            if doPlayer == 1:

                Entity_Enemy.HpReduction(Inventory_body[0][5])
                print(f"Вы нанесли противнику {Inventory_body[0][5]} урона.")

    
