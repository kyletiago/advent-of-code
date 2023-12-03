## Please ignore how straight ugly my code is LOL

class Game:
    def __init__(self, id):
        self.id = id
        self.red = 0 
        self.green = 0
        self.blue = 0
        self.isValid = True
    
    def addRed(self, toAddRed):
        self.red = toAddRed

    def addGreen(self, toAddGreen):
        self.green = toAddGreen

    def addBlue(self, toAddBlue):
        self.blue = toAddBlue

    def isGameValid(self, wordsOfWisdom):
        self.isValid = wordsOfWisdom



def main():
    f = open('input.txt',"r")
    gameList = []
    n = 1
    sum = 0
    powerSum = 0

    for line in f:
        tmpGame = Game(n)

        semiColonSplit = line.split(':',1)[1].strip()
        wholeGame = semiColonSplit.split(';')
        token = [[x.strip() for x in game.split(',')] for game in wholeGame]

        for i in token:
            for g in i:
                
                if "red" in g:
                    if int(g[:2]) > 12:
                        tmpGame.isGameValid(False)
                    
                    if int(g[:2]) > tmpGame.red:
                        tmpGame.addRed(int(g[:2]))

                if "green" in g:
                    if int(g[:2]) > 13:
                        tmpGame.isGameValid(False)
                    
                    if int(g[:2]) > tmpGame.green:
                        tmpGame.addGreen(int(g[:2]))
                if "blue" in g:
                    if int(g[:2]) > 14:
                        tmpGame.isGameValid(False)

                    if int(g[:2]) > tmpGame.blue:
                        tmpGame.addBlue(int(g[:2]))

        gameList.append(tmpGame)
        n+=1

    for j in gameList:
        if (j.isValid):
            sum += j.id
        powerSum += j.red * j.green * j.blue

main()