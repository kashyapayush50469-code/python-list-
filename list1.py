'''1.Find the second largest element in a list without using sort().'''
def largest_fun():
    lst = [12, 15, 17, 18, 20] 
    largest = lst[0] # 12, 15, 17, 18
    second = lst[0]  # 12 , 15, 17
    for i in lst:  # 12, 15 , 17, 18, 20 
        if i > largest:  # 12 > 12, 15 > 12, 17> 15, 18 > 17 , 20 > 18
            second = largest # second = 12, 15 17, 18
            largest = i # largest = 15 , 17, 18, 20 
        elif i > second and i != largest: #12 > 12 and 12 != 12 
            second = i 
    print("second largest:", second) # 18 
largest_fun() 

'''2.find the third smallest element in a list''' 
def smallest_third(num): # num = [1, 2, 4, 6, 7, 5, 2]
    num.sort()    # num = [1, 2, 2, 4, 5, 6, 7] 
    set(num)      # {1, 2, 4, 5, 6, 7}
    x = list(num)  # x = [1, 2, 4, 5, 6, 7]
    y = x[3:4] [0] # y = [4] [0] = 4 
    print(y)  # y = 4 
smallest_third(num=[1, 2, 4, 6, 7, 5, 2])
    
'''3.Check if a list contains duplicate elements.'''
def find_duplicate(nums): # nums = [1, 2, 3, 4, 5, 2,3, 2, 7]
    if len(nums) != len(set(nums)): # 9 != 6  because this condition is true so that will not go to the else condition.
        print("Ture")  # True
    else: 
        print("false")
find_duplicate(nums=[1, 2, 3, 4, 5, 2, 3, 2, 7] ) 

'''another method''' 
def find_duplicate(n): # n = [1, 2, 3, 4, 5, 2, 3, 2, 7]
    x = set()  # x = {"set(5)":[1,2,3,4,5]}
    for i in n: # 1,2,3,4,5,2 the loop will false because if any character will repeat then it will return True.
        if i in x: 
            return "True" # True
        x.add(i) # 1,2,3,4,5 # the next character will not satisfy because it will be  a repeating chracter.
    return "false" 
print(find_duplicate(n=[1, 2, 3, 4, 5, 2, 3, 2, 7])) 

'''4.Find all duplicate elements in a list.'''
def find_dup(text):
    x = set() # x = {"set(5)": [1, 2, 3, 4, 5]}
    duplicates = set() # d = {"set(2)": [2, 3]}
    for i in text: # 1, 2, 3, 4, 2 ,5, 2, 3
        if i in x: 
            duplicates.add(i) # 2 , 3
        else: 
            x.add(i) # 1, 2, 3, 4, 5
    return list(duplicates) 
print(find_dup(text=[1, 2, 3, 4, 2, 5, 2, 3]))  


text = [1, 2, 3, 4, 2, 5, 2] 
duplicates = [] 
for i in range(len(text)): 
    for j in range(i+1, len(text)): 
        if text[i] == text[j] and text[i] not in duplicates: 
            duplicates.append(text[i]) 
            print(duplicates) 

'''5.Count the frequency of each element in a list.'''
x = [1, 2, 2, 3, 3, 3, 4]
freq = {} # {1:1, 2:2, 3:3, 4:1}
for num in x: # num = 1, 2, 2, 3, 3, 3, 4 
    if num in freq: # 1, 2, 3, 4
        freq[num] += 1  
    else: 
        freq[num] = 1 
print(freq) 

'''6.find the most frequency element in a list.''' 

num1 = [1, 3, 2, 3, 4, 3, 2, 1, 3] 
freq = {} # {1:2, 2:2 , 3:4, 4:1}
for item in num1: # 1, 3, 2, 3, 4,3, 2, 1, 3
    freq[item] = freq.get(item, 0) + 1 # basically it counts how many times each numbers appear.
most_frequent = max(freq, key=freq.get) # 3:4 
print("mostfrequent element:", most_frequent) 

'''7.Find the least frequent element in a list.'''
num1 = [1, 3, 2, 3, 4, 3, 2, 1, 3] 
freq = {} 
for item in num1:   ## same as the question number 6. 
    freq[item] = freq.get(item, 0) + 1 
least_frequent = max(freq, key=freq.get) 
print("Least frequent element:", least_frequent) 
'''8.check if two list are equal without using ==''' 
num1 = [1, 3, 2, 3, 4, 3, 2, 1, 3] 
num2 = [1, 3, 2, 3, 4, 3, 2, 1, 3] 
if num1 is not num2: 
    print("True") 
