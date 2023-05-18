# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Player = Dangeon_Action_Player_Conqueror("Олег", "Красивый парень", [(4334,  "onehand", "hand", "Потрёпаный меч", "Весьма старый и сильно притупившийся меч из железа", 1), (1231,  "tissue", "boots", "Ботики из старой кожи", "Лучше, чем ничего", 1)], [(3221,  "onehand", "hand", "Старые штаны", "Старые штаны, покрытые пылью и какими-то липкими нитками", 1), (2,  "tissue", "boots", "Ботики", "Ботнки из обрывков какой-то ткани", 1), (3,  "tissue", "leggs", "Штаны", "Потрёпанные тканевые штаны. Во многих местах видны заплатки", 1)], 100)

Player.BodyChangeMelee(4334)
Player.BodyChangeBoots(1231)
Player.BodyChangeLeggs(3221)

Player.InventoryAdd((4334,  "onehand", "hand", "Желеный меч", "Железный меч в неплохом состоянии", 1))

print(Player.InventoryOutput())
print(Player.BodyOutput())

i = input()