# 2. DSA 
# Max Number

def Maxi(arr):
    if not arr:
        return None
    
    max_num = arr[0]
    
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num 