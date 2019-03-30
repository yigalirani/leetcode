# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def partition_using_vectors(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller=[]
        bigger=[]
        while head:
            if head.val>=x:
                bigger.append(head.val)
            else:
                smaller.append(head.val)
            head=head.next
        smaller.extend(bigger)
        last=None
        smaller.reverse()
        for x in smaller:
            new_head=ListNode(x)
            new_head.next=last
            last=new_head
        return last
    def partition_without_vectors(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        def set_next(head,the_next):
            head.next=the_next
            return head
        def reverse(head,last):
            while head:
                next_head=head.next
                head.next=last
                last=head
                head=next_head
            return last
        smaller=None
        bigger=None
        while head:
            next_head=head.next
            if head.val>=x:
                bigger=set_next(head,bigger)
            else:
                smaller=set_next(head,smaller)
            head=next_head
            
        return reverse(smaller,reverse(bigger,None))
            
    def partition(self, head, x):
        return self.partition_without_vectors(head,x)
            
            
        