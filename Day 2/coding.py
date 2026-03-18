
# Missing Value:
num = int(input())
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num //= 10
print(rev)

# Second Largest number
num = list(map(int, input().split()))

first = -1 #init min value
sec = -1

for i in num:
    if i > first:
        sec = first
        first = i
    elif i > sec:
        sec = i
print(sec)
