class Dangeon_Action_Player_Guardian:

    def __init__(self, Player_rooms, Player_money, Player_hp):
        self.__player_rooms = Player_rooms
        self.__player_money = Player_money
        self.__player_hp = Player_hp

    def RoomAdd(self, Room_type, Room_dmg, Room_copasity, Roome_sellvalue, Room_cost):

        self.__player_money -= Room_cost
        self.__player_rooms.append([Room_type, Room_dmg, Room_copasity, Roome_sellvalue])

    def RoomDelete(self, Room_Num):
        Room_Num = Room_Num - 1
        del self.__player_rooms[Room_Num]

    def RoomSell(self, Room_Num):
        Room_Num = Room_Num - 1
        self.__player_money += self.__player_rooms[Room_Num][3]
        del self.__player_rooms[Room_Num]

    def RoomReturn(self, Room_Num):
        Room_Num = Room_Num - 1
        return self.__player_rooms[Room_Num]

    def RoomsReturn(self):
        return self.__player_rooms

    def MoneyAdd(self, Money_ToAdd):
        self.__player_money += Money_ToAdd

    def MoneyReduction(self, Money_ToRed):
        self.__player_money -= Money_ToRed

    def MoneyCheck(self, Money_ToCheck):
        if self.__player_money >= Money_ToCheck:
            return True
        else:
            return False

    def MoneyReturn(self):
        return self.__player_money

    def HpAdd(self, Hp_ToAdd):
        self.__player_hp += Hp_ToAdd

    def HpReduction(self, Hp_ToRed):
        self.__player_hp -= Hp_ToRed

    def HpReturn(self):
        return self.__player_hp