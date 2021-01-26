name=input("Enter your name:\n")
name=name.upper()
print(f"Hi {name}! Let's start the game")
li=["rock","paper","sessar"]
chance=1
score=0
computer=0
draw=0

while (chance<=10):
	import random
	a=random.choice(li)
#	print(a)

	man=input("Enter r for rock ,p for paper or s for sessar:\n")
	if a=="rock" and man=="p":
			print("computer give ",a)
			print ("you win")
			score+=1
	elif a=="rock" and man=="s":
			print("computer give ",a)
			print ("you loss")
			computer+=1
	elif a=="rock" and man=="r":
			print("computer give ",a)
			print ("Draw")
			draw+=1
	elif a=="paper" and man=="s":
			print("computer give ",a)
			print ("you win")
			score+=1
	elif a=="paper" and man=="r":
			print("computer give ",a)
			print ("you loss")
			computer+=1
	elif a=="paper" and man=="p":
			print("computer give ",a)
			print ("Draw")
			draw+=1
	elif a=="sessar" and man=="r":
			print("computer give ",a)
			print ("you win")
			score+=1
	elif a=="sessar" and man=="p":
			print("computer give ",a)
			print ("you loss")
			computer+=1
	elif a=="sessar" and man=="s":
			print("computer give ",a)
			print ("Draw")
			draw+=1
	else:
			print("Invalied input")
	print("\n")
			
	chance+=1
if (chance>10):
	print("Game over")
print("Here is the score board : ")
print(f"{name} your score: ",score)
print("Computer score: ",computer)
print("Draw score : ",draw)
if score>computer:
	print("Overall you win the game")
elif score<computer:
	print("Overall computer win the game")
else:
	print("Tie or draw")
	
