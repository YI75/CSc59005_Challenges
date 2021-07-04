#Sample input
A=[[1,2,3],[4,5,6],[7,8,9]]
#Search for 6
#Binary Seach Function with Recursion
def binarySearch(A,low,high,x): 
    if high >= low:
        mid = (high + low)//2
        if A[mid]==x:
            return mid
        elif A[mid] > x: 
            return binarySearch(A, low, mid-1,x)
        else:
            return binarySearch(A, mid+1, high,x)

    else:
        return -1
#Searches the 2x2 matrix for the number m
def searchMatrix(A,num):
   position_i = 0
   position_j = 0
   for index in range(0, len(A)):
       placeHolder = binarySearch(A[index],0,len(A[index])-1,num)
       if (placeHolder != -1):
           position_i = index
           position_j = placeHolder
           return [position_i,position_j] 
   return -1 
#A=[[1,2,3],[4,5,6],[7,8,9]]
print(searchMatrix(A,2))