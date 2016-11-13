# Goes in MyBot.py

from hlt import *
from networking import *
import util
import random

myID, gameMap = getInit()
sendInit("PBOT")

def move(location, gameMap, myID, border):
    site = gameMap.getSite(location)
    # Anytime we can claim a spot, do so
    all_mine = True
    for d in CARDINALS:
        neighbour_site = gameMap.getSite(location, d)
        if neighbour_site.owner != myID:
            all_mine = False
            if neighbour_site.strength < site.strength:
                return Move(location, d)

    if not all_mine:
        return Move(location, STILL)

    if site.strength < site.production * 3:
        return Move(location, STILL)

    # min_point = random.choice(border)
    min_point = Location(0,0)
    for each in border:
        if each.x > min_point.x and each.y > min_point.y:
            min_point = each

    # util.log(min_distance)
    angle = gameMap.getAngle(location, min_point)
    # util.log(str(location.x) + " " + str(location.y))
    # util.log(str(min_point.x) + " " + str(min_point.y))
    # util.log(angle)
    angle = math.degrees(angle) % (360)
    if angle >= (315) or angle <= (45):
        return Move(location, EAST)
    elif (45) < angle <= (90+45):
        return Move(location, NORTH)
    elif (90+45) < angle <= (180+45):
        return Move(location, WEST)
    else:
        return Move(location, SOUTH)

while True:
    moves = []
    gameMap = getFrame()
    mine = []
    border = []
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x,y)
            if gameMap.getSite(location).owner == myID:
                mine.append(location)

                for d in CARDINALS:
                    neighbour_site = gameMap.getSite(location, d)
                    if neighbour_site.owner != myID:
                        border.append(location)
                        break
    util.log(str([(p.x, p.y) for p in border]), myID)
    for each in mine:
        moves.append(move(each, gameMap, myID, border))

    sendFrame(moves)
