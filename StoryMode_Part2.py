# -*- coding: cp1251 -*-
from Dangeon_Room import *
from PYGame_SaveLoad import *
import random

def StoryMode_Part2(Player):

    def Player_inventory_check(Player):

        Inv_list = Player.InventoryOutput()

        print("=====================================================")
        print("���������:")
        print("=====================================================")

        for i in Inv_list:

            print("-------------------------------------------------------")
            print(f"{i[0]} | {i[3]} | {i[4]}")
            print("-------------------------------------------------------")

        print("")
        print("1. ������ ������� 2. ������� ������� 3. �����")

        Player_answer = input()

        if Player_answer == "1":

            print("")
            print("������� id �������� ( ����� � �������� �������� )")

            Player_answer = int(input())

            for i in Inv_list:

                if i[0] == Player_answer:

                    if i[2] == "hand":
                        Player.BodyChangeMelee(Player_answer)
                    elif i[2] == "boots":
                        Player.BodyChangeBoots(Player_answer)
                    elif i[2] == "leggs":
                        Player.BodyChangeLeggs(Player_answer)
                    elif i[2] == "chest":
                        Player.BodyChangeChest(Player_answer)
                    elif i[2] == "arms":
                        Player.BodyChangeArms(Player_answer)
                    elif i[2] == "head":
                        Player.BodyChangeHead(Player_answer)

        elif Player_answer == "2":
                    
            print("")
            print("������� id �������� ( ����� � �������� �������� )")

            Player_answer = int(input())

            Player.InventoryDel(Player_answer)

        elif Player_answer == "3":
            print("")

    def Player_body_check(Player):

        Body_list = Player.BodyOutput()
        print("=====================================================")
        print(f"{Player.NameOutPut()} | {Player.StoryOutPut()}")
        print("=====================================================")

        for i in Body_list:

            print("-------------------------------------------------------")
            print(f"{i[0]} | {i[3]} | {i[4]}")
            print("-------------------------------------------------------")

    for i in range(25):

        print("")

    print("=====================================================")
    print("��� 2 - � �������")
    print("=====================================================\n")
    print("")

    Player = Player

