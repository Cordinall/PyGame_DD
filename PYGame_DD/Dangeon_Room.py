# -*- coding: cp1251 -*-

import random
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

    def __init__(self, Chest_size, Chest_type, Chest_treasure_type, Chest_treasure_weapon_dmg):
        self.__chest_size = Chest_size
        self.__chest_type = Chest_type
        self.__chest_treasure_type = Chest_treasure_type
        self.__chest_treasure_weapon_dmg = Chest_treasure_weapon_dmg

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
        
        if self.__chest_treasure_type == 1:
            Melee_name_rnd = random.randint(1,5)
            Melee_name = self.__Readtxt(f"Items\Melee\\x0{Melee_name_rnd}.txt")
            Melee_type = self.__Readtxt(f"Items\Melee\\x0201.txt")
            Melee_story = self.__Readtxt(f"Items\Melee\\x0{Melee_name_rnd + 100}.txt")
            Melee_dmg = self.__chest_treasure_weapon_dmg

            return Item.MeleeGeneration(Melee_name, Melee_type, Melee_story, Melee_dmg)


class Dangeon_Room_Action_Enemy:

    def __init__(self, Enemy_name, Enemy_dmg, Enemy_hp):
        
        self.__enemy_name = Enemy_name
        self.__enemy_dmg = Enemy_dmg
        self.__enemy_hp = Enemy_hp


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

        print(self.__Readtxt(f"Dungeon_Active\Gen\Enemy\Enemy_present_{1}.txt"))
        print(self.__Readtxt(f"Dungeon_Active\Gen\Enemy\Enemy_name_{self.__enemy_name}.txt"))
        print(self.__Readtxt(f"Dungeon_Active\Gen\Enemy\Enemy_story_{self.__enemy_name}.txt"))

    def DamageDeal(self):

        return self.__enemy_dmg

    def HpAdd(self, HpToAdd):
    
        self.__enemy_hp += HpToAdd
    
    def HpReduction(self, Damage):

        self.__enemy_hp -= Damage