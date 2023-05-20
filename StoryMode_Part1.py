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
    print("Рекомендации: прохождение ночью, композиция The Fire Is Gone в качестве фона.")
    print("=====================================================")
    print("Акт 1 - Во тьме")
    print("=====================================================\n")
    print("")
    print("Вы приходите в себя в тёмном помещении. Ваш взгляд затуманен и единственное, что вы можете спокойно разглядеть - яркое пятно, излучающее свет.")
    print("Вокруг довольно сухо, но вы слышите как рядом с вами падают капли, разбиваясь о воду.")

    Player = Dangeon_Action_Player_Conqueror("Пустой", "Ещё один житель Подземелья", [], [(1,  "onehand", "hand", "Руки", "Всё в ваших руках", 1), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 8),  (3,  "tissue", "leggs", "Старые штаны", "Старые штаны, покрытые пылью и липкой субстанцией", 4), (4, "tissue", "chest", "Порваная рубаха", "Старая, изодранная рубаха. Возможно её можно носить", 5), (5, "tissue", "arms", "Тканевая повязка", "Тканевая повязка, весьма грязная.", 8), (6, "tissue", "head", "Влажная тканевая повязка", "Мокрая тканевая повязка", 1)], 100)

    Situation = 0
    Water = True
    Body_watch = False
    ExitSituation = 0
    while ExitSituation == 0:
        
        if Body_watch == False and Water == True:
            Situation = 1
        elif Body_watch == True and Water == True:
            Situation = 2

        Player_answer = input("\n1. Осмотреться 2. Взаимодействовать 3. Отдыхать\n")

        if Player_answer == "1":

            print("Вы пытаетесь встать, но сильное головокружение заставляет вас прекратить эти попытки. Под собой вы чувствете холодный и отностительно")
            print("гладкий камень.")
            print("Вы стараетесь вглядеться в окружение. Сквозь туман проглядываются очертания каменных стен.")
            print("")
            print("Тем не менее, глаза всё ещё не могут фокусироваться на чём - то конкретном.")

        elif Player_answer == "2":

            Player_answer = input("\n1. Вода 2. Назад\n")

            if Player_answer == "1" and Situation == 1:

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

            elif Player_answer == "1" and Situation == 2:

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
                    print("Вы снимаете с руки тканевую повязку и стараетесь смыть грязь с её поверхности.")
                    print("Грязь отмывается с трудом, но в конце концов поддаётся вашим усилиям.")
                    print("Под слоем грязи вы обнаруживаете белую повязку с тремя параллельными линиями, расположенными вертикально.")

                    Player.InventoryAdd((5, "tissue", "arms", "Тканевая повязка", "Белая повязка с тремя параллельными линиями, расположенными вертикально.", 8))
                    Player.BodyChangeArms(5)
                    Player.InventoryDel(5)

                elif Player_answer == "4":
                    continue

            elif Player_answer == "2":
                continue

        elif Player_answer == "3":

            print("Вы стараетесь отдохнуть. Ваши веки постепенно тяжелеют и в конце концов вы засыпаете.")
            print("Вы просыпаетесь почти сразу. Несмотря на это, вы чувствете себя отдохнувшим.")
            break

        elif Player_answer == "I" or Player_answer == "i":
            print("У вас нет ничего с собой")

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)
            Body_watch = True

        elif Player_answer == "H" or Player_answer == "h":
            print("Вы не испытываете болевых ощущуений и чувствете себя вполне здоровым")

    print("Ваше самочувствие улучшилось, а дымка в глазах почти пропала.")
    
    Trystoexit = 0
    Torch = False
    ExitSituation = 0
    while ExitSituation == 0:

        if Torch == False and Trystoexit == 0:
            Situation = 1
        elif Torch == True:
            Situation = 2
        elif Torch == False and Trystoexit == 1:
            Situation = 3
        elif Torch == False and Trystoexit == 2:
            Situation = 4
        elif Torch == False and Trystoexit == 3:
            Situation = 5

        Player_answer = input("\n1. Осмотреться 2. Взаимодействовать 3. Отдыхать\n")

        if Player_answer == "1":

            print("Вы пытаетесь встать. Весьма удачно. Вы обнаруживаете себя в окружении пещерных стен.")
            print("Единственным источником света остаётся факел, висящий на одной из стен. Вокруг сухо, но весьма прохладно.")
            print("")
            print("Вдали комнаты виднеется тёмный участок стены. Он словно пожирает свет, исходящий от факела, освещающего комнату.")

        elif Player_answer == "2" and Situation == 1:

            Player_answer = input("\n1. Факел 2. Участок стены 3. Назад\n")

            if Player_answer == "1":

                print("Вы подходите к факелу. Он выглядит явно не новым, половина факела уже выгорела.")

                Player_answer = input("\n1. Взять факел 2. Назад\n")

                if Player_answer == "1":

                    print("Вы взяли факел.")
                    Player.InventoryAdd((10,  "onehand", "hand", "Факел", "Вполовину сгоревший факел", 1))
                    Player.BodyChangeMelee(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("Вы отходите от факела к центру комнаты.")
                    continue

            elif Player_answer == "2":

                print("Вы подходите к тёмному участку стены. У вас возникает странное предчуствие опасности.")

                Player_answer = input("\n1. Дотронуться до тьмы 2. Назад\n")

                if Player_answer == "1":

                    print("Вы пытаетесь дотронуться до тёмного участка стены. Вы ощущаете резкую боль в той руке, что дотронулась до тьмы.")
                    print("Вы инстинктивно отшатываетесь от стены. Боль быстро проходит, но неприяное ощущуение в руке остаётся ещё некоторое время.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 2:

            Player_answer = input("\n1. Участок стены 2. Назад\n")

            if Player_answer == "1":

                print("Вы подходите к стене с факелом в руках. Первое время ничего не происходит, но когда вы подходите вплотную к тьме, она расступается.")
                print("Перед вами освещается небольшой участок каменистого пола.")

                Player_answer = input("\n1. Вперёд 2. Назад\n")

                if Player_answer == "1":

                    print("Вы проходите на только что освещённый участок пола с факелом в руках. Перед вами открывается пещерный коридор.")
                    print("Единственным источником освещения остаётся факел.")

                    ExitSituation = 1

            elif Player_answer == "2":
                continue

        elif Player_answer == "2" and Situation == 3:

            Player_answer = input("\n1. Факел 2. Участок стены 3. Назад\n")

            if Player_answer == "1":

                print("Вы подходите к факелу. Он выглядит явно не новым, половина факела уже выгорела.")

                Player_answer = input("\n1. Взять факел 2. Назад\n")

                if Player_answer == "1":

                    print("Вы взяли факел.")
                    Player.InventoryAdd((10,  "onehand", "hand", "Факел", "Вполовину сгоревший факел", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("Вы отходите от факела к центру комнаты.")
                    continue

            elif Player_answer == "2":

                print("Вы подходите к тёмному участку стены. У вас возникает странное предчуствие опасности.")

                Player_answer = input("\n1. Дотронуться до тьмы 2. Назад\n")

                if Player_answer == "1":

                    print("Вы пытаетесь дотронуться до тёмного участка стены. Вы ощущаете резкую боль в той руке, что дотронулась до тьмы.")
                    print("Вы инстинктивно отшатываетесь от стены. Боль быстро проходит, но неприяное ощущуение в руке остаётся ещё некоторое время.")
                    print("Поначалу вы этого не заметили, но боль не столь сильна. А вы испытываете странное ощущение, которое сложно описать.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 4:

            Player_answer = input("\n1. Факел 2. Участок стены 3. Назад\n")

            if Player_answer == "1":

                print("Вы подходите к факелу. Он выглядит явно не новым, половина факела уже выгорела.")

                Player_answer = input("\n1. Взять факел 2. Назад\n")

                if Player_answer == "1":

                    print("Вы взяли факел.")
                    Player.InventoryAdd((10,  "onehand", "hand", "Факел", "Вполовину сгоревший факел", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("Вы отходите от факела к центру комнаты.")
                    continue

            elif Player_answer == "2":

                print("Вы подходите к тёмному участку стены. У вас возникает странное предчуствие опасности.")

                Player_answer = input("\n1. Дотронуться до тьмы 2. Назад\n")

                if Player_answer == "1":

                    print("Вы пытаетесь дотронуться до тёмного участка стены. Вы ощущаете резкую боль в той руке, что дотронулась до тьмы.")
                    print("Вы инстинктивно отшатываетесь от стены. Боль быстро проходит, но неприяное ощущуение в руке остаётся ещё некоторое время.")
                    print("Ощущение, испытанное в предыдущий раз понемногу усиливается. Боль всё ещё остаётся, но кажется незначительной.")
                    Trystoexit += 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "2" and Situation == 5:

            Player_answer = input("\n1. Факел 2. Участок стены 3. Назад\n")

            if Player_answer == "1":

                print("Вы подходите к факелу. Он выглядит явно не новым, половина факела уже выгорела.")

                Player_answer = input("\n1. Взять факел 2. Назад\n")

                if Player_answer == "1":

                    print("Вы взяли факел.")
                    Player.InventoryAdd((10,  "onehand", "hand", "Факел", "Вполовину сгоревший факел", 1))
                    Player.BodyChangeArms(10)
                    Player.InventoryDel(1)
                    Torch = True

                if Player_answer == "2":

                    print("Вы отходите от факела к центру комнаты.")
                    continue

            elif Player_answer == "2":

                print("Вы подходите к тёмному участку стены. У вас возникает странное предчуствие опасности.")

                Player_answer = input("\n1. Дотронуться до тьмы 2. Назад\n")

                if Player_answer == "1":

                    print("Боль пропадает. Ощущения от контакта со стеной непроглядной тьмы становятся всё яснее.")
                    print("Вы дотрагиваетесь до стены ещё раз, чувствуя как рука проходит сквозь стену. Вы не ощущаете боли или радости.")
                    print("Чувство, испытываемое вами не похожк ни на боль, ни на радость. Скорее просто удовлетворение чем - то.")

                    Player_answer = input("\n1. Вперёд 2. Назад\n")

                    print("Вы проникаете внутрь стены. Зрение не может уловить ни единого луча света.")
                    print("Идя на ощупь, вы ощущаете пещерные стены и каменистый пол.")

                    ExitSituation = 1

                elif Player_answer == "2":
                    continue

            elif Player_answer == "3":
                continue

        elif Player_answer == "3":

            print("Вы стараетесь отдохнуть. Заснуть у вас не получается.")
    
        elif Player_answer == "I" or Player_answer == "i":
            Player_inventory_check(Player)

        elif Player_answer == "M" or Player_answer == "m":
            Player_body_check(Player)

        elif Player_answer == "H" or Player_answer == "h":
            print("Вы не испытываете болевых ощущуений и чувствете себя вполне здоровым")