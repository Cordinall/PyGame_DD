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
