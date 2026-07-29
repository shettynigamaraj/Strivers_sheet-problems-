class Solution:
    def getLength(self, head):
        # Your code goes here
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count
