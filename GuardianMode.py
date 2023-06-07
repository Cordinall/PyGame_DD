# -*- coding: cp1251 -*-
import copy
from Dangeon_Room import *
from PYGame_SaveLoad import *
from Guardian_EnemySet import *
from Guardian_RoomsSet import *
import random

def GuardianMode(Enemys, Player):

    Player = Player
    Enemys_stack = Enemys
    Turns_num = 0

    print("����� ���� - ���������.")
    print("")
    print("������������: ����������� �����, ���������� The Fire Is Gone � �������� ����.")
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
        
            print(f"\n\n�������� ���: {Player.MoneyReturn()}")
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

                    print("������� ����� ������� ( � ������� ������� ), ������� ������ �������\n")

                    Player_answer = int(input())
                    Player.RoomDelete(Player_answer)
                    print(f"������� �{Player_answer} �������")

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

                    print("������� ����� ������� ( � ������� ������� ), ������� ������ �������\n")

                    Player_answer = input()

                    try:
                        int(Player_answer)
                    except ValueError:
                        Player_answer = "43980465"
                    
                    Player_answer = int(Player_answer)

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

                    print("������� ����� ������� ( � ������� ������� ), ������� ������ ������\n")

                    Player_answer = input()

                    try:
                        int(Player_answer)
                    except ValueError:
                        Player_answer = "43980465"

                    Player_answer = int(Player_answer)

                    if Player_answer <= len(Rooms_list) and Player_answer > 0:
                        if Player.MoneyCheck(Rooms_list[Player_answer-1][3]):
                            Player.RoomAdd(Rooms_list[Player_answer-1][0], Rooms_list[Player_answer-1][1], Rooms_list[Player_answer-1][2], Rooms_list[Player_answer-1][3]-10, Rooms_list[Player_answer-1][3])
                            del Rooms_list[Player_answer-1]


            elif Player_answer == "3":

                Turns_num += 1
                Phase1 = 1

            elif Player_answer == "Main":
                return

        print("=====================================================")
        print("���� 2 - �����.")
        print("=====================================================\n")

        Phase2 = 0
        while Phase2 == 0:

            print("\n=====================================================")
            print("������� ��������� ������:")
            

            for i in Enemys_stack:

                print("-------------------------------------------------------")
                print(f"��� ����� - {i[0]}")
                print(f"���� �������� - {i[1]}")
                print(f"���� - {i[2]}")
                
            print("=====================================================\n")

            New_unit = Enemy_randomunit()

            if New_unit[0] == "������":
                Enemys_stack.append(New_unit)
                Enemys_stack.append(New_unit)
            else:
                Enemys_stack.append(New_unit)
            
            print(f"����� ���� - {New_unit[0]}")
            print("")
            print("������� Enter ��� �� ����������")

            Player_answer = input()

            if Player_answer == "Main":
                return

            Phase2 = 1

        print("=====================================================")
        print("���� 3 - �����")
        print("=====================================================\n")

        Phase3 = 0
        while Phase3 == 0:

            Rooms_list_battle = copy.deepcopy(Player.RoomsReturn())
            Enemys_stack_battle = copy.deepcopy(Enemys_stack)

            Player_answer = input()

            DeductionEnd = 0
            while DeductionEnd == 0:

                print("-------------------------------------------------------")
                print(f"������� - {Rooms_list_battle[0][0]}\n")
                print(f"�����: {Enemys_stack_battle[0][0]}")
                if len(Enemys_stack_battle) > 1:
                    print(f"       {Enemys_stack_battle[1][0]}")
                if len(Enemys_stack_battle) > 2:
                    print(f"       {Enemys_stack_battle[2][0]}")
                print("-------------------------------------------------------\n")

                Enemys_Survived = 0

                for i in range(Rooms_list_battle[0][2]):

                    if Enemys_Survived >= len(Enemys_stack_battle):
                        continue

                    Enemys_stack_battle[Enemys_Survived][1] -= Rooms_list_battle[0][1]
                    if Enemys_stack_battle[Enemys_Survived][1] <= 0:
                        print(f"���� {Enemys_stack_battle[0][0]} ����")
                        del Enemys_stack_battle[0]
                    else:
                        Enemys_Survived += 1
                        print(f"���� {Enemys_stack_battle[0][0]} �����")

                del Rooms_list_battle[0]

                if Enemys_stack_battle == []:

                    print("\n�� ������ ����� ��� ������!")

                    Phase3 = 1
                    DeductionEnd = 1

                elif Rooms_list_battle == []:

                    print("\n�� ���������� ������ � ����")

                    Damage = 0
                    for enemy in Enemys_stack_battle:
                        Damage += enemy[2]

                    Player.HpReduction(Damage)
                    print(f"���� �������� {Damage} �����!")

                    if Player.HpReturn() <= 0:
                        print("""���� � ����������� ���������. ��� ������ ���-��� �����������, �� � ��������� ������ ����� ��� ���������� ������� �������� � ������������ ��������.
��� ���������� ���������� ����������� � ������������� ����. �� �������� ����� �� ���������� �����������, �� ����� ����������� � ���, ��� �����������.
���������� �� ����, ���� ��������� �������������� � ���� �������. ��������� ������ ��������� ���. �� ���������� ������� ���� � ������� ������.
���� �������� ��� � �� ������� �� �����. ���������, ��� �� ������� ���������� ����� ��� ���� ���������, ������������ �������� �� ���.\n\n\n""")

                        return

                    Phase3 = 1
                    DeductionEnd = 1

                print("\n������� Enter ��� �� ����������")

                Player_answer = input()

                if Player_answer == "Main":
                    return

            print("\n�� ����������� ����� ��� ��������� 60 �������� ���")
            Player.MoneyAdd(60)

            if Turns_num % 3 == 0:
                print("\n�� ������ ��������� ��������. ��������� ������� Save, ��� �� ��������� �������� ��� ������� Enter, ��� �� �������� ����������.\n")

                Player_answer = input()

                if Player_answer == "Save":

                    print("������� ����� ����� ( �� 1 �� 4 )")

                    Player_answer = input()

                    if Player_answer == "1":
                        GuardianMode_Save(1, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "2":
                        GuardianMode_Save(2, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "3":
                        GuardianMode_Save(3, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "4":
                        GuardianMode_Save(4, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])