else: 
    print("False") 

def list_equal(a, b): # a = [1, 2, 3] and b = [1, 2, 3]
    if len(a) != len(b): # 3 != 3 
        return False  # this condition is not true because 3 is same as 3.
    
    for i in range(len(a)): # 0, 1, 2
        if a[i] != b[i]:  # 1, 2, 3 != 1, 2, 3 
            return False  # this condition is not true.
    return True # so as we can see this condition is match and returns the value is true.
list1 = [1, 2, 3] 
list2 = [1, 2, 3] 
print(list_equal(list1, list2)) 

'''9.check if two lists are permutations of each other''' 
def permutations(lst1, lst2): 
    if len(lst1) != len(lst2): 
        return False 
    freq = {} 
    for i in lst1: 
        freq[i] = freq.get(i, 0) + 1 
    
    for i in lst2: 
        if i not in freq or freq[i] == 0: 
            return False 
        freq[i] -= 1  
    return True 
a  = [1, 2, 2, 3] 
b = [2, 1, 3, 2] 
print(permutations(a, b))

'''10.Find common elements between two lists without using set.''' 
def common_elements(lst1, lst2): 
    lst1.sort() # [1,2,3,4]
    lst2.sort() # [3,4,5]
    i = j = 0 # j = i = 0
    result = [] # []
    while i < len(lst1) and j< len(lst2): # 4 < 4 and 3 < 3  
        if lst1[i] == lst2[j]: # 3 == 3, 4 == 4 
            if lst1[i] not in result: 
                result.append(lst1[i]) #[3, 4]
            i += 1 # i = 4
            j += 1 # i = j = 4
        elif lst1[i] < lst2[j]: # 1<3, 2 < 3, 
            i += 1  # i = 2 , i = 3 
        else: 
            j += 1 
    return result # [3, 4] answer.
a = [4, 2, 1, 3] 
b = [3, 4, 5] 
print(common_elements(a, b)) 

'''11.Reverse a list without using slicing or reverse()''' 
def reverse_list(lst):  
    left = 0 # 0
    right = len(lst) -1 # 5 
    while left < right: 
        lst[left], lst[right] = lst[right], lst[left] # 1 = 5 , 2 = 4 , 3 = 3, 4 = 2 5 = 1
        left += 1 # 
        right -= 1 
    return lst 
x = [1, 2, 3, 4, 5] 
print(reverse_list(x)) 

'''another basic method''' 
def reverse_lst(lst): 
    result = [] # [3,2,1]
    for i in range(len(lst)-1, -1, -1): # 3, 2, 1 
        result.append(lst[i]) 
    return result 
y = [1, 2, 3] 
print(reverse_lst(y)) 

'''12.Rotate a list left by k positions.'''
def left_rotate(lst, k): 
    n = len(lst) 
    k = k % n 
    return lst[k:] + lst[:k] 
a = [1, 2, 3, 4, 5] 
print(left_rotate(a, 2)) 


def reverse(lst, start, end): 
    while start < end: 
        lst[start] , lst[end] = lst[end], lst[start] 
        start += 1 
        end -= 1 
def left_rotate(lst, k): 
    n = len(lst) 
    k = k % n 

    reverse(lst, 0, k-1) 
    reverse(lst, k, n-1) 
    reverse(lst, 0, n-1) 

    return lst 
a = [1, 2, 3, 4, 5] 
print(left_rotate(a, 2)) 

'''13.Rotate a list right by k positions.'''
def reverse(lst, start, end): 
    while start < end: 
        lst[start], lst[end] = lst[end], lst[start] 
        start  +=1 
        end-=1 
def right_rotate(lst, k): 
    n = len(lst) 
    k = k % n 
    
    reverse(lst, 0, n-1) 
    reverse(lst, 0, k-1) 
    reverse(lst, 0, n-1) 

    return lst 
a = [1, 2, 3, 4, 5] 
print(right_rotate(a, 2))
'''14.Remove all occurrences of a given element.'''
l = [1, 2, 3, 2, 4, 2, 5] # [1, 2, 3, 2,4, 2, 5]
element = 2 # element = 2 

while element in l:  # 2 in l;
    l.remove(element) # [1, 3, 4, 5] the right answer.

