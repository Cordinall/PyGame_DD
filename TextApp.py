# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Player = Dangeon_Action_Player_Conqueror("����", "�������� ������", [(4334,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 1), (1231,  "tissue", "boots", "������ �� ������ ����", "�����, ��� ������", 1)], [(3221,  "onehand", "hand", "������ �����", "������ �����, �������� ����� � ������-�� ������� �������", 1), (2,  "tissue", "boots", "������", "������ �� �������� �����-�� �����", 1), (3,  "tissue", "leggs", "�����", "���������� �������� �����. �� ������ ������ ����� ��������", 1)], 100)

Player.BodyChangeMelee(4334)
Player.BodyChangeBoots(1231)
Player.BodyChangeLeggs(3221)

Player.InventoryAdd((4334,  "onehand", "hand", "������� ���", "�������� ��� � �������� ���������", 1))

print(Player.InventoryOutput())
print(Player.BodyOutput())

i = input()