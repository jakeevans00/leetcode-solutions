class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False 
    
        # return len(set(nums)) != len(nums) <- Alternate (slower) approach

    
print(Solution.containsDuplicate([1,2,2,3]))

