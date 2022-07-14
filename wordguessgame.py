import random
words=["hello","well done","project","program","life","VITCollege"]
guessed_word=random.choice(words)
hint=guessed_word[0],guessed_word[-1]
store_g_l=[]
try_p=8
a=input("enter your name")
print("welcome to this game world",a)
print("we are giving you 8 attempts for guessing")
 
for guess in range(try_p):
    while True:
        letter=input("guess the letter")
        if len(letter)==1:
            break
        else:
            print("guess single letter only")
    if letter in guessed_word:
        print("yes!!!!")
        store_g_l.append(letter)
    else:
        print("no!!")
    
    if guess==3:
        print()
        clue_request=input("do you neeed clue")
        if clue_request.lower().startswith("y"):
            print()
            print("the first and last letter of the word is",hint)
        else:
            print("you seem consfident carry on!!")
 
print()
print('''now lets see what have u guessed so far you have guesssed:''',len(store_g_l),"till now correctly")
print("these letters are",store_g_l)
 
word_guess=input("guess the whole word now")
if word_guess.lower()==guessed_word:
    print("congrats ur right")
else:
    print("sorry the answer was",guessed_word)
 
print()
print("press enter and leave the game bye bye")
 
