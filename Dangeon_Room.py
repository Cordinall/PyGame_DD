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

        print(self.__Readtxt(f"Dangeon\Gen\Bioms\Stone_room_{self.__room_biome}.txt"))

        print(self.__Readtxt(f"Dangeon\Gen\Size\Size_{self.__room_size}.txt"))
        
class Dangeon_Room_Action_Chest:

    def __init__(self, Chest_size, Chest_type, Chest_treasure_type, Chest_treasure_item_stat):
        self.__chest_size = Chest_size
        self.__chest_type = Chest_type
        self.__chest_treasure_type = Chest_treasure_type
        self.__chest_treasure_item_stat = Chest_treasure_item_stat

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

        print(self.__Readtxt(f"Dungeon_Active\Gen\Chest\Size\Size_{self.__chest_size}.txt"))

        print(self.__Readtxt(f"Dungeon_Active\Gen\Chest\Type\Type_{self.__chest_type}.txt"))

    def ItemGeneration(self):

        Item = Dangeon_Items()
        
        if self.__chest_treasure_type == 0:
            Melee_name_rnd = random.randint(1,5)
            Melee_name = self.__Readtxt(f"Items\Melee\\x0{Melee_name_rnd}.txt")
            Melee_type = self.__Readtxt(f"Items\Melee\\x0{Melee_name_rnd + 200}.txt")
            Melee_story = self.__Readtxt(f"Items\Melee\\x0{Melee_name_rnd + 100}.txt")
            Melee_dmg = self.__chest_treasure_item_stat

            return Item.MeleeGeneration(Melee_name, Melee_type, Melee_story, Melee_dmg)

        elif self.__chest_treasure_type == 1:
            Boots_name_rnd = random.randint(1,2)
            Boots_name = self.__Readtxt(f"Items\Boots\\x0{Boots_name_rnd}.txt")
            Boots_type = self.__Readtxt(f"Items\Boots\\x0{Boots_name_rnd + 200}.txt")
            Boots_story = self.__Readtxt(f"Items\Boots\\x0{Boots_name_rnd + 100}.txt")
            Boots_def = self.__chest_treasure_item_stat

            return Item.BootsGeneration(Boots_name, Boots_type, Boots_story, Boots_def)

        elif self.__chest_treasure_type == 2:
            Leggs_name_rnd = random.randint(1,2)
            Leggs_name = self.__Readtxt(f"Items\Leggs\\x0{Leggs_name_rnd}.txt")
            Leggs_type = self.__Readtxt(f"Items\Leggs\\x0{Leggs_name_rnd + 200}.txt")
            Leggs_story = self.__Readtxt(f"Items\Leggs\\x0{Leggs_name_rnd + 100}.txt")
            Leggs_def = self.__chest_treasure_item_stat

            return Item.LeggsGeneration(Leggs_name, Leggs_type, Leggs_story, Leggs_def)

        elif self.__chest_treasure_type == 3:
            Chest_name_rnd = random.randint(1,2)
            Chest_name = self.__Readtxt(f"Items\Chest\\x0{Chest_name_rnd}.txt")
            Chest_type = self.__Readtxt(f"Items\Chest\\x0{Chest_name_rnd + 200}.txt")
            Chest_story = self.__Readtxt(f"Items\Chest\\x0{Chest_name_rnd + 100}.txt")
            Chest_def = self.__chest_treasure_item_stat

            return Item.ChestGeneration(Chest_name, Chest_type, Chest_story, Chest_def)

        elif self.__chest_treasure_type == 4:
            Arms_name_rnd = random.randint(1,2)
            Arms_name = self.__Readtxt(f"Items\Arms\\x0{Arms_name_rnd}.txt")
            Arms_type = self.__Readtxt(f"Items\Arms\\x0{Arms_name_rnd + 200}.txt")
            Arms_story = self.__Readtxt(f"Items\Arms\\x0{Arms_name_rnd + 100}.txt")
            Arms_def = self.__chest_treasure_item_stat

            return Item.ArmsGeneration(Arms_name, Arms_type, Arms_story, Arms_def)

        elif self.__chest_treasure_type == 5:
            Head_name_rnd = random.randint(1,2)
            Head_name = self.__Readtxt(f"Items\Head\\x0{Head_name_rnd}.txt")
            Head_type = self.__Readtxt(f"Items\Head\\x0{Head_name_rnd + 200}.txt")
            Head_story = self.__Readtxt(f"Items\Head\\x0{Head_name_rnd + 100}.txt")
            Head_def = self.__chest_treasure_item_stat

            return Item.HeadGeneration(Head_name, Head_type, Head_story, Head_def)


    def ItemGive(self, Item_body, Item_name, Item_type, Item_story, Item_def):

        Item = Dangeon_Items()

        if Item_body == 0:
            return Item.MeleeGeneration(Item_name, Item_type, Item_story, Item_def)
        elif Item_body == 1:
            return Item.BootsGeneration(Item_name, Item_type, Item_story, Item_def)
        elif Item_body == 2:
            return Item.LeggsGeneration(Item_name, Item_type, Item_story, Item_def)
        elif Item_body == 3:
            return Item.ChestGeneration(Item_name, Item_type, Item_story, Item_def)
        elif Item_body == 4:
            return Item.ArmsGeneration(Item_name, Item_type, Item_story, Item_def)
        elif Item_body == 5:
            return Item.HeadGeneration(Item_name, Item_type, Item_story, Item_def)


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

        # 0 ����� � ���� - ����, 1 - �������, 2 - �����, 3 - ����, 4 - ����, 5 - ������

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

            if i[2] != "hand":
                continue

            if i[0] == Melee_id:

                self.__player_inventory.append(self.__player_body[0])
                self.__player_body[0] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeBoots(self, Boots_id):

        for i in self.__player_inventory:

            if i[2] != "boots":
                continue

            if i[0] == Boots_id:

                self.__player_inventory.append(self.__player_body[1])
                self.__player_body[1] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeLeggs(self, Leggs_id):

        for i in self.__player_inventory:

            if i[2] != "leggs":
                continue

            if i[0] == Leggs_id:

                self.__player_inventory.append(self.__player_body[2])
                self.__player_body[2] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeChest(self, Chest_id):

        for i in self.__player_inventory:

            if i[2] != "chest":
                continue

            if i[0] == Chest_id:

                self.__player_inventory.append(self.__player_body[3])
                self.__player_body[3] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeArms(self, Hands_id):

        for i in self.__player_inventory:

            if i[2] != "arms":
                continue

            if i[0] == Hands_id:

                self.__player_inventory.append(self.__player_body[4])
                self.__player_body[4] = i
                self.__player_inventory.remove(i)
                
    def BodyChangeHead(self, Head_id):

        for i in self.__player_inventory:

            if i[2] != "head":
                continue

            if i[0] == Head_id:

                self.__player_inventory.append(self.__player_body[5])
                self.__player_body[5] = i
                self.__player_inventory.remove(i)

    def BodyOutput(self):

        return self.__player_body
                
    def InventoryAdd(self, Item):
        
        self.__player_inventory.append(Item)
        
    def InventoryDel(self, Item_id):
        
        for i in self.__player_inventory:
            
            if i[0] == Item_id:
                
                self.__player_inventory.remove(i)

    def InventoryOutput(self):

        return self.__player_inventory
        
    def NameChange(self, Player_name):
        
        self.__player_name = Player_name

    def NameOutPut(self):

        return self.__player_name
        
    def StoryChange(self, Player_story):
        
        self.__player_story = Player_story

    def StoryOutPut(self):

        return self.__player_story
        
    def HpVis(self):

        return self.__player_hp

    def HpReduction(self, Damage):

        self.__player_hp -= Damage

    def HpAdd(self, Heal):

        self.__player_hp += Heal

    def DamageOutPut(self):

        return self.__player_body[0][5]

    def BootsDefOutPut(self):

        return self.__player_body[1][5]

    def LeggsDefOutPut(self):

        return self.__player_body[2][5]

    def ChestDefOutPut(self):

        return self.__player_body[3][5]

    def ArmsDefOutPut(self):

        return self.__player_body[4][5]

    def HeadDefOutPut(self):

        return self.__player_body[5][5]
