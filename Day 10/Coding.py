#binary search
arr = [5, 10, 15, 20, 25, 30, 35]
target = 25
l = 0
h = len(arr) - 1

while l <= h:
    mid = (l + h) // 2 
    
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        l = mid + 1  
    else:
        h = mid - 1 

