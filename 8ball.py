import random
from os import system, name

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is definitely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very Doubtful'

#screen clear function
def screen_clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Beginning of program
screen_clear()
print('The Magic 8 Ball is ready to give you your fortune:')
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
print('')