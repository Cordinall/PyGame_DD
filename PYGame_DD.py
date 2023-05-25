# -*- coding: cp1251 -*-
from Dangeon_Room import *
from StoryMode import *
from ObserverHub import *
from UnlimitHub import *
from GuardianMode import *
from PYGame_SaveLoad import *

def readtxt(adr):
      ans = ""
      for i in open(adr, encoding="utf-8"):
        endans = i.strip()
        if endans == "":
            ans = ans + endans + "\n" + "\n"
            continue
        else:
            ans = ans + endans + "\n"

      return ans

Player_answer = ""

print("=====================================================")
print("����������� � ���� Dangeon and Dangeon")
print("=====================================================\n")

print("=====================================================")
print("� �������� ����� ����������� ������������� ��� ��������� ��������.\n���� �������� ����� ������� ������.\n������:")
print("1. �����\n2. ������\n")
print("1")
print("=====================================================\n")

ExitMainMenu = 0
while ExitMainMenu == 0:

    print("=====================================================")
    print("Main Menu\n")
    print("     1. ������ ����� ����")
    print("     2. ���������� ���� ( � ���������� )")
    print("     3. ���������� ( ������������� � ��������� )")
    print("     4. ������")
    print("     5. �����")
    print("=====================================================\n")

    Player_answer = input()

    if Player_answer == "1":

        print("=====================================================")
        print("     1. ����������")
        print("     2. ���������")
        print("     3. �����������")
        print("     4. ��������� ( � ���������� )")
        print("")
        print("     5. �����")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":

            print("=====================================================")
            print("�� �������?")
            print("")
            print("1. �� 2. ���")
            print("=====================================================\n")

            Player_answer = input()

            if Player_answer == "1":
                Player = Dangeon_Action_Player_Conqueror(" ", " ", [], [(1,  "onehand", "hand", "����", "�� � ����� �����", 1), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "�������� �������", "�������� �������, ������ �������.", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
                StoryMode(0, Player)
            else:
                continue

        elif Player_answer == "2":
            Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 5), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "������� ����������", "���������� �� ������ ����. ���� ����� �� ������� �������, ������� ��������", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
            Dangeon_difficult = 5
            Everlast_Hub(Dangeon_difficult, Player)
        elif Player_answer == "3":
            Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 5), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "������� ����������", "���������� �� ������ ����. ���� ����� �� ������� �������, ������� ��������", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
            Dangeon_difficult = 5
            Observer_Hub(Dangeon_difficult, Player)
        elif Player_answer == "4":
            GuardianMode()
        elif Player_answer == "5":
            continue
        
    elif Player_answer == "2":
        
        print("")
        print("=====================================================")
        print("1. ����������. ��������� ���")
        print("")
        print("2. ���������. ���� �1")
        print("3. ���������. ���� �2")
        print("4. ���������. ���� �3")
        print("5. ���������. ���� �4")
        print("")
        print("6. �����������. ���� �1")
        print("7. �����������. ���� �2")
        print("8. �����������. ���� �3")
        print("9. �����������. ���� �4")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":
            StoryMode_List = StoryMode_Load()
            StoryMode(StoryMode_List[0], Dangeon_Action_Player_Conqueror(StoryMode_List[1][0], StoryMode_List[1][1], StoryMode_List[1][2], StoryMode_List[1][3], StoryMode_List[1][4]))
        elif Player_answer == "2":
            EverlastMode_List = UnlimitMode_Load(1)
            Everlast_Hub(EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "3":
            EverlastMode_List = UnlimitMode_Load(2)
            Everlast_Hub(EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "4":
            EverlastMode_List = UnlimitMode_Load(3)
            Everlast_Hub(EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "5":
            EverlastMode_List = UnlimitMode_Load(4)
            Everlast_Hub(EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "6":
            ObserverMode_List = ObserverMode_Load(1)
            Observer_Hub(ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "7":
            ObserverMode_List = ObserverMode_Load(2)
            Observer_Hub(ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "8":
            ObserverMode_List = ObserverMode_Load(3)
            Observer_Hub(ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "9":
            ObserverMode_List = ObserverMode_Load(4)
            Observer_Hub(ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))

    elif Player_answer == "3":
        print(readtxt("MainMenu\\Directory.txt"))
    elif Player_answer == "4":
        print(readtxt("MainMenu\Autors.txt"))
    elif Player_answer == "5":
        break