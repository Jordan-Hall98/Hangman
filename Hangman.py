import random


#importing art and words from other pyton documents
import hangman_words
import Hangman_art
import os



#creating variable called word_list for the list of words stored in hangman words file



#length of word
def hangman():
    '''The hangman game'''
    print (Hangman_art.logo)
    word_list = hangman_words.word_list

    #Picking a random word from list
    chosen_word = random.choice(word_list)

    
    word_length = len(chosen_word)

    #creating empty list
    display = []

    #adding "_" for every letter in chosen word to list. e.g for Camel add 5 times "_"
    for letter in chosen_word:
        display += "_"

    print (display) 
    print (f"This word is {word_length} letters long")
    #creating boolean variable to use when determining end of game conditions
    end_of_game = False


    #creating variable for lives
    lives = 6


    #While loop used to create multiple guesses. While not end of game = whilst end of game is not True
    while not end_of_game:
        #allow the user to guess a letter, converting to lower case
        guess = input("Guess a letter: ").lower()
        
        #if statement here to check for previous guesses of the letter to let the user know
        if guess in display:
            print (f"You have already guessed {guess}")

        #using for loop to define letter as a variable to be used for each character in the chosen word \n
        #with a stored location, called position
        for position in range(word_length):
            letter = chosen_word[position]
            
            #Compare each character in the chosen word with the guessed letter. 
            #If the same, replace "_" in list with the letter 
            if letter == guess:
            #add the guess to the list    
                display[position] = letter

        #if guessed letter not in word, lose a life
        #print the stage of lives user is at with ascii art.
        if guess not in chosen_word:
            print (f"{guess} is not in the word! Please try again!")
            lives -= 1
            print (Hangman_art.stages[(lives)])
            print (f"You have {lives} lives remaining! ")
            #if lives reach 0 then end of game becomes true
            if lives == 0:
                end_of_game = True
                print ("Game over! You ran out of lives")
                print (f"The word was {chosen_word}")
                print (Hangman_art.logo)

        print (display)                     

        #if player guesses all of the letters, and guesses the word, there is no longer any "_" 
        #therefore end of game is true and this will break the while loop        
        if "_" not in display:
            end_of_game = True
            print ("You win!")    
   
hangman()

stop_playing = False

while not stop_playing:
    if input("Would you like to play another game of Hangman? Type 'y' for yes, or anything else for no: ") == "y":
        os.system('cls')
        hangman()
    else:
        os.system('cls')
        stop_playing = True
        print ("Thank you for playing!")