print(l)  
'''15.Replace every element with the next greatest element.'''
arr = [16, 17, 4, 3, 5, 2] # [16, 17, 4, 3, 2, -1] # final list = [17, 5, 5, 5, 2, -1]
max_right = -1 # -1, 2, 5
for i in range(len(arr)-1, -1, -1): # len(i) = 5
    temp = arr[i] # temp = 2, 5, 3
    arr[i] = max_right # 2 = -1 it means the position of 2 change into -1 , 5 = 2, 3 = 5 
    if temp > max_right: # 2 > -1 , 5 > 2 , 3 > 5(this condition is false so the next excution is not allowed)
        max_right = temp # max = 2, 5
print(arr) 
'''16.Move all zeros to the end of the list.'''
def move_zeros_end(nums): 
    j = 0 # 0, 1 , 2, 3
    for i in range(len(nums)): # 0, 1, 2, 3, 4, 5 
        if nums[i] != 0: # 0 != 0, 1 != 0 , 0 != 0 , 3 != 0 ,12!=0, 34 != 0  
            nums[j], nums[i]  = nums[i], nums[j] # [1, 3, 12, 34, 0, 0] 
            j += 1 
    return nums # [1, 3, 12, 34, 0, 0]
nums=[0, 1, 0, 3, 12, 34] 
print(move_zeros_end(nums)) 
'''17.Move all negative numbers to the beginning'''
def move_negatives_start(lst):  
    j = 0 
    for i in range(len(lst)): 
        if lst[i] < 0: 
            lst[j], lst[i] = lst[i], lst[j] 
            j += 1 
    return lst 
lst = [1, -2, -3, -5, 5, 3] 
print(move_negatives_start(lst)) 
'''18.Convert a list into a dictionary of index–value pairs.'''
def list_to_dict(lst): 
    return dict(enumerate(lst)) 
lst = ['a', 'b', 'c', 'd'] # {0:'a', 1:'b', 2:'c', 3:'d'}
print(list_to_dict(lst)) 
'''19.Convert a list into a nested list of pairs'''
def list_to_pairs(lst): 
    return [[i, val] for i, val in enumerate(lst)]
lst = ['x', 'y', 'z'] #[[1, 'x'], [2,'y'], [3,'z']] 
print(list_to_pairs(lst)) 
'''20.Flatten a nested list of arbitrary depth''' 
def flatten(lst): 
    result = [] 
    for item in lst: 
        if isinstance(item, list): 
            result.extend(flatten(item)) 
        else: 
            result.append(item) 
    return result 
lst = [1, [2, [3, 4], 5], 6] 
print(flatten(lst))  
'''21.implement buble sort using lists''' 
def bubble_sort(lst): #[5,2,9,1]
    n = len(lst) # n = 4 
    for i in range(n): # 0, 1, 2, 3 
        for j in range(0, n-i-1): # 4-0-1 = 3(0, 3), 4-1-1(0, 2), 4-2-1(0, 1), 4-3-1(0, 0)
            if lst[j] > lst[j+1]: # 5 > 2, 5>9(false), 9 > 1, 2>5(false), 5>1 , 2>1 next i = 3 in j condition is false so it does not work this condition . 
                lst[j], lst[j+1] = lst[j+1], lst[j] # [1, 2, 5, 9] 
    return lst # [1, 2, 5, 9]
print(bubble_sort([5,2,9,1])) 
'''22.implement selection sort using lists''' 
def selection_sort(lst): 
    n = len(lst) # n =  4 
    for i in range(n): # 0, 1, 2, 3
        min_dx = i   # 0 ,1
        for j in range(i+1, n): # 1,2,3, 2,3
            if lst[j] < lst[min_dx]: #2<5,9<2,1<2,9<5(false),1<5
                min_dx = j # mindx = 2, 1
        lst[i], lst[min_dx] = lst[min_dx], lst[i] # [2,5,9,1], [1,5,9,2]
    return lst 
print(selection_sort([5,2,9,1])) # [1,2,5,9]
'''23.implement insertion sort using lists''' 
def insertion_sort(lst): 
    for i in range(1, len(lst)):# 1,2,3
        key = lst[i] # key = 2,9,1               
        j = i -1# 1-1 = 0, 2-1 = 1, 3-1 = 2 
        while j >= 0 and lst[j] >key:# 0 >= 0 and 5 > 2, 1 >= 0 and 2 > 9(false), 2 >= 0 and 9 > 1 
            lst[j+1] = lst[j]# 2 = 5, 1 = 9 
            j -= 1 # -1,-1 
        lst[j+1] = key # 5 = 2, 9 = 9, 5 = 1  
    return lst 
