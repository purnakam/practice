import random
def method2():
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
    
    method2()