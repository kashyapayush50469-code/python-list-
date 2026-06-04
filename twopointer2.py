'''reverse an array''' 
arr = [1, 2, 3, 4, 5] 
i = 0# 0,1,2
j = len(arr)-1#4,3,2 
while i < j: #0<4,1<3,2<2(false)
    arr[i], arr[j] = arr[j], arr[i]#[5,4,3,2,1] 
    i += 1 #1,1
    j -= 1 #-1,-1
print(arr) #[5,4,3,2,1] 
'''check palindrome string''' 
s = "madam" 
i = 0 #0,1,2
j = len(s)-1#4,3,2 
p = True # True
while i<j: #0<4,1<3,2<2(false)
    if s[i] != s[j]:# 
        p = False 
        break 
    i += 1 # 1, 1,
    j -= 1 # -1,-1
print(p) #true("madam")
'''count vowels from both sides''' 
s  = "education" 
i,j =0, len(s)-1# 0, 8
count = 0 # 0
v = "aeiou" #"aeiou"
while i<=j: #0<=8
    if s[i] in v:#e 
        count += 1 # 1
    if i != j and s[j] in v: 
        count += 1 
    i += 1 
    j -= 1 
print(count) # count = 5
'''count pairs with sum<target''' 
arr = [1, 2, 3, 4] 
target = 5 #5
i,j = 0, len(arr)-1 # 0,1, 3,2,1
count = 0 # 1
while i < j: # 0<3,0<2,1<2,1<1(false)
    if arr[i] + arr[j] < target: # 1+4<5 ,4<5,5<5
        count  += (j -i) # 0+2-0 = 2
        i += 1 # 1
    else: 
        j -= 1 # -1,-1
print(count) # 2
'''check if array is sorted''' 
arr = [1, 2, 3, 4, 5] 
i = 0; j = 1 # i = 0,1,2,3j = 1,2,34
f = True # True
while j < len(arr): # 1<5,2<5,3<5,4<5,5<5(false)
    if arr[i] > arr[j]: #flase
        f = False 
        break 
    i += 1 # 1, 1,1,1
    j += 1 # 1, 1,1,1
print(f)# True 
'''reverse words in list''' 
words = ["I","love","python"] 
i, j = 0, len(words)-1 # i = 0,1, j = 2,1
while i < j: # 0<2,1<1(false)
    words[i], words[j] = words[j], words[i] #'['python','love','I'] 
    i += 1 # 1
    j -= 1 # -1
print(words) #'['python','love','I'] 
'''remove spaces from both ends''' 
s = " hello " 
i, j = 0, len(s)-1 # i=0,1j=5
while s[i] ==" ": # it's a true condition.
    i += 1 # 1
while s[j] == " ": # it's a also true condtition.
    j -= 1 # -1
print(s[i:j+1]) #"hello"
'''Merge two sorted array'''  
a = [1, 3, 5] 
b = [2, 4, 6] 
i = j = 0 # i=0,1,2 j=0
res = [] # []
while i < len(a) and j < len(b): 
    if a[i] < b[j]: # 1<2,
        res.append(a[i]); i += 1 #[1,3,5] 
    else: 
        res.append(b[j]); j += 1 #[2,4,6]
res += a[i:] + b[j:] #[1,2,3,4,5,6]
print(res) 
'''find first mismatch''' 
s = "abcde" 
t = "abfde" 
i, j = 0, 0 # i =0,1,2 j = 0,1,2
while i < len(s): #0<5,1<5,2<5
    if s[i] != t[j]: #a!=a,b!=b,C!=f
        print(s[i]) # c
        break # break
    i += 1; j +=1 # 1, 1, 1, 1
'''check reverse equality''' 
a = [1,2, 3] 
b = [3, 2, 1] 
i , j = 0, len(b)-1#i=0,1,2j=2,1,0 
f = True #f=True
while i < len(a):#0<3,1<3,2<3,3<3
    if a[i] != b[j]: #1!=1,2!=2,3!=3
        f = False 
        break 
    i += 1; j -=1 #1,-1,1,-1
print(f) #True
'''swap alternate elements''' 
arr = [1, 2, 3, 4] 
i = 0  # i = 0 
while i < len(arr)-1: #0<3,
    arr[i], arr[i+1] = arr[i+1], arr[i] #[2,1,4,3] 
    i += 2 
print(arr) #[2,1,4,3] 
'''find middle element''' 
arr = [1, 2, 3, 4, 5] 
i , j = 0, len(arr)-1 #i=0
while i < j: #0<5
    i +=1; j -= 1 # 1, -1  
print(arr[i]) # 3

s = 123 
num = str(s) 
rev ="" 
for i in num: 
    rev = i + rev 
print(int(rev)) 


'''1.Twosum(return indices)''' 
def two_sum(arr, target):
    d = {}#{}
    for i in range(len(arr)):#0,1,2,3
        diff = target - arr[i]# diff = 9-2 = 7,9-7=2
        if diff in d:
            return [d[diff], i]
        d[arr[i]] = i #{2,7}

