#Heirde :) 
#Enjoy my beginner code!!!!!!

#asks name before starting the Sorting Hat quiz
name = input("Hello there, what is your name?: ")

#IF, ELIF, and Else statements for specific names and any other names to output a string
if name == "Harry Potter": 
    print("wow a member of Gryffindor ayy!?")
elif name == "Severus Snape" or "Voldemort":
    print("Wow a member of Slytherin!?")
elif name == "Dumbledore":
    print("Well your just cheating playting your own game")
else:
    print("Well your an insignificant Hufflepuff or Ravenclaw then!")

########################################################################################################################################################
#this is the original scores of all houses so the scores can be calculated at the end
slytherin = 0 
ravenclaw = 0 
hufflepuff = 0
gryffindor = 0

print("===  THE SORTING HAT ===")
print()

print("Q1) What kind of wizard are you?")
print("1) Evil")
print("2) Good")

answer = int(input("What is your answer (1 - 2): "))

if answer == 1:
    slytherin = slytherin + 1
    ravenclaw = ravenclaw + 1
elif answer == 2:
    gryffindor = gryffindor + 1
    hufflepuff = hufflepuff + 1
else:
    print("wrong iput: try again")

#####################################################################
print("Q2) who would you rather be?")
print("1) Voldemort")
print("2)vDumbledore")

answer = int(input("What is your answer (1 - 2): "))

if answer == 1:
    slytherin = slytherin + 2
    ravenclaw = ravenclaw + 2
elif answer == 2:
    gryffindor = gryffindor + 2
    hufflepuff = hufflepuff + 2
else:
    print("wrong input, try again!")

#########################################################################
print("Q3) would you kill to save the world")
print("1) Yes")
print("2) No")

answer = int(input("What is your answer (1 - 2): "))

if answer == 1:
    slytherin = slytherin + 4
    ravenclaw = ravenclaw + 4
elif answer == 2:
    gryffindor = gryffindor + 4
    hufflepuff = hufflepuff + 4
else:
    print("Try again?")

print("Gryffindor: ", gryffindor) #this will print out the new scores with the added on points after quiz is finished
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)
print("Ravenclaw: ", ravenclaw)

############################################################################

#these if and else statements will print who has won depending on the scores
print("=== THE MAGIC HAT HAS CHOSEN! ===") 

if gryffindor > hufflepuff > slytherin > ravenclaw: 
    print("Gryffindor and hufflepuff win!") 
else:
    print("slytherin and ravenclaw win!") 

