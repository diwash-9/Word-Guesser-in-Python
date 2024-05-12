import random

print("\n\t\t\t\tGUESS THE WORD")


while True:
    list_of_words = ["root", "cause", "heaven","concatinate","python","programming","hridima","hridham","ronish","nikesh", "ankit"]
    random.shuffle(list_of_words)
    length = len(list_of_words)
    print("Choose any number between 0 and",length-1,"to get an anagram.")
    n = int(input())
    

    the_word = list_of_words[n]

    computer_word = list_of_words[n]

    new_list = [*computer_word]

    random.shuffle(new_list)

    anagram = ' '.join(new_list).upper()
    print("\n\n")

    print("\tYour anagram is ---> \t",anagram)

    trials = 0
    print("\n\t You have five trials to guess the correct name.")
    while True:
        

        user_guess = input("\nYour first guess? \t").lower()

        if user_guess == the_word:
            print("\n\t\tCongratulations, you got the word in",trials+1,"trial(s).")
            break
        
        else:
            print("\nWrong word, try again.")
            trials = trials + 1
            if trials == 4:
                print("\nThis is your last trial.")
            elif trials == 5:
                print("\n\nTrials Completed, You lost.")
                input("\nPress enter to find out the word.")
                print("\nThe correct word was",computer_word.upper())
                break
            continue
        
    question = input("\n\t\tDo you want to play again?(Y/N)\t").lower()
    if question == "y":
        continue
    else:
        print("\n\t\tThanks for playing.")
        break





