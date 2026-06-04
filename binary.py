lst = [1,2,3,4,5,6,7,8,9,10] 
s = 12 
l = 0
h = len(lst)-1 
while l <= h: 
    m = (l+h)//2 
    if s == lst[m]: 
        print("True")
        break 
    elif s > lst[m]: 
        l = m+1 
    else: 
        h = m-1
print("False")

nums = [5,7,7,8,8,10]
target =  8 
low = 0 
high = len(nums)-1 
left =  -1 
while low <= high: 
    mid  = (low + high)//2 
    if nums[mid] ==  target: 
        left = mid 
        high = mid -1 
    elif nums[mid] < target: 
        low = mid + 1 
    else: 
        high = mid -1 
low =  0 
high = len(nums)-1
right =  -1 
while low <= high: 
    mid = (low+high)//2 
    if nums[mid] == target: 
        right = mid 
        low = mid + 1 

    elif nums[mid] < target: 
        low = mid + 1 
    else: 
        high = mid -1 
print([left, right]) 


