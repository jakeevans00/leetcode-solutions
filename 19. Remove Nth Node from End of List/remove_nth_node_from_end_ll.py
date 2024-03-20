# Core idea: 
# 1. Two pointers, fast and slow. Give fast a head start of n steps.
# 2. If fast is None, then n is the length of the list. Remove the head node.
# 3. If fast is not None, move together until fast.next is None. Remove node after slow

class Solution:
    def removeNthFromEnd(self, head, n: int):
        slow, fast = head, head

        for i in range(n):
            fast = fast.next
        
        if not fast:
            return slow.next
        
        while fast.next:
            slow, fast = slow.next, fast.next


        slow.next = slow.next.next

        return head


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution().removeNthFromEnd(head, 2)

while s:
    print(s.val)
    s = s.next
# Output: 1 2 3 5