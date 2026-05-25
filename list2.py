# import datetime

# x = datetime.datetime.now()
# print(x)

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

# s = "a good   example"
# y = s.strip() 
# x = y.split() 
# i = 0 
# j = len(x)-1 
# while i < j: 
#     x[i], x[j] = x[j], x[i] 
#     i += 1 
#     j -=1 
# print(' '.join(x)) 

# x  = "pwwkew"
# y = list((set(x)))
# z = len(y) 
# print(z)   

# s = [2,14,18,22,22]
# dic = {} 
# for i in s: 
#     if i not in dic: 
#         dic[i] = 1 
#     else: 
#         dic[i] += 1 
# for k , v in dic.items(): 
#     if v >= 2: 
#         print("True")
#         break  
# else: 
#         print("False") 


# nums = [1,3,5,7,8,9,10] # target = 9 
# s = 0
# r = 10
# l = len(nums)+1 
# while s<=l: 
#     m = (s+l)//2 
#     if nums[m] == r: 
#           print("print found index", m) 
#           break 
#     elif m<r: 
#          s = m+1  
#     else: 
#          l = m-1 


# moves = "DURDLDRRLL"
# dic = {} 
# for i in moves: 
#     if i not in dic: 
#         dic[i] = 1 
#     else: 
#         dic[i] += 1 
# ans = [] 
# for k , v in dic.items(): 
#     if k not in ans: 
#           ans.append(k) 
#           if list('U') in ans and list('D') in ans and ans[list('U')] == ans[list('D')] and list('R') in ans and list('L') in ans and ans[list('R')] == ans[list('L')]: 
#                print("True") 
#           else: 
#                print("False") 

# '''sliding window''' 
# def max_sum_subarray(arr, k): # [2,1,5,1,2,3,2] and # size = k = 3
#     window_sum = sum(arr[:k])# 2+1+5 = 8, 
#     max_sum = window_sum # max-sum = 8 
#     for i in range(k, len(arr)):# 
#           window_sum += arr[i] 
#           window_sum -= arr[i-k] 
#           max_sum = max(max_sum, window_sum) 
#     return max_sum 
# print(max_sum_subarray([2,1,5,1,3,2], 3)) 

    
# def longest_unique(s): 
#      seen = set() 
#      left = 0 
#      max_len = 0 
#      for right in range(len(s)): 
#           while s[right] in seen: 
#                seen.remove(s[left]) 
#                left += 1 
#           seen.add([right]) 
#           max_len = max(max_len, right-left+1) 
     
#      return max_len 
# print(longest_unique("abcabcbb")) 
        
'''sliding window with fixed size''' 
'''max sum subarray of size k''' 
arr = [2,1,5,1,3,2] 
k = 3 
window_sum = sum(arr[:k])#2+1+5 = 8 
max_sum = window_sum # max_sum = 8 

for i in range(k, len(arr)): 
    window_sum = window_sum + arr[i] - arr[i-k] 
    max_sum = max(max_sum, window_sum) 
print(max_sum) 
'''first negative number in every window size k'''
from collections import deque 
arr = [12, -1, -7, 8, -15, 30, 16, 28] 
k = 3 
q = deque() 
result = [] 
for i in range(len(arr)): 
    if arr[i] < 0: 
        q.append(i) 
    if q and q[0] <= i - k: 
        q.popleft() 
    if i >= k - 1: 
        if q: 
            result.append(arr[q[0]]) 
        else: 
            result.append(0) 
print(result) 
'''count distinct elements in every window of size k''' 
arr = [1,2,1,3,4,2,3] 
k = 4 
freq = {} 
result = [] 
for i in range(len(arr)): 
    freq[arr[i]] = freq.get(arr[i], 0) + 1 
    if i >= k: 
        left_element = arr[i-k] 
        freq[left_element] -= 1 
        if freq[left_element] == 0:
            del freq[left_element] 
    if i >= k-1: 
        result.append(len(freq)) 
print(result) 
'''maximum of all subarrays of size k''' 
from collections import deque 
arr = [1, 3, -1, -3, 5, 3, 6, 7] 
k = 3 
dq = deque() 
result = [] 
for i in range(len(arr)): 
    if dq and dq[0] <= i - k: 
        dq.popleft() 
    while dq and arr[dq[-1] < arr[i]]: 
        dq.pop() 
    dq.append(i) 
    if i >= k- 1: 
        result.append(arr[dq[0]]) 
print(result)
'''average of suvarray of size k''' 
arr = [2,1,5,1,3,2] 
k = 3 
window_sum = sum(arr[:k]) 
result = [window_sum / k] 
for i in range(k, len(arr)): 
    window_Sum = window_sum + arr[i] - arr[i - k] 
    result.append(window_sum / k)
print(result) 

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
intervals.sort() 
print(intervals) 

'''3sum'''
nums = [-4,-1,-1,0,1,2] 
nums.sort()
ans = []
for i in range(len(nums)-2): 
    if i > 0 and nums[i] == nums[i-1]: 
        continue
    left = i + 1 
    right = len(nums)-1 
    while left < right: 
        total = nums[i] + nums[left] + nums[right] 
        if total == 0: 
            ans.append([nums[i], nums[left], nums[right]]) 
            while left < right and nums[left] == nums[left+1]: 
                left += 1 
            while left < right and nums[right] == nums[right-1]: 
                right -= 1 
            left += 1 
            right -= 1 
        elif total < 0: 
            left += 1 
        else: 
            right -= 1 
print(ans) 
'''two sum'''
nums = [1,2,3,4,8,6]
target = 10
lst = [] 
for i in range(len(nums)): 
    lst.append((nums[i], i))
lst.sort() 
left = 0 
right = len(lst)-1 
while left < right: 
       total = lst[left][0] + lst[right][0] 
       if total == target: 
           print(lst[left][0], lst[right][0]) 
           left += 1
           right -= 1
       elif total < target: 
           left += 1
       else: 
           right -= 1 
'''3sum closet'''   
nums = [-1,2,1,-4]
target = 1 
nums.sort()
for i in range(len(nums)-2): 
    if i>0 and nums[i] == nums[i-1]: 
        continue
    left = i + 1 
    right = len(nums)-1 
    while left < right: 
        total = nums[i] + nums[left] + nums[right]
        if total > target and total < 3: 
            print(total) 
            while left < right and nums[left] == nums[left+1]: 
                left +=1 
            while left < right and nums[right]  == nums[right-1]: 
                right -=1 
            left +=1  
            right -=1 
        elif total < target and total > target: 
            print(total) 
            left +=1
        else: 
            right -=1 



            