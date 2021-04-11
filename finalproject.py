print("Welcome to our Quiz! You'll  be asked 10 Questions. You have to answer at least six questions correctly to pass this quiz. Keep in mind that the answers are case-sensitive. Good luck!")
totalpoints=0


try:
 answer = int(input("Let's start with the first question. On which year was Turkey declared as republic: "))
except ValueError:
  print("Please enter an integer value!!!")
  answer = int(input("Let's start with the first question. On which year was Turkey declared as republic: "))
if (answer==1923):
 totalpoints+=10
 

answer = input("Which city is the capital of Turkey: ")
if (answer=='Ankara'):
 totalpoints+=10 
 
answer = input("To which famous singer does the song 'The Smooth Criminal' belong to? ")
if (answer=='Michael Jackson'):
 totalpoints+=10  
 

answer = input("Which extraterrestrial planet does SpaceX want to colonize in the next 10 years? ")
if (answer=='Mars'):
 totalpoints+=10   
 
try:  
 answer = int(input("In which year did the humanity reach to the Moon? "))
except ValueError: 
 print("Please enter an integer value!!!")
 answer = int(input("In which year did the humanity reach to the Moon? "))
if (answer==1969):
 totalpoints+=10 
 
try: 
 answer = float(input("What is the Pi number to the fifth decimal place? "))
except ValueError:
 print("Please enter a float value!!!")
 answer = float(input("What is the Pi number to the fifth decimal place? "))
if (answer==3.14159):
 totalpoints+=10  

try: 
 answer = int(input("In which year did Sertab Erener win the Eurovision? "))
except ValueError:
 print("Please enter an integer value!!!")
 answer = int(input("In which year did Sertab Erener win the Eurovision? "))
if (answer==2003):
 totalpoints+=10     
 
answer = input("Who is the Turkish author who won the Nobel Prize in Literature in 2006? ")
if (answer=='Orhan Pamuk'):
 totalpoints+=10   
 
answer = input("What is the name of the American Space Agency (All in Capitals)? ")
if (answer=='NASA'):
 totalpoints+=10    
 
answer = input("Who is the greatest NBA basketball player of all times? ")
if (answer=='Michael Jordan'):
 totalpoints+=10   
 
numberofcorrectanswers=int(totalpoints/10)
numberofwronganswers=10-numberofcorrectanswers
if totalpoints>50:
 print("Congratulations!!! You've passed this quiz. You've had", numberofcorrectanswers, "correct answers")
else:
 print("Unfortunately you couldn't pass this quiz. You've had", numberofwronganswers, "wrong answers. Please try it again")
