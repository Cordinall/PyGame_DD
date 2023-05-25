# -*- coding: cp1251 -*-
from Dangeon_Room import *
from ObserverMode import *
import random

def Observer_Hub(Dangeon_difficult, Player):
    
    print("=====================================================")
    print("Режим игры - Наблюдатель.")
    print("")
    print("I - инвентарь")
    print("H - показатели здоровья")
    print("M - текущее снаряжение, описание персонажа")
    print("")
    print("Рекомендации: прохождение ночью, композиция The Fire Is Gone в качестве фона.")
    print("=====================================================\n")

    Player = Player
    Dangeon_difficult = Dangeon_difficult

    Never = 0
    while Never == 0:

        Random_level = random.randint(1,3)

        if Random_level == 1:
            Enemy_Num = 1
            Chest_Num = 1
            Exit_list = ObserverMode(Dangeon_difficult, Player, Enemy_Num, Chest_Num)
        elif Random_level == 2:
            Enemy_Num = 2
            Chest_Num = 1
            Exit_list = ObserverMode(Dangeon_difficult, Player, Enemy_Num, Chest_Num)
        elif Random_level == 3:
            Enemy_Num = 3
            Chest_Num = 2
            Exit_list = ObserverMode(Dangeon_difficult, Player, Enemy_Num, Chest_Num)

        Dangeon_difficult = Exit_list[0]
        Player = Exit_list[1]
        Never = Exit_list[2]