print(insertion_sort([5,2,9,1])) #the final answer is [1,2,5,9]
'''24.implement merge sort using list''' 
def merge_sort(lst): 
    if len(lst) <= 1: 
        return lst 
    mid = len(lst) // 2 
    left = merge_sort(lst[:mid]) 
    right = merge_sort(lst[mid:]) 
    return merge(left, right) 
def merge(left, right): 
    result = [] 
    i = j = 0 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
    result.extend(left[i:]) 
    result.extend(right[j:]) 
    return result 
print(merge_sort([5,2,9,1])) 
'''25.implement quick sort using list''' 
def quick_sort(lst): 
    if len(lst) <= 1: 
        return lst 
    p = lst[0] 
    left = [x for x in lst[1:] if x <= p] 
    right = [x for x in lst[1:] if x > p] 
    return quick_sort(left) + [p] + quick_sort(right) 
print(quick_sort([5,2,9,1]))
'''26.Find pairs whose sum equals a target value''' 
def find_pairs(lst, target): 
    s = set() 
    result = [] 
    for num in lst: 
        if target - num in s: 
            result.append([num, target-num]) 
        s.add(num) 
    return result 
print(find_pairs([1, 2, 3, 4, 5], 6)) 
'''27.find the triplets whose sum equals zero''' 
def there_sum(lst): 
    lst.sort() 
    result = [] 
    for i in range(len(lst)-2): 
        if i > 0 and lst[i] == lst[i-1]: 
            continue 
        left, right = i+1, len(lst)-1 
        while left < right: 
            total = lst[i] + lst[left] + lst[right] 
            if total ==0: 
                result.append([lst[i], lst[left], lst[right]]) 
                left += 1 
                right -= 1 
                while left < right and lst[left] == lst[left-1]:
                    left += 1 
                while left < right and lst[right] == lst[right+1]: 
                    right -= 1 
            elif total<0: 
                left += 1 
            else: 
                right -= 1 
    return result 
print(there_sum([-1,0,1,2,-1,-4])) 
'''28.find the maximum product of two numbers:''' 
def max_product(lst): 
    lst.sort() 
    return max(lst[-1]*lst[-2], lst[0] * lst[1]) 
print(max_product([1, 10, -5, 1, -100 ]))
''''29.find the maximum difference between two elements''' 
def max_difference(lst):
    min_val = lst[0] 
    max_diff = float('-inf') 
    for num in lst[1:]: 
        max_diff = max(max_diff, num - min_val) 
        min_val = min(min_val, num) 
    return max_diff 
print(max_difference([2, 3, 10, 6, 4 ,8, 1])) 
'''30.find all sublists with sum equal to k'''
def subarryas_with_sum(lst, k): 
    prefix_sum = 0 
    hashmap = {0:1} 
    count = 0 
    for num in lst: 
        prefix_sum += num 
        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum-k] 
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1 
    return count 
print(subarryas_with_sum([1,1,1], 2)) 
'''31.sort a list without using built-in functions''' 
def sort_list(lst): 
    n = len(lst) 
    for i in range(n): 
        for j in range(n-i-1): 
            if lst[j] > lst[j+1]: 
                lst[j], lst[j+1] = lst[j+1] , lst[j] 
    return lst 
print(sort_list([5,3,1,4]))
'''32.sort a list of tuples by second element '''
def sort_by_second(lst): 
    return sorted(lst, key=lambda x: x[1]) 
lst = [(1, 3), (4, 1), (2, 2)] 
print(sort_by_second(lst)) 
'''33.sort a list based on frequency of elements''' 
from collections import Counter 
def sort_by_frequency(lst): 
    freq = Counter(lst) 
    return sorted(lst, key=lambda x :(-freq[x], x)) 
print(sort_by_frequency([4,5,6,5,4,3])) 

'''34.sort a list of strings by their length''' 
def sort_by_length(lst): 
    return sorted(lst, key=len) 
print(sort_by_length(["apple", "kiwi", "banana"])) 

'''35.sort a list containig numbers and strings separatley''' 
def sort_mixed(lst): 
    nums = sorted([x for x in lst if isinstance(x, (int, float))]) 
    strs = sorted([s for s in lst if isinstance(s, str)]) 
    return nums + strs 
