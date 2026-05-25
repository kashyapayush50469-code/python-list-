'''1.two sum''' 
def two_sum(array, target): 
    i = 0 # i = 0, 1
    j = len(array) -1 # 4 
    while i < j: # 
        s = array[i] + array[j] # 1 + 5 = 6 , 2 + 5 = 7 
        if s==target: # 6 ==7 , 7 == 7
            return [i, j] #[1, 4] answer. 
        elif s < target: # 6 < 7
            i  += 1 # 1 
        else: 
            j -= 1 
print(two_sum([1, 2, 3, 4, 5], 7)) 
'''2.reverse array.''' 
arr = [1, 2, 3, 4, 5] 
i = 0 # 0 , 1, 2, 3, 4
j = len(arr) -1 # 4, 3, 2, 1
while i < j: 
    arr[i] , arr[j] = arr[j], arr[i] # [5, 4, 3, 2, 1]
    i += 1 # 1
    j -= 1 
print(arr) # [5, 4, 3, 2, 1]
'''3.check palindrome array''' 
arr = [1,2,3,2,1] 
i = 0 # 0 1, 2,3, 4 
j = len(arr)-1 # 1, 2, 3, 2, 1 
p = True # True
while i < j: 
    if arr[i] != arr[j]:# 1!=1, 2 != 2 3 != 3 
        p = False 
        break 
    i += 1 # 1, 1,1, 1
    j -= 1 # -1, -1 -1, -1 
print(p) # True
'''4.count matching pairs from both ends''' 
arr = [1, 2, 3, 2, 1] 
i = 0 # 1, 2
j = len(arr)-1 # 1, 2,
count = 0 # 2 
while i < j: 
    if arr[i] == arr[j]: # 1==1 2 ==2  
        count += 1 # count = 1+1 =2 
    i += 1 # 1
    j -= 1 # -1
print(count) 
'''5.remove duplicates''' 
arr = [1,1,2,2,3] 
i = 0 # 1, 1, 2, 2, 3
for j in range(1, len(arr)): #j = 1, 5 
    if arr[j] != arr[i]: #1!=1, 1 !=2 2 != 3
        i += 1 # 1,1
        arr[i] = arr[j] # [1, 2, 3, 2, 3] 
print(arr[:i+1]) # [1, 2, 3]

'''6.count even numbers from both sides''' 
arr = [2, 3, 4, 5, 6] 
i = 0 # 0, 1
j = len(arr)-1 # 6 , 5
count = 0 # 1 
while i <= j: 
    if arr[i] % 2 ==0: # 2 % 2 ==0 3 % 2 ==0(false), 
        count += 1 # 1,
    if i != j and arr[j] % 2==0: # 3 != 5 and 5 % 2==0 (this conditin is false and operator the both condition must be true)
         count += 1 
    i += 1 
    j -= 1 
print(count) # 3
'''7.replace elements from the ends''' 
arr = [1, 2, 3, 4] # [1,2, 3,4]
i = 0 # 1, 2, 
j = len(arr)-1 # 4, 3 
while i < j: #  
    arr[i] += arr[j]  # 5  5, 
    arr[j] -= arr[i] # 4 - 5 = -1 , 3 - 5 = -2 
    i += 1  # 1, 1
    j -= 1  # -1 -1 
print(arr) # [5, 5, -2, -1] 

'''8.swap alternate pairs.''' 
def swap_alternate(arr):
    i = 0 # 0= 1 2 = 3 
    while i < len(arr) - 1: 
        # swap arr[i] and arr[i+1]
        arr[i], arr[i+1] = arr[i+1], arr[i] # 1, 2 = 2, 1 
        i += 2 # 2 
    return arr

# Example
arr = [1, 2, 3, 4, 5, 6] # [2, 1, 4, 3, 6, 5]
print(swap_alternate(arr))


'''9.trim equal values from both ends''' 
arr = [2, 2, 3, 4, 2, 2] # 
i = 0 # 0 1 2, 3, 4
j = len(arr) -1 #  2 , 2, 4 , 3
while i < j and arr[i] == arr[j]: # 2 < 2 and 2 == 2 , 3 < 4 3 == 4 
    i += 1 # 1
    j -= 1 # -1
print(arr[i:j+1]) #[3,4]
'''10.find first mismatch from ends''' 
aarr = [1, 2, 3, 4, 5] 
i = 0 # 0
j = len(arr)-1 # 4
while i < j: 
    if arr[i] != arr[j]: # 0!=4
        print(i, j)  # 0, 4 final answer
        break
    i += 1 
    j -= 1 
