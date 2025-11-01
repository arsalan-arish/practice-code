'''
Errors

1- Add order checking in addition & subtraction & Multiplication & all other functions efficiently
2- Add error handling and coefficient matrix function
3- Add feature of rounding off or giving answers in fractions
4- Do 'comment documentation' for readability

Add extra functionality
'''

# Imports
import random
# User functions

def transpose(A):
    ans = []
    for i in range(len(A)):
        templist = []
        for j in range(len(A[0])):
             templist.append(A[j][i])
        ans.append(templist)
    
    return ans
    

    

def minor3x3(A,n): # n is a List representing the index of the element which's minor is to be found
        if len(A) == 3 and len(A[0]) == 3:
            if   n == [0,0]:
                ans = (A[1][1]*A[2][2]) - (A[1][2]*A[2][1])

            elif n == [0,1]:
                ans = (A[1][0]*A[2][2]) - (A[1][2]*A[2][0])

            elif n == [0,2]:
                ans = (A[1][0]*A[2][1]) - (A[1][1]*A[2][0])

            elif n == [1,0]:
                ans = (A[0][1]*A[2][2]) - (A[0][2]*A[2][1])

            elif n == [1,1]:
                ans = (A[0][0]*A[2][2]) - (A[0][2]*A[2][0])

            elif n == [1,2]:
                ans = (A[0][0]*A[2][1]) - (A[0][1]*A[2][0])

            elif n == [2,0]:
                ans = (A[0][1]*A[1][2]) - (A[0][2]*A[1][1])

            elif n == [2,1]:
                ans = (A[0][0]*A[1][2]) - (A[0][2]*A[1][0])

            elif n == [2,2]:
                ans = (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])


            return ans



def cofactor3x3(A,n): # n is a List representing the index of the element which's cofactor has to be found

    # Formula --> (-1)raised to 1 + (sum of indexes of that element) multiplied by its minor
    temp = (-1)**((n[0]+1) + (n[1]+1))
    ans = temp * minor3x3(A,n)

    return ans # returns the cofactor of that element of the list
    


def adjoint(A):
    if len(A) == 2 and len(A[0]) == 2:
        #print(A)
        # Exchange A[0][0] with A[1][1]
        temp    = A[0][0]
        A[0][0] = A[1][1]
        A[1][1] = temp
        # Change the signs of A[0][1] and A[1][0]
        A[0][1] = -A[0][1] 
        A[1][0] = -A[1][0]
        #print(A)
        ans = A
        return ans
    
    elif len(A) == 3 and len(A[0]) == 3:
        # Take cofactor of every element of A to create a new matrix
        ans = []

        for i in range(len(A)):
            templist = []
            for j in range(len(A[0])):
                temp = 0
                temp = cofactor3x3(A,[i,j])
                templist.append(temp)
            ans.append(templist)
        # Then take transpose of the matrix
        ans = transpose(ans)
        return ans


 

def add(A,B): # This function can add matrices of any order 
    ans = []
    for i in range(len(A)):
        tempList1 = []
        for j in range(len(A[i])):
            temp = A[i][j] + B[i][j]
            tempList1.append(temp)
        ans.append(tempList1)
    return ans

    
    
def subtract(A,B):  # This function can subtract matrices of any order 
    ans = []
    for i in range(len(A)):
        templist = []
        for j in range(len(A[i])):
            temp = A[i][j] - B[i][j]
            templist.append(temp)
        ans.append(templist)
    return ans


def scalarmultiply(A,n): # This function can multiply matrix of any order with a scalar
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]*=n

    ans = A
    return ans


def scalardivide(A,n):  # This function can divide matrix of any order with a scalar
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]/=n

    ans = A
    return ans



def multiply(A,B):

    B = transpose(B)
    ans = []
    for i in range(len(A)):
        templist = []
        for j in range(len(B[0])):
            temp = 0
            temp = A[i][0]*B[j][0] + A[i][1]*B[j][1]
            templist.append(temp)
        ans.append(templist)
    
    return ans


def determinant(A):
    if len(A) == 2 and len(A[0]) == 2:
        ans = (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])
        return ans
    elif len(A) == 3 and len(A[0]) == 3:
        ans = A[0][0]*minor3x3(A,[0,0]) - A[0][1]*minor3x3(A,[0,1]) + A[0][2]*minor3x3(A,[0,2])
        return ans


def inverse(A):
    # Adjoint / Determinant
    ans = scalardivide(adjoint(A),determinant(A))
    return ans


def create_matrix(r,c):
    ans = []

    for i in range(r):
        templist = []
        for j in range(c):
            n = random.randint(1,99)
            templist.append(n)
        ans.append(templist)

    return ans



# Sample Matrices

A = [[2, -3], [5, 4]]                   # 2x2
B = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]   # 3x3
C = [[1, 2, 3],[4, 5, 6]]               # 2x3
D = [[7, 8],[9, 10],[11, 12]]           # 3x2



