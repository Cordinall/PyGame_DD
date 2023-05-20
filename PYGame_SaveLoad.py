# -*- coding: cp1251 -*-
from Dangeon_Room import *
import json
import random

def StoryMode_Save(Game_CurrentStoryPart, Player_Ex):

    StoryMode_DataToSave = {
        "Player": Player_Ex,
        "Game_CurrentStoryPart": Game_CurrentStoryPart
        }

    with open('SaveLoad\StoryMode\StoryMode_SavedData.json', 'w') as SavingFile:
        SavingFile.write(json.dumps(StoryMode_DataToSave))

def StoryMode_Load():

    with open('SaveLoad\StoryMode\StoryMode_SavedData.json') as LoadedFile:
        StoryMode_DataToLaod_JSON = LoadedFile.read()
        StoryMode_DataToLaod = json.loads(StoryMode_DataToLaod_JSON)

        Player_Ex = StoryMode_DataToLaod["Player"]
        Player_Ex[3][0] = tuple(Player_Ex[3][0])
        Player_Ex[3][1] = tuple(Player_Ex[3][1])
        Player_Ex[3][2] = tuple(Player_Ex[3][2])
        Player_Ex[3][3] = tuple(Player_Ex[3][3])
        Player_Ex[3][4] = tuple(Player_Ex[3][4])
        Player_Ex[3][5] = tuple(Player_Ex[3][5])
        Game_CurrentStoryPart = int(StoryMode_DataToLaod["Game_CurrentStoryPart"])

        return [Game_CurrentStoryPart, Player_Ex]

def UnlimitMode_Save(SlotNum, Dangeon_difficult, Player_Ex):

    UnlimitMode_DataToSave = {
        "Player": Player_Ex,
        "Dangeon_difficult": Dangeon_difficult
        }

    with open(f'SaveLoad\\UnlimitMode\\UnlimitMode_SavedData_{SlotNum}.json', 'w') as SavingFile:
        SavingFile.write(json.dumps(UnlimitMode_DataToSave))

def UnlimitMode_Load(SlotNum):

    with open(f'SaveLoad\\UnlimitMode\\UnlimitMode_SavedData_{SlotNum}.json') as LoadedFile:
        StoryMode_DataToLaod_JSON = LoadedFile.read()
        StoryMode_DataToLaod = json.loads(StoryMode_DataToLaod_JSON)

        Player_Ex = StoryMode_DataToLaod["Player"]
        Player_Ex[3][0] = tuple(Player_Ex[3][0])
        Player_Ex[3][1] = tuple(Player_Ex[3][1])
        Player_Ex[3][2] = tuple(Player_Ex[3][2])
        Player_Ex[3][3] = tuple(Player_Ex[3][3])
        Player_Ex[3][4] = tuple(Player_Ex[3][4])
        Player_Ex[3][5] = tuple(Player_Ex[3][5])
        Dangeon_difficult = StoryMode_DataToLaod["Dangeon_difficult"]

        return [Dangeon_difficult, Player_Ex]


