'''The Minion Game'''

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += (len(s) - i)  # Number of possible words left to right from a word of length n is always 
                                         # n + (n-1) + (n-2) +..1
        else:
            stuart_score += (len(s) - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
       
    
if __name__ == '__main__':
    s = input('Enter String:')
    minion_game(s)