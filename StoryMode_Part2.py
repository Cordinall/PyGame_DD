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
        print("Инвентарь:")
        print("=====================================================")

        for i in Inv_list:

            print("-------------------------------------------------------")
            print(f"{i[0]} | {i[3]} | {i[4]}")
            print("-------------------------------------------------------")

        print("")
        print("1. Надеть предмет 2. Удалить предмет 3. Назад")

        Player_answer = input()

        if Player_answer == "1":

            print("")
            print("Введите id предмета ( Цифра в описании предмета )")

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
            print("Введите id предмета ( Цифра в описании предмета )")

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
    print("Акт 2 - В забытие")
    print("=====================================================\n")
    print("")

    Player = Player
    KnownAboutAmnesia = False

    print("Идя вперёд по коридору, в один момент вас ослепляет яркая вспышка света. Ваши глаза накрывает лёгкая боль и вы зажмуриваетесь.")
    print("Вновь открыв глаза, вы видите перед собой просторную площадь, по которой идёт множество людей. Некоторые из них обратили на вас своё внимание,")
    print("но их интерес к вам продлился не больше пары секунд. Площадь представляла собой широкое круглое пространство под высокоми свдами пещеры. По ")
    print("периметру площади располагались различные здания. Несмотря на отсутствие явных источников света, площадь была хорошо освещена.")
    print("Вы заметили, как к вам начал подходить один из людей, вами заинтересовавшихся.")
    print("- Приветствую в городе Надежда, уважаемый. - произнёс он, подойдя поблже к вам.")

    PhraseRepeat_1_2 = 0
    PhraseRepeat_1_3 = 0
    Dialog_1 = 0
    while Dialog_1 == 0:

        Player_answer = input("\n\n1. Промолчать \n2. 'Кто вы?' 3. 'Что это за место?'\n")

        if Player_answer == "1":
            
            print("- Я гид, в обязанности которого входит проведение новичкам небольших экскурсий по городу. Разумеется, если ты хочешь сам изучить всё -")
            print("я не буду против.")

            Player_answer = input("\n\n1. Промолчать \n2. 'Да, я не против' 3. 'Я сам'\n")



        elif Player_answer == "2" and PhraseRepeat_1_2 == 0:

            print("- Я - Эдвард, местный гид. Провожу экскурсии по городу новичкам.")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 == 1:

            print("- Эмм... Я - Эдвард, местный гид. Провожу экскурсии по городу новичкам.")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 == 2:

            print("- Слушай, если ты плохо слышишь, то скажи об этом сразу. - повышенным тоном сказал Эдвард")
            PhraseRepeat_1_2 += 1

        elif Player_answer == "2" and PhraseRepeat_1_2 >= 3:

            print("- ...")
            print("Вы чувствете некоторую напряжённость между вами.")

        elif Player_answer == "3" and PhraseRepeat_1_3 == 0:

            print("- Это самый верхний из городов Подземелья. Ниже только Отчаяние, но он полузаброшен, так что туда мало кто ходит, если не считать Искателей.")
            PhraseRepeat_1_3 += 1

        elif Player_answer == "3" and PhraseRepeat_1_3 == 1:

            print("- Отчаяние? Ну, этот город построили довольно давно и основная масса людей ушла оттуда, когда Подземелье выросло в высоту.")
            PhraseRepeat_1_3 += 1

        elif Player_answer == "3" and PhraseRepeat_1_3 == 2:

            print("- Погоди, в смысле? Ты не знаешь что такое Подземелье? Это... это же внештатный случай, да?")
            print("Ваш собеседник почесал затылок с задумчивым видом.")
            print("- Слушай, я думаю ты потерял память после того, как вошёл в Подземелье. Я такого раньше не встречал, так что лучше будет показать тебя")
            print("врачу, да и в целом понять что случилось.")
            print("Гид указал на одно из зданий на окраине площади. Оно состояло из 3-х этажей и было выкрашено в красноватый цвет.")
            print("- Иди туда. Это городская ратуша. Сообщи им о своей ситуации и тебе помогут.")
            Dialog_1 = 1
            KnownAboutAmnesia = True