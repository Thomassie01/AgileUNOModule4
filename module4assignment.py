# Jeremy Thomassie
# Module 4 Assignment

#import the function exit from sys module
from sys import exit
# import the randint function from the random module
from random import randint


myData = {} #Create dictionary called myData.
guesses = 0 #Create a variable called guesses and set it to 0.
wins = 0 #Create a variable called wins and set it to 0

#Useing a context manager to open the file "questions.txt" as infile, read only.
with open("questions.txt", "r") as infile:
    #Read the infile and store in variable called questions
    questions = infile.readlines()
    #Create a for loop to cycle through all the text lines in the variable questions
    for question in questions:
        #If stsatement checks to see if question contains the string "first"
        if "first" in question:
            #Stores the input from the question into the myData dictionary with the key name "first_name"
            myData['first_name'] = input(question)
        #If stsatement checks to see if question contains the string "last"
        elif "last" in question:
            #Stores the input from the question into the myData dictionary with the key name "last_name"
            myData['last_name'] = input(question)
        #if the conditions for the if and elif statements above are not met, this else statement will trigger
        else:
            #Print statement tells the user that the infile is bad
            print("bad question in input file")
            #exits the application
            exit()
#For loop cycles through the included code 10 times
for play in range(10):
    number = randint(0, 100) #store a random interger from 0 to 100 in variable "number"
    solved = False #sets boolean variable "solved" to false
    # While loop cycles through the included code until solved no longer equals false
    while not solved:
        #Asks the user for an interger and stores the input in a variable "guess"
        guess = int(input(f"Guess a number from 0 to 100: "))
        # Increments the value stored on "guesses" by one
        guesses += 1
        #if statement checks to see if the value in guess is the same as the value in number
        if guess == number:
            #Prints a message to the user informing them that the number they guessed is correct
            #Inserts the string called first_name from dictionary "myData" into the printed string
            print(f"Great job, {myData['first_name']}. Your guess of {guess} is correct!")
            #Increments value stored in "wins" by 1
            wins +=1
            #sets boolean solved to True
            solved = True
            #exits the while loop
            break
        #if the value stored in guess is not equal to value stored in number then do the following
        if guess != number:
            #informs the user that the guess was incorrect
            print(f"your guess of {guess} is incorrect!")
        #if statement checks to see if the value in guess is greater than the value in number
        if guess > number:
            #informs the user that their guess was higher than the selected number
            print(f"Sorry, you guessed too high!")
        #if statement checks to see if the value in guess is less than the value in number
        elif guess < number:
            #informs the user that the guess was lower than the selected number
            print(f"Sorry, you guessed too low!")
        #if none of the if conditions above are met, do this
        else:
            #null statement
            pass

    #if the value stored in "solved is "True" solved == True
    if solved:
        #prints out the total wins out of ten plays
        print(f"Let's play again! You have completed {wins} out of 10 plays.")
        #Exits to the begining of the for loop
        continue

#prints a string that includes the users first and last name, and total number of wins
print(f"{myData['first_name']} {myData['last_name']} guessed the correct number {wins} out of 10 plays")
#prints the user's first and last name again and the total number of guess it took them to finish 10 rounds
print(f"It took {myData['first_name']} {myData['last_name']} {guess} guesses to do this.")

