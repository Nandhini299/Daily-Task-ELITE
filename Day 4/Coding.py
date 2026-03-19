# Find the duplicate in arr
arr = list(map(int,input().split()))
seen = set()
res = []

for i in arr:
    if i in seen:
        res.append(i)
    else:
        seen.add(i)
print(res)


# First Non-Repeating String
s = input() #apple

for i in s:
    count[i] = count.get(i,0) + 1

found = False

for i in s:
    if count[i] == 1:
        print(i)
        found = True
        break
if not found:
    print("None")
    
