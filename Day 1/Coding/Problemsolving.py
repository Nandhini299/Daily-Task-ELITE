# 1. Missing value 
n = len(num)+1
sum_n = n * (n+1) /2
a = sum(num)
print(sum_n - a)
num = list(map(int,input().split()))


