# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = 0
        p = 0
        
        while True:
            num1 = num1 + l1.val*(10**p)
            p = p + 1
            if l1.next is None:
                break
            l1 = l1.next
        
        num2 = 0
        p = 0
        
        while True:
            num2 = num2 + l2.val*(10**p)
            p = p + 1
            if l2.next is None:
                break
            l2 = l2.next
            
            
        sum_num = num1 + num2
        
        
        new_node = None
        head_node = None        
        
        while True:
            prev_node = new_node
            new_node = ListNode(sum_num%10)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                head_node = new_node

            sum_num = sum_num//10
            
            if sum_num is 0:
                break
        return head_node
            
