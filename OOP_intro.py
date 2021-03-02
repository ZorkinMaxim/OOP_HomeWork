# declare template
class Player:
    pass

# create object with this template
def newPlayer(name, hp, avatar):
    player = Player()
    player.name = name
    player.hp = hp
    player.avatar = avatar
    return player

def printPlayer(player):
    print(player.name, player.hp, player.avatar)

#######################################################

p1 = newPlayer('Kinguru99', 70, 'kingu.gif')
p2 = newPlayer('Tiger', 100, 't.gif')

printPlayer(p1)
printPlayer(p2)
