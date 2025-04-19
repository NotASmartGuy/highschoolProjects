#Editors note
#Written sometime during year 10 IST 
#This was MORE PROFANE because teehee undeveloped pre-frontal cortex

#Written by Richard 
#Just a script for IST python question 

x = 0 
score = x

# Question Uno 
#most of this is going to be repeated so i'll just comment on the unique or first appearance of each instance
print("What is the Capital of France") #prints out the question
answer_1 = input("a)Paris\nb)Berlin\nc)Lyon\nd)Marseille\n:") #sets the user input as the variable answer_1 whilst also displaying the options
if answer_1 == "a" or answer_1 == "paris" or answer_1 == "Paris" or answer_1 == "A": #conditional checks for the right answers
    print("Correct") #prints this
    x = x + 1   #adds to score
else:
    print("INCORRECT\nRemember who was in Paris?") #output with a "helpful" tip

# Question Er 
print("What is the Y intercept for the following equation?\ny=x^2-4x+5")
answer_2 = input("a)2\nb)3\nc)4\nd)5\n:")
if answer_2 == "d" or answer_2 == "5" or answer_2 == "five" or answer_2 == "D": 
    print("Correct")
    x = x + 1   
else:
    print("INCORRECT\nRemember to sub 0 as x in the equation")

# Question tre 
print("What was the time period was Shakespeare Twelfth Night written in?")
answer_3 = input("a)Victorian Era\nb)Tudor Era\nc)Elizabethan Era\nd)Georgian Era\n:")
if answer_3 == "c" or answer_3 == "Elizabethan Era" or answer_3 == "elizabethan era" or answer_3 == "C": 
    print("Correct")
    x = x + 1   
else:
    print("INCORRECT\nRemember the two prominant ones")

# Question vier 
print("What type of wood is plywood?")
answer_4 = input("a)Hardwood\nb)Semi-Hardwood\nc)Softwood\nd)Driftwood\n:")
if answer_4 == "a" or answer_4 == "A" or answer_4 == "Hardwood" or answer_4 == "hardwood": 
    print("Correct")
    x = x + 1   
else:
    print("INCORRECT\nRemember the two prominant ones")

# Question pyat 
print("The car model 911 GT3 RS is manufactured by which of the following company")
answer_5 = input("a)MAN\nb)Audi\nc)Mercedes Benz\nd)Porsche\n:")
if answer_5 == "D" or answer_5 == "d" or answer_5 == "Porsche" or answer_5 == "porsche": 
    print("Correct")
    x = x + 1   
else:
    print("INCORRECT\nVroom Vroom!")
    
    
    
#Total Score
score = float(x / 5) * 100 #calculates the percentage
good =(x*10000) 
great= float(x*10000/5) *100
print(x,"out of 5, that is",score, "%")
print("But because you are so good I'll give you extra points, so that's",good,"correct or", great,"%") #because i felt like it
