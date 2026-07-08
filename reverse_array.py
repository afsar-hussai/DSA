import time

def reverse_arr_On(arr)->None:
    n=len(arr)
    
    l=0
    r=n-1
    
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
        

def reverse_arr_On2(arr):
    n=len(arr)
    
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        
    
arr=[1,2,3,4,5,6,7,8,9]

print(f"Before reverse: {arr}")
s=time.time()
reverse_arr_On(arr)

# reverse_arr_On2(arr)

print(f"After reverse: {arr} \nand time taken: {time.time() - s} ")

