# -*- coding: cp1251 -*-
from Dangeon_Room import *
from UnlimitMode import *
import random

def Everlast_Hub(Room_Num, Dangeon_difficult, Player):
    
    print("=====================================================")
    print("����� ���� - ���������.")
    print("")
    print("I - ���������")
    print("H - ���������� ��������")
    print("M - ������� ����������, �������� ���������")
    print("")
    print("������������: ����������� �����, ���������� The Fire Is Gone � �������� ����.")
    print("=====================================================\n")

    Player = Player
    Dangeon_difficult = Dangeon_difficult
    Room_Num = Room_Num

    Never = 0
    while Never == 0:

        Random_level = random.randint(1,3)

        if Random_level == 1:
            Enemy_Num = 1
            Chest_Num = 1
            Exit_list = EverlastMode(Room_Num, Dangeon_difficult, Player, Enemy_Num, Chest_Num)
        elif Random_level == 2:
            Enemy_Num = 2
            Chest_Num = 1
            Exit_list = EverlastMode(Room_Num, Dangeon_difficult, Player, Enemy_Num, Chest_Num)
        elif Random_level == 3:
            Enemy_Num = 3
            Chest_Num = 2
            Exit_list = EverlastMode(Room_Num, Dangeon_difficult, Player, Enemy_Num, Chest_Num)

        Room_Num = Exit_list[0]
        Dangeon_difficult = Exit_list[1]
        Player = Exit_list[2]
        Never = Exit_list[3]