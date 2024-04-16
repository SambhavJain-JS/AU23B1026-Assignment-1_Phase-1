# """ 

# Problem: Knock Knock are you there?

# Input Format:

# 1. Take M int input from the User 
# 2. Get M , seperated values from a user 
# 3. Enter a number 'N' you are looking for

# Output Format:

# 1. Print index on console once Found or Print 'Better Luck Next Time' to the console

M=int(input())              #Length of string
elements=input()            #string

lis=[]                      #list to store value as different element   
num=''                      #to distinguish number
for char in elements:       #loop to store value as different element
   
    if char != ';' and char != ',' :        #checking element not ;
        num+=char           

    elif num:               #if ';' comes 
        lis.append(num)     #add num to list 
        num=''              #making num empty for another number 

lis.append(num)             #add last num to list 

lis_int=[]                  #list to store integer value from lis
for i in range (len(lis)):      #loop to convert every element of lis from str to int
    z=int(lis[i])
    lis_int.append(z)


N=int(input())              #Taking input to check present or not

found=False

for i in range(len(lis_int)):       #checking of N present or not 
    if lis_int[i]==N:
        index=i
        found=True                      #if present k=true
        
    i=i+1

if found==True:                         #if k=true print index
  print(index)                         
  

else:
    print("Better Luck Next Time")          #if not found
