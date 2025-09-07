# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1=[]
        result2=[]
        curr=l1
        while curr:
            result1.append(curr.val)
            curr=curr.next
        curr=l2
        while curr:
            result2.append(curr.val)
            curr=curr.next
        result1.reverse()
        result2.reverse()
        n1=""
        for i in result1:
            n1+=str(i)
        n1=int(n1)
        n2=""
        for i in result2:
            n2+=str(i)
        n2=int(n2)
        n3=n1+n2
        arr=[]
        while n3>9:
            a=n3%10
            arr.append(a)
            n3=n3//10
        arr.append(n3)
        def convert(arr):
            if not arr:
                return None
        head=ListNode(arr[0])
        curr=head
        for val in arr[1:]:
            curr.next=ListNode(val)
            curr=curr.next
        return head

        