'''valid prentheses''' 
s = "()[]{}" 
def isValid(s): 
    s = "()[]{}" 
    stack = [] 
    mapping = {
        ')':'(',
        ']':'[',
        '}':'{'
        }
    for ch in s: 
        if ch in mapping: 
            if not stack or stack.pop() != mapping[ch]: 
                return False 
        else: 
            stack.append(ch)  
    return len(stack) == 0
isValid(s = "()[]{}") 

'''remove all adjecent duplicates''' 
def removeDuplicates(s): 
    stack = [] 
    for ch in s: 
        if stack and stack[-1] == ch: 
            stack.pop() 
        else: 
            stack.append(ch) 
    return ''.join(stack) 
print(removeDuplicates(s="abbaca"))
'''backspace string compare'''
def build(string): 
    stack = [] 
    for ch in string: 
        if ch=='#':
             if  stack: 
                 stack.pop() 
        else: 
            stack.append(ch) 
    return ''.join(stack) 
def backspacecompare(s, t): 
    return build(s) == build(t)
print(backspacecompare("ab#c", "ad#c")) 
'''Make the string Great''' 
def makeGood(s): 
    stack = [] 
    for ch in s: 
        if stack and abs(ord(stack[-1])-ord(ch)) == 32: 
            stack.pop() 
        else: 
            stack.append(ch) 
    return ''.join(stack) 
print(makeGood("LeEeetcode")) 
'''Baseball Game''' 
def calpoints(operations): 
    stack = [] 
    for op in operations: 
        if op  == "C": 
            stack.pop() 
        elif op == "D": 
            stack.append(stack[-1]*2) 
        elif op == '+': 
            stack.append(stack[-1]+stack[-2]) 
        else: 
            stack.append(int(op)) 
    return sum(stack) 
print(calpoints(['5','2','C','D',"+"])) 

'''min stack''' 
class Minstack:
    def __init__(self):
        self.stack = [] 
    def push(self, val): 
        if not self.stack: 
            self.stack.append(val, val)
        else: 
            self.stack.append(val, min(val, self.stack[-1][1]))   
    def pop(self): 
        self.stack.pop()  
    def top(self): 
        return self.stack[-1][0] 
    def getmin(self): 
        return self.stack[-1][1] 
obj = Minstack() 
obj.push(5) 
obj.push(2) 
obj.push(8) 
print(obj.getmin()) 

'''next greater element''' 
def nextGreaterElement(nums1, nums2): 
    stack = [] 
    mp = {} 
    for num in nums2: 
        while stack and stack[-1] < num: 
            mp[stack.pop()] = num 
        stack.append(num) 
    while stack: 
        mp[stack.pop()] = -1 
    return [mp[num] for num in nums1] 
print(nextGreaterElement([4,1,2], [1,3,4,2])) 

'''Remove outermost Parentheses''' 
def removeOutermostparentheses(s): 
    count = 0 
    result = [] 
    for ch in s: 
        if ch == '(': 
            if count > 0: 
                result.append(ch) 
            count += 1 
        else: 
            count -= 1 
            if count > 0: 
                result.append(ch) 
    return ''.join(result) 
print(removeOutermostparentheses("(()())(())"))

'''Final Prices with Special Discount''' 
def finalPrices(prices): 
    result = prices[:] 
    stack = [] 
    for i in range(len(prices)): 
        while stack and prices[stack[-1]] >= prices[i]: 
            idx = stack.pop() 
            result[idx] -=  prices[i] 
        stack.append(i) 
    return result 
print(finalPrices([8, 4, 6, 2, 3])) 

 