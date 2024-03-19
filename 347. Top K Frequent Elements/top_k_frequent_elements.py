from collections import defaultdict

class Solution:
    def topKFrequent(nums, k: int):
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        return get_top_n_keys(counts, k)
        
def get_top_n_keys(dict, n):
        sorted_dictionary = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        top_n_keys = [s[0] for s in sorted_dictionary[:n]]
        return top_n_keys

print(Solution.topKFrequent([1,1,1,2,2,3],2))