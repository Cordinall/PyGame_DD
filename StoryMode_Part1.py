# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

def StoryMode_Part1():

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
    print("Акт 1 - Во тьме")
    print("=====================================================\n")
    print("")
    print("Вы приходите в себя в тёмном помещении. Ваш взгляд затуманен и единственное, что вы можете спокойно разглядеть - яркое пятно, излучающее свет.")
    print("Вокруг довольно сухо, но вы слышите как рядом с вами падают капли, разбиваясь о воду.")

    Player = Dangeon_Action_Player_Conqueror("Пустой", "Ещё один житель Подземелья", [], [(1,  "onehand", "hand", "Руки", "Всё в ваших руках", 1), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 8),  (3,  "tissue", "leggs", "Старые штаны", "Старые штаны, покрытые пылью и липкой субстанцией", 4), (4, "tissue", "chest", "Порваная рубаха", "Старая, изодранная рубаха. Возможно её можно носить", 5), (5, "tissue", "arms", "Тканевая повязка", "Тканевая повязка, весьма грязная.", 8), (6, "tissue", "head", "Влажная тканевая повязка", "Мокрая тканевая повязка", 1)], 100)
    Player_hp = 100

    Body_watch = 0
    ExitSituation = 0
    while ExitSituation == 0:


        Player_answer = input("\n1. Осмотреться 2. Взаимодействовать 3. Отдыхать\n")

        if Player_answer == "1":

            print("Вы пытаетесь встать, но сильное головокружение заставляет вас прекратить эти попытки. Под собой вы чувствете холодный и отностительно")
            print("гладкий камень.")
            print("Вы стараетесь вглядеться в окружение. Сквозь туман проглядываются очертания каменных стен.")
            print("")
            print("Тем не менее, глаза всё ещё не могут фокусироваться на чём - то конкретном.")

        elif Player_answer == "2":

            Player_answer = input("\n1. Вода\n")

            if Player_answer == "1" and Body_watch == "0":

                print("Ваш взгляд размыт, поэтому вам не удаётся разглядеть воду в подробностях, но, принюхавшись, вы обнаружили отсутствие запаха.")
                print("Лужа неболшая, вряд ли получится распределить её на несколько задач.")

                Player_answer = input("\n1. Выпить 2. Вымыть лицо 3. Отстраниться от лужи\n")

                if Player_answer == "1":

                    print("Вы набираете воду из лужицы в горсть и пробуете на вкус. Ничего необычного. Вы продолжаете пить.")
                    print("Лужа довольно быстро изчезает. Вы чувствете себя лучше.")

                elif Player_answer == "2":

                    print("Вы набираете воду из лужицы в горсть и ополаскиваете лицо.")
                    print("Вода весьма прохладная.")
                    break

                elif Player_answer == "3":
                    continue

            elif Player_answer == "1" and Body_watch == "1":

                print("Ваш взгляд размыт, поэтому вам не удаётся разглядеть воду в подробностях, но, принюхавшись, вы обнаружили отсутствие запаха.")
                print("Лужа неболшая, вряд ли получится распределить её на несколько задач.")

                Player_answer = input("\n1. Выпить 2. Вымыть лицо 3. Отмыть тканевую повязку 4. Отстраниться от лужи\n")

                if Player_answer == "1":

                    print("Вы набираете воду из лужицы в горсть и пробуете на вкус. Ничего необычного. Вы продолжаете пить.")
                    print("Лужа довольно быстро изчезает. Вы чувствете себя лучше.")

                elif Player_answer == "2":

                    print("Вы набираете воду из лужицы в горсть и ополаскиваете лицо.")
                    print("Вода весьма прохладная.")
                    break

                elif Player_answer == "3":
                    continue

                elif Player_answer == "4":

                    print("Вы снимаете с руки тканевую повязку и стараетесь мныть грязь с её поверхности.")
                    print("Грязь отмывается с трудом, но в конце концов поддаётся вашим усилиям.")
                    print("Под слоем грязи вы обнаруживаете белую повязку с тремя параллельными линиями, расположенными вертикально.")

                    Player.BodyChangeArms((5, "tissue", "arms", "Тканевая повязка", "Белая повязка с тремя параллельными линиями, расположенными вертикально.", 8))
                    Player.InventoryDel(5)

        elif Player_answer == "3":

            print("Вы стараетесь отдохнуть. Ваши веки постепенно тяжелеют и в конце концов вы засыпаете.")
            print("Вы просыпаетесь почти сразу. Несмотря на это, вы чувствете себя отдохнувшим.")
            break

        elif Player_answer == "I" or Player_answer == "i":
            print("У вас нет ничего с собой")

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)
            Body_watch = 1

        elif Player_answer == "H" or Player_answer == "h":
            print("Вы не испытываете болевых ощущуений и чувствете себя вполне здоровым")

    print("Ваше самочувствие улучшилось, а дымка в глазах почти пропала.")

    ExitSituation = 0
    while ExitSituation == 0:

        torch = 0

        Player_answer = input("\n1. Осмотреться 2. Взаимодействовать 3. Отдыхать\n")

        if Player_answer == "1":

            print("Вы пытаетесь встать. Весьма удачно. Вы обнаруживаете себя в окружении пещерных стен.")
            print("Единственным источником света остаётся факел, висящий на одной из стен. Вокруг сухо, но весьма прохладно.")
            print("")

        elif Player_answer == "2":

            print("Вам не с чем взаимодействовать.")

        elif Player_answer == "3":

            print("Вы стараетесь отдохнуть. Заснуть у вас не получается.")
    
        elif Player_answer == "I" or Player_answer == "i":
            Player_inventory_check(Player)

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)

        elif Player_answer == "H" or Player_answer == "h":
            print("Вы не испытываете болевых ощущуений и чувствете себя вполне здоровым")