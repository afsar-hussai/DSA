# for zeros and positive numbers only
# def max_length(arr,k):
#     left=0
#     maxl=0
#     current_sum=0
#     for right in range(len(arr)):
#         current_sum+=arr[right]
#         while current_sum > k and left <= right:
#             current_sum-=arr[left]
#             left+=1
#         if current_sum == k:
#             maxl=max(maxl,right-left+1)
        
#     return maxl
# arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
# k = 3

# print(max_length(arr,k))

## for zeros and negatives and positives also

def max_length_subarray(arr,k):
    # current_sum=0
    # prefix_sum_hash={}
    # max_length=0
    
    # for i in range(len(arr)):
    #     current_sum+=arr[i]
        
    #     if current_sum == k:
    #         max_length=i+1
    #     rem=current_sum-k
        
    #     if rem in prefix_sum_hash:
    #         length=i-prefix_sum_hash[rem]
    #         max_length=max(length,max_length)
    #     if current_sum not in prefix_sum_hash:
    #         prefix_sum_hash[current_sum]=i
    # return max_length
    
    ps={}
    cs=0
    ml=0
    n=len(arr)
    for i in range(n):
        cs+=arr[i]
        if cs in ps:
            ln=i-ps[cs-k]
            ml=max(ln,ml)
        if cs == k:
            ml=i+1
        if cs not in ps:
            ps[cs]=i
    return ml



arr = [1, -1, 5, -2, 3]
k = 3

print(max_length_subarray(arr,k))