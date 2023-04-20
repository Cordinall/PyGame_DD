# -*- coding: cp1251 -*-

from Dangeon_Items import *

class Dangeon_Room_NonAction:
    
    def __init__(self, room_size, room_biome):
        self.__room_size = room_size
        self.__room_biome = room_biome

    # Room_size = 1 or 2 or 3. 1 - little room, 2 - medium, 3 - high.
    # Room_biome = 1 or 2 or 3 or 4 - 1 - stone room, 2 - green stone room, 3 - bloody stone room, 4 - bloody green stone room

    def __Readtxt(self, adr):
      ans = ""
      for i in open(adr, encoding="utf-8"):
        endans = i.strip()
        if endans == "":
            ans = ans + endans + "\n" + "\n"
            continue
        else:
            ans = ans + endans + "\n"

      return ans

    def VisualGeneration(self):

        match self.__room_size:
            case 1:
                print(self.__Readtxt("Dangeon\Gen\Size\Size_1.txt"))
            case 2:
                print(self.__Readtxt("Dangeon\Gen\Size\Size_2.txt"))
            case 3:
                print(self.__Readtxt("Dangeon\Gen\Size\Size_3.txt"))

        match self.__room_biome:
            case 1:
                print(self.__Readtxt("Dangeon\Gen\Bioms\Stone_room_1.txt"))
            case 2:
                print(self.__Readtxt("Dangeon\Gen\Bioms\Stone_room_2.txt"))
            case 3:
                print(self.__Readtxt("Dangeon\Gen\Bioms\Stone_room_3.txt"))

        
class Dangeon_Room_Action_Chest:

    def __init__(self, chest_size, chest_type, chest_treasure_type):
        self.__chest_size = chest_size
        self.__chest_type = chest_type
        self.__chest_treasure = chest_treasure_type

    def __Readtxt(self, adr):
      ans = ""
      for i in open(adr, encoding="utf-8"):
        endans = i.strip()
        if endans == "":
            ans = ans + endans + "\n" + "\n"
            continue
        else:
            ans = ans + endans + "\n"

      return ans

    def VisualGeneraton(self):

        match self.__chest_type:
            case 1:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Type\Type_usual.txt"))
            case 2:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Type\Type_unusual.txt"))
            case 3:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Type\Type_extended.txt"))

        match self.__chest_size:
            case 1:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Size\Size_little.txt"))
            case 2:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Size\Size_middle.txt"))
            case 3:
                print(self.__Readtxt("Dungeon_Active\Gen\Chest\Size\Size_big.txt"))

    def ItemGeneration(self):

        Item = Dangeon_Items()
        Item.RandomGeneration