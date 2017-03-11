import random
import sys

# ______     __  ______ _____  _    _
#|  _ \ \   / / |  ____|  __ \| |  | |
#| |_) \ \_/ /  | |__  | |__) | |  | |
#|  _ < \   /   |  __| |  _  /| |  | |
#| |_) | | |    | |____| | \ \| |__| |
#|____/  |_|    |______|_|  \_\\____/

#-----GET WORD LIST-----
with open('words.txt') as wordfile:
    words = wordfile.readlines()

def play():
    #-----SET VARS-----
    wordguess = ""
    #Hangman stages
    hangman = ["\n\n\n\n",
               "\n\n\n\n_____",
               ". |\n. |\n. |\n. |\n _|___",
               ". |----\n. |\n. |\n. |\n _|___",
               ". |--|-\n. |\n. |\n. |\n _|___",
               ". |--|-\n. |  O\n. |\n. |\n _|___",
               ". |--|-\n. |  O\n. |  |\n. |\n _|___",
               ". |--|-\n. |  O\n. |  |\n. |  /\ \n _|___",
               "  |--|-\n. |  O\n. | /|\ \n. | /\ \n _|___"]
    stage = 0
    #Choose a random word from the word list
    word = words[random.randint(0, len(words) - 1)].lower()
    guesses = ""
    #All valid guesses
    chars = "abcdefghijklmnopqrstuvwxyz"

    #-----SETUP WORD-----
    for i in range(0,len(word)-1):
        if word[i] == " ":
            wordguess = wordguess + " "
        else:
            wordguess = wordguess + "_"

    #-----GAME-----
    while "_" in wordguess and stage < 8:
        guessvalid = False
        print("\n" + hangman[stage] + "\nWord: " + wordguess + "\nGuesses: " + guesses)
        while not guessvalid:
            #Continue looping if guess is invalid
            guess = str.lower(input("\nPlease guess a letter\n>_ "))
            if not len(guess) == 1:
                print("Your guess must be 1 character")
            elif guess not in chars:
                print("Your guess must be a letter of the alphabet")
            elif guess in guesses:
                print("You have already guessed this letter")
            else:
                guessvalid = True

        #Add the guess to the list of previous guesses
        guesses = guesses + guess + " "
        newguess = ""
        for i in range(0,len(word)-1):
            #Check every letter in the word
            if guess == word[i]:
                #If the guess is the same as the letter being checked then add the guess to that part of wordguess
                newguess = newguess + guess
            else:
                #If not then add an underscore or whatever has already been guessed
                newguess = newguess + wordguess[i]
        if newguess == wordguess:
            #If there is no change, take a life/add a stage to the hangman
            stage = stage + 1

        #Set wordguess to the new wordguess
        wordguess = newguess

    #End of while loop
    if stage == 8:
        #If the game ended because of no lives left then display that message and ask to replay
        print("You ran out of lives! The word was " + word)
        replayask()
        return
    else:
        #If the game ended because they guessed the word then congratulate them then ask to replay
        print("Well done! You got the word, " + word)
        replayask()

def replayask():
    #Ask the user if they would like to replay
    replay = str(input("Would you like to replay?\n1. Yes\n2. No\n>_ "))
    if replay == "1":
        #If yes then play again
        play()
    elif replay == "2":
        #If not then exit the program
        sys.exit()
    else:
        #If the input is not either '1' or '2' then ask again
        print("\nYou must enter either '1' or '2'")
        replayask()

#-----START GAME-----
play()
