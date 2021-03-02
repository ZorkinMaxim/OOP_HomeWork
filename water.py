class Water:
    def __init__(self, volume, unit = "L"):
        self.volume = volume
        self.unit = unit
    def __str__(self):
        return f"WATER({self.volume}{self.unit})"
    def __len__(self):
        return self.volume
    def __add__(self, other):
        if self.unit == "mL":
            self.volume = self.volume / 1000
        if other.unit == "mL":
            other.volume = other.volume / 1000
        return Water(float(self.volume + other.volume))
    def __sub__(self, other):
        if self.unit == "mL":
            self.volume = self.volume / 1000
        if other.unit == "mL":
            other.volume = other.volume / 1000
        return Water(float(self.volume - other.volume))
    def __gt__(self, other):
        if self.volume > other.volume:
            print("water1 is gt")
        else:
            print("water1 is not gt")
        return self.volume > other.volume
    def __ge__(self, other):
        if self.volume >= other.volume:
            print("water1 is gt or eq")
        else:
            print("water1 is not gt or eq")
        return self.volume >= other.volume
    def __eq__(self, other):
        if self.volume == other.volume:
            print("water1 and water2 is eq")
        else:
            print("water1 and water2 is not eq")
        return self.volume == other.volume
    def __lt__(self, other):
        if self.volume < other.volume:
            print("water1 is less")
        else:
            print("water1 is not less")
        return self.volume < other.volume
    def __le__(self, other):
        if self.volume <= other.volume:
            print("water1 is less or eq")
        else:
            print("water1 is not less or eq")
        return self.volume <= other.volume


##############################################
water1 = Water(500, "L")
water2 = Water(600, "mL")
water3 = Water(500, "mL")

water = water1 + water2 - water3
# print(water1, water2, water3)
print(water)

Water(water1 > water2)
