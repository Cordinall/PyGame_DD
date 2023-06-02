# -*- coding: cp1251 -*-
import random
from Dangeon_Guardian import *

def Enemy_randomadd():

    enemy_name = random.choice("Мечник", "Танк", "Сильвер", "Минион")
    
    if enemy_name == "Мечник":
        enemy_hp = 5
        enemy_dmg = 10
    elif enemy_name == "Танк":
        enemy_hp = 10
        enemy_dmg = 5
    elif enemy_name == "Сильвер":
        enemy_hp = 7
        enemy_dmg = 6
    elif enemy_name == "Минион":
        enemy_hp = 3
        enemy_dmg = 2

    enemy_list = [enemy_name, enemy_hp, enemy_dmg]

    return enemy_list

def Enemy_add(Enemy_name, Enemy_hp, Enemy_dmg):

    return [Enemy_name, Enemy_hp, Enemy_dmg]