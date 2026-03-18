# Check Palindrome
num = int(input())
cast = str(num) #int cannot use str rev
rev = cast[::-1]

if rev == cast:
  print("True")
else:
  print("False")


# Reverse a string
def ReverseString(s):
  return s[::-1]
