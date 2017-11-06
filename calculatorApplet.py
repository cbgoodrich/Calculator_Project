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

#NUMBER PROCESSING FUNCTION
def processNumber(num):
    if data["operations"] == "":
        data["num1Text"].destroy()
        data["number1"] += str(num)
        data["num1"] = TextAsset(data["number1"], fill = black, style = "Bold 24pt Times")
        data["num1Text"] = Sprite(data["num1"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
    else:
        while data["i"] == 1:
            data["num1Text"].destroy()
            data["i"] += 1
        data["num2Text"].destroy()
        data["number2"] += str(num)
        data["num2"] = TextAsset(data["number2"], fill = black, style = "Bold 24pt Times")
        data["num2Text"] = Sprite(data["num2"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
   
#MOUSECLICK FUNCTION 
def mouseClick(event):
    if event.x>=sevenBox.x and event.x<=sevenBox.x+BUTTON_X and event.y>=sevenBox.y and event.y<=sevenBox.y+BUTTON_Y:
        processNumber(7)
    elif event.x>=eightBox.x and event.x<=eightBox.x+BUTTON_X and event.y>=eightBox.y and event.y<=eightBox.y+BUTTON_Y:
        processNumber(8)
    elif event.x>=nineBox.x and event.x<=nineBox.x+BUTTON_X and event.y>=nineBox.y and event.y<=nineBox.y+BUTTON_Y:
        processNumber(9)
    elif event.x>=fourBox.x and event.x<=fourBox.x+BUTTON_X and event.y>=fourBox.y and event.y<=fourBox.y+BUTTON_Y:
        processNumber(4)
    elif event.x>=fiveBox.x and event.x<=fiveBox.x+BUTTON_X and event.y>=fiveBox.y and event.y<=fiveBox.y+BUTTON_Y:
        processNumber(5)
    elif event.x>=sixBox.x and event.x<=sixBox.x+BUTTON_X and event.y>=sixBox.y and event.y<=sixBox.y+BUTTON_Y:
        processNumber(6)
    elif event.x>=oneBox.x and event.x<=oneBox.x+BUTTON_X and event.y>=oneBox.y and event.y<=oneBox.y+BUTTON_Y:
        processNumber(1)
    elif event.x>=twoBox.x and event.x<=twoBox.x+BUTTON_X and event.y>=twoBox.y and event.y<=twoBox.y+BUTTON_Y:
        processNumber(2)
    elif event.x>=threeBox.x and event.x<=threeBox.x+BUTTON_X and event.y>=threeBox.y and event.y<=threeBox.y+BUTTON_Y:
        processNumber(3)
    elif event.x>=zeroBox.x and event.x<=zeroBox.x+BUTTON_X and event.y>=zeroBox.y and event.y<=zeroBox.y+BUTTON_Y:
        processNumber(0)
    elif event.x>=decimalBox.x and event.x<=decimalBox.x+BUTTON_X and event.y>=decimalBox.y and event.y<=decimalBox.y+BUTTON_Y:
        processNumber(".")
    elif event.x>=divBox.x and event.x<=divBox.x+BUTTON_X and event.y>=divBox.y and event.y<=divBox.y+BUTTON_Y:
        data["operations"] += "/"
    elif event.x>=multiBox.x and event.x<=multiBox.x+BUTTON_X and event.y>=multiBox.y and event.y<=multiBox.y+BUTTON_Y:
        data["operations"] += "*"
    elif event.x>=minusBox.x and event.x<=minusBox.x+BUTTON_X and event.y>=minusBox.y and event.y<=minusBox.y+BUTTON_Y:
        data["operations"] += "-"
    elif event.x>=plusBox.x and event.x<=plusBox.x+BUTTON_X and event.y>=plusBox.y and event.y<=plusBox.y+BUTTON_Y:
        data["operations"] += "+"
    elif event.x>=equalsBox.x and event.x<=equalsBox.x+BUTTON_X and event.y>=equalsBox.y and event.y<=equalsBox.y+BUTTON_Y:
        compute()
    elif event.x>=onBox.x and event.x<=onBox.x+BUTTON_X and event.y>=onBox.y and event.y<=onBox.y+BUTTON_Y:
        clear()

#CLEAR FUNCTION        
def clear():
    if data["number1"] != "":
        data["num1Text"].destroy()
        data["number1"] = ""
    if data["number2"] != "":
        data["num2Text"].destroy()
        data["number2"] = ""
    if data["operations"] != "":
        data["operations"] = ""
    data["ans"].destroy()

#COMPUTING FUNCTION
def compute():
    data["num2Text"].destroy()
    if data["operations"] == "/":
        data["answer/"] = float(data["number1"])/float(data["number2"])
        data["answer"] = TextAsset(data["answer/"], fill = black, style = "Bold 24pt Times")
        data["ans"] = Sprite(data["answer"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
    elif data["operations"] == "*":
        data["answer*"] = float(data["number1"])*float(data["number2"])
        data["answer"] = TextAsset(data["answer*"], fill = black, style = "Bold 24pt Times")
        data["ans"] = Sprite(data["answer"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
    elif data["operations"] == "-":
        data["answer-"] = float(data["number1"])-float(data["number2"])
        data["answer"] = TextAsset(data["answer-"], fill = black, style = "Bold 24pt Times")
        data["ans"] = Sprite(data["answer"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
    elif data["operations"] == "+":
        data["answer+"] = float(data["number1"])+float(data["number2"])
        data["answer"] = TextAsset(data["answer+"], fill = black, style = "Bold 24pt Times")
        data["ans"] = Sprite(data["answer"], (ansBox.x + 10, ansBox.y + BUTTON_Y/2 - 15))
    data["number1"] = ""
    data["number2"] = ""

if __name__ == "__main__":
    
    #DICTIONARIES
    data = {}
    data["number1"] = ""
    data["number2"] = ""
    data["operations"] = ""
    data["i"] = 1
    
    #COLORS
    red = Color(0xFF0000, 1)
    white = Color(0x000000, 0)
    black = Color(0x000000, 1)
    data["num1Text"] = Sprite(TextAsset("", fill = black, style = "Bold 24pt Times"))
    data["num2Text"] = Sprite(TextAsset("", fill = black, style = "Bold 24pt Times"))
    
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
    