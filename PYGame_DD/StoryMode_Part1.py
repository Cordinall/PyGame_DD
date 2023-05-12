# -*- coding: cp1251 -*-
from Dangeon_Room import *
import random

def StoryMode_Part1():

    for i in range(50):
        print("")


    Sex = ""
    Name = ""
    Story = ""

    print("�� ���������� �� ���������� ������, ���� ������� ������� �����, �� ������� ������ ������.")
    print("������ ������ ������ �������, � ���� ����� ����� ���� ������.\n")

    print("�������� �����, �������� ������-�� ������ �������:")
    Sex = input(" - ��� ��?\n")

    if Sex == "1":
        Sex = "�������."
    elif Sex == "2":
        Sex = "�������."
    elif Sex == "3":
        Sex = "?."
    elif Sex == "7000000":
        Sex = "��������."

    Name = input(" - ��� ���� �����?\n")
    Story = input(" - ����� �� �����?\n")
    
    print(f" - �� - {Sex} {Name}, {Story}?")
    