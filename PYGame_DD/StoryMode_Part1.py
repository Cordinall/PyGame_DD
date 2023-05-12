# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

def StoryMode_Part1():

    for i in range(50):
        print("")


    Sex = ""
    Name = ""
    Story = ""

    print("Вы находитесь на просторной поляне, края которой тянутся вдаль, за пределы вашего обзора.")
    print("Воздух пахнет свежей зеленью, а кожу греют яркие лучи солнца.\n")

    print("Приятный голос, звучащий откуда-то сверху говорит:")
    Sex = input(" - Кто ты?\n")

    if Sex == "1":
        Sex = "Мужчина. "
    elif Sex == "2":
        Sex = "Женщина. "
    elif Sex == "3":
        Sex = "?. "
    elif Sex == "7000000":
        Sex = "Думатель. "

    Name = input(" - Как тебя зовут?\n")
    Story = input(" - Зачем ты здесь?\n")
    
    print(f" - Ты - {Sex} {Name}, {Story}?")
    