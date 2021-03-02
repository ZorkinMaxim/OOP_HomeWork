class Title:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"-= {self.name.upper()} =-"

t1 = Title("Programming in Python 3")

print(t1)
