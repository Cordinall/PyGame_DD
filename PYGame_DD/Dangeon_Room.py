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

    def VisualDeath(self):

        print(self.__Readtxt(f"Dungeon_Active\Gen\Enemy\Enemy_death_{self.__enemy_name}.txt"))

    def DamageDeal(self):

        return self.__enemy_dmg

    def HpAdd(self, HpToAdd):
    
        self.__enemy_hp += HpToAdd
    
    def HpReduction(self, Damage):

        self.__enemy_hp -= Damage

    def HpVis(self):

        return self.__enemy_hp


class Dangeon_Action_Player_Conqueror:

    def __init__(self, Player_name, Player_story, Player_inventory, Player_body, Player_hp):
        
        self.__player_name = Player_name
        self.__player_story = Player_story
        self.__player_inventory = Player_inventory
        self.__player_body = Player_body
        self.__player_hp = Player_hp

        # 0 ianoi a aiae - ieee i?o?ea, 1 - aioeiee, 2 - iiae, 3 - oaei, 4 - ?oee, 5 - aieiaa

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

    def VisualPresentation(self):

        print(self.__player_name)
        print(self.__player_story)

    def BodyChangeMelee(self, Melee_id):

        for i in self.__player_inventory:

            if i[0] == Melee_id:

                self.__player_inventory.append(self.__player_body[0])
                self.__player_body[0] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeBoots(self, Boots_id):

        for i in self.__player_inventory:

            if i[0] == Boots_id:

                self.__player_inventory.append(self.__player_body[1])
                self.__player_body[1] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeLeggs(self, Leggs_id):

        for i in self.__player_inventory:

            if i[0] == Leggs_id:

                self.__player_inventory.append(self.__player_body[2])
                self.__player_body[2] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeChest(self, Chest_id):

        for i in self.__player_inventory:

            if i[0] == Chest_id:

                self.__player_inventory.append(self.__player_body[3])
                self.__player_body[3] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeHands(self, Hands_id):

        for i in self.__player_inventory:

            if i[0] == Hands_id:

                self.__player_inventory.append(self.__player_body[4])
                self.__player_body[4] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeHead(self, Head_id):

        for i in self.__player_inventory:

            if i[0] == Head_id:

                self.__player_inventory.append(self.__player_body[5])
                self.__player_body[5] = i
                self.__player_inventory.remove(i)
                
    def InventoryAdd(self, Item):
        
        self.__player_inventory.append(Item)
        
    def InventoryDel(self, Item_id):
        
        for i in self.__player_inventory:
            
            if i[0] == Item_id:
                
                self.__player_inventory.remove(i)
        
    def NameChange(self, Player_name):
        
        self.__player_name = Player_name
        
    def StoryChange(self, Player_story):
        
        self.__player_story = Player_story
        
    def HpVis(self):

        return self.__player_hp

    def HpReduction(self, Damage):

        self.__player_hp -= Damage