print(two_sum([2,7,11,15], 9))

'''2.triplet sum''' 
def triplet_sum(arr, target):
    arr.sort()#[1,2,3,4,5]
    n = len(arr) # 5

    for i in range(n-2):#5-2 = 3 ,0,1,2
        left = i + 1 # 0+1 = 1+1 = 2 
        right = n - 1 # 5-1= 4

        while left < right:#1<4,2<4
            s = arr[i] + arr[left] + arr[right]#1+2+5 = 8, 1+3+5=9

            if s == target:#9==9
                return [arr[i], arr[left], arr[right]]#answer = [1,3,5] 
            elif s < target:#8<9
                left += 1# 1
            else:
                right -= 1

print(triplet_sum([1,2,3,4,5], 9))
'''3.remove element''' 
def remove_element(arr, val):
    k = 0#k = 0, 1 
    for i in range(len(arr)):#0, 1, 2, 3
        if arr[i] != val: #3!=3, 2 != 3
            arr[k] = arr[i]#[2,2,3]
            k += 1 # 1
    return arr[:k]


print(remove_element([3,2,2,3], 3))
'''4.container''' 
def max_area(height):
    left, right = 0, len(height) - 1 # 0,1 r = 8,7 
    max_water = 0 # 0 

    while left < right:#0<8, 1<8, 
        h = min(height[left], height[right]) # h = min(1, 7) h = 1,7
        w = right - left # 8 - 0 = 8 , 8 -1 = 7
        max_water = max(max_water, h * w) # max_water = 8, 49

        if height[left] < height[right]: # 1<7, 8<7
            left += 1 # 1
        else:
            right -= 1 # -1 

    return max_water # The final answer will be:– 49 

print(max_area([1,8,6,2,5,4,8,3,7]))
'''5.valid palndrome'''  
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left, right = 0, len(s) - 1# 0,1,2j = 3,2,1

    while left < right:#0<3,1<2,2<1(false)
        if s[left] != s[right]:#a!=a,b!=c
            return (is_palindrome(s, left+1, right) or #i = 1, j = -1
                    is_palindrome(s, left, right-1))
        left += 1#1,
        right -= 1#-1

    return True#True

print(valid_palindrome("abca"))
'''6.square of sorted array''' 
arr = [-4, -1, 0, 3, 10]

n = len(arr)#5
result = [0] * n # [0,1,9,16,100]

i = 0 # 0,1
j = n - 1 #4,3,2
k = n - 1 #4 ,3,2,1

while i <= j:#0<=4,0<=3,1<=3,1<=2
    if abs(arr[i]) > abs(arr[j]):#-4>10, 4>3, 1>3,1>0
        result[k] = arr[i] ** 2 # 16,1
        i += 1
    else:
        result[k] = arr[j] ** 2 # 100,9
        j -= 1# -1,-1,
    k -= 1# -1,-1

print(result)

def intersection(nums1, nums2):
    nums1.sort() # [1,2,3,4,5,8,45]
    nums2.sort() # [2,3,4,12,23,56,80]
    
    i, j = 0, 0 # i = 0,1 ,j =0 
    result = [] # []
    
    while i < len(nums1) and j < len(nums2): # 0<7and 0<7
        if nums1[i] == nums2[j]:#2==2,
            # avoid duplicates
            if not result or result[-1] != nums1[i]:#/
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:#1<2,
            i += 1# 1 
        else:
            j += 1
    
    return result
a = [1, 2, 3, 4, 5, 8, 45] 
b = [2, 3, 4, 56, 23, 12,80]
print(intersection(a, b)) 
'''find duplicates.'''
def find_duplicates(nums):
    nums.sort()#[1,2,3,3,,34,5,6,8]
    i = 1 # 1,2,3,4 
    duplicates = []# []
    
    while i < len(nums):#1<9,2<9,3<9
        if nums[i] == nums[i - 1]: # 2 == 1,3==2,3==3
            duplicates.append(nums[i])#[3,3]
        i += 1# 1,1,1
    
    return duplicates
print(find_duplicates([1, 2, 3, 4, 3, 5, 6, 3, 8])) #[3,3]
'''mininum difference pair''' 
def min_diff_pair(nums):
    nums.sort()# [1,2,3,4,5,6,7,8]
    min_diff = float('inf')# sabse bara number
    
    for i in range(1, len(nums)):#1,
        min_diff = min(min_diff, nums[i] - nums[i - 1]) #1-0= 1, 2-1=1
    
    return min_diff
print(min_diff_pair([1, 2, 3, 4, 5, 6, 8]))#findal output = 1 

