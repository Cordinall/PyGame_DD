# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random
from StoryMode_Part1 import *

def StoryMode():

    Game_storystage = 0

    match Game_storystage:

        case 0:

            print("=====================================================")
            print("Рекомендации: прохождение ночью, композиция The Fire Is Gone в качестве фона.")
            print("=====================================================\n")

            StoryMode_Part1()