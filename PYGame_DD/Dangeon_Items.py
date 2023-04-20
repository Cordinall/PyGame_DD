class Dangeon_Items:

    
    def SwordGeneration(self, sword_name, sword_story, sword_dmg):

        import random

        __Sword_id = random.randint(0, 99999)
        __Sword_type = "weapon"
        __Sword_name = sword_name
        __Sword_story = sword_story
        __Sword_dmg = sword_dmg

        __Sword_statistics_output = ( __Sword_id,  __Sword_type, __Sword_name, __Sword_story, __Sword_dmg)

        return __Sword_statistics_output