'''11.merge two arrays alternately ''' 
a = [1, 2, 3] # [1, 2, 3]
b = [4, 5, 6] # [4, 5, 6]
i = j = 0 # i = 0 j = 0 
res = [] #  []
while i < len(a) and j < len(b): 
    res.append(a[i]) # res = [1, 4, 2, 5, 3, 6] 
    res.append(b[j]) 
    i += 1 # 1, 1, 1
    j += 1 # 1, 1, 1
print(res) # [1, 4, 2, 5, 3, 6] the final answere. 
'''12.compare mirror elements difference''' 
arr = [1, 3, 5, 7] 
i = 0 # 0 = 1, 1 = 3
j = len(arr)-1 # 3 = 7 2 = 5
while i < j: 
    print(abs(arr[i]-arr[j])) # 7 -1 = 6 , 5-3 =2 answer = 6, 2
    i += 1 # 1, 
    j -= 1  # -1
'''13.replace with product of ends''' 
arr = [1, 2, 3, 4]
i = 0 # 0 
j = len(arr)-1 # 3 
while i <= j: 
    print(arr[i]*arr[j]) # 4 * 1 = 4, 2 * 3 = 6 final answer = 4, 6 
    i += 1 # 1, 1
    j -= 1 # -1, -1
'''14.chech if array is sysmmetric''' 
arr = [1, 2, 2, 1]  
i = 0 # 0 = 1
j = len(arr)-1 # 3 = 1
print(all(arr[i+k] == arr[j-k] for k in range(len(arr)//2))) # i+ k = 0 + 2 = , 2 == 2 in the same way next excuation. True  
'''15.count elements greater than both ends''' 
arr = [1, 5, 3, 6, 2] 
i = 0 # 0, 1, 
j = len(arr)-1 # 4, 3 
count = 0 # 1
for k in range(1, len(arr)-1): # k = 1 = 5,  
    if arr[k] > arr[i] and arr[k] > arr[j]: # 5 > 1 and 5 > 2 
        count +=1 # 1 
print(count) 
'''16.reverse only even numbers.''' 
arr = [1, 2, 3, 4, 5, 6] #[4, 2, 5, 7] =  
i = 0 # 0, 1 , 2, 3 
j = len(arr)-1 # 5, 4 
while i < j: # 1 < 5 
    if arr[i] % 2 != 0: # 1 % 2 != 0, 2 % 2 != 0   
        i += 1 # 1, 
    elif arr[j] % 2 != 0: # 6 % 2 != 0 
        j -= 1 
    else: 
        arr[i], arr[j] = arr[j], arr[i] # 1, 6, 3, 4, 5, 2 
        i += 1 # 1,
        j -= 1  # -1
print(arr) # [1, 6, 3, 4, 5, 2]
'''17.remove elements equal from both ends''' 
arr = [3,3,1,2,3,3] 
i = 0 # i = 0 1, 2
j = len(arr)-1 # 5 , 4, 3
while i <= j and arr[i] ==3: # 3 <= 3 and 3 == 3, 1<=2and1==3 
    i += 1  # 1, 
while j >= i and arr[j] ==3:  # 3 >= 3 and 3 == 3 , 2>=1 and 2 == 3
    j -= 1 # -1 
print(arr[i:j+1]) # [1, 2]
'''18.create reversed copy''' 
arr = [1, 2, 3, 4] 
res = [0]*len(arr) # [0] * 4
i = 0 # 0, 1 = 2
j = len(arr)-1 # 3 , 2  
while i < len(arr): # 0<3, 2<4
    res[i] = arr[j] # 1 = 4 , 3 = 2 [4, 3, 2, 1] 
    i += 1 # 1, 
    j -= 1 # -1
print(res) #[4, 3, 2, 1] 
'''19.check if first half equals reversed second half''' 
arr = [1,2,3,3,2,1]  
i = 0 # i = 0 , 1, 2
j = len(arr)-1 # j = 5, 4, 3 
flag = True # True 
while i < j: # 0 < 5 , 1 < 4, 2 < 3
    if arr[i] != arr[j]: # 1 != 1, 2 != 2 , 3 != 3    
        flag  = False 
    i += 1 # 1, 1, 
    j -= 1 # -1, -1
print(flag) # true
'''20.swap max and min using two pointers.''' 
arr = [3, 1, 4, 2]  
i = arr.index(min(arr)) # 1
j = arr.index(max(arr)) # 2
arr[i], arr[j] = arr[j], arr[i] # 2 = 1,  1 =2
print(arr) # [3, 4, 1, 2]
'''21.reverse part of array''' 
arr = [1, 2, 3, 4, 5] 
i = 1 # 2 
j = 3 # 4 
while i < j: #2 < 4 
    arr[i], arr[j] = arr[j], arr[i] # 4= 2 
    i += 1 # 1, 
    j -= 1  #-1
print(arr) # [1, 4, 3, 2, 5]
'''22.count pairs with same value from ends'''  
arr = [1, 2, 1, 2, 1] 

i = 0 # i = 0, 1, 2
j = len(arr)-1 # 4, 3, 2
count = 0 # 2
while i < j: # 0<4, 1<3, 2 < 2(this condtition will be false)
    if arr[i] == arr[j]: # 1 = 1, 2 == 2 
        count += 1 # 2
        i += 1 # 1, 1
        j -= 1 # -1, -1
print(count) # 2
'''23.replace left with right sum''' 
arr = [1, 2, 3, 4] 
i = 0 # 0 1,2
j = len(arr)-1 # 3 2,1 
while i < j: # 0 < 3, 1 < 2, 2 < 1(false)
    arr[i]+=arr[j] # 1 + 4 = 5, 2 + 3 = 5  
    i += 1 # 1, 1, 
    j -=1  # -1 -1, 
print(arr) # [5,5, 3, 4]
'''24.reverse odd index elements''' 
arr = [1, 2, 3, 4, 5] 
i = 1 # 1, 3
j = len(arr)-2 # 3, 1 
while i < j: #1<3, 3<1(false)
    arr[i], arr[j] = arr[i], arr[j] # [1, 4, 3, 2, 5] 
    i += 2 # 2, 
    j -= 2 # -2 
print(arr) # [1, 4, 3, 2, 5] 
'''check equal sum pairs.''' 
arr = [1, 2, 3, 4] 
i = 0 # 0 = 1
j = 3 # 3 = 4
print(arr[i]+arr[j]) # 4 + 1  = 5

arr = [1, 2, 3, 4] 
i = 0 # 0 , 1, 2,
j = 3 # 3, 2, 1
while i < j: # 0 < 3, 1 < 2 , 2<1(false)
    print(arr[i], arr[j]); i += 1; j -=1 # 1, 4, 2, 3 

arr = [1, 3, 5, 2] 
i = 0 # 0, 1
j = 3 # 3, 2
c = 0 # 1
while i <= j: # 1<=2, 1 < 2 
    if arr[i]%2:c+=1 # 1 % 2 , 1  
    if i != j and arr[j]%2:c+=1 
    i += 1; j-=1 # 1, -1
print(c) # 3

#swap ends until middle
arr = [1, 2, 3, 4] 
i = 0  # 0 1, 
j = 3 # 3 2, 
while i < j: # 0<3, 1 < 2
    arr[i], arr[j] = arr[j], arr[i] # [4, 2, 3, 1] ,[4, 3, 2, 1]  
    i += 1; j-=1 # 1, -1
print(arr) #[4, 3, 2, 1]

arr = [1, 2, 3, 4] 
i = 0 # 0, 1, 
j = 1 # 1, 0,
while i < j: # 0<1, 1<0(false)
    arr[i], arr[j] = arr[j], arr[i], # [2, 1, 3, 4]
    i += 1; j-=1 # 1, -1,1, -1
print(arr) # [2, 1, 3, 4] 
#chech first last equal 
arr = [1, 2, 3] 
print(arr[0]==arr[-1]) # return False
#print middle
arr = [1, 2, 3, 4, 5] 
i = 0 # 0, 1, 2
j = 4 # 4, 3, 2
while i <= j: # 0 <= 4, 1<=3, 2<=2 
    if i ==j: print(arr[i])  # 2 == 2 print(3)
    i+=1;j-=1 # 1, -1, 1, -1
#remove edges
arr = [1, 2, 3] 
print(arr[1:-1]) # 1, 3 remove karo , ans=[2]
# mirror copy 
arr = [1, 2, 3] 
res = [] # []
i = 0 # 0,1
j = 2 # 2,1
while i <= j: # 0 < 2, 2 <= 2
    res.append(arr[i]) # [1,2] 
    res.append(arr[j]) #[1,3,2,2]
    i +=1; j-=1 # 1, -1
print(res) # [1,3,2,2]
#swap until condition 
arr = [1, 5, 2, 6] 
i = 0 # 0,1,2
j = 3 # 3,2,1
while i <j:#0<3, 1<2, 2<1(false) 
    if arr[i]>arr[j]:# 1>6, 2>5 
        arr[i], arr[j] = arr[j], arr[i] 
    i +=1;j-=1 # 1, -1, 1, -1
print(arr) #[1,2,5,6]
#count less than boht ends
arr = [1, 4, 2, 5] 
i = 0 # 0 
j = 3 # 3
c = 0 # 2
for i in range(1, 3):#1, 2 
    if arr[i]<arr[j]and arr[i]<arr[j]:# 1<5and1<5, 4<5and4<5
        c +=1 # 2
print(c) # 2
# reverse only greater than >2: 
arr = [1, 3, 5, 2] 
i = 0 # 0, 1,2
j = 3 # 3, 2, 1
while i<j:#0<3, 1<2 , 2<1
    if arr[i]<=2:i+=1 #1<=2, i = 1, 3<=2(false), 
    elif arr[j]<=2:j-=1 #2<=2, j = -1, 
    else: 
        arr[i], arr[j] = arr[j], arr[i]# [1, 5,  3, 2]
        i += 1;j-=1 # 1, -1
print(arr) # [1, 5,  3, 2]
#shift edges inward. 
arr = [1, 2, 3, 4] 
i = 0 # i = 0,1,2
j = 3 # j = 3,2,1
while i < j: # 0<3,1<2, 2<1(false)
    arr[i]=arr[j]# 1 = 4, 2 = 3
    i += 1;j-=1 # 1, -1, 1, -1
print(arr) #[4, 3, 3, 4]
#replace with diff
arr = [5, 2, 8, 1] 
i = 0 # 0,1,2
j = 3 # 3,2,1
while i<j:#0<3,1<2, 2<1(false) 
    print(abs(arr[i]-arr[j])) #5 -1= 4,2-8 = -6 
    i +=1;j-=1 # 1, -1, 1 -1
#count equal pairs. 
arr = [1, 2, 2, 1] 
i= 0 # 0,1
j = 3 # 3,2
c = 0 # 2
while i <j: # 0<3,1<2 
    if arr[i]==arr[j]:c+=1# 1 ==1, c = 1, 2 ==2 , c = 1 + 1 =2 
    i  +=1;j-=1# 1, -1 
print(c) #2
#reverse using while
arr = [1, 2, 3] 
i = 0# 0,1
j = 2 # 2,1
while i<j:#0<2,1<1(false) 
    arr[i], arr[j] = arr[j], arr[i] #[3, 2, 1]
    i +=1;j-=1 # 1, -1
print(arr) #[3, 2, 1]
#swap if even. 
arr = [2, 3, 4, 5] 
i = 0 # 0,1,2
j = 3 # 3,2,1
while i<j:#0<3,1<2,2<1(false) 
    if arr[i]%2==0 and arr[j]%2==0: # 2 % 2 ==0 and 5%2==0, 3%2==0and 4 % 2==0 
        arr[i], arr[j] = arr[j], arr[i] 
    i +=1;j-=1 # 1, -1, 1, -1
print(arr) #[2, 3, 4, 5]
#mirror add 
arr= [1,2,3] 
i = 0 # 0,1
j = 2 # 2,1
while i<=j:#0<=2, 1 <= 1 
    print(arr[i]+arr[j]) # 1 + 3 = 4 , 2 + 2 = 4
    i += 1;j-=1 # 1, -1
#reverse edges only 
arr = [1, 2, 3, 4] 
arr[0], arr[-1] = arr[-1], arr[0] # [4,2, 3, 1]
print(arr)  # [4,2, 3, 1]
#  swap mid neighbors 
arr = [1, 2, 3, 1, 2, 3] 
mid = len(arr)//2 # 1
arr[mid-1], arr[mid] = arr[mid], arr[mid-1] #[1, 2, 1, 3, 2, 3]
print(arr) #[1, 2, 1, 3, 2, 3]
#compare halfs 
# arr = [1, 2, 3, 1, 2, 3] 
# i = 0 # 0, 1, 2,3
# j = 3 # 3, 4, 5False(index out of range so the answer of this code will unavailable.)
# while i<j: # 0<3,1<4 2<5
#     print(arr[i] == arr[j])#1 ==1, 2 ==2, 3 ==3
#     i +=1;j+=1 # 1, 1 1, 1,1, 1
#reverse using step
arr = [1, 2, 3] 
i = 0#0,1
j = 2 #2,1
while i<j:#0<2, 1<1(false) 
    arr[i], arr[j] = arr[j], arr[i] #[3, 2, 1]
    i+=1;j-=1 # 1, -1
print(arr) #[3,2,1]
#print cross pairs 
arr = [1, 2, 3, 4] 
i = 0 # 0,1,2
j = 3 # 3,2,1
while i<j:#0<3 ,1<2,2<1(false)
    print(arr[i], arr[j])# 1, 4,,2, 3 
    i+=1;j-=1 # 1, -1, 1, -1
#check increaisn -decreasing order
arr = [1, 2, 3, 2, 1] 
i = 0 #0
j = 4 #4
print(arr[i]<arr[i+1] and arr[j]<arr[j-1]) #1<2and1<2 # True 