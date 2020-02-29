import csv
import random
f = open('animals.csv', encoding='utf-8-sig')
reader = csv.reader(f)
##this code reads a csv file using the encoding description to get rid
## of ï»¿ in the first line of a csv file

Word = {}


for row in reader:
    Word[row[0]] = {'Definition':row[1]}

##data is read into the dictionary Word where the keys are word and the values
## are the words definitions

print ("Its Study Time")
score=0
maxscore=(len(Word))
x=None
whichword=None
missedanswer = []
i=0
for key in random.sample(list(Word.keys()),len(Word)):
    print(Word[key])
    whichword=key
    x=input("Which word matches that definition \n")
    if (x==whichword):
        print('correct')
        score+=1
        Word.pop(key)
    else:
        print("wrong")
        print("The correct answer was " , whichword)
## this code goes through the word dictionary randomly, spits out a definition
## the user inputs what word they think matches the definition
## if they are right the key is popped from the dictionary 
        
print("You scored " , score , " out of " , maxscore)
if (score==maxscore):
    print("\nYou have a perfect score!")
while (score!=maxscore):
    print("Lets go over what you missed!\n" )
    for key in random.sample(list(Word.keys()),len(Word)):
        print(Word[key])
        whichword=key
        x=input("Which word matches that definition \n")
        if (x==whichword):
            print('correct')
            score+=1
            Word.pop(key)
        else:
            print("wrong")
            print("The correct answer was " , whichword)
## if the user did not get a perfect score the dictionary is once again
## iterated through randomly which the same questions given
## though this time the dictionary will only contain the words they missed
## it will keep looping until the user finally gets a perfect score no matter
## how many tries it takes them

    if (score==maxscore):   
        print("Your score is now " , score , " out of ", maxscore)
        print("\nYou have a perfect score!")
   






    
    
            
        
            



    


    
   
   
    


