## Time complexity is O(logN)
## space complexity: O(1)

## For Binary search it needs to be first in sorted order of ascending

##Traditional Binary search


A=[-3,-2,0,1,5,7]

def binary_search(array,target):
    N=len(array)
    L=0
    R=N-1
    
    while L<=R:
        M=(L+R)//2 # or for efficiency and to avoid variable overload we can use L+((R-L)//2)
        if array[M] == target:
            return True
        elif target > array[M]:
            L=M+1
        else:
            R=M-1
    
    return False

print(binary_search(A,5))
        

## conditon based binary search, means here we find first True index

B=[False,False,False,True,True,True]

def condition_binary_search(arr):
    N=len(arr)
    L=0
    R=N-1
    while L < R:
        M=(L+R)//2
        if arr[M]:
            R=M
        else:
            L=M+1
    return L

print(condition_binary_search(B))