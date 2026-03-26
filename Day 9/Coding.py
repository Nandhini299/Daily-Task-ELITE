# SECOND LARGEST NUMBER IN AN ARRAY
# INPUT : [10, 5, 20, 8, 15]
# OUTPUT : 15
# Constraint: Do not sort the array.
ar = list(map(int, input().split()))
n = len(ar)
for i in range(n):
  for j in range(i+1,n):
    if ar[i] > ar[j]:
      temp = ar[i]
      ar[i] = ar[j]
      ar[j] = temp
print(ar[-2])


# FIBONACCI USING RECURSION
# INPUT : 4 
# OUTPUT : 0 1 1 2
def Fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return Fib(n-1) + Fib(n-2)