'''colset sum pair''' 
def closest_sum(nums, target):
    nums.sort() #[1,2,3,3,4,5,6,7]
    i, j = 0, len(nums) - 1 # 0,1, 7 
    
    closest = float('inf')# sabse bara number. 
    
    while i < j: # 0<7,1<7
        curr_sum = nums[i] + nums[j] #1+7=8
        
        if abs(target - curr_sum) < abs(target - closest):#6-8<6-inf=2<inf
            closest = curr_sum
        
        if curr_sum < target:#8<6
            i += 1# 1
        else:
            j -= 1
    
    return closest
print(closest_sum([1,2,3,4,5,3,6,7], 6)) #the final output = 6 
'''count unique element''' 
def count_unique(nums):
    if not nums:# [] list is not empty
        return 0 # return 0 
    
    nums.sort()#[1,1,2,2,3,3,4,5]
    count = 1 # count = 1
    
    for i in range(1, len(nums)): # i = 1
        if nums[i] != nums[i - 1]: # 1 != 1 , so on, 4 != 5(true)
            count += 1
    
    return count
print(count_unique([1,1,2,2,3,3,4,5])) # Then the unique element is 5
'''sort dutch flag''' 
def sortcolors(nums): 
    low=mid=0#0
    high = len(nums)-1#7  
    while mid<=high:#0<=7
        if num[mid] ==0:#
            nums[low], nums[mid] = nums[mid], nums[low] 
            low += 1 
            mid += 1 
        elif nums[mid] == 1:# 1 ==1  
            mid += 1 # mid = 1
        else: 
            nums[mid], nums[high] = nums[high], nums[mid] 
            high -= 1 
print(sortcolors(1,2,3,4,5,5,6,7))
'''max pair product'''   
def maxProduct(nums): 
    nums.sort() 
    return max(nums[-1]*nums[-2], nums[0]*nums[1]) 
a = [1,2,3,4,5,6,9,8,4,2,5]
print(maxProduct(a))

'''partition Negatives positives''' 
def partition(nums): 
    left, right = 0, len(nums)-1 
    while left<=right: 
        if nums[left]<0: 
            left += 1 
        elif nums[right] >= 0: 
            right -= 1 
        else: 
            nums[left], nums[right] = nums[right], nums[left] 
print(partition([1,2,2,23,4,34,234,2423,234,234]))

'''compamre string '''
def compare(s1, s2):
    return s1.lower() == s2.lower()

'''check anagram''' 
def isAnagram(s, t):
    return sorted(s) == sorted(t) 

'''reverse only letters''' 
def reveseonlyletters(s): 
    s = list(s) 
    left, right  = 0, len(s)-1 
    while left<right: 
        if not s[left].isalpha(): 
            left += 1 
        elif not s[right].isalpha(): # its very simple two pointer program 
            right -= 1 
        else: 
            s[left], s[right] = s[right], s[left] 
            left += 1 
            right -= 1 
    return ''.join(s) 
print(reveseonlyletters(['dd-ct']))
'''longest substring without repeating character''' 
s = "pwwkew" 
char_set = set() # set() 
left = 0 # 0,1,2,3,4,5
max_len = 0 # 0 
for right in range(len(s)): # 0,1,2,3,4,5  
    while s[right] in char_set:# p,w,k,e
        char_set.remove(s[left]) # p(p was rmoved here by s[left]), same = w, k, e 
        left += 1 # left = 1, 2,3,4
    char_set.add(s[right]) # p was adding here by right by s[right], same add w,k ,e,w, 
    max_len = max(max_len, right-left+1)# (0, 0-1+1) = 0(no count), then (0, 1-2+1)= 0, 2-2+1 = 1, 3-3+1 = 1, 4-4+1 = 1   
print(max_len) # then final answer is 3
'''find pivot index''' 
def pivotindex(nums):
    total = sum(nums)# 28
    left_sum = 0#0,1,8, 11
    for i in range(len(nums)):#0,1,2, 
        if left_sum == total - left_sum - nums[i]:#0 == 28 - 0 - 1,1 == 28 - 1 -7 = 20, 8 == 28 - 8-3 = 17 11 == 28 - 11 -6 = 11 and 11 == 11 its right   
            return i 
        left_sum += nums[i]# 0 + 1 = 1+7 = 8+3 = 11 
    return -1
print(pivotindex([1,7,3,6,5,6]))# 11=11 then its right and index will be 3(6)
'''remove duplicates from string'''
def removeduplicates(s): 
    seen = set()# set() 
    result = [] # []
    for ch in s:# p
        if ch not in seen:# p 
            seen.add(ch)# adding p
            result.append(ch)#[p]
    return ''.join(result) 
print(removeduplicates("programming")) 

'''two pointer'''
def removeDuplicatesTwoPointer(s):
    s = list(s)
    seen = set()
    i = 0
    for j in range(len(s)):
        if s[j] not in seen:
            seen.add(s[j])
            s[i] = s[j]
            i += 1
    return ''.join(s[:i])
print(removeDuplicatesTwoPointer("programming"))
 

