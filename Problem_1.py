# """
# Given a list of length M, you need to print and find sum of the elements of list 

# Input Format :

# Line 1 : An int M 
# Line 2 : M int elements of list seperated by ';'

# Output Format:

# Addition 

# Constraints :
# 1 <= M <= 10^6

# """

#Taking Intput
M=int(input())              #Length of string
elements=input()            #string

lis=[]                      #list to store value as different element   
num=''                      #to distinguish number

for char in elements:       #loop to store value as different element
   
    if char != ';' :        #checking element not ;
        num+=char           

    elif num:               #if ';' comes 
        lis.append(num)     #add num to list 
        num=''              #making num empty for another number 

lis.append(num)             #add last num to list 

lis_int=[]                  #list to store integer value from lis
for i in range (len(lis)):      #loop to convert every element of lis from str to int
    z=int(lis[i])
    lis_int.append(z)
add=0
for i in range (len(lis_int)):      #loop to add number
    add+=lis_int[i]

print(add)
