import random
import math

# Reference from previous retrospective
def get_menu_choice():
    # Prompt for a choice and validate it
    while (True):
        try:
            choice = int(input("\nWhat would you like to do? "))
            if (choice < 1 or choice > 3):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice

# Reference from previous retrospectives
def get_game_choice():
    # Prompt for a choice and validate it
    while (True):
        try:
            choice = int(input("\nWhat number wuld it be? "))
            if (choice < 1 or choice > 100):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice
# Reference from https://www.geeksforgeeks.org/number-guessing-game-in-python/
def game(name,win,lose,tie,count):
    while True:
        print("Round " + str(count))
        count = count + 1
        print("Please enter the max number between 1 to 100")
        mn = get_game_choice()
        print("Please enter the minimum number between 1 to 100")
        sm = get_game_choice()
        x = random.randint(sm,mn)
        chance = round(math.log(mn - sm + 1, 2))
        c = 0
        remain = chance;
        while c < remain:
            c += 1
            print("\n\tYou've only ",chance," chances to guess the integer!\n")
            print("Please Guess a number")
            guess = get_game_choice()
            if x == guess:
                print("Congrtualations! You got it in ",c, "try")
                win = win + 1
                break
            elif x > guess:
                chance = chance -1
                print("You guessed too small!")
            elif x < guess:
                chance = chance - 1
                print("You Guessed too high!")
        if c > chance:
            print("\nThe number is %d" % x)
            print("\nBetter Luck Next time!")
            lose = lose + 1
        print("What would you liek to do")
        print("1 Play again")
        print("2. View Statistics")
        print("3. Quit")
        choice2 = get_menu_choice()
        if ( choice2 == 1):
            print()
        elif ( choice2 == 2):
            print( name + " here are you game statics:")
            print("Wins: " + str(win))
            print("loses: " + str(lose))
            print("Ties: " + str(tie))
            rate = win / (count-1) * 100
            ratio = round(rate,2)
            print("Win/loss Rato: " + str(ratio)+"%")
            f = open('%s.rsp' % name, 'w')
            data =[str(win) + '\n', str(lose) + '\n',str(tie)+ '\n',str(count)+ '\n']
            f.writelines(data)
            f.close()
            break
        elif (choice2 == 3):
            print(name + " Your game has been saved.")
            print("Thank you for playing.")
            f = open('%s.rsp' % name, 'w')
            data =[str(win) + '\n', str(lose) + '\n',str(tie)+ '\n',str(count)+ '\n']
            f.writelines(data)
            f.close()
            break
        else:
            print("Please enter a value from 1 to 3 only")
def guess():
    win = 0
    lose = 0
    tie = 0
    count = 1
    while True:
        print("Welcome to number guessing game!")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = get_menu_choice()
        if choice == 1:
            name = input("What is your name?:")
            print("Hello," + name + " Lets Play!")
            game(name,win,lose,tie,count)
        elif choice == 2:
            while True:
                name = input("What is your name?:")
                try:
                    filename = str(name)+ ".rsp"
                    f = open(filename, 'r')
                    print("Hello," + name +"Your data is")
                    data = f.read()
                    result = data.split()
                    win = result[0]
                    lose = result[1]
                    tie = result[2]
                    count = result[3]
                    print("Win:"+ str(win))
                    print("Lose:"+ str(lose))
                    print("Tie:"+ str(tie))
                    count = int(count) 
                    win = int(win)
                    lose = int(lose)
                    tie = int(tie)
                    print("Hello," + name + " Lets Play!")
                    f.close()
                    game(name,win,lose,tie,count)
                    break
                except Exception as err:
                    print('An error occurred finding your record')
                    print('The error is', err)
        elif choice == 3:
            print("Thank you for playing.")
            break
        else:
            print("Wrong choice, please enter a number between 1 to 3")

