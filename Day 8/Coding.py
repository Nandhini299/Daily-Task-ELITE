# FIND THE INTERSECTION OF TWO ARR 
# BUBBLE SORT 
# I/P : arr1 = [1,2,3,4,5] 
      # arr2 = [3,4,5,6,7]
# O/P : [3,4,5]

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

res1 = set(arr1) & set(arr2)
print(res1)

res2 = set(arr1).intersection(arr2)
print(res2)


# SELECTION SORT
# I/P : [4,0,3,2]
# O/P : [0,2,3,4]
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    print(arr)
