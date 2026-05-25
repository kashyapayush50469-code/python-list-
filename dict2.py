'''create a dictonary''' 
d = {"a": 1, "b": 2}
print(d)
'''access value by key'''
d = {"name": "Ayush"}
print(d["name"])
'''add key value pair'''
d = {}
d["age"] = 20
print(d)
'''update value'''
d = {"a": 1}
d["a"] = 5
print(d)
'''delete a key''' 
d = {"a": 1, "b": 2}
del d["a"]
print(d)
'''check key exists''' 
d = {"a": 1}
print("a" in d)
'''get all keys''' 
d = {"a": 1, "b": 2}
print(d.keys())
'''get all values''' 
print(d.values())
'''get all items''' 
print(d.items())
'''loop through dictionary''' 
for k, v in d.items():
    print(k, v)
'''length of dic'''
print(len(d))
'''clear dictinary''' 
d.clear()
'''copy dic''' 
d2 = d.copy()
'''use get method''' 
print(d.get("x", "Not found")) 
'''create a dictionary from a list''' 
keys = ["a", "b"]
values = [1, 2]
d = dict(zip(keys, values))
print(d)
'''count frequency of elements''' 
lst = [1, 2, 2, 3] 
d = {} 
for i in lst: 
    d[i] = d.get(i, 0)+1 
print(d) 
'''merge two dictionay''' 
d1 = {"a":1} 
d2 = {"b":2} 
print({**d1, **d2}) 
'''sorted dic by keys''' 
d = {"b":2, "a":1} 
print(dict(sorted(d.items()))) 
'''sort by values''' 
print(dict(sorted(d.items(), key=lambda x: x[1])))
'''find max vlaue''' 
print(max(d, key=d.get)) 
'''remove duplicates value''' 
d = {"a":1, "b":1, "c":2} 
res = {} 
for k, v in d.items(): 
    if v not in res.values(): 
        res[k] = v 
print(res) 
'''reverse dictionary''' 
d = {"a":1, "b":2} 
print({v:k for k, v in d. items()}) 
'''check if tow dicts ae equal''' 
print(d1 == d2) 
'''nested dictionary''' 
d = {"a":{'x':1}} 
print(d["a"]["x"]) 
'''flatten nested dic''' 
d = {'a':{'x':1}} 
print({k2:v2 for k1, v1 in d.items() for k2, v2 in v1.items()}) 
'''sum all vlues''' 
# print(sum(d.values()))
'''multipy all values''' 
d = {"a":1,"b":2,"c":3,"d":4} 
res = 1 
for v in d.values(): 
    res *= v 
print(res) 
'''remove key with specify value''' 
d = {k:v for k, v in d.items() if v != 2} 
print(d) 
'''find common keys''' 
# print(d1.keys() & d2.keys()) 
'''dictionary comprehension''' 
d = {i:i*i for i in range(5)} 
'''convert stirng to dict frequency''' 
s = "hello"
d = {} 
for c in s: 
    d[c] = d.get(c, 0)+1
print(d) 
'''group element''' 
lst = ["a", "apple", "b"] 
d = {} 
for i in lst:
    d.setdefault(i[0], []).append(i) 
print(d) 
'''defaultdic ex''' 
from collections import defaultdict 
d = defaultdict(int) 
d["a"] += 1 
print(d) 
'''get key from value''' 
d =  {"a":1, "b":2, "c":3, "D":4} 
print([k for k, v in d.items()if v ==2])


'''####leval up####''' 
'''LRU cache''' 
from collections import OrderedDict 
d2 = {"a":1, "b":2, "c":3, "D":4} 
d2 = OrderedDict() 
d2["a"] = 1 
d2.move_to_end("a")
print(d2)
'''deep merging dictonary''' 
def merge(d1, d2): 
    for k, v in d2.items(): 
        if k in d1 and isinstance(v, dict): 
            merge(d1[k], v)
        else: 
            d1[k] = v 
    return d1
d1 = {"a":1,"b":2,"c":3,"d":5} 
d2 = {"a":2,"b":3}
print(merge(d1, d2))
'''find top k frequent elements''' 
from collections import Counter 
print(Counter([1, 1, 2, 3]).most_common(2))
'''anagram grouping''' 
words = ["eat", "tea", "tan"] 
d3 = {} 
for w in words: 
    key = ''.join(sorted(w))
    d3.setdefault(key, []).append(w) 
print(d3.values) 
'''tow sum using dictionary''' 
nums = [2, 7, 11, 13] 
target = 9 
d = {} 
for i , n in enumerate(nums): 
    if target-n in d: 
        print(d[target-n], i) 
    d[n] = i 
print(d) 
'''subarray sum equals k ''' 
nums = [1, 2, 3] 
k = 3
d = {0:1} 
sum = 0 
count = 0 
for n in nums: 
    sum+=n 
    count+=d.get(sum-k, 0) 
    d[sum] = d.get(sum, 0)+1 
print(count) 
'''longest substring without repeating chareacter''' 
s = "abcabc" 
d = {} 
i = 0 
res = 0 
for k , n in enumerate(s): 
    if n in d: 
       k = max(i, d[n]+1) 
    d[n] = k 
    res = max(res, k-i+1) 
print(res) 
'''check isomorhich string''' 
s = "egg";t="add" 
d1,d2 = {}, {} 
for i in range(len(s)): 
    if d1.get(s[i]) != t[i] or d2.get(t[i]!=s[i]): 
        print(False) 
        break 
    d1[s[i]] = t[i] 
    d2[t[i]] = s[i] 
"word pattern match"  
pattern="abba"
words="dog cat cat dog".split()
print(len(set(zip(pattern,words)))==len(set(pattern))==len(set(words)))
'''find dupliciates files (hash map concept)''' 
paths = ["a.txt content1","b.txt content1"]
d={}
for p in paths:
    name,content=p.split()
    d.setdefault(content,[]).append(name)
print([v for v in d.values() if len(v)>1])
'''Group numbers by frequency''' 
from collections import Counter
print(dict(Counter([1, 2, 2, 3]))) 
"""sliding window max""" 
from collections import deque 
nums=[1, 3, -1, -3, 5] 
k = 3 
dq = deque() 
'''count pairs with given sum''' 
nums = [1, 5, 7, -1] 
k = 6 
d = {} 
count = 0 
for n in nums: 
    count += d.get(k-n, 0)
    d[n] = d.get(n, 0)+ 1 
print(count) 
'''Longest consecutie sequence''' 
nums = [100, 4, 200, 1, 3, 2] 
s = set(nums) 
longest = 0 
for n in s: 
    if n-1 not in s:
        cur = n 
        count =1 
        while cur+1 in s: 
            cur+=1 
            count+=1 
        longest=max(longest, count) 
print(longest)  
'''trie using dictionray''' 
trie = {} 
word = "cat" 
node = trie 
for i in word: 
    node = node.setdefault(i, {}) 
node["#"] = True 
print(trie)
