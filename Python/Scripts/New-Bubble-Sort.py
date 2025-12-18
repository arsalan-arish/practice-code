'''
Write a function that takes a iList (unsorted) as input, and returns it (sorted)

'''
# Imports

# Functions
def insertion_sort(iList):
    temp = 0
    x = len(iList)
    i = 1


    for j in range (x):
        while(i<x):                   # this loop will carry a round of checking all the elements
            if (iList[i]<iList[i-1]): # this conditional block will check between two elements and swap if not in ascending order
                temp = iList[i]
                iList[i] = iList[i-1]
                iList[i-1] = temp

            i+=1 
    return iList



# Program

iList = [56,24,13,50,5]
oList = insertion_sort(iList)

print("Your unsorted list was:", iList)
print("\n  Your sorted list is:", oList)
