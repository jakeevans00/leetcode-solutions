# Core Ideas:
# 1. Find the middle of the list
# 2. Reverse the second half of the list
# 2.5 Break the list into halves (reverse starting at middle.next and set middle.next to None to prevent cycle)
# 3. Merge the two lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findHalf(self, head):
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def reorderList(self, head) -> None:
        dummy = ListNode(0)
        dummy.next = head

        half = self.findHalf(head)

        reverse_start = self.reverseList(half.next)

        half.next = None # To prevent cycle

        while head and reverse_start:
            temp, temp2 = head.next, reverse_start.next
            head.next = reverse_start
            reverse_start.next = temp
            head = temp
            reverse_start = temp2
        
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().reorderList(head) # 1 -> 5 -> 2 -> 4 -> 3

for i in range(5):
    print(head.val)
    head = head.next