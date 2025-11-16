# Imports (None)


# Functions
def sort_element(iList, w):     # This function takes a List and the index 'w' of the element to sort in the list.
    b = w-1
    if(iList[w]< iList[b]): 
        temp = iList[w]
        iList[w] = iList[b]
        iList[b] = temp
        if (b==0):
            return
        else:
            sort_element(iList, b) #recursion

def insertion_sort(iList):   # This function recieves the input List and gives command to compare() function to sort
    x = len(iList)           # all its elements. Then it returns the sorted list
    for i in range(1,x):     # iList is input List
        sort_element(iList, i)  
    
    return iList




# Program
List = [1,52,24,6,3,251,15,6,2,5,7,2,25,11,55,551,52,5252] # any list
print(List) # Unsorted
insertion_sort(List) # this will sort the list
print(List) # Sorted
