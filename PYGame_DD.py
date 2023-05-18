# -*- coding: cp1251 -*-
from Dangeon_Room import *
from StoryMode import *
from ObserverMode import *
from UnlimitMode import *
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
print("Приветствую в игре Dangeon and Dangeon")
print("=====================================================\n")

print("=====================================================")
print("В качестве ввода используйте целочисленные значения.\nИные варианты могут вызвать ошибку.\nПример:")
print("1. Атака\n2. Защита\n")
print("1")
print("=====================================================\n")

ExitMainMenu = 0
while ExitMainMenu == 0:

    print("=====================================================")
    print("Main Menu\n")
    print("     1. Начать новую игру")
    print("     2. Продолжить игру ( в разработке )")
    print("     3. Справочник ( рекомендовано к просмотру )")
    print("     4. Авторы")
    print("     5. Выход")
    print("=====================================================\n")

    Player_answer = input()

    if Player_answer == "1":

        print("=====================================================")
        print("     1. Покоритель ( в разработке )")
        print("     2. Покорённый")
        print("     3. Наблюдатель")
        print("     4. Хранитель ( в разработке )")
        print("")
        print("     5. Назад")
        print("=====================================================\n")

        Player_answer = input()

        if Player_answer == "1":
            StoryMode()
        elif Player_answer == "2":
            EverlastMode()
        elif Player_answer == "3":
            ObserverMode()
        elif Player_answer == "4":
            GuardianMode()
        elif Player_answer == "5":
            continue
        
    elif Player_answer == "2":
        print("В разработке.")
    elif Player_answer == "3":
        print(Readtxt("MainMenu\\Directory.txt"))
    elif Player_answer == "4":
        print(Readtxt("MainMenu\Autors.txt"))
    elif Player_answer == "5":
        break