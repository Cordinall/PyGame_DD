# -*- coding: cp1251 -*-
from Dangeon_Room import *
from Guardian_EnemySet import *
from Guardian_RoomsSet import *
import random

def GuardianMode(Player, Enemys):

    Player = Player
    Enemeys_stack = Enemys
    Turns_num = 0

    print("Режим игры - Хранитель.")
    print("")
    print("Раунд проходит в 3 стадии: Игрок, Враги и Вычет")
    print("")
    print("Игрок - Первая стадия. Игрок осуществляет управление подземельем.")
    print("Враги - Осуществляется генерация волны, в стек волны добавляются новые враги.")
    print("Вычет - Происходит атака волны на игрока. Если во время этой фазы ядро разрушится - игрок проиграет.")
    print("")
    print("")

    Never = 0
    while Never == 0:

        Rooms_list = Rooms_RandomSet()

        print("=====================================================")
        print("Фаза 1 - Игрок.")
        print("=====================================================\n")

        Phase1 = 0
        while Phase1 == 0:
        
            print(f"Осколков душ: {Player.MoneyReturn()}")
            print("1. Текущие комнаты 2. Создать новую комнату 3. Начать следующую фазу\n")

            Player_answer = input()

            if Player_answer == "1" and Turns_num % 2 != 0:

                print("=====================================================\n")
            
                for i in Player.RoomsReturn():

                    print("-------------------------------------------------------")
                    print(f"Тип комнаты - {i[0]}")
                    print(f"Урон - {i[1]}")
                    print(f"Вместимость - {i[2]}")
                    print(f"Стоимость продажи - {i[3]}")

                print("=====================================================\n")
                print("1. Удалить комнату 2. Назад\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("Впишите номер комнаты, которую хотите удалить\n")

                    Player_answer = int(input())
                    Player.RoomDelete(Player_answer)
                    print(f"Комната №{Player_answer}")

            elif Player_answer == "1" and Turns_num % 2 == 0:

                print("=====================================================\n")
            
                for i in Player.RoomsReturn():

                    print("-------------------------------------------------------")
                    print(f"Тип комнаты - {i[0]}")
                    print(f"Урон - {i[1]}")
                    print(f"Вместимость - {i[2]}")
                    print(f"Стоимость продажи - {i[3]}")

                print("=====================================================\n")
                print("1. Удалить комнату 2. Продать комнату 3. Назад\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("Впишите номер комнаты, которую хотите удалить\n")

                    Player_answer = int(input())

                    if Player_answer <= len(Player.RoomsReturn()):
                        Player.RoomDelete(Player_answer)
                        print(f"Комната №{Player_answer} удалена")

                elif Player_answer == "2":

                    print("Впишите номер комнаты, которую хотите продать\n")

                    Player_answer = int(input())
                    print(len(Player.RoomsReturn()))
                    if Player_answer <= len(Player.RoomsReturn()):
                        Player.RoomSell(Player_answer)
                        print(f"Комната №{Player_answer} продана")

            elif Player_answer == "2":
            
                print("=====================================================\n")

                for i in Rooms_list:

                    print("-------------------------------------------------------")
                    print(f"Тип комнаты - {i[0]}")
                    print(f"Урон - {i[1]}")
                    print(f"Вместимость - {i[2]}")
                    print(f"Стоимость покупки - {i[3]}")

                print("=====================================================\n")
                print("1. Купить комнату 2. Назад\n")

                Player_answer = input()

                if Player_answer == "1":

                    print("Впишите номер комнаты, которую хотите купить\n")

                    Player_answer = int(input())
                    if Player_answer <= len(Rooms_list):
                        if Player.MoneyCheck(Rooms_list[Player_answer-1][3]):
                            Player.RoomAdd(Rooms_list[Player_answer-1][0], Rooms_list[Player_answer-1][1], Rooms_list[Player_answer-1][2], Rooms_list[Player_answer-1][3]-10, Rooms_list[Player_answer-1][3])
                            del Rooms_list[Player_answer-1]


            elif Player_answer == "3":

                Turns_num += 1
                Phase1 = 1

        print("=====================================================")
        print("Фаза 2 - Враги.")
        print("=====================================================\n")

        Phase2 = 0
        while Phase2 == 0:

