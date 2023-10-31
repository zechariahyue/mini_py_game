from rps import *
from guess import *
import turtle
import math

# draw grid
# Reference from https://www.youtube.com/watch?v=8eHpXLDhi6w&t=184s

def drawBoard():
    screen = turtle.Screen()
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)

    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12))
            num += 1

        
    screen.update()

# draw X
def drawX(x,y):
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()

    drawer.setheading(60)
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    screen.update()

# draw O
def drawO(x,y):
        drawer.penup()
        drawer.goto(x,y+75)
        drawer.pendown()
        drawer.setheading(0)
        for i in range(180):
            drawer.forward((150 * math.pi)/180)
            drawer.right(2)
        screen.update()
        
def checkWon(letter):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
            return True
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
            return True
        return False
def checkDraw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count += 1
    if count > 3:
        return True
    else:
        return False
def addO(i,j):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 - 200*i)
                    return
                board[i][j] = " "
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 -200 * i)
                    return
                board[i][j] = " "
    for i in range (0,3,2):
        for j in range(0,3,2):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200 *i)
                return
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200*i)
                return
                    
            
        
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i+1))
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i+1))
#add on x to the inputted location
def addX(row,column):
    announcer.clear()
    if board[row][column] == "x" or board[row][column] == "o":
        announcer.write("That spot is taken!", font = ("Arial", 36))
        screen.update()
    else:
        drawX(-200 + 200 * column, 200 - 200 * row)
        board[row][column] = "x"
        if checkWon("x"):
            announcer.goto(-97,0)
            announcer.write("You Won! Please click for more games!", font = ("Arial", 36))
            screen.update()
            deactivate()
        else:
            addO(i,j)
            if checkWon("o"):
                announcer.goto(-90, 0)
                announcer.write("You lost! Please click for more games!", font = ("Arial", 36))
                screen.update()
                deactivate()
            elif checkDraw():
                announcer.goto(-90,0)
                announcer.write("It's a tie! Please click for more games!", font = ("Arial", 36))
        
def squareOne():
    addX(0,0)
def squareTwo():
    addX(0,1)
def squareThree():
    addX(0,2)
def squareFour():
    addX(1,0)
def squareFive():
    addX(1,1)
def squareSix():
    addX(1,2)
def squareSeven():
    addX(2,0)
def squareEight():
    addX(2,1)
def squareNine():
    addX(2,2)
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive,
             squareSix, squareSeven, squareEight, squareNine]
    
drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200,0)
announcer.color("red")

drawBoard()
screen = turtle.Screen()
screen.tracer(0)



board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)
activate(functions)
screen.listen()
turtle.exitonclick()
def main():
    while True:
        print("Thank you for playing tic tac toe ")
        print("Do you want to play any other game?")
        print("1. Guessing Game")
        print("2. Rock paper scissors spock lizard")
        print("3. Quit")
        mc = get_menu_choice()
        if mc == 1:
            guess()
        if mc == 2:
            rps()
        elif mc == 3:
            print("Thank you for playing.")
            break
        else:
            print("Wrong choice, please enter a number between 1 to 4")
main()
