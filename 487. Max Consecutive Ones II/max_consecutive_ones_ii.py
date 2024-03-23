input = [1,0,1,1,0]

class Solution: 
    def max_consecutive_ones_ii(array):
        count_of_zeros = 0
        left, right = 0, 0
        max_length = 0

        while right < len(array):
            if array[right] == 0:
                count_of_zeros += 1
            
            while count_of_zeros == 2:
                max_length = max(max_length, right - left)

                if array[left] == 0:
                    count_of_zeros -= 1
                left += 1

            right += 1

        max_length = max(max_length, right - left)

        return max_length

print(Solution.max_consecutive_ones_ii(input))
