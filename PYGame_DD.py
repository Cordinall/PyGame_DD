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
print("Перед началом игры ознакомьтесь с файлом README.txt в папке игры.")
print("Запуская программу, вы признаёте согласие со всеми пунктами пользовательского соглашения.")
print("=====================================================\n")
print("")
print("Нажмите Enter для продолжения.")

Start_game = input()

print("=====================================================")
print("Приветствую в игре Dangeon and Dangeon")
print("=====================================================\n")

print("=====================================================")
print("В качестве ввода используйте целочисленные или командные значения.\nИные варианты могут вызвать ошибку.\nПример:")
print("1. Атака\n2. Защита\n")
print("1")
print("=====================================================\n")

ExitMainMenu = 0
while ExitMainMenu == 0:

    print("=====================================================")
    print("Main Menu\n")
    print("     1. Начать новую игру")
    print("     2. Продолжить игру")
    print("     3. Справочник ( рекомендовано к просмотру )")
    print("     4. Авторы")
    print("     5. Выход")
    print("=====================================================\n")

    Player_answer = input()

    if Player_answer == "1":

        print("=====================================================")
        print("     1. Покоритель")
        print("     2. Покорённый")
        print("     3. Наблюдатель")
        print("     4. Хранитель")
        print("")
        print("     5. Назад")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":

            print("=====================================================")
            print("Вы уверены?")
            print("")
            print("1. Да 2. Нет")
            print("=====================================================\n")

            Player_answer = input()

            if Player_answer == "1":
                Player = Dangeon_Action_Player_Conqueror(" ", " ", [], [(1,  "onehand", "hand", "Руки", "Всё в ваших руках", 1), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 8),  (3,  "tissue", "leggs", "Старые штаны", "Старые штаны, покрытые пылью и липкой субстанцией", 4), (4, "tissue", "chest", "Порваная рубаха", "Старая, изодранная рубаха. Возможно её можно носить", 5), (5, "tissue", "arms", "Тканевая повязка", "Тканевая повязка, весьма грязная.", 8), (6, "tissue", "head", "Влажная тканевая повязка", "Мокрая тканевая повязка", 1)], 100)
                StoryMode(0, Player)
            else:
                continue

        elif Player_answer == "2":
            Player = Dangeon_Action_Player_Conqueror("Пустой", "Ещё один житель Подземелья", [], [(1,  "onehand", "hand", "Потрёпаный меч", "Весьма старый и сильно притупившийся меч из железа", 5), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 4),  (3,  "tissue", "leggs", "Старые штаны", "Старые штаны, покрытые пылью и липкой субстанцией", 4), (4, "tissue", "chest", "Порваная рубаха", "Старая, изодранная рубаха. Возможно её можно носить", 4), (5, "tissue", "arms", "Кожаные наплечники", "Наплечники из старой кожи. Если особо не двигать плечами, кажутся удобными", 4), (6, "tissue", "head", "Влажная тканевая повязка", "Мокрая тканевая повязка", 1)], 100)
            Dangeon_difficult = 5
            Room_Num = 1
            Everlast_Hub(Room_Num, Dangeon_difficult, Player)
        elif Player_answer == "3":
            Player = Dangeon_Action_Player_Conqueror("Пустой", "Ещё один житель Подземелья", [], [(1,  "onehand", "hand", "Потрёпаный меч", "Весьма старый и сильно притупившийся меч из железа", 5), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 8),  (3,  "tissue", "leggs", "Старые штаны", "Старые штаны, покрытые пылью и липкой субстанцией", 4), (4, "tissue", "chest", "Порваная рубаха", "Старая, изодранная рубаха. Возможно её можно носить", 5), (5, "tissue", "arms", "Кожаные наплечники", "Наплечники из старой кожи. Если особо не двигать плечами, кажутся удобными", 8), (6, "tissue", "head", "Влажная тканевая повязка", "Мокрая тканевая повязка", 1)], 100)
            Dangeon_difficult = 5
            Room_Num = 1
            Observer_Hub(Room_Num, Dangeon_difficult, Player)
        elif Player_answer == "4":
            Player = Dangeon_Action_Player_Guardian([["Single", 10, 1, 90]], 100, 100)
            Enemys = [["Минион", 3, 2],["Минион", 3, 2]]
            GuardianMode(Enemys, Player)
        elif Player_answer == "5":
            continue
        
    elif Player_answer == "2":
        
        print("")
        print("=====================================================")
        print("1. Покоритель. Последний акт")
        print("")
        print("2. Покорённый. Слот №1")
        print("3. Покорённый. Слот №2")
        print("4. Покорённый. Слот №3")
        print("5. Покорённый. Слот №4")
        print("")
        print("6. Наблюдатель. Слот №1")
        print("7. Наблюдатель. Слот №2")
        print("8. Наблюдатель. Слот №3")
        print("9. Наблюдатель. Слот №4")
        print("")
        print("10. Хранитель. Слот №1")
        print("11. Хранитель. Слот №2")
        print("12. Хранитель. Слот №3")
        print("13. Хранитель. Слот №4")
        print("")
        print("14. Сбросить прогресс всех сохранений")
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
            print("Вы уверены?")
            print("")
            print("1. Да 2. Нет")
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