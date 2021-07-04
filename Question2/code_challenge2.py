from typing import Annotated
#Sample inpuit
A = [1,2,3,4,5,6,6,7,8,9,10]
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
#Finds the repeated number in the list, 
#returns the repeated number
def repeatedNum(A):
    copyList = A
    for i in range(0,len(copyList)):
        track = copyList[i]
        copyList.remove(copyList[i])
        if binarySearch(A,0,5,track) != -1:
            return track

print(repeatedNum(A))


 
