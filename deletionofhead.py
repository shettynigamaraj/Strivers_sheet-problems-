# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteHead(self, head):
        #your code goes here
        if head==None:
            return None 
        temp=head.next
        head.next=None
        head=temp
        return head
