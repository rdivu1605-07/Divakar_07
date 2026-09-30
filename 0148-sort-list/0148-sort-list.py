class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        temp=head
        for i in l:
            temp.val=i
            temp=temp.next
        return head 