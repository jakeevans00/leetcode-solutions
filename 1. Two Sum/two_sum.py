class Solution:
    def twoSum(nums, target):
        complements = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in complements:
                return [i, complements[comp]]
            else:
                complements[n] = i
        
        return []
    
print(Solution.twoSum([2,7,11,15], 9)) # Answer should be [0,1] or [1,0]