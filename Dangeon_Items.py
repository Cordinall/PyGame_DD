class Dangeon_Items:
    
    def MeleeGeneration(self, Melee_name, Melee_type, Melee_story, Melee_dmg):

        import random

        __Melee_id = random.randint(0, 99999)
        __Melee_type = Melee_type
        __Item_body = "hand"
        __Melee_name = Melee_name
        __Melee_story = Melee_story
        __Melee_dmg = Melee_dmg

        __Melee_statistics_output = ( __Melee_id,  __Melee_type, __Item_body, __Melee_name, __Melee_story, __Melee_dmg)

        return __Melee_statistics_output


    def BootsGeneration(self, Boots_name, Boots_type, Boots_story, Boots_defence):

        import random

        __Boots_id = random.randint(0, 99999)
        __Boots_type = Boots_type
        __Item_body = "boots"
        __Boots_name = Boots_name
        __Boots_story = Boots_story
        __Boots_defence = Boots_defence

        __Boots_statistics_output = ( __Boots_id, __Boots_type, __Item_body, __Boots_name, __Boots_story, __Boots_defence)

        return __Boots_statistics_output


    def LeggsGeneration(self, Leggs_name, Leggs_type, Leggs_story, Leggs_defence):

        import random

        __Leggs_id = random.randint(0, 99999)
        __Leggs_type = Leggs_type
        __Item_body = "leggs"
        __Leggs_name = Leggs_name
        __Leggs_story = Leggs_story
        __Leggs_defence = Leggs_defence

        __Leggs_statistics_output = ( __Leggs_id, __Leggs_type, __Item_body, __Leggs_name, __Leggs_story, __Leggs_defence)

        return __Leggs_statistics_output


    def ChestGeneration(self, Chest_name, Chest_type, Chest_story, Chest_defence):

        import random

        __Chest_id = random.randint(0, 99999)
        __Chest_type = Chest_type
        __Item_body = "chest"
        __Chest_name = Chest_name
        __Chest_story = Chest_story
        __Chest_defence = Chest_defence

        __Chest_statistics_output = ( __Chest_id, __Chest_type, __Item_body, __Chest_name, __Chest_story, __Chest_defence)

        return __Chest_statistics_output


    def ArmsGeneration(self, Arms_name, Arms_type, Arms_story, Arms_defence):

        import random

        __Arms_id = random.randint(0, 99999)
        __Arms_type = Arms_type
        __Item_body = "arms"
        __Arms_name = Arms_name
        __Arms_story = Arms_story
        __Arms_defence = Arms_defence

        __Arms_statistics_output = ( __Arms_id, __Arms_type, __Item_body, __Arms_name, __Arms_story, __Arms_defence)

        return __Arms_statistics_output


    def HeadGeneration(self, Head_name, Head_type, Head_story, Head_defence):

        import random

        __Head_id = random.randint(0, 99999)
        __Head_type = Head_type
        __Item_body = "head"
        __Head_name = Head_name
        __Head_story = Head_story
        __Head_defence = Head_defence

        __Head_statistics_output = ( __Head_id, __Head_type, __Item_body, __Head_name, __Head_story, __Head_defence)

        return __Head_statistics_output