#Charlie Goodrich
#11/01/17
#calculatorApplet.py - displays a 4-function calculator that executes commands

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 530
CALC_X = 400
CALC_Y = 500
BUTTON_X = 60
BUTTON_Y = 60
ANSWER_X = 380
DIFF = 20



def processNumber(num):
    var = 0
    
def compute():
    var = 0
    
def clear():
    var = 0
    
def mouseClick(event):
    if event.x <= 0:
        kill = 0
    


if __name__ == "__main__":
    
    red = Color(0xFF0000, 1)
    white = Color(0x000000, 0)
    black = Color(0x000000, 1)
    
    background = RectangleAsset(CALC_X, CALC_Y, LineStyle(1, black), white)
    answerBox = RectangleAsset(ANSWER_X, BUTTON_Y, LineStyle(1, black), white)
    button = RectangleAsset(BUTTON_X, BUTTON_Y, LineStyle(1, black), white)
    specialButton = RectangleAsset(BUTTON_X, BUTTON_Y, LineStyle(1, black), red)
    
    #SPRITING ALL THE CALCULATOR STUFF
    calc = Sprite(background, (WINDOW_X/2-CALC_X/2, WINDOW_Y/2-CALC_Y/2))
    ansBox = Sprite(answerBox, (WINDOW_X/2-ANSWER_X/2, BUTTON_Y/2))
    sevenBox = Sprite(button, (calc.x + 10, ansBox.y + BUTTON_Y + DIFF))
    eightBox = Sprite(button, (sevenBox.x + BUTTON_X + DIFF, ansBox.y + BUTTON_Y + DIFF))
    nineBox = Sprite(button, (eightBox.x + BUTTON_X + DIFF, ansBox.y + BUTTON_Y + DIFF))
    divBox = Sprite(specialButton, (nineBox.x + BUTTON_X + 4*DIFF, ansBox.y + BUTTON_Y + DIFF))
    fourBox = Sprite(button, (calc.x + 10, sevenBox.y + BUTTON_Y + DIFF))
    fiveBox = Sprite(button, (fourBox.x + BUTTON_X + DIFF, eightBox.y + BUTTON_Y + DIFF))
    sixBox = Sprite(button, (fiveBox.x + BUTTON_X + DIFF, nineBox.y + BUTTON_Y + DIFF))
    multiBox = Sprite(specialButton, (sixBox.x + BUTTON_X + 4*DIFF, divBox.y + BUTTON_Y + DIFF))
    oneBox = Sprite(button, (calc.x + 10, fourBox.y + BUTTON_Y + DIFF))
    twoBox = Sprite(button, (oneBox.x + BUTTON_X + DIFF, fiveBox.y + BUTTON_Y + DIFF))
    threeBox = Sprite(button, (twoBox.x + BUTTON_X + DIFF, sixBox.y + BUTTON_Y + DIFF))
    minusBox = Sprite(specialButton, (threeBox.x + BUTTON_X + 4*DIFF, multiBox.y + BUTTON_Y + DIFF))
    onBox = Sprite(button, (calc.x + 10, oneBox.y + BUTTON_Y + DIFF))
    zeroBox = Sprite(button, (onBox.x + BUTTON_X + DIFF, twoBox.y + BUTTON_Y + DIFF))
    decimalBox = Sprite(button, (zeroBox.x + BUTTON_X + DIFF, twoBox.y + BUTTON_Y + DIFF))
    plusBox = Sprite(specialButton, (decimalBox.x + BUTTON_X + 4*DIFF, minusBox.y + BUTTON_Y + DIFF))
    equalsBox = Sprite(specialButton, (decimalBox.x + BUTTON_X + 4*DIFF, plusBox.y + BUTTON_Y + DIFF))
    
    App().listenMouseEvent("click", mouseClick)
    App().run()
    
    
    
    
