# -*- coding: cp1251 -*-
from Dangeon_Room import *
from Dangeon_Guardian import *
from StoryMode import *
from ObserverHub import *
from UnlimitHub import *
from GuardianMode import *
from PYGame_SaveLoad import *
from PYGame_Defaulter import *

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
print("����� ������� ���� ������������ � ������ README.txt � ����� ����.")
print("�������� ���������, �� �������� �������� �� ����� �������� ����������������� ����������.")
print("=====================================================\n")
print("")
print("������� Enter ��� �����������.")

Start_game = input()

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
    print("     2. ���������� ����")
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
        print("     4. ���������")
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
            Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 5), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 4),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 4), (5, "tissue", "arms", "������� ����������", "���������� �� ������ ����. ���� ����� �� ������� �������, ������� ��������", 4), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
            Dangeon_difficult = 5
            Room_Num = 1
            Everlast_Hub(Room_Num, Dangeon_difficult, Player)
        elif Player_answer == "3":
            Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 5), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "������� ����������", "���������� �� ������ ����. ���� ����� �� ������� �������, ������� ��������", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
            Dangeon_difficult = 5
            Room_Num = 1
            Observer_Hub(Room_Num, Dangeon_difficult, Player)
        elif Player_answer == "4":
            Player = Dangeon_Action_Player_Guardian([["Single", 10, 1, 90]], 100, 100)
            Enemys = [["������", 3, 2],["������", 3, 2]]
            GuardianMode(Enemys, Player)
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
        print("")
        print("10. ���������. ���� �1")
        print("11. ���������. ���� �2")
        print("12. ���������. ���� �3")
        print("13. ���������. ���� �4")
        print("")
        print("14. �������� �������� ���� ����������")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":
            StoryMode_List = StoryMode_Load()
            StoryMode(StoryMode_List[0], Dangeon_Action_Player_Conqueror(StoryMode_List[1][0], StoryMode_List[1][1], StoryMode_List[1][2], StoryMode_List[1][3], StoryMode_List[1][4]))
        elif Player_answer == "2":
            EverlastMode_List = UnlimitMode_Load(1)
            Everlast_Hub(EverlastMode_List[2], EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "3":
            EverlastMode_List = UnlimitMode_Load(2)
            Everlast_Hub(EverlastMode_List[2], EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "4":
            EverlastMode_List = UnlimitMode_Load(3)
            Everlast_Hub(EverlastMode_List[2], EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "5":
            EverlastMode_List = UnlimitMode_Load(4)
            Everlast_Hub(EverlastMode_List[2], EverlastMode_List[0], Dangeon_Action_Player_Conqueror(EverlastMode_List[1][0], EverlastMode_List[1][1], EverlastMode_List[1][2], EverlastMode_List[1][3], EverlastMode_List[1][4]))
        elif Player_answer == "6":
            ObserverMode_List = ObserverMode_Load(1)
            Observer_Hub(ObserverMode_List[2], ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "7":
            ObserverMode_List = ObserverMode_Load(2)
            Observer_Hub(ObserverMode_List[2], ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "8":
            ObserverMode_List = ObserverMode_Load(3)
            Observer_Hub(ObserverMode_List[2], ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "9":
            ObserverMode_List = ObserverMode_Load(4)
            Observer_Hub(ObserverMode_List[2], ObserverMode_List[0], Dangeon_Action_Player_Conqueror(ObserverMode_List[1][0], ObserverMode_List[1][1], ObserverMode_List[1][2], ObserverMode_List[1][3], ObserverMode_List[1][4]))
        elif Player_answer == "10":
            Guardian_list = GuardianMode_Load(1)
            GuardianMode(Guardian_list[0], Dangeon_Action_Player_Guardian(Guardian_list[1][0], Guardian_list[1][1], Guardian_list[1][2]))
        elif Player_answer == "11":
            Guardian_list = GuardianMode_Load(2)
            GuardianMode(Guardian_list[0], Dangeon_Action_Player_Guardian(Guardian_list[1][0], Guardian_list[1][1], Guardian_list[1][2]))
        elif Player_answer == "12":
            Guardian_list = GuardianMode_Load(3)
            GuardianMode(Guardian_list[0], Dangeon_Action_Player_Guardian(Guardian_list[1][0], Guardian_list[1][1], Guardian_list[1][2]))
        elif Player_answer == "13":
            Guardian_list = GuardianMode_Load(4)
            GuardianMode(Guardian_list[0], Dangeon_Action_Player_Guardian(Guardian_list[1][0], Guardian_list[1][1], Guardian_list[1][2]))
        elif Player_answer == "14":

            print("=====================================================")
            print("�� �������?")
            print("")
            print("1. �� 2. ���")
            print("=====================================================\n")

            Player_answer = input()

            if Player_answer == "1":
                PYGame_Defaulter()

    elif Player_answer == "3":
        print(readtxt("MainMenu\\Directory.txt"))
    elif Player_answer == "4":
        print(readtxt("MainMenu\Autors.txt"))
    elif Player_answer == "5":
        break