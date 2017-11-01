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
ANSWER_X = 350


def processNumber(num):
    var = 0
    
def compute():
    var = 0
    
def clear():
    var = 0
    
def mouseClick(event):
    var = 0
    


if __name__ == "__main__":
    
    red = Color(0xFF0000, 1)
    white = Color(0x000000, 0)
    black = Color(0x000000, 1)
    
    background = RectangleAsset(CALC_X, CALC_Y, LineStyle(1, black), white)
    answerBox = RectangleAsset(ANSWER_X, BUTTON_Y, LineStyle(1, black), white)
    button = RectangleAsset(BUTTON_X, BUTTON_Y, LineStyle(1, black), white)
    
    
    
    calc = Sprite(background, (WINDOW_X/2-CALC_X/2, WINDOW_Y/2-CALC_Y/2))
    ans = Sprite(answerBox, (WINDOW_X/2-ANSWER_X/2, BUTTON_Y/2))
    Sprite(button, (calc.x + 10, ans.y + BUTTON_Y + 10))
    App().run()
    
    
    
    
