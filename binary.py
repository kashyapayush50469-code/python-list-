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


