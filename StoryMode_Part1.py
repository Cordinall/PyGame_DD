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
    print("��� 1 - �� ����")
    print("=====================================================\n")
    print("")
    print("�� ��������� � ���� � ����� ���������. ��� ������ ��������� � ������������, ��� �� ������ �������� ���������� - ����� �����, ���������� ����.")
    print("������ �������� ����, �� �� ������� ��� ����� � ���� ������ �����, ���������� � ����.")

    Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "����", "�� � ����� �����", 1), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "�������� �������", "�������� �������, ������ �������.", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
    Player_hp = 100

    Body_watch = 0
    ExitSituation = 0
    while ExitSituation == 0:


        Player_answer = input("\n1. ����������� 2. ����������������� 3. ��������\n")

        if Player_answer == "1":

            print("�� ��������� ������, �� ������� �������������� ���������� ��� ���������� ��� �������. ��� ����� �� ��������� �������� � �������������")
            print("������� ������.")
            print("�� ���������� ���������� � ���������. ������ ����� �������������� ��������� �������� ����.")
            print("")
            print("��� �� �����, ����� �� ��� �� ����� �������������� �� ��� - �� ����������.")

        elif Player_answer == "2":

            Player_answer = input("\n1. ����\n")

            if Player_answer == "1" and Body_watch == "0":

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

            elif Player_answer == "1" and Body_watch == "1":

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
                    continue

                elif Player_answer == "4":

                    print("�� �������� � ���� �������� ������� � ���������� ����� ����� � � �����������.")
                    print("����� ���������� � ������, �� � ����� ������ �������� ����� �������.")
                    print("��� ����� ����� �� ������������� ����� ������� � ����� ������������� �������, �������������� �����������.")

                    Player.BodyChangeArms((5, "tissue", "arms", "�������� �������", "����� ������� � ����� ������������� �������, �������������� �����������.", 8))
                    Player.InventoryDel(5)

        elif Player_answer == "3":

            print("�� ���������� ���������. ���� ���� ���������� �������� � � ����� ������ �� ���������.")
            print("�� ������������ ����� �����. �������� �� ���, �� ��������� ���� �����������.")
            break

        elif Player_answer == "I" or Player_answer == "i":
            print("� ��� ��� ������ � �����")

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)
            Body_watch = 1

        elif Player_answer == "H" or Player_answer == "h":
            print("�� �� ����������� ������� ��������� � ��������� ���� ������ ��������")

    print("���� ������������ ����������, � ����� � ������ ����� �������.")

    ExitSituation = 0
    while ExitSituation == 0:

        torch = 0

        Player_answer = input("\n1. ����������� 2. ����������������� 3. ��������\n")

        if Player_answer == "1":

            print("�� ��������� ������. ������ ������. �� ������������� ���� � ��������� �������� ����.")
            print("������������ ���������� ����� ������� �����, ������� �� ����� �� ����. ������ ����, �� ������ ���������.")
            print("")

        elif Player_answer == "2":

            print("��� �� � ��� �����������������.")

        elif Player_answer == "3":

            print("�� ���������� ���������. ������� � ��� �� ����������.")
    
        elif Player_answer == "I" or Player_answer == "i":
            Player_inventory_check(Player)

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)

        elif Player_answer == "H" or Player_answer == "h":
            print("�� �� ����������� ������� ��������� � ��������� ���� ������ ��������")