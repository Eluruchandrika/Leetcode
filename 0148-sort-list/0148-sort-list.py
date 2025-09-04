# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  
  def sortList(self,head):
    vals=[]
    temp=head
    while temp:
        vals.append(temp.val)
        temp=temp.next
    vals.sort()
    i=0
    temp=head
    while temp:
        temp.val=vals[i]
        i=i+1
        temp=temp.next
    return head

    
        