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

    print("Режим игры - Хранитель.")
    print("")
    print("Рекомендации: прохождение ночью, композиция The Fire Is Gone в качестве фона.")
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
        
            print(f"\n\nОсколков душ: {Player.MoneyReturn()}")
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

                    print("Впишите номер комнаты ( с верхней комнаты ), которую хотите удалить\n")

                    Player_answer = int(input())
                    Player.RoomDelete(Player_answer)
                    print(f"Комната №{Player_answer} удалена")

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

                    print("Впишите номер комнаты ( с верхней комнаты ), которую хотите продать\n")

                    Player_answer = input()

                    try:
                        int(Player_answer)
                    except ValueError:
                        Player_answer = "43980465"
                    
                    Player_answer = int(Player_answer)

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

                    print("Впишите номер комнаты ( с верхней комнаты ), которую хотите купить\n")

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
        print("Фаза 2 - Враги.")
        print("=====================================================\n")

        Phase2 = 0
        while Phase2 == 0:

            print("\n=====================================================")
            print("Текущий вражеский состав:")
            

            for i in Enemys_stack:

                print("-------------------------------------------------------")
                print(f"Имя врага - {i[0]}")
                print(f"Очки здоровья - {i[1]}")
                print(f"Урон - {i[2]}")
                
            print("=====================================================\n")

            New_unit = Enemy_randomunit()

            if New_unit[0] == "Минион":
                Enemys_stack.append(New_unit)
                Enemys_stack.append(New_unit)
            else:
                Enemys_stack.append(New_unit)
            
            print(f"Новый враг - {New_unit[0]}")
            print("")
            print("Нажмите Enter что бы продолжить")

            Player_answer = input()

            if Player_answer == "Main":
                return

            Phase2 = 1

        print("=====================================================")
        print("Фаза 3 - Вычет")
        print("=====================================================\n")

        Phase3 = 0
        while Phase3 == 0:

            Rooms_list_battle = copy.deepcopy(Player.RoomsReturn())
            Enemys_stack_battle = copy.deepcopy(Enemys_stack)

            Player_answer = input()

            DeductionEnd = 0
            while DeductionEnd == 0:

                print("-------------------------------------------------------")
                print(f"Комната - {Rooms_list_battle[0][0]}\n")
                print(f"Враги: {Enemys_stack_battle[0][0]}")
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
                        print(f"Враг {Enemys_stack_battle[0][0]} мёртв")
                        del Enemys_stack_battle[0]
                    else:
                        Enemys_Survived += 1
                        print(f"Враг {Enemys_stack_battle[0][0]} выжил")

                del Rooms_list_battle[0]

                if Enemys_stack_battle == []:

                    print("\nВы отбили волну без потерь!")

                    Phase3 = 1
                    DeductionEnd = 1

                elif Rooms_list_battle == []:

                    print("\nВы пропустили врагов к Ядру")

                    Damage = 0
                    for enemy in Enemys_stack_battle:
                        Damage += enemy[2]

                    Player.HpReduction(Damage)
                    print(f"Ядру нанесено {Damage} урона!")

                    if Player.HpReturn() <= 0:
                        print("""Ядро в критическом состоянии. Оно готово вот-вот разрушиться, но в последний момент перед ним появляются сияющие существа с белоснежными крыльями.
Они уничтожают оставшихся захватчиков и стабилизируют ядро. На короткое время вы чувствуете спокойствие, но затем вспоминаете о том, что провалились.
Отвлекаясь от ядра, ваши создатели поворачиваются в вашу сторону. Секундная паника накрывает вас. Вы чувствуете всплеск боли в грудной клетке.
Силы покидают вас и вы падаете на землю. Последним, что вы сможете разглядеть будет ещё один Хранитель, презрительно глядящий на вас.\n\n\n""")

                        return

                    Phase3 = 1
                    DeductionEnd = 1

                print("\nНажмите Enter что бы продолжить")

                Player_answer = input()

                if Player_answer == "Main":
                    return

            print("\nЗа прохождение волны вам начислено 60 осколков душ")
            Player.MoneyAdd(60)

            if Turns_num % 3 == 0:
                print("\nВы можете сохранить прогресс. Пропишите команду Save, что бы сохранить прогресс или нажмите Enter, что бы избежать сохранения.\n")

                Player_answer = input()

                if Player_answer == "Save":

                    print("Введите номер слота ( от 1 до 4 )")

                    Player_answer = input()

                    if Player_answer == "1":
                        GuardianMode_Save(1, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "2":
                        GuardianMode_Save(2, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "3":
                        GuardianMode_Save(3, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])
                    elif Player_answer == "4":
                        GuardianMode_Save(4, Enemys_stack, [Player.RoomsReturn(), Player.MoneyReturn(), Player.HpReturn()])