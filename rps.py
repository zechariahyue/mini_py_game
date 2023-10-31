import random

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
            choice = int(input("\nWhat would you like to do? "))
            if (choice < 1 or choice > 5):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice
# Regerence
# https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
# https://www.youtube.com/watch?v=Kov2G0GouBw&t=24s
# The rules are: 
# Scissors cuts Paper Paper covers Rock Rock crushes Lizard Lizard poisons Spock Spock smashes Scissors
# Scissors decapitates Lizard Lizard eats Paper Paper disproves Spock Spock vaporizes Rock (and as it always has) Rock crushes Scissors

def game(name,win,lose,tie,count):
    while True:
        print("Round " + str(count))
        count = count + 1
        print("1.Rock")
        print("2. Paper")
        print("3. Scissors.")
        print("4. Spock")
        print("5. Lizard")
        options = ["Rock","Paper","Scissors", "Spock","Lizard"]
        choice = get_game_choice()    
        ai = random.randint(1,5)
        if(choice == ai):
            print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You tie!")
            tie = tie + 1
        elif(choice == 1):
            if (ai == 5):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif ( ai == 4):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
            elif ( ai == 3):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif( ai == 2):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
        elif( choice == 2):
            if (ai == 1):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif ( ai == 3):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
            elif ( ai == 4):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif( ai == 5):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
        elif ( choice == 3):
            if (ai == 2):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif ( ai == 1):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
            elif ( ai == 5):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif( ai == 4):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
        elif ( choice == 4):
            if (ai == 1):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif ( ai == 2):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
            elif ( ai == 3):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif( ai == 5):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
        elif ( choice == 5):
            if (ai == 2):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                win = win + 1
            elif ( ai == 1):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
                lose = lose + 1
            elif ( ai == 3):
                   print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You win!")
                   win = win + 1
            elif( ai == 4):
                print("You chose "+options[choice-1]+". The computer chose "+options[ai-1]+". You lose!")
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



                

def rps():
    win = 0
    lose = 0
    tie = 0
    count = 1
    while True:
        print("Welcome to rock paper scissors spock lizard!")
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


                 
