"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome



"""

def reflection(elements):
    lis=[]                      #list to store value as different element   
    num=''                      #to distinguish number

    for char in elements:       #loop to store value as different element
   
        if char != ',' :        #checking element not ;
            num+=char           

        elif num:               #if ';' comes 
           lis.append(num)     #add num to list 
           num=''              #making num empty for another number 

    lis.append(num) 
    return reversed(lis)


M=int(input())              #Length of string
elements=input()            #string

reversed_words = reflection(elements)       #call of function

for word in reversed_words:                 #loop to print word in next line
    print(word)
