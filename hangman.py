# Write your code here
import random
print("H A N G M A N")

menu = True
print('Type "play" to play the game, "exit" to quit:')
controller = input()
if controller == "play":
    menu == True
elif controller == "exit":
    exit()

while menu == True:
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    random_word = random.choice(list_of_words)
    letters = set(random_word)
    strings = "-" * len(random_word)
    guessed = set()
    counter = 8
    cond = True
    tries = 0
    all_guess = set()

    while tries < 8:
        print()
        print(strings)
        answer = str(input("Input a letter:"))
        if answer.islower():
            lower_cond = True
        else:
            lower_cond = False
        if len(answer) > 1 or len(answer) < 1:
            length_cond = False
        else:
            length_cond = True
        if(answer in all_guess):
            print("You've already guessed this letter")

        elif(answer in strings) and length_cond is True:
            print("No improvements")


        elif (answer in letters):
            guessed.add(answer)
            all_guess.add(answer)
            strings = ''
            for i in random_word:
                if i in guessed:
                    strings += i
                else:
                    strings += "-"

        if letters == set(guessed):
            print("You guessed the word!")
            print("You survived!")
            break

        elif answer not in letters and answer not in all_guess and lower_cond is True and length_cond is True :
            print("That letter doesn't appear in the word")
            all_guess.add(answer)
            tries+=1
        elif lower_cond is False and length_cond is True:
            print("Please enter a lowercase English letter")
        elif length_cond is False:
            print("You should input a single letter")

    if tries == 8:
        print("You lost!")
        print()
    print('Type "play" to play the game, "exit" to quit:')
    second_round = input()
    if second_round == "play":
        menu == True
    elif second_round == "exit":
        break
    else:
        break
