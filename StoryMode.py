# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random
from StoryMode_Part1 import *

def StoryMode(Game_CurrentStoryPart, Player_En):

    Player = Player_En

    Game_CurrentStoryPart = Game_CurrentStoryPart

    match Game_CurrentStoryPart:
        case 0:
            StoryMode_Part1(Player)