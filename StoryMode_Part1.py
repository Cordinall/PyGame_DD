# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

def StoryMode_Part1():

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
    print("������������: ����������� �����, ���������� The Fire Is Gone � �������� ����.")
    print("=====================================================")
    print("��� 1 - �� ����")
    print("=====================================================\n")
    print("")
    print("�� ��������� � ���� � ����� ���������. ��� ������ ��������� � ������������, ��� �� ������ �������� ���������� - ����� �����, ���������� ����.")
    print("������ �������� ����, �� �� ������� ��� ����� � ���� ������ �����, ���������� � ����.")

    Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "����", "�� � ����� �����", 1), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "�������� �������", "�������� �������, ������ �������.", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)

    Situation = 0
    Water = True
    Body_watch = False
    ExitSituation = 0
    while ExitSituation == 0:
        
        if Body_watch == False and Water == True:
            Situation = 1
        elif Body_watch == True and Water == True:
            Situation = 2

        Player_answer = input("\n1. ����������� 2. ����������������� 3. ��������\n")

        if Player_answer == "1":

            print("�� ��������� ������, �� ������� �������������� ���������� ��� ���������� ��� �������. ��� ����� �� ��������� �������� � �������������")
            print("������� ������.")
            print("�� ���������� ���������� � ���������. ������ ����� �������������� ��������� �������� ����.")
            print("")
            print("��� �� �����, ����� �� ��� �� ����� �������������� �� ��� - �� ����������.")

        elif Player_answer == "2":

            Player_answer = input("\n1. ���� 2. �����\n")

            if Player_answer == "1" and Situation == 1:

                print("��� ������ ������, ������� ��� �� ������ ���������� ���� � ������������, ��, ������������, �� ���������� ���������� ������.")
                print("���� ��������, ���� �� ��������� ������������ � �� ��������� �����.")

                Player_answer = input("\n1. ������ 2. ������ ���� 3. ������������ �� ����\n")

                if Player_answer == "1":

                    print("�� ��������� ���� �� ������ � ������ � �������� �� ����. ������ ����������. �� ����������� ����.")
                    print("���� �������� ������ ��������. �� ��������� ���� �����.")

                elif Player_answer == "2":

                    print("�� ��������� ���� �� ������ � ������ � ������������� ����.")
                    print("���� ������ ����������.")
                    break

                elif Player_answer == "3":
                    continue

            elif Player_answer == "1" and Situation == 2:

                print("��� ������ ������, ������� ��� �� ������ ���������� ���� � ������������, ��, ������������, �� ���������� ���������� ������.")
                print("���� ��������, ���� �� ��������� ������������ � �� ��������� �����.")

                Player_answer = input("\n1. ������ 2. ������ ���� 3. ������ �������� ������� 4. ������������ �� ����\n")

                if Player_answer == "1":

                    print("�� ��������� ���� �� ������ � ������ � �������� �� ����. ������ ����������. �� ����������� ����.")
                    print("���� �������� ������ ��������. �� ��������� ���� �����.")

                elif Player_answer == "2":

                    print("�� ��������� ���� �� ������ � ������ � ������������� ����.")
                    print("���� ������ ����������.")
                    break

                elif Player_answer == "3":
                    print("�� �������� � ���� �������� ������� � ���������� ����� ����� � � �����������.")
                    print("����� ���������� � ������, �� � ����� ������ �������� ����� �������.")
                    print("��� ����� ����� �� ������������� ����� ������� � ����� ������������� �������, �������������� �����������.")

                    Player.InventoryAdd((5, "tissue", "arms", "�������� �������", "����� ������� � ����� ������������� �������, �������������� �����������.", 8))
                    Player.BodyChangeArms(5)
                    Player.InventoryDel(5)

                elif Player_answer == "4":
                    continue

            elif Player_answer == "2":
                continue

        elif Player_answer == "3":

            print("�� ���������� ���������. ���� ���� ���������� �������� � � ����� ������ �� ���������.")
            print("�� ������������ ����� �����. �������� �� ���, �� ��������� ���� �����������.")
            break

        elif Player_answer == "I" or Player_answer == "i":
            print("� ��� ��� ������ � �����")

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)
            Body_watch = True

        elif Player_answer == "H" or Player_answer == "h":
            print("�� �� ����������� ������� ��������� � ��������� ���� ������ ��������")

    print("���� ������������ ����������, � ����� � ������ ����� �������.")
    
    Trystoexit = 0
    Torch = False
    ExitSituation = 0
    while ExitSituation == 0:

        if Torch == False and Trystoexit == 0:
            Situation = 1
        elif Torch == True:
            Situation = 2
        elif Torch == False and Trystoexit == 1:
            Situation = 3
        elif Torch == False and Trystoexit == 2:
            Situation = 4
        elif Torch == False and Trystoexit == 3:
            Situation = 5

        Player_answer = input("\n1. ����������� 2. ����������������� 3. ��������\n")

        if Player_answer == "1":

            print("�� ��������� ������. ������ ������. �� ������������� ���� � ��������� �������� ����.")
            print("������������ ���������� ����� ������� �����, ������� �� ����� �� ����. ������ ����, �� ������ ���������.")
            print("")
            print("����� ������� ��������� ����� ������� �����. �� ������ �������� ����, ��������� �� ������, ����������� �������.")

        elif Player_answer == "2" and Situation == 1:

            Player_answer = input("\n1. ����� 2. ������� ����� 3. �����\n")

            if Player_answer == "1":

                print("�� ��������� � ������. �� �������� ���� �� �����, �������� ������ ��� ��������.")

                Player_answer = input("\n1. ����� ����� 2. �����\n")

                if Player_answer == "1":

                    print("�� ����� �����.")
                    Player.InventoryAdd((10,  "onehand", "hand", "�����", "��������� ��������� �����", 1))
                    Player.BodyChangeMelee(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("�� �������� �� ������ � ������ �������.")
                    continue

            elif Player_answer == "2":

                print("�� ��������� � ������ ������� �����. � ��� ��������� �������� ����������� ���������.")

                Player_answer = input("\n1. ����������� �� ���� 2. �����\n")

                if Player_answer == "1":

                    print("�� ��������� ����������� �� ������ ������� �����. �� �������� ������ ���� � ��� ����, ��� ����������� �� ����.")
                    print("�� ������������ ������������� �� �����. ���� ������ ��������, �� ��������� ��������� � ���� ������� ��� ��������� �����.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 2:

            Player_answer = input("\n1. ������� ����� 2. �����\n")

            if Player_answer == "1":

                print("�� ��������� � ����� � ������� � �����. ������ ����� ������ �� ����������, �� ����� �� ��������� �������� � ����, ��� ������������.")
                print("����� ���� ���������� ��������� ������� ����������� ����.")

                Player_answer = input("\n1. ����� 2. �����\n")

                if Player_answer == "1":

                    print("�� ��������� �� ������ ��� ���������� ������� ���� � ������� � �����. ����� ���� ����������� �������� �������.")
                    print("������������ ���������� ��������� ������� �����.")

                    ExitSituation = 1

            elif Player_answer == "2":
                continue

        elif Player_answer == "2" and Situation == 3:

            Player_answer = input("\n1. ����� 2. ������� ����� 3. �����\n")

            if Player_answer == "1":

                print("�� ��������� � ������. �� �������� ���� �� �����, �������� ������ ��� ��������.")

                Player_answer = input("\n1. ����� ����� 2. �����\n")

                if Player_answer == "1":

                    print("�� ����� �����.")
                    Player.InventoryAdd((10,  "onehand", "hand", "�����", "��������� ��������� �����", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("�� �������� �� ������ � ������ �������.")
                    continue

            elif Player_answer == "2":

                print("�� ��������� � ������ ������� �����. � ��� ��������� �������� ����������� ���������.")

                Player_answer = input("\n1. ����������� �� ���� 2. �����\n")

                if Player_answer == "1":

                    print("�� ��������� ����������� �� ������ ������� �����. �� �������� ������ ���� � ��� ����, ��� ����������� �� ����.")
                    print("�� ������������ ������������� �� �����. ���� ������ ��������, �� ��������� ��������� � ���� ������� ��� ��������� �����.")
                    print("�������� �� ����� �� ��������, �� ���� �� ����� ������. � �� ����������� �������� ��������, ������� ������ �������.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 4:

            Player_answer = input("\n1. ����� 2. ������� ����� 3. �����\n")

            if Player_answer == "1":

                print("�� ��������� � ������. �� �������� ���� �� �����, �������� ������ ��� ��������.")

                Player_answer = input("\n1. ����� ����� 2. �����\n")

                if Player_answer == "1":

                    print("�� ����� �����.")
                    Player.InventoryAdd((10,  "onehand", "hand", "�����", "��������� ��������� �����", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("�� �������� �� ������ � ������ �������.")
                    continue

            elif Player_answer == "2":

                print("�� ��������� � ������ ������� �����. � ��� ��������� �������� ����������� ���������.")

                Player_answer = input("\n1. ����������� �� ���� 2. �����\n")

                if Player_answer == "1":

                    print("�� ��������� ����������� �� ������ ������� �����. �� �������� ������ ���� � ��� ����, ��� ����������� �� ����.")
                    print("�� ������������ ������������� �� �����. ���� ������ ��������, �� ��������� ��������� � ���� ������� ��� ��������� �����.")
                    print("��������, ���������� � ���������� ��� ��������� �����������. ���� �� ��� �������, �� ������� ��������������.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 5:

            Player_answer = input("\n1. ����� 2. ������� ����� 3. �����\n")

            if Player_answer == "1":

                print("�� ��������� � ������. �� �������� ���� �� �����, �������� ������ ��� ��������.")

                Player_answer = input("\n1. ����� ����� 2. �����\n")

                if Player_answer == "1":

                    print("�� ����� �����.")
                    Player.InventoryAdd((10,  "onehand", "hand", "�����", "��������� ��������� �����", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("�� �������� �� ������ � ������ �������.")
                    continue

            elif Player_answer == "2":

                print("�� ��������� � ������ ������� �����. � ��� ��������� �������� ����������� ���������.")

                Player_answer = input("\n1. ����������� �� ���� 2. �����\n")

                if Player_answer == "1":

                    print("���� ���������. �������� �� �������� �� ������ ������������ ���� ���������� �� �����.")
                    print("�� �������������� �� ����� ��� ���, �������� ��� ���� �������� ������ �����. �� �� �������� ���� ��� �������.")
                    print("�������, ������������ ���� �� ������ �� �� ����, �� �� �������. ������ ������ �������������� ��� - ��.")

                    Player_answer = input("\n1. ����� 2. �����\n")

                    print("�� ���������� ������ �����. ������ �� ����� ������� �� ������� ���� �����.")
                    print("��� �� �����, �� �������� �������� ����� � ���������� ���.")

                    ExitSituation = 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "3":

            print("�� ���������� ���������. ������� � ��� �� ����������.")
    
        elif Player_answer == "I" or Player_answer == "i":
            Player_inventory_check(Player)

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)

        elif Player_answer == "H" or Player_answer == "h":
            print("�� �� ����������� ������� ��������� � ��������� ���� ������ ��������")