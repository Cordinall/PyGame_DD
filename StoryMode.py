# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random
from StoryMode_Part1 import *
from StoryMode_Part2 import *

def StoryMode(Game_CurrentStoryPart, Player_En):

    Player = Player_En

    Game_CurrentStoryPart = Game_CurrentStoryPart

    ExitMode = 0
    while ExitMode == 0:
        match Game_CurrentStoryPart:
            case 0:
                Exit_list = StoryMode_Part1(Player)
                Player = Exit_list[0]
                ExitMode = Exit_list[1]
                Game_CurrentStoryPart = Exit_list[2]
            case 1:
                Exit_list = StoryMode_Part2(Player)
                Player = Exit_list[0]
                ExitMode = Exit_list[1]
                Game_CurrentStoryPart = Exit_list[2]