print(sort_mixed([3, "apple",1, "banana",2])) 
'''36.find the maximum subarray sum''' 
def max_subarray_sum(lst): 
    max_sum = curr_sum = lst[0] 
    for num in lst[1:]: 
        curr_sum = max(num, curr_sum+num) 
        max_sum = max(max_sum, curr_sum) 
    return max_sum 
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 
'''37.find the minimum subarray sum''' 
def min_subarray_sum(lst): 
    min_sum = curr_sum = lst[0] 
    for num in lst[1:]: 
        curr_sum = min(num, curr_sum+num) 
        min_sum = min(min_sum, curr_sum) 
    return min_sum 
print(min_subarray_sum([3, -4, 2, -3, -1, 7, -5]))
'''38.find all prime numbers in a list'''  
def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1): 
        if n % i ==0: 
            return False 
    return True 
def find_prime(lst): 
    return [x for x in lst if is_prime(x)] 
print(find_prime([1, 2, 3, 4, 5, 10, 13]))
'''39.find the median of a list without sorting''' 
import random 
def quickselect(lst, k): 
    p = random.choice(lst)
    lows = [x for x in lst if x < p]
    high = [x for x in lst if x > p] 
    p1 = [x for x in lst if x == p] 

    if k < len(lows): 
        return quickselect(lows, k) 
    elif k < len(lows) + len(p1): 
        return p 
    else: 
        return quickselect(high, k - len(lows) - len(p1))
def median(lst): 
    n = len(lst) 
    if n % 2 == 1: 
        return quickselect(lst, n//2) 
    else: 
        return (quickselect(lst, n//2 - 1) + quickselect(lst, n//2))/2
print(median([7, 1, 3, 4, 5]))
'''40.find the mode of a list''' 
from collections import Counter 
def find_mode(lst): 
    freq = Counter(lst) 
    max_freq = max(freq.values()) 
    return [key for key, val in freq.items() if val == max_freq] 
print(find_mode([1, 2, 2, 3, 3])) 
'''41.longest increasing subsequence(LIS)''' 
import bisect 
def LIS(arr): 
    sub = [] 
    for num in arr: 
        pos = bisect.bisect_left(sub, num) 
        if pos == len(sub): 
            sub.append(num) 
        else: 
            sub[pos] = num 
        return len(sub) 
print(LIS([10, 9, 2, 5, 3, 7, 101, 18]))
'''42.Longest consecutive sequence''' 
def longest_consecutive(nums): 
    num_set = set(nums) 
    longest = 0 
    for num in num_set: 
        if num -1 not in num_set: 
            current = num 
            length = 1 
            while current+1 in num_set: 
                current += 1 
                length += 1 
            longest = max(longest, length) 
    return longest 
print(longest_consecutive([100, 4, 200, 1, 3, 2])) 
'''43.find the missing number 1 to n''' 
lst = [1, 2, 4, 5] 
n = 5 
for i in range(1, n + 1): 
    if i not in lst: 
        print(i) 

def find_missing(arr, n): 
    return list(set(range(1, n + 1))- set(arr))
print(find_missing([1, 2, 4, 6], 6))
'''44.Merge two sorted lists without sort''' 
def merge_sort(a, b): 
    i = j = 0 
    result = [] 
    while i < len(a) and j < len(b): 
        if a[i] < b[j]: 
            result.append(a[i]) 
            i += 1 
        else: 
            result.append(b[j]) 
            j += 1 
    result.extend(a[i:]) 
    result.extend(b[j:]) 
    return result 
print(merge_sort([1, 3, 5],[2, 4, 6]))
'''45.intersection of multiple lists''' 
def intersectio_list(lists): 
    result = set(lists[0]) 
    for lst in lists[1:]: 
        result &= set(lst) 
    return list(result) 
print(intersectio_list([[1,2,3],[2,3,4],[2,5,3]])) 
'''46.union of multiple list without using set()''' 
def uniont_lists(lists): 
    result = [] 
    for lst in lists: 
        for item in lst:
            if item not in result: 
                result.append(item) 
    return result 
print(uniont_lists([[1, 2, 3], [2, 3, 4], [4, 5]])) 
'''47.Detect a cycle pattern in a list''' 
def has_cycle(lst): 
    s = [] 
    for i in lst: 
        if i in s: 
            return True 
        s.append(i) 
    return False 
print(has_cycle([1,2,3,4,2]))
print(has_cycle([1,2,3,4])) 
'''48.find the first repeating element''' 
def first_repeating(lst): 
    s = [] 
    for i in lst: 
        if i in s: 
            return i 
        s.append(i) 
    return None 
print(first_repeating([1,2,3,4,2,5])) 
'''49.implement a stach using a list'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
print(s.pop())  
'''50.implement a queue using a list '''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        if self.queue:
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  