# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map={}
        curr=head
        while curr:
            if curr in map:
                map[curr]+=1
                return True
            else:
                map[curr]=1
            curr=curr.next
        return False
        
        