import pandas as pd
import numpy as np
import random
import locale
import matplotlib.pyplot as plt
color = ''
spaces = []
d1 = 0
d2 = 0



ut = True

u = input('should both utilities be owned by the same person? ')

if(u == 'yes'or u == 'Yes'):
    ut = True
else:
    ut = False
class MakeSpace():
    def __init__(self, name, color, landed, rent,money):
        self.name = name
        self.color = color
        self.landed = 0
        self.rent = 0
        self.money = 0

def createSpaces():
    x = 0

    def assignNames(x):
        names = {
            0: "GO",
            1: "Mediterranean Avenue",
            2: "Community chest",
            3: "Baltic Avenue",
            4: 'Income Tax',
            5: 'Reading Railroad',
            6: 'Oriental Avenue',
            7: 'Chance',
            8: 'Vermont Avenue',
            9: 'Connecticut Avenue',
            10: 'Jail',
            11: "St.Charles Place",
            12: "Electric Company",
            13: 'States Avenue',
            14: 'Virginia Avenue',
            15: 'Pennsylvania Railroad',
            16: 'St James Place',
            17: 'Community Chest',
            18: 'Tennessee Avenue',
            19: 'New York Avenue',
            20: 'Free Parking',
            21: 'Kentucky Avenue',
            22: 'Chance',
            23: 'Indiana Avenue',
            24: 'Illinois Avenue',
            25: 'B & O Railroad',
            26: 'Atlantic Avenue',
            27: 'Ventnor Avenue',
            28: 'Water Works',
            29: 'Marvin Gardens',
            30: 'Go to Jail',
            31: 'Pacific Avenue',
            32: 'North Carolina Avenue',
            33: 'Community Chest',
            34: 'Pennsylvania Avenue',
            35: 'Short Line Railroad',
            36: 'Chance',
            37: 'Park Place',
            38: 'Luxury Tax',
            39: 'Boardwalk',
        }

        return names.get(x, "nothing")

    def assignColors(x):
        colors = {
            0: "N/A",
            2: "N/A",
            4: "N/A",
            7: "N/A",
            10: 'N/A',
            17: 'N/A',
            20: 'N/A',
            22: 'N/A',
            30: 'N/A',
            33: 'N/A',
            36: 'N/A',
            38: 'N/A',
            1: 'Brown',
            3: 'Brown',
            5: 'Railroad',
            15: "Railroad",
            25: 'Railroad',
            35: 'Railroad',
            6: 'Light Blue',
            8: 'Light Blue',
            9: 'Light Blue',
            11: "Pink",
            13: 'Pink',
            14: 'Pink',
            12: 'Utility',
            28: 'Utility',
            16: 'Orange',
            18: 'Orange',
            19: 'Orange',
            21: 'Red',
            23: 'Red',
            24: 'Red',
            26: 'Yellow',
            27: 'Yellow',
            29: 'Yellow',
            31: 'Green',
            32: "Green",
            34: "Green",
            37: 'Dark Blue',
            39: "Dark Blue"

        }

        return colors.get(x, "nothing")

    def assignRents(x):

        rents = {
            0: [0],
            2: [0],
            4: [0],
            7: [0],
            10: [0],
            17: [0],
            20: [0],
            22: [0],
            30: [0],
            33: [0],
            36: [0],
            38: [0],
            1: [2, 10, 30, 90,160,250],
            3: [4,20,60,180,320,450],
            5: [25,50,100,200],
            15: [25,50,100,200],
            25: [25,50,100,200],
            35: [25,50,100,200],
            6: [6,30,90,270,400,550],
            8: [6,30,90,270,400,550],
            9: [8,40,100,300,450,625],
            11: [10,50,150,450,625,750],
            13: [10,50,150,450,625,750],
            14: [12,60,180,500,700,900],
            12: [4],
            28: [4],
            16: [14,70,200,550,750,950],
            18: [14,70,200,550,750,950],
            19: [16,80,220,600,800,975],
            21: [18,90,250,700,875,1050],
            23: [18,90,250,700,875,1050],
            24: [20,100,300,750,925,1100],
            26: [22,110,330,800,975,1150],
            27: [22,110,330,800,975,1150],
            29: [24,120,360,850,1025,1200],
            31: [26,130,390,900,1100,1275],
            32: [26,130,390,900,1100,1275],
            34: [28,150,450,1000,1200,1400],
            37: [35,175,500,1100,1300,1500],
            39: [50,200,600,1400,1700,2000],

            }

        return rents.get(x, "nothing")

    while (x < 40):
        name = assignNames(x)
        color = assignColors(x)
        rent = assignRents(x)
        spaces.append(MakeSpace(name, color, 0,0,0))
        spaces[x].rent = rent

        x = x + 1

def roll():
    d1 = random.randint(0, 6)
    d2 = random.randint(0, 6)
    #print('number is ' + str(d1+d2))
    return d1+d2



def testRun(c,x,u):
    space = 0
    timesLandedOnUtility = 0
    t = 0
    while (t < c):
        total = roll()

        temp = 0
        space += total
        if (space >= 40):
            space -= 40

        if spaces[space].color == 'Utility':
            #print('IN UTILITY')

            if(u):
                spaces[space].money += (total * 10)
                spaces[space].landed += total

            else:
                spaces[space].money += (total*4)
                spaces[space].landed += total
            timesLandedOnUtility += 1
            #print('utilty space money '+str(spaces[space].money))

        else:
            spaces[space].landed += 1
            temp = x
            if (len(spaces[space].rent) <= x):
                x = len(spaces[space].rent) - 1
            spaces[space].money += spaces[space].landed * spaces[space].rent[x]
            x = temp
        t += 1
    for space in spaces:
        if space.color == 'Utility':
            space.landed = round(space.landed/timesLandedOnUtility)

