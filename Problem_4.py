"""   Turn Around Function 

Design a Function that should take list as an argument and perform turnaround() it in following fasion.

Input Format:

1. Take M, Inputs for Turnaround
2. Enter M numbers on new line 

10
10
20
30
40
50
60
70
80
90

Output Format:
50
60
70
80
90
100
30
40
10
20

"""
def turnaround():
    
    
    for i in range(midpoint, M):
        add.append(inputs[i])

    return add

M = int(input(""))
inputs = []
add=[]
midpoint = M // 2
midpoint2=midpoint//2

for i in range(M):
    num = int(input())
    inputs.append(num)

if M == 8:
    x=turnaround()
    for i in range(len(add)):
        print(x[i])

    for i in range(midpoint):
        print(inputs[i])

elif M==10:
    print(inputs[midpoint-1])
    x=turnaround()
    for i in range(len(add)):
        print(x[i])

    midpoint2=midpoint//2

    lis1=(inputs[:midpoint2])
    lis2=(inputs[midpoint2:midpoint-1])

    for i in range(int(midpoint2)):
        print(lis2[i])

    for i in range(int(midpoint2)):
        print(lis1[i])

elif M==11:
    print(inputs[midpoint-1])
    x=turnaround()
    for i in range(len(add)):
        print(x[i])


    lis1=(inputs[:midpoint2])
    lis2=(inputs[midpoint2:midpoint-1])
    
    i=len(lis2)-1    
    j=len(lis1)
    k=0
    while(i>=0):
        print(lis2[i])
        

        while(k<j):
            print(lis1[k])
            k+=1
        
        i-=1
