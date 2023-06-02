# -*- coding: cp1251 -*-
from Dangeon_Room import *
from Guardian_EnemySet import *
from Guardian_RoomsSet import *
import random

def GuardianMode(Player, Enemys):

    Player = Player
    Enemeys_stack = Enemys
    Turns_num = 0

    print("����� ���� - ���������.")
    print("")
    print("����� �������� � 3 ������: �����, ����� � �����")
    print("")
    print("����� - ������ ������. ����� ������������ ���������� �����������.")
    print("����� - �������������� ��������� �����, � ���� ����� ����������� ����� �����.")
    print("����� - ���������� ����� ����� �� ������. ���� �� ����� ���� ���� ���� ���������� - ����� ���������.")
    print("")
    print("")

    Never = 0
    while Never == 0:

        Rooms_list = Rooms_RandomSet()

        print("=====================================================")
        print("���� 1 - �����.")
        print("=====================================================\n")

        Phase1 = 0
        while Phase1 == 0:
        
            print(f"�������� ���: {Player.MoneyReturn()}")
            print("1. ������� ������� 2. ������� ����� ������� 3. ������ ��������� ����\n")

            Player_answer = input()

            if Player_answer == "1" and Turns_num % 2 != 0:

                print("=====================================================\n")
            
                for i in Player.RoomsReturn():

                    print("-------------------------------------------------------")
                    print(f"��� ������� - {i[0]}")
                    print(f"���� - {i[1]}")
                    print(f"����������� - {i[2]}")
                    print(f"��������� ������� - {i[3]}")

                print("=====================================================\n")
                print("1. ������� ������� 2. �����\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("������� ����� �������, ������� ������ �������\n")

                    Player_answer = int(input())
                    Player.RoomDelete(Player_answer)
                    print(f"������� �{Player_answer}")

            elif Player_answer == "1" and Turns_num % 2 == 0:

                print("=====================================================\n")
            
                for i in Player.RoomsReturn():

                    print("-------------------------------------------------------")
                    print(f"��� ������� - {i[0]}")
                    print(f"���� - {i[1]}")
                    print(f"����������� - {i[2]}")
                    print(f"��������� ������� - {i[3]}")

                print("=====================================================\n")
                print("1. ������� ������� 2. ������� ������� 3. �����\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("������� ����� �������, ������� ������ �������\n")

                    Player_answer = int(input())

                    if Player_answer <= len(Player.RoomsReturn()):
                        Player.RoomDelete(Player_answer)
                        print(f"������� �{Player_answer} �������")

                elif Player_answer == "2":

                    print("������� ����� �������, ������� ������ �������\n")

                    Player_answer = int(input())
                    print(len(Player.RoomsReturn()))
                    if Player_answer <= len(Player.RoomsReturn()):
                        Player.RoomSell(Player_answer)
                        print(f"������� �{Player_answer} �������")

            elif Player_answer == "2":
            
                print("=====================================================\n")

                for i in Rooms_list:

                    print("-------------------------------------------------------")
                    print(f"��� ������� - {i[0]}")
                    print(f"���� - {i[1]}")
                    print(f"����������� - {i[2]}")
                    print(f"��������� ������� - {i[3]}")

                print("=====================================================\n")
                print("1. ������ ������� 2. �����\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("������� ����� �������, ������� ������ ������\n")

                    Player_answer = int(input())
                    if Player_answer <= len(Rooms_list):
                        if Player.MoneyCheck(Rooms_list[Player_answer-1][3]):
                            Player.RoomAdd(Rooms_list[Player_answer-1][0], Rooms_list[Player_answer-1][1], Rooms_list[Player_answer-1][2], Rooms_list[Player_answer-1][3]-10, Rooms_list[Player_answer-1][3])
                            del Rooms_list[Player_answer-1]


            elif Player_answer == "3":

                Turns_num += 1
                Phase1 = 1

        print("=====================================================")
        print("���� 2 - �����.")
        print("=====================================================\n")

        Phase2 = 0
        while Phase2 == 0:

