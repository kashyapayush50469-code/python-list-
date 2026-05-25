'''Create a dictionary with keys name, age, city and print each value using a loop.'''
dic = {"name":"Arman", 
       "Age":10,
       "City":"Dbg"
    }
for num in dic.values(): 
    print(num) 
'''2.Given the dictionary below, how do you access the value of key "b"? What happens if you try to access a key that does not exist?'''
d = {"a": 1, "b": 2, "c": 3}
# Hint: Try both d["x"] and d.get("x") and observe the difference
print(d.get("a"))  
print(d["a"]) 

'''3.Add a new key "country": "India" to an existing dictionary and then delete the key "age".
💡 Hint: Use del or .pop() to remove a key
'''
s = {"name":"Arman", 
       "Age":10,
       "City":"Dbg",
       
    }

s.update({"country":"Indai"}) 
s.pop("Age") 
print(s) 
print(s) 
# another without bultain method 
s["country"] = "India" 
print(s) 
'''4. Write a program to count the frequency of each character in a string using a dictionary.
string = "hello world"
# Output: {'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}''' 
string = "hello world"
dic = {} 
for i in string: 
    if i not in dic: 
        dic[i] = 1 
    else: 
        dic[i] += 1 
print(dic) 
'''5.Given two dictionaries, merge them. If a key exists in both, keep the value from the second dictionary.
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
# Output: {"a": 1, "b": 99, "c": 3}'''
d1 = {"a":1, "b":2} 
d2 = {"b":99, "c":3}
d1.update(d2)
print(d1) 
'''6. Write a program to invert a dictionary (swap keys and values).
d = {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}''' 

d = {"a":1, "b":2, "c":3} 
swap = {} 
for k, v in d.items(): 
     
      swap[v] = k  
   
print(swap) 
'''7.Given a dictionary of students and marks, find the student with the highest marks.
marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
# Output: Bob'''
marks={"Alice":85, "Bob":92, "charlie":78} 
highest_key = max(marks, key=marks.get)

print(highest_key)
'''8.words = ["apple", "bat", "avocado", "ball", "cherry"]
# Output: {"a": ["apple","avocado"], "b": ["bat","ball"], "c": ["cherry"]}'''
words = ["apple", "bat", "avocado", "ball", "cherry"]
x = {}
for i in words:
    k = i[0] #a
    
    if k not in x:
        x[k] = []
    
    x[k].append(i)

print(x)
'''9.Output: {1: 1, 2: 4, 3: 9, 4: 16, ..., 10: 100}'''
x = {x:x*x for x in range(1, 11)} 
print(x) 

res = {} 
for i in range(1, 11): 
    res[i] = i * i 
print(res) 

'''10.company = {
    "Alice":   {"dept": "HR", "salary": 50000},
    "Bob":     {"dept": "IT", "salary": 70000},
    "Charlie": {"dept": "IT", "salary": 65000},
}
# Output: Total Salary = 185000'''
company = {
    "Alice":   {"dept": "HR", "salary": 50000},
    "Bob":     {"dept": "IT", "salary": 70000},
    "Charlie": {"dept": "IT", "salary": 65000},
}
total = 0 
for num in company.values(): 
    total += num["salary"] 
print("total salary:",total) 



def lists():
        s = "IceCreAm" #output = "AceCreIm"
        s = [x for x in s]   #['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']
        lst = ['a','A','e','E','i','I','o','O','u','U'] 
        i = 0 # i = 0 
        j = len(s)-1 # it takes last index 
        while i<len(s) and j< len(s): 
            if s[i] in lst and s[j] in lst:       
                s[i], s[j] = s[j], s[i] 
                i += 1
                j -= 1 
            elif s[i] not in lst: 
                i += 1 
            else: 
                j -=1  
        return ''.join(s) 
print(lists())

# reverse value in a dictiontary: 
d = {10:[0], 3:[1],8:[2],9:[3],4:[4]} 
keys = list(d.keys()) # [10,3,8,9,4]
values = [v[0] for v in d.values()] #[0, 1, 2, 3, 4]
values.reverse() # [4, 3, 2, 1, 0]
res = {} # {}
i = 0  # i = 0, 1, 2, 3, 4
while i < len(keys): # 0<5,1<5,2<5, 3<5, 4<5,5<5(false) 
    res[keys[i]] = [values[i]] # {10:[4],3:[3],8:[2],9:[1],4:[0]}
    i += 1 # 1, 1, 1 , 1
print(res)  

'''swap first and last values.''' 
d = {1:[10],2:[20],3:[30],4:[40]} 
keys = list(d.keys())# [1, 2, 3, 4]
values = [v[0] for v in d.values()] #[10,20,30,40]
values[0], values[-1] = values[-1], values[0] # [40, 20, 30, 10]
res = {} # {}
i = 0 # 0
while i < len(keys): #0<4,1<4,2<4,3<4,4<4(false)
    res[keys[i]] = [values[i]]#{1:[40],2:[20],3:[30],4:[10]} 
    i += 1 # 1, 1, 1, 
print(res) # final answer = #{1:[40],2:[20],3:[30],4:[10]} 
'''rorate vaues right by 1''' 
d = {1:[1], 2:[2], 3:[3], 4:[4]}

keys = list(d.keys())#[1,2,3,4]
values = [v[0] for v in d.values()]#[1,2,3,4] 
last = values[-1] # last = 4
i = len(values)-1 # 3
while i > 0: #3>0,2>0,1>0
    values[i]  = values[i-1] # 4 = 3,3=2 ,2=1 
    i -= 1 # -1,-1
values[0] = last # [4,1,2,3]
res = {} # {}
i = 0 # i = 0
while i < len(keys): # 0<4,1<4,2<4,3<4,4<4(false)
    res[keys[i]] = [values[i]] #{1:[4],2:[1],3:[2],3:[3]} 
    i += 1 # 1, 1, 1,1
print(res) # final output = {1:[4],2:[1],3:[2],3:[3]} 

'''4.rorate values left by 1''' 
d = {1:[1], 2:[2], 3:[3], 4:[4]} 
keys = list(d.keys()) # [1,2, 3, 4]
values = [v[0] for v in d.values()] # [1, 2, 3, 4] 
first  = values[0] # first = 1
i = 0 # i =0,1,2
while i < len(values)-1:#0<3,1<3,2<3 
    values[i] = values[i+1]#1=2,2=3,3=4 # [2,3,4,4]
    i += 1 # 1,1
values[-1] = first #[2,3,4,1] # 4 = 1 
res = {} # {}
i = 0 # i = 0,1,2,3
while i < len(keys): # 0<4,1<4.2<4,3<4 
    res[keys[i]] = [values[i]] #{1:[2],2:[3],3:[4],4:[1]}  
    i += 1# 1,1,1,1
print(res) # final output = {1:[2],2:[3],3:[4],4:[1]}  

'''5.Swap adjacent values''' 
d = {1:[1], 2:[2], 3:[3], 4:[4]} 
keys = list(d.keys()) # [1,2,3,4]
values = [v[0] for v in d.values()]#[1,2,3,4] 
i = 0 # i = 0, 2
while i < len(values)-1:#0<3,2<3,4<3(false)
    values[i], values[i+1] = values[i+1], values[i]#[2,1,4]  
    i += 2 # 2
res = {} # {} 
i = 0 # i = 0 
while i < len(keys)-1:#0<3
    res[keys[i]] = [values[i]]#{1:[2],2:[1],3:[4]} 
    i += 1 # 1, 1, 1, 1
print(res) # final output = {1:[2],2:[1],3:[4]}
'''6.Even index values reverse only''' 
d = {1:[10], 2:[20], 3:[30], 4:[40], 5:[50]} 
keys = list(d.keys()) #[1,2,3,4,5]
values = [v[0] for v in d.values()] #[10,20,30,40,50] 
ever_vals = [] # []
i = 0 # i = 0
while i < len(values): #0<5
    if i % 2 == 0: # 10 % 2 ==0
        ever_vals.append(values[i]) # [10,30,50]
    i += 1 # 1
ever_vals.reverse() # [50,30,10]
j = 0 #j = 0 
i = 0 # i = 0 
while i < len(values): 
    if i % 2==0: 
        values[i] = ever_vals[j] 
        j += 1 
    i += 1 # this condition is always go while the condition is ture or not.
res = {} 
i = 0 
while i < len(keys): 
    res[keys[i]] = [values[i]] #{1:[50],2:[20],3:[30],4:[40],5:[10]}
    i += 1 
print(res) # the output will be = {1:[50],2:[20],3:[30],4:[40],5:[10]}

'''7.odd index values reverse''' 
d = {1:[10], 2:[20], 3:[30], 4:[40], 5:[50]}
keys = list(d.keys())# [1,2,3,4,5] 
values = [v[0] for v in d.values()]#[10,20,30,40,50] 
odd_vals = [] # []
i = 0 # i = 0
while i < len(values):# 0<5
    if i % 2 != 0: 
        odd_vals.append(values[i]) # [20,40]
    i += 1 # 1
odd_vals.reverse() #[40,20]
i = 0 
j = 0 
while i < len(values): 
    if i % 2 != 0: 
        values[i] = odd_vals[j] 
        j += 1 
    i += 1 
res = {} 
i = 0 
while i < len(keys): 
    res[keys[i]] = [values[i]]#{1:[10],2:[40],3:[30],4:[20],5:[50]} 
    i += 1 
print(res) #{1:[10],2:[40],3:[30],4:[20],5:[50]} 
'''8.sort values''' 
d = {1:[40], 2:[10], 3:[30], 4:[20]}
keys = list(d.keys()) # [1,2,3,4,5]
values = [v[0] for v in d.values()] #[40,10,30,20]
values.sort() # [10,20,30,40]
res = {} # {}
i = 0 
while i < len(keys): 
    res[keys[i]] = [values[i]] #{1:[10],2:[20],3:[30],4:[40]}
    i  += 1 
print(res) # ouput = {1:[10],2:[20],3:[30],4:[40]}
'''9.custom rearragne'''
d = {10:[0], 3:[1], 8:[2], 9:[3], 4:[4]}
keys = list(d.keys())#[10,3,8,9,4] 
values = [v[0] for v in d.values()] # [0,1,2,3,4] 
new_values = [values[0], values[4], values[2], values[1], values[3]] # [0,4,2,1,3] 
res = {} # {}
i = 0 # i = 0 
while i < len(keys):#0<5 
    res[keys[i]] = [new_values[i]] #{10:[0],3:[4],8:[2],9:[1],4:[3]} 
    i += 1 # 1
print(res) # the ouput = {10:[0],3:[4],8:[2],9:[1],4:[3]} 
'''10. reverse only first hlaf''' 
d = {1:[1], 2:[2], 3:[3], 4:[4], 5:[5], 6:[6]}
keys = list(d.keys())#[1,2,3,4,5,6]
values = [v[0] for v in d.values()] #[1,2,3,4,5,6] 
mid = len(values)//2 # mid = 3 
first_half = values[:mid] # [1,2,3]
first_half.reverse() #[3,2,1]
values = first_half + values[mid:]#[3,2,1,4,5,6] 
res = {} # {}
i = 0 # i = 0 
while i < len(keys): 
    res[keys[i]] = [values[i]] # {1:[3],2:[2],3:[1],4:[4],5:[5],6:[6]}
    i += 1 
print(res)  # output =  {1:[3],2:[2],3:[1],4:[4],5:[5],6:[6]}