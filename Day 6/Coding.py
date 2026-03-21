# First Non - Repeating number:
# input: [4,5,1,2,0,4,1,2]
# output : 5
nums = list(map(int,input().split()))
count = {}
for i in nums:
    count[i] = count.get(i, 0) +1
    
for i in nums:
    if count[i] == 1:
        print(i)
        break

  # Remove the Duplicate from Sorted Array
  # input : [1,1,2] 
  # output: 2
      def removeDuplicates(self, nums):
        n = len(nums) #3
        j = 1

        for i in range(1, n): #starting from 1st index
            if nums[i] != nums[i-1]: #checking whther i and next of i is not eq
                nums[j] = nums[i]
                j += 1
        return j
