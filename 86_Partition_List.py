
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller=[]
        bigger=[]
        while head:
            if head.val>=x:
                bigger.append(x)
            else:
                smaller.append(x)
        smaller.extend(bigger)
        last=None
        for x in smaller.reverse():
            head=Head(x)
            head.next=last
            last=head
        return last
            
            
            
for x in list(range(10)).reverse():
    print(x)