'''EX 2-> Snak Water Gun game'''

import numpy as np
def method1():
    while(1):
        print('Snak Water Gun Game:')
        print('Snak=0 Water=1 Gun=2')
        game=['Snak','Water','Gun']
        user=int(input('Enter your choice:'))
        print(f'user:{game[user]}')
        computer=np.random.randint(0,3)
        print(f'Computer:{game[computer]}')
        if(user==computer):
            print(f'{game[user]}={game[computer]}\n Result=Draw')
        if(user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
            print('Result: You won')
        if(computer==0 and user==1) or (computer==1 and user==2) or (computer==2 and user==0):
            print('Result: Compuer won')
        n=int(input('*For continue Enter 1* \n *For exit enter 0*'))
        if n==0: 
            break

# aanother method

def method2():
    import random
    while(1):
        def check(comp,user):
            if user==comp:
                return 0
            if user==0 and comp==1: return 1
            if user==1 and comp==2: return 1
            if user==2 and comp==0: return 1
            return -1
        
        comp=random.randint(0,3)
        print('0 for snake , 1 for water and 2 for gun')
        user=int(input('Enter choice:'))
        score=check(comp,user)
        
        if score==0: print("it's a Draw ")
        if score==1: print('Congratulation ! You Won')
        if score==-1: print('You Lost ! Better luck next time')
        
        new=int(input(print('For coninue enter 1 else enter 0: ')))
        if new!=1: 
            break
        
if __name__ == "__main__":
    
    #choose any method:
    
    # method1()
    
    #OR
    
    method2()