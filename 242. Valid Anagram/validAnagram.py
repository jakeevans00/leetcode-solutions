class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        
        for char in t:
            if char not in map:
                return False
            else:
                map[char] -= 1
            
        for value in map.values():
            if value != 0:
                return False
        
        return True
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         counts = defaultdict(int)

#         if len(s) != len(t):
#             return False

#         for i in range(len(s)):
#             counts[s[i]] += 1
#             counts[t[i]] -= 1

#         for value in counts.values():
#             if value != 0:
#                 return False
        
#         return True
