# -*- coding: cp1251 -*-
from http.client import PRECONDITION_REQUIRED
from string import printable
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
    KnownAboutAmnesia = False

    print("��� ����� �� ��������, � ���� ������ ��� ��������� ����� ������� �����. ���� ����� ��������� ����� ���� � �� ��������������.")
    print("����� ������ �����, �� ������ ����� ����� ���������� �������, �� ������� ��� ��������� �����. ��������� �� ��� �������� �� ��� ��� ��������,")
    print("�� �� ������� � ��� ��������� �� ������ ���� ������. ������� ������������ ����� ������� ������� ������������ ��� �������� ������ ������. �� ")
    print("��������� ������� ������������� ��������� ������. �������� �� ���������� ����� ���������� �����, ������� ���� ������ ��������.")
    print("�� ��������, ��� � ��� ����� ��������� ���� �� �����, ���� ������������������.")
    print("- ����������� � ������ �������, ���������. - ������� ��, ������� ������ � ���.")

    PhraseRepeat_1_2 = 0
    PhraseRepeat_1_3 = 0
    Dialog_1 = 0
    while Dialog_1 == 0:

        Player_answer = input("\n\n1. ���������� \n2. '��� ��?' 3. '��� ��� �� �����?'\n")

        if Player_answer == "1":
            
            print("- � ���, � ����������� �������� ������ ���������� �������� ��������� ��������� �� ������. ����������, ���� �� ������ ��� ������� �� -")
            print("� �� ���� ������.")

            Player_answer = input("\n\n1. ���������� \n2. '��, � �� ������' 3. '� ���'\n")



        elif Player_answer == "2" and PhraseRepeat_1_2 == 0:

            print("- � - ������, ������� ���. ������� ��������� �� ������ ��������.")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 == 1:

            print("- ���... � - ������, ������� ���. ������� ��������� �� ������ ��������.")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 == 2:

            print("- ������, ���� �� ����� �������, �� ����� �� ���� �����. - ���������� ����� ������ ������")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 >= 3:

            print("- ...")
            print("�� ��������� ��������� ������������ ����� ����.")

        elif Player_answer == "3" and PhraseRepeat_1_3 == 0:

            print("- ��� ����� ������� �� ������� ����������. ���� ������ ��������, �� �� ������������, ��� ��� ���� ���� ��� �����, ���� �� ������� ���������.")
            PhraseRepeat_1_3 += 1

        elif Player_answer == "3" and PhraseRepeat_1_3 == 1:

            print("- ��������? ��, ���� ����� ��������� �������� ����� � �������� ����� ����� ���� ������, ����� ���������� ������� � ������.")
            PhraseRepeat_1_3 += 1

        elif Player_answer == "3" and PhraseRepeat_1_3 == 2:

            print("- ������, � ������? �� �� ������ ��� ����� ����������? ���... ��� �� ���������� ������, ��?")
            print("��� ���������� ������� ������� � ���������� �����.")
            print("- ������, � ����� �� ������� ������ ����� ����, ��� ����� � ����������. � ������ ������ �� ��������, ��� ��� ����� ����� �������� ����")
            print("�����, �� � � ����� ������ ��� ���������.")
            print("��� ������ �� ���� �� ������ �� ������� �������. ��� �������� �� 3-� ������ � ���� ��������� � ����������� ����.")
            print("- ��� ����. ��� ��������� ������. ������ �� � ����� �������� � ���� �������.")
            Dialog_1 = 1
            KnownAboutAmnesia = True