# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

Player = Dangeon_Room_Action_Player("����", "�������� ������", [(1,  "onehand", "hand", "��������� ���", "������ ������ � ������ ������������� ��� �� ������", 1)], [(1,  "onehand", "hand", "����", "������ ����", 1)], 100)

Player.BodyAddMelee("��������� ���")

i = input()