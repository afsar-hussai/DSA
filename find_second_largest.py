arr=[2,5,8,3,1,9,4]

largest=float('-inf')
slargest=float('-inf')

n=len(arr)

for i in range(n):
    if arr[i]>largest and arr[i]> slargest:
        slargest=largest
        largest=arr[i]
    if arr[i]>slargest and arr[i]!=largest:
        slargest=arr[i]
        

print(f"second largest is: {slargest}")