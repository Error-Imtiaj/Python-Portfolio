import random
from words import words as w
from stages import stages
from stages import logo

#TODO Variable
blanks = []
lives = 6

#TODO LOGO PRINT AND GAME INSTRUCTION
print(logo[0])
print("Rules -- \n",
      "=> You have to guess the letter.\n"
      " => You have 6 life. \n",
      "=> Every wrong guess will take 1 of you life. \n",
      "=> If all the lifes out the hangman will dead and the game is end. \n",
      "=> If you guess the correct word you will win and the hangman will saved by you. \n"
      )
player_name = input("Please write your name before start: ")

#TODO Generate Random Word
chosen_words = random.choice(w)

#TODO find the lenth and generate blanks
gen_word_len = len(chosen_words)
for i in range(gen_word_len):
    blanks += "_"

print(chosen_words) #! generated word

#TODO BEGIN INPUT OF THE GAME 
    
while '_' in blanks:
    #TODO Take input
    guess = input("Guess The letter : ")

    #TODO For loops replacing the _ with the word
    for position in range(len(chosen_words)): #* This position start from 0 and end eith the lenth of chosen words
        letter = chosen_words[position] #* indexing chosen words letter into letter variable
        if letter == guess: #* checking guess letter and letter are same
            blanks[position] = letter #* if they are same blanks[position] will update to letter
            
    
    #TODO checking if you inputed a wrong guess        
    if guess not in chosen_words:
        print(f"You have guessed a wrong letter. It's not {guess}")
        lives -= 1 #* Cut live if the guessed word is wrong
    
    #TODO printing words and hangman
    print(stages[lives])       #* print hangman based on lives
    print(f"{''.join(blanks) }")
    
    #TODO checking you have lost all the lives or not
    if lives == 0:
        break #* if all the lives end the games is end

#! Check you won or loss 
if '_' in blanks: #* if _ have in blanks then excute this
    print(logo[1])
else:
    print(f"Hangman -> Thank you {player_name} for saving me. ")



