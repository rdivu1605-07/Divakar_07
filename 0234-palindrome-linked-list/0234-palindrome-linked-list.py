# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next


        prev=None
        current=slow
         
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

         
        pointer2=prev
        pointer1=head
        while pointer2:
            if pointer1.val!=pointer2.val:
                return False
            pointer1=pointer1.next
            pointer2=pointer2.next

        return True

            





         