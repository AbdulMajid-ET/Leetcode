class Solution(object):
    def reverseList(self, head):

        previous = None
        current = head

        while current:

            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        return previous

# Recursive Solution also

'''
class Solution(object):
    def reverseList(self, head):

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        
        return new_head
'''
