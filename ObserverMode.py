# -*- coding: cp1251 -*-
from Dangeon_Room import *
from PYGame_SaveLoad import *
import random

def ObserverMode(Room_Num_En, Dangeon_difficult_En, Player_En, Enemy_Num_En, Chest_Num_En):

    def Random_Room_Size():

        Size = random.randint(1,3)

        return Size

    def Random_Room_Biome():

        Biome = random.randint(1,5)

        return Biome

    def Random_Chest_Size():

        Size = random.randint(1,3)

        return Size

    def Random_Chest_Type():

        Type = random.randint(1,5)

        return Type

    def Random_Chest_TType():

        TType = random.randint(0,5)

        return TType

    def Random_Chest_Dmg(Dangeon_difficult, Player):

        Current_Player_dmg = Player.DamageOutPut()

        if Dangeon_difficult < 3:
            Dmg = Current_Player_dmg + 2
        elif Dangeon_difficult <= 5 and Dangeon_difficult > 3:
            Dmg = Current_Player_dmg + 1
        elif Dangeon_difficult <= 8 and Dangeon_difficult > 5:
            Dmg = Current_Player_dmg
        else:
            Dmg = Current_Player_dmg - 1

        return Dmg

    def Random_Enemy_Name():

        Name = random.randint(1,3)

        return Name

    def Random_Enemy_Dmg(Dangeon_level, Player):

        Current_Player_hp = Player.HpVis()

        Dmg = Dangeon_level + Current_Player_hp // 5

        return Dmg

    def Random_Enemy_Hp(Dangeon_level, Player):

        Current_Player_dmg = Player.DamageOutPut()

        Hp = Dangeon_level + 5 + Current_Player_dmg * 3

        return Hp

    def Player_HpRandomHeal():

        rnd = random.randint(0,10)

        if rnd <= 7 and rnd > 3:
            return 5
        elif rnd <= 3:
            return 10
        elif rnd >=9 and rnd <10:
            return 20
        elif rnd == 10:
            return 25
        else:
            return rnd



    Player = Player_En
    Dangeon_difficult = Dangeon_difficult_En
    Room_Num = Room_Num_En
    Dangeon_level = 1

    Never = 0
    while Never == 0:

        Room = Dangeon_Room_NonAction(Random_Room_Size(), Random_Room_Biome())
        Chest = Dangeon_Room_Action_Chest(Random_Chest_Size(), Random_Chest_Type(), Random_Chest_TType(), Random_Chest_Dmg(Dangeon_difficult, Player))
        Enemy = Dangeon_Room_Action_Enemy(Random_Enemy_Name(), Random_Enemy_Dmg(Dangeon_level, Player), Random_Enemy_Hp(Dangeon_level, Player))

        Chest_num = Chest_Num_En
        Enemy_num = Enemy_Num_En
        Sleep_num = 0

        Room.VisualGeneration()

        ExitRoom = 0
        while ExitRoom == 0:

            print("1. ����������� 2. �������������� 3. �����")

            Player_answer = input("\n")

            if Player_answer == "1":

                Chest.VisualGeneraton()
                if Enemy_num > 0:
                    print(f"���������� ������: {Enemy_num}")
                    Enemy.VisualGeneraton()
                    print(f"����: {Enemy.HpVis()}")
                    Enemy_num -= 1
                    Enemy = Dangeon_Room_Action_Enemy(Random_Enemy_Name(), Random_Enemy_Dmg(Dangeon_level, Player), Random_Enemy_Hp(Dangeon_level, Player))
            
            elif Player_answer == "2" and Chest_num > 0:

                print("")
                print("1. ������")

                Player_answer = input()

                if Player_answer == "1":

                    print("")
                    print("�� ���������� ������.")
                    
                    Item = Chest.ItemGeneration()

                    print("=====================================================")
                    print(f"�� ��������� {Item[3]} � �������� ��������������� {Item[5]}")
                    print("=====================================================\n")

                    Player.InventoryAdd(Item)

                    Chest_num -= 1

                    if Chest_num > 0:
                        Chest = Dangeon_Room_Action_Chest(Random_Chest_Size(), Random_Chest_Type(), Random_Chest_TType(), Random_Chest_Dmg(Dangeon_difficult, Player))

            elif Player_answer == "2" and Chest_num == 0:

                print("")
                print("� ������� �� � ��� �����������������.")

            elif Player_answer == "3" and Sleep_num < 3:

                Player.HpAdd(Player_HpRandomHeal())
                Sleep_num += 1

            elif Player_answer == "3" and Sleep_num >= 3:

                print("")
                print("�� ���������� ���������.")

            elif Player_answer == "I" or Player_answer == "i":

                Inv_list = Player.InventoryOutput()

                print("=====================================================")
                print("���������:")
                print("=====================================================")

                for i in Inv_list:

                    print("-------------------------------------------------------")
                    print(f"{i[0]} | {i[3]} | {i[4]}")
                    print("-------------------------------------------------------")

                print("")
                print("1. ������������ ������� 2. ������� ������� 3. �����")

                Player_answer = input()

                if Player_answer == "1":

                    print("")
                    print("������� ID �������� ( ������ ����� � �������� )")

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
                    print("������� ID �������� ( ������ ����� � �������� )")

                    Player_answer = int(input())

                    Player.InventoryDel(Player_answer)

                elif Player_answer == "3":
                    continue

            elif Player_answer == "M" or Player_answer == "m":

                Body_list = Player.BodyOutput()
                print("=====================================================")
                print(f"{Player.NameOutPut()} | {Player.StoryOutPut()}")
                print("=====================================================")

                for i in Body_list:

                    print("-------------------------------------------------------")
                    print(f"{i[0]} | {i[3]} | {i[4]}")
                    print("-------------------------------------------------------")

            elif Player_answer == "H" or Player_answer == "h":

                print(f"������� ������� ��������: {Player.HpVis()}")

            elif Player_answer == "Rooms":

                print(f"\n\n���������� ���������� ������: {Room_Num}\n\n")

            elif Player_answer == "Ex":

                print("")
                print("������ ���� ��������� ���, ���� �������� ����� � ����������������. ��� ������ �� �����. ���� ������ � �� ����� ������������ ������ ��������� �������.")
                
                if Player.HpVis() < 41:
                    Dangeon_difficult -= 1
                else:
                    Dangeon_difficult += 1

                ExitRoom = 1
                Room_Num += 1
                Exit_list = [Room_Num, Dangeon_difficult, Player, 0]
                return Exit_list

            elif Player_answer == "Save":

                print("")
                print("���������� ���� ��������� ���, ���� �������� ����������� � ������������.")
                print("�������� ����: �� 1 �� 4\n")
                
                Player_answer = input()

                if Player_answer == "1":
                    ObserverMode_Save(1, Dangeon_difficult, [Player.NameOutPut(), Player.StoryOutPut(), Player.InventoryOutput(), Player.BodyOutput(), Player.HpVis()], Room_Num)
                elif Player_answer == "2":
                    ObserverMode_Save(2, Dangeon_difficult, [Player.NameOutPut(), Player.StoryOutPut(), Player.InventoryOutput(), Player.BodyOutput(), Player.HpVis()], Room_Num)
                elif Player_answer == "3":
                    ObserverMode_Save(3, Dangeon_difficult, [Player.NameOutPut(), Player.StoryOutPut(), Player.InventoryOutput(), Player.BodyOutput(), Player.HpVis()], Room_Num)
                elif Player_answer == "4":
                    ObserverMode_Save(4, Dangeon_difficult, [Player.NameOutPut(), Player.StoryOutPut(), Player.InventoryOutput(), Player.BodyOutput(), Player.HpVis()], Room_Num)

            elif Player_answer == "Main":
                Exit_list = [Room_Num, Dangeon_difficult, Player, 1]
                return Exit_list