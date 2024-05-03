'''EX.1->Number guessing game'''

import random
import math
class data:
    def __init__(self):
        print('\tNumber guessing game')
        lower_range=int(input('Enter range:from '))
        upper_range=int(input('\tto '))
        self.number=random.randint(lower_range,upper_range+1)
        self.chance=int(math.log(upper_range-lower_range+1,2))
        print(f'You have only "{self.chance}" chance to guess the number')

def new():
    i =int(input('If want to continue enter 1 else 0:'))
    if i==1:
        global g_no
        global obj1
        g_no=0
        obj1=data()
        go()
    else:
        print('Thankyou for playing')
        
def check(g_no):
    if (obj1.chance==g_no):
        print('Your chance is over')
        new()
    else: go()
    
g_no=0
obj1=data()

def go():
    guess=int(input('Enter your guess:'))
    global g_no
    g_no=g_no+1
    if guess==obj1.number:
        print('You are right')
        print(f'Total no. of guess:{g_no}')
        new()
    else:
        if(guess>obj1.number):
            print('guess is high')
            check(g_no)
        if(guess<obj1.number):
            print('Guess is low')
            check(g_no)
    
print('\tStart guessing:-')
go() 



