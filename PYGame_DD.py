# -*- coding: cp1251 -*-
from Dangeon_Room import *
from StoryMode import *
from ObserverMode import *
from UnlimitHub import *
from GuardianMode import *

def Readtxt(adr):
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
print("� �������� ����� ����������� ������������� ��������.\n���� �������� ����� ������� ������.\n������:")
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
        print("     1. ���������� ( � ���������� )")
        print("     2. ���������")
        print("     3. �����������")
        print("     4. ��������� ( � ���������� )")
        print("")
        print("     5. �����")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":
            StoryMode()
        elif Player_answer == "2":
            Player = Dangeon_Action_Player_Conqueror("������", "��� ���� ������ ����������", [], [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 5), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 8),  (3,  "tissue", "leggs", "������ �����", "������ �����, �������� ����� � ������ �����������", 4), (4, "tissue", "chest", "�������� ������", "������, ���������� ������. �������� � ����� ������", 5), (5, "tissue", "arms", "������� ����������", "���������� �� ������ ����. ���� ����� �� ������� �������, ������� ��������", 8), (6, "tissue", "head", "������� �������� �������", "������ �������� �������", 1)], 100)
            Dangeon_difficult = 5
            Everlast_Hub(Dangeon_difficult, Player)
        elif Player_answer == "3":
            ObserverMode()
        elif Player_answer == "4":
            GuardianMode()
        elif Player_answer == "5":
            continue
        
    elif Player_answer == "2":
        print("� ����������.")
    elif Player_answer == "3":
        print(Readtxt("MainMenu\\Directory.txt"))
    elif Player_answer == "4":
        print(Readtxt("MainMenu\Autors.txt"))
    elif Player_answer == "5":
        break