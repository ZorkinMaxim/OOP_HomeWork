class Box:
    def __init__(self, v):
        self.value = v
    # def setValue(self, v):
    #     self.value = v
    def printIt(self):
        print("This is a Box object!")
        print(">>>", self.value)


##############################################
b1 = Box(100)
b2 = Box(200)

# b1.setValue(100)
# b2.setValue(200)

b1.printIt()
b2.printIt()