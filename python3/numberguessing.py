#NUMBER GUESSSING - Day 1
#WRITTEN BY - GitHub.com/ItzKakarotto

import random as r
import math

#Just too lazy
THANK = "\nThank You For Playing!"

#Numbers in English to use later
position = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Last"}

#Most important Element in the Game, the Encrypted difficulty
game = [[1, 100, 3], [1, 100, 5], [1, 10, 3], "cancel"]

#Just some random bullshit. Who reads rules anyway
rules = ["I'll generate Random Numbers Between 1-100 or 1-10 depending upon Difficulty", "Hard mode Gives you only 3 Chances, Medium Gives 5, Easy gives 3", "Enter 'cancel' at any point of the game to Stop The Game\n"]

#Printing all the rules
print("RULES OF THE GAME ARE:\n")
for i in range(0, len(rules)):
	print(f"{i+1}⟩ {rules[i]}")

print("Difficulty Options: Hard, Medium, Easy")
def getdifficulty():
    """Get the difficulty in Integer form"""
    dig = input("\nSelect Difficulty: ")
    dif = dig.lower()
    if dif.startswith("ha"):
    	print("Difficulty Chosen: Hard\n")
    	return 0
    if dif.startswith("me"):
    	print("Difficulty Chosen: Medium\n")
    	return 1
    if dif.startswith("ea"):
    	print("Difficulty Chosen: Easy\n")
    	return 2
    if dif=="cancel":
    	return 3
    else:
    	print(f"{dig} not in options!")
    	return getdifficulty()

def gengame(dif):
	"""The game"""
	#dif == difficulty, but Encrypted hehe
	if dif=='cancel':
		return print(THANK)
	
	num = r.randint(dif[0], dif[1])
	hints = dif[2]
	
	print(f"Guess the number between {dif[0]} and {dif[1]}")
	#Main Code Starts
	while hints!=0:
	   inp = input(f"{position[dif[2]-hints+1]} Try:  ")
	   try:
	   	if inp.lower()=="cancel":
	   		print(f"\nCancelled the game!{THANK}")
	   		return
	   	inp = int(inp)
	   	hints-=1
	   except:
	   	print("Thats not a number...")
	   	continue
	   		
	   if inp>dif[1]:
	   	print(f"Uh... The Number can't be more than {dif[1]}")
	   		   	
	   if inp==num:
	   	print(f"Congratulations!, You Guessed the number in {position[dif[2]-hints]} Try Champ!\n")
	   	re = input("Press Enter to play again: ")
	   	if re=="":
	   		restart()
	   	else:
	   		print(THANK)
	   		return
	   		
	   if hints==0:
	   	break

	   if inp>num and inp<dif[1]:
	   	if math.isclose(inp, num, abs_tol=5):
	   		 print("Very close! Just a Little Less")
	   	elif math.isclose(inp, num, abs_tol=10):
	   		 print("You're close! Try Little Less ") 
	   	elif math.isclose(num, inp, abs_tol=25):
	   		print("Try A Little Less") 
	   	else:
	   	    print("You entered a number too High")
	   	    
	   if inp<num:
	   	if math.isclose(inp, num, abs_tol=5):
	  	 	print("Very close! Just a Little More")
	   	elif math.isclose(inp, num, abs_tol=10):
	  		 print("You're close! Try Little More")
	   	elif math.isclose(num, inp, abs_tol=25):
	   		print("Try A Little More") 
	   	else:
	   	    print("You entered a number too Low")
	       
	if hints==0:
	       loser = input(f"\nYou lost the game Loser! The Number was {num}\n\nPress Enter to play again: ")
	       if loser=="":
	       	restart()
	       else:
	       	print(THANK)
	       	return
        
def restart():
	"""The Switch"""
	difRaw = getdifficulty()
	dif = game[int(difRaw)]
	gengame(dif)
	
restart()
