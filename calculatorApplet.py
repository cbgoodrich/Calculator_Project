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
    mouseClick(event)
    if event.x>=sevenBox.x and event.x<=sevenBox.x+BUTTON_X and event.y>=sevenBox.y and event.y<=sevenBox.y+BUTTON_Y:
        print(7)

def mouseClick(event):
    return event.x
    return event.y

if __name__ == "__main__":
    
    #COLORS
    red = Color(0xFF0000, 1)
    white = Color(0x000000, 0)
    black = Color(0x000000, 1)
        
    #CREATING THE BASIS FOR THE CALCULATOR
    background = RectangleAsset(CALC_X, CALC_Y, LineStyle(1, black), white)
    answerBox = RectangleAsset(ANSWER_X, BUTTON_Y, LineStyle(1, black), white)
    button = RectangleAsset(BUTTON_X, BUTTON_Y, LineStyle(1, black), white)
    specialButton = RectangleAsset(BUTTON_X, BUTTON_Y, LineStyle(1, black), red)
    seven = TextAsset("7", fill = black, style = "Bold 24pt Times")
    eight = TextAsset("8", fill = black, style = "Bold 24pt Times")
    nine = TextAsset("9", fill = black, style = "Bold 24pt Times")
    div = TextAsset("/", fill = black, style = "Bold 24pt Times")
    four = TextAsset("4", fill = black, style = "Bold 24pt Times")
    five = TextAsset("5", fill = black, style = "Bold 24pt Times")
    six = TextAsset("6", fill = black, style = "Bold 24pt Times")
    multi = TextAsset("*", fill = black, style = "Bold 24pt Times")
    one = TextAsset("1", fill = black, style = "Bold 24pt Times")
    two = TextAsset("2", fill = black, style = "Bold 24pt Times")
    three = TextAsset("3", fill = black, style = "Bold 24pt Times")
    minus = TextAsset("-", fill = black, style = "Bold 24pt Times")
    on = TextAsset("C", fill = black, style = "Bold 24pt Times")
    zero = TextAsset("0", fill = black, style = "Bold 24pt Times")
    decimal = TextAsset(".", fill = black, style = "Bold 24pt Times")
    plus = TextAsset("+", fill = black, style = "Bold 24pt Times")
    equals = TextAsset("=", fill = black, style = "Bold 24pt Times")
    
    #SPRITING ALL THE CALCULATOR STUFF
    calc = Sprite(background, (WINDOW_X/2-CALC_X/2, WINDOW_Y/2-CALC_Y/2))
    ansBox = Sprite(answerBox, (WINDOW_X/2-ANSWER_X/2, BUTTON_Y/2))
    sevenBox = Sprite(button, (calc.x + 10, ansBox.y + BUTTON_Y + DIFF))
    Sprite(seven, (sevenBox.x + DIFF, sevenBox.y + DIFF - 5))
    eightBox = Sprite(button, (sevenBox.x + BUTTON_X + DIFF, ansBox.y + BUTTON_Y + DIFF))
    Sprite(eight, (eightBox.x + DIFF, eightBox.y + DIFF - 5))
    nineBox = Sprite(button, (eightBox.x + BUTTON_X + DIFF, ansBox.y + BUTTON_Y + DIFF))
    Sprite(nine, (nineBox.x + DIFF, nineBox.y + DIFF - 5))
    divBox = Sprite(specialButton, (nineBox.x + BUTTON_X + 4*DIFF, ansBox.y + BUTTON_Y + DIFF))
    Sprite(div, (divBox.x + DIFF, divBox.y + DIFF - 5))
    fourBox = Sprite(button, (calc.x + 10, sevenBox.y + BUTTON_Y + DIFF))
    Sprite(four, (fourBox.x + DIFF, fourBox.y + DIFF - 5))
    fiveBox = Sprite(button, (fourBox.x + BUTTON_X + DIFF, eightBox.y + BUTTON_Y + DIFF))
    Sprite(five, (fiveBox.x + DIFF, fiveBox.y + DIFF - 5))
    sixBox = Sprite(button, (fiveBox.x + BUTTON_X + DIFF, nineBox.y + BUTTON_Y + DIFF))
    Sprite(six, (sixBox.x + DIFF, sixBox.y + DIFF - 5))
    multiBox = Sprite(specialButton, (sixBox.x + BUTTON_X + 4*DIFF, divBox.y + BUTTON_Y + DIFF))
    Sprite(multi, (multiBox.x + DIFF, multiBox.y + DIFF - 5))
    oneBox = Sprite(button, (calc.x + 10, fourBox.y + BUTTON_Y + DIFF))
    Sprite(one, (oneBox.x + DIFF, oneBox.y + DIFF - 5))
    twoBox = Sprite(button, (oneBox.x + BUTTON_X + DIFF, fiveBox.y + BUTTON_Y + DIFF))
    Sprite(two, (twoBox.x + DIFF, twoBox.y + DIFF - 5))
    threeBox = Sprite(button, (twoBox.x + BUTTON_X + DIFF, sixBox.y + BUTTON_Y + DIFF))
    Sprite(three, (threeBox.x + DIFF, threeBox.y + DIFF - 5))
    minusBox = Sprite(specialButton, (threeBox.x + BUTTON_X + 4*DIFF, multiBox.y + BUTTON_Y + DIFF))
    Sprite(minus, (minusBox.x + DIFF, minusBox.y + DIFF - 5))
    onBox = Sprite(specialButton, (calc.x + 10, oneBox.y + BUTTON_Y + DIFF))
    Sprite(on, (onBox.x + DIFF, onBox.y + DIFF - 5))
    zeroBox = Sprite(button, (onBox.x + BUTTON_X + DIFF, twoBox.y + BUTTON_Y + DIFF))
    Sprite(zero, (zeroBox.x + DIFF, zeroBox.y + DIFF - 5))
    decimalBox = Sprite(button, (zeroBox.x + BUTTON_X + DIFF, twoBox.y + BUTTON_Y + DIFF))
    Sprite(decimal, (decimalBox.x + DIFF, decimalBox.y + DIFF - 5))
    plusBox = Sprite(specialButton, (decimalBox.x + BUTTON_X + 4*DIFF, minusBox.y + BUTTON_Y + DIFF))
    Sprite(plus, (plusBox.x + DIFF, plusBox.y + DIFF - 5))
    equalsBox = Sprite(specialButton, (decimalBox.x + BUTTON_X + 4*DIFF, plusBox.y + BUTTON_Y + DIFF))
    Sprite(equals, (equalsBox.x + DIFF, equalsBox.y + DIFF - 5))
    
    App().listenMouseEvent("click", mouseClick)
    App().run()
    
    
    
    
