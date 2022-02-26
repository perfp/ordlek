from colorama import init, Fore, Back, Style
import random
import time

def clear():
    print("\033[H\033[J", end="")


def print_guesses(list_guesses): 
    for g in list_guesses: 
        (match, word) = g
        for c in range(5):
            if match[c]==2:
                print(Back.GREEN + word[c] + Style.RESET_ALL, end='')
            if match[c]==1:
                print(Back.YELLOW + word[c] + Style.RESET_ALL, end='')
            if match[c]==0:
                print(word[c], end='')
        print("")


init()
#os.system('cls' if os.name=='nt' else 'clear') 
# Clear screen

file = open("5words.txt", "r")
words = file.readlines()
count = len(words)
for n in range(count):
    words[n] = words[n].replace("\n", "")
solution = words[random.randrange(count)]

guesses = []
done = False

attempts = 5
while attempts > 0:
    clear()
    print_guesses(guesses)

    print ("Skriv inn et ord, 5 bokstaver: ")
    word = input()

    if len(word)==5:
        if word in words: 
            guess = [0,0,0,0,0]
            for i in range(5):
                if word[i] in solution:
                
                    guess[i] = 1
                if word[i] == solution[i]:
                
                    guess[i] = 2
            guesses.append((guess, word))

            if (guess == [2,2,2,2,2]):
                done = True
            attempts = attempts - 1

            
            
        else:
            print(word + " finnes ikke i ordlista")
            time.sleep(1)
    else:
        print("Du må velge et ord på 5 bokstaver")
        time.sleep(1)

    if done: 
        print("Gratulerer!")
        break

if not done:
    print("Bedre lykke neste gang.")