import random


class Soldier:
    def __init__(self, id, team):
        self.id = id
        self.team = team

    def __str__(self):
        return f"Soldier:{self.id:4}, Team:{self.team:4}"

    def followHero(self, Hero):
        return print(f"Soldier with ID:{self.id} follows Hero with ID:{Hero.id}")


class Hero(Soldier):
    def __init__(self, id, team, level=1):
        Soldier.__init__(self, id, team)
        self.level = level

    def __str__(self):
        return f"Hero:{self.id:2}, Team:{self.team:4}, Level:{self.level:2}"

    def levelUp(self):
        self.level += 1


###############################################################
h1 = Hero(1, "red")
h2 = Hero(2, "blue")

red_team = []
blue_team = []

for s in range(10):
    t = random.randint(1, 2)
    if t == 1:
        red_team.append(Soldier(s + 100, "red"))
    else:
        blue_team.append(Soldier(s + 100, "blue"))

print("----------------------------")
print(f"In Red Team {len(red_team)} soldiers")
print(f"In Blue Team {len(blue_team)} soldiers")
print("----------------------------")

for r in red_team:
    print(r)

for b in blue_team:
    print(b)

if len(red_team) > len(blue_team):
    h1.levelUp()
elif len(red_team) < len(blue_team):
    h2.levelUp()
else:
    pass

print("----------------------------")
print(h1)
print(h2)
print("----------------------------")
Soldier.followHero(red_team[1], h1)
