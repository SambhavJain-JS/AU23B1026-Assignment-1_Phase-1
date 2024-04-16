""" 

You have been given an ilist of size M that contains 1 and 2. Write a function to arrange them in order.
function name=arrange() 
#You are not allowed to use sort function in this program

Sample Input 1:
1
7
1 2 2 2 1 2 2

Sample Output 1:

1 1 2 2 2 2 2


Sample Input 2:
2
8
2 1 2 2 1 2 1 2
5
1 2 1 2 1

Sample Output 2:
1 1 1 2 2 2 2 2

1 1 1 2 2 

"""
def arrange():
    get = []                                # List to store input lists as strings
    elements = []                           # List to store arranged elements
    length = []                             # List to store lengths of input lists
    
    
    t_list = int(input(""))                 # Number of input lists
    for i in range(t_list):                 #loop to take input and short them
        
        len_input = int(input())            # Length of the current list
        length.append(len_input)            # Add length of string to the length list
        ele = input()                       # Elements of the current list as a string
        get.append(ele)                     # Add the string to the get list


        check1 = 0                          # Counter for '1's
        check2 = 0                          # Counter for '2's
        j=0
        # for j in range(len(ele)) :          #Loop to count '1' and '2'
        while j<len(ele):
            if ele[j] == '1':
                check1 += 1
            else:
                check2 += 1
            j += 2                          #increament of 2 to skip ','

        i = 0
        while i < check1:                    #
            k = 1                            # 
            elements.append(k)               #
            i += 1                           #
                                             #Loop to '1' and '2' in order
        i = 0                                #
        while i < check2:                    #
            k = 2                            #
            elements.append(k)               #
            i += 1                           #

    amount = 0 
    i=0       
    j=0                       
    result = []                                                 #to store arranged string of input
    while(i<t_list):
        amount += length[i]                                     #initialize loop  adding length of string
        arranged_str = ""
        while j<int(amount):                          
            arranged_str += str(elements[j])+' '                
            j += 1
        result.append(arranged_str.rstrip())                    #add arranged string to result list
        i+=1
    return result


arranged_outputs = arrange()

for output in arranged_outputs:                                 #printing arranged output
    print(output)
