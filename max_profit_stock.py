arr=[7,1,5,3,6,4]

min_element=arr[0]
profit=0

for num in arr[1:]:
    current_profit=num-min_element
    profit=max(current_profit,profit)
    min_element=min(min_element,num)

print(profit)