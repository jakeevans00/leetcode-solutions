class Solution:
    def longestOnes(nums, k: int) -> int:
        left, right = 0, 0
        count_of_zeros = 0
        max_sequence = 0

        while right < len(nums):
            if nums[right] == 0:
                count_of_zeros += 1
            
            while count_of_zeros == k + 1:
                max_sequence = max(max_sequence, right - left)

                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1

            right += 1

        max_sequence = max(max_sequence, right - left)

        return max_sequence
    
print(Solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))