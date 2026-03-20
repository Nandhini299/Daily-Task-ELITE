# First Non-Repeating Number 
# Input : [1,2,3,4,2,5,3]
# output : 2
# key - number, value - freq
n = list(map(int,input().split()))
count = {} #hashing 
# count freq
for i in n:
    count[i] = count.get(i,0) +1
    
# First non num
for i in n:
    if count[i] > 1:
        print(i)
        break

# Find square root of a number using binary search
# input : 10 
# output : 3
def SqrtRoot_Binary(n):
    low, high = 0, n
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
    if mid * mid == n:
        return n
    
    elif mid * mid < n:
        ans = mid
        low = mid + 1 #move right 
        
    else:
        high = mid - 1 #move left
return ans
