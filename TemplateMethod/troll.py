from fighter import Fighter


class Troll(Fighter):
    def pick_up_weapon(self):
        print("Pick up club")

    def defense_action(self):
        print("Defend with club")

    def move_to_safety(self):
        print("Return to the mountain")
