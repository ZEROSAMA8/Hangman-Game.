#Step 2

import random
word_list = ["aardvark", "baboon","spatula","horoscope","rumours", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
for letter in chosen_word:
    display+="_"
    
print(display)


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# len_word= len(chosen_word)
end_of_game= False
life= 5 
while not end_of_game:
    if display=="_":
        print("You win")
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        # print(f"Current position: {position} .\nCurrent letter: {letter}  ")
        if letter == guess:
        
            display[position]= letter
        
      
    if guess not in display:
        life-= 1
        print(f"You lost a life, You have {life} lifes left.")
        if life <= 0:
            end_of_game= True
            print("You lost this game.")
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You win!")

            
 
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