def printValues(h):
    p = 0
    print('h is ' + str(h))
    while(p<10):

        print('p is ' +str(p))
        testRun(10000, h, ut)
        p+=1
    for space in spaces:
        temp = h
        if (space.color!= 'Utility'):
            if (len(space.rent) <= h):
                h = len(space.rent) - 1
           # print('Before: ' +str(space.money))
            space.money = round(space.money/10000)
            #print('after ' + str(space.money))

            if (space.rent[h] != 0):
                space.landed = round(space.money / space.rent[h])
        else:
            h = len(space.rent) - 1
           # print('Before utility'+ str(space.money))
            #print('utility roll: '+ str(space.landed))
            space.money = round(space.money/space.landed)

        if (space.color != 'Utility'):
            print('name is: ' + space.name + ',' + ' color is: ' + space.color + ', times landed on: ' + str(space.landed) + ' rent per night is ' + str(space.rent[h]) + ', money from rent: $' + f"{space.money:,}")
        else:
            print('name is: ' + space.name + ',' + ' color is: ' + space.color + ', average roll: ' + str(space.landed) + ' rent per night is ' + str(space.rent[h]) + ', money from rent: $'+f'{space.money:,}')
        h = temp
    """for space in spaces:
        print('name is: ' + space.name + ' color is: ' + space.color) """
def makePlot(h):
    printValues(h)
    landedOnNa = 0
    landedOnBrown = 0
    brownRent = 0
    landedOnLightBlue = 0
    lightBlueRent = 0
    pinkRent = 0
    landedOnPink = 0
    utilityRent = 0
    landedOnUtility = 0
    orangeRent = 0
    landedOnOrange = 0
    redRent = 0
    landedOnRed = 0
    yellowRent = 0
    landedOnYellow = 0
    greenRent = 0
    landedOnGreen = 0
    darkBlueRent = 0
    landedOnDarkBlue = 0
    landedOnRailroad = 0
    railRoadRent = 0
    t = 0
    houses = h
    for space in spaces:
        print('before h is ' + str(h))
        temp = h
        if (len(space.rent) <= h):
            h = len(space.rent) - 1
        if space.color == 'N/A':
            landedOnNa += space.landed
        elif space.color == 'Brown':
            landedOnBrown +=  space.landed
            brownRent = brownRent + space.money
        elif space.color == 'Railroad':
            landedOnRailroad += space.landed
            railRoadRent +=  space.money
        elif space.color == 'Light Blue':
            landedOnLightBlue = landedOnLightBlue + space.landed
            lightBlueRent = lightBlueRent + space.money
        elif space.color == 'Pink':
            landedOnPink = landedOnPink + space.landed
            pinkRent = pinkRent + space.money
        elif space.color == 'Orange':
            landedOnOrange = landedOnOrange + space.landed
            orangeRent = orangeRent + space.money
        elif space.color == 'Red':
            landedOnRed = landedOnRed + space.landed
            redRent = redRent + space.money
        elif space.color == "Utility":
            landedOnUtility += space.landed
            utilityRent +=space.money
        elif space.color == 'Yellow':
            landedOnYellow = landedOnYellow + space.landed
            yellowRent = yellowRent + space.money
        elif space.color == 'Green':
            landedOnGreen = landedOnGreen + space.landed
            greenRent = greenRent + space.money
        elif space.color == 'Dark Blue':
            landedOnDarkBlue = landedOnDarkBlue + space.landed
            darkBlueRent = darkBlueRent +space.money
        h = temp
        print('h is' + str(h))
    print('Landed on Non colored spaces: ' + str(landedOnNa) + ' times.')
    print('Landed on Brown spaces ' + str(landedOnBrown) + ' times. Rent: $' + f"{brownRent:,}")
    print('Landed on Light Blue spaces ' + str(landedOnLightBlue) + ' times. Rent: $' + f"{lightBlueRent:,}")
    print('Landed on Pink spaces ' + str(landedOnPink) + ' times. Rent: $' + f"{pinkRent:,}")
    print('avg roll was ' + str(landedOnUtility) + '. Rent: $' + f"{utilityRent:,}")
    print('Landed on Orange ' + str(landedOnOrange) + ' times. Rent: $' + f"{orangeRent:,}")
    print('Landed on Red ' + str(landedOnRed) + ' times. Rent: $' + f"{redRent:,}")
    print('Landed on Yellow ' + str(landedOnYellow) + ' times. Rent: $' + f"{yellowRent:,}")
    print('Landed on Green ' + str(landedOnGreen) + ' times. Rent: $' + f"{greenRent:,}")
    print('Landed on Dark Blue:' + str(landedOnDarkBlue) + ' times. Rent: $' + f"{darkBlueRent:,}")
    print('Landed on Railroads ' + str(landedOnRailroad) + ' times: Rent: $'+ f"{railRoadRent:,}")

    colors = ['Brown','Light Blue', 'Pink','Utilities', 'Orange', 'Red', "Yellow", 'Green', 'Dark Blue','Railroads']
    colorMoney = [brownRent, lightBlueRent, pinkRent, utilityRent, orangeRent, redRent, yellowRent, greenRent,
                      darkBlueRent,railRoadRent]

    index = np.arange(len(colors))
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.bar(index, colorMoney)
    plt.xlabel('Color', fontsize=5)
    plt.ylabel('Money made ', fontsize=4)

    plt.xticks(index, colors, fontsize=6, rotation=30)

    plt.title('Average money made per color when simulating 10k rolls 10 times on a monopoly board  with ' + str(houses) + ' houses.',fontsize =8 )
    plt.show()
createSpaces()
printValues(0)
printValues(5)
makePlot(0)
makePlot(5)