import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return f"{self.name} - HP{self.health}"

    def hit(self, damage):
        self.health -= damage

    def heal(self, h_points):
        self.health += h_points


############### 1 #################

w1 = Warrior("Mad_Max")
w2 = Warrior("Vladimir_the_Great")

while w1.health > 0 and w2.health > 0:
    h = random.randint(1, 2)
    h_l = random.randint(3, 4)
    if h == 1:
        Warrior.hit(w1, 20)
        print(f"{w2.name} hit {w1.name}")
        print(w1)
        print(w2)
        print("-----------")
    elif h == 2:
        Warrior.hit(w2, 20)
        print(f"{w1.name} hit {w2.name}")
        print(w1)
        print(w2)
        print("-----------")
    if h_l == 3 and w1.health > 0 and w1.health < 100:
        Warrior.heal(w1, 10)
        print(f"{w1.name} was heald!")
        print(w1)
        print(w2)
        print("-----------")
    elif h_l == 4 and w2.health > 0 and w2.health < 100:
        Warrior.heal(w2, 10)
        print(f"{w2.name} was heald!")
        print(w1)
        print(w2)
        print("-----------")
    if w1.health <= 0:
        print(f"\nWe have a winner!!! {w2.name} wins!")
    elif w2.health <= 0:
        print(f"\nWe have a winner!!! {w1.name} wins!")

############### 2 #################

# warriors = []
# warriors.append(Warrior("Mad_Max"))
# warriors.append(Warrior("Vladimir_the_Great"))
#
# print('Nowww you are going to watch the most exiting battle in the whole history!!!')
#
# while warriors[0].health > 0 and warriors[1].health > 0:
#     hit = random.choice(warriors)
#     if hit == warriors[0]:
#         warriors[0].health -= 20
#         print("-----------")
#     elif hit == warriors[1]:
#         warriors[1].health -= 20
#         print("-----------")
#     for w in warriors:
#         print(w)
#     if warriors[0].health == 0:
#         print(f"\nWe have a winner!!! {warriors[1].name} wins!")
#     elif warriors[1].health == 0:
#         print(f"\nWe have a winner!!! {warriors[0].name} wins!")
