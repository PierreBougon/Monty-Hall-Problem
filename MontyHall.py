import time
import random

# Doors code => 0 is goat 1 is car 3 is eliminatedDoor

WITHOUT_CHANGEMENT = 0
WITH_CHANGEMENT = 1

winWITH = 0
loseWITH = 0
totWITH = 0
winWITHOUT = 0
loseWITHOUT = 0
totWITHOUT = 0

def printStats():
    averageWITH = -1
    averageWITHOUT = -1
    if (totWITH != 0):
        averageWITH = winWITH / totWITH
    if (totWITHOUT != 0):
        averageWITHOUT = winWITHOUT / totWITHOUT
    print("\rAverage with door changement : " + str(averageWITH * 100) + "% Average with no door changement : " + str(averageWITHOUT * 100) + "%", end='', flush=True)



def run(FLAG):
    global WITHOUT_CHANGEMENT, WITH_CHANGEMENT, winWITH, loseWITH, totWITH, winWITHOUT, loseWITHOUT, totWITHOUT
    winDoor = random.randint(0, 2)
    doors = [0, 0, 0]
    doors[winDoor] = 1
    pickDoor = random.randint(0, 2)
    eliminatedDoor = 0
    while (doors[eliminatedDoor] != 3):
        eliminatedDoor = (pickDoor + random.randint(1, 2)) % 3
        if (doors[eliminatedDoor] != 1):
            doors[eliminatedDoor] = 3
    if (FLAG == WITH_CHANGEMENT):
        totWITH += 1
        pickDoor = (pickDoor + 1) % 3
        if (doors[pickDoor] == 3):
            pickDoor = (pickDoor + 1) % 3
        if (doors[pickDoor] == 1):
            winWITH += 1
        else:
            loseWITH += 1
    else:
        totWITHOUT += 1
        if (doors[pickDoor] == 1):
            winWITHOUT += 1
        else:
            loseWITHOUT += 1

if __name__ == "__main__":
    random.seed(time.time())
    for i in range(0, 1000000):
        run(WITH_CHANGEMENT)
        printStats()
    for i in range(0, 1000000):
        run(WITHOUT_CHANGEMENT)
        printStats()
