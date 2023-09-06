# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #size N
        #N even
        #i == twin of (n-1-i)
        # if 0<= i <= (n/2)-1
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast= fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_val = 0

        while slow:
            max_val = max(max_val,slow.val+prev.val)
            slow=slow.next
            prev = prev.next

        return max_val