import random
import sys

f = open("wordle.txt", "r")
words = []

correct = [0, 0, 0, 0, 0]
correct_letters = ['0', '0', '0', '0', '0']
letters = []
guesses = []
guess = [[], [], [], [], [], []]
flag = True

for tmp in f:
    words.append(tmp[0:5])

words.sort()

while flag:
        
    seed = words[random.randint(0, len(words))]
    
    for j in range(6):
        
        word = input('Enter a five letter word:\n')
        
        if word == '':
            flag = False
            print('Thanks for playing')
            break
            
        
        while True:
            
            if len(word) != 5:
                word = input('Not five letters, try another one...\n')
                continue
            elif word not in words:
                word = input('Not in words list, try another one...\n')
                continue
            else:
                break
            
        guesses.append(word)
        
        
        for k in range(5):
            if word[k] == seed[k]:
                correct[k] = 1
                correct_letters[k] = word[k]
                guess[j].append(1)
            elif word[k] in seed:
                letters.append(word[k])
                guess[j].append(2)
            else:
                guess[j].append(0)
                
        print()   
             
        print('Guesess')
        
        for t in guesses:
            for x in range(5):
                if guess[guesses.index(t)][x] == 1:    
                    print('\x1b[6;30;42m' + guesses[guesses.index(t)][x] + '\x1b[0m', end='')
                elif guess[guesses.index(t)][x] == 2:
                    print('\x1b[0;30;47m' + guesses[guesses.index(t)][x] + '\x1b[0m', end='')
                else:
                    print('\x1b[6;30;43m' + guesses[guesses.index(t)][x] + '\x1b[0m', end='')
            print(end='\n')
                    
        print(end='\n')
        
        
        for l in range(5):
            if correct[l] == 1:
                print(correct_letters[l], end='')
            else:
                print('.', end='')
                
        print(end='\n')   
        
        if word == seed: 
            print('YOU WON!!!')
            break
            
    if word != seed:
        print('The word was', seed)
        print('Better luck next time!')
        print()
        