import random
import hangman_word
word=random.choice(hangman_word.word_list)
end= False
lives=6 
from hangman_art import logo,stages
print(logo)
display=[]
for i in range (len(word)):
    display+="_" 
while not end:
     guess= input("Guess a letter").lower()
     if guess in display:
        print("You've already guessed this letter ")
     for position in range(len(word)):
        letter = word[position]
        if letter ==guess:
            display[position]=letter
     if  guess not in word:
         print("The letter is not preset in the chosen word")
         lives-=1
         if lives==0:
               end=True
               print("you lose")
     print (f"{' '.join(display)}")
     if "_" not in display:
         end=True
         print("You've won")
     print(stages[lives])
        
        


     

