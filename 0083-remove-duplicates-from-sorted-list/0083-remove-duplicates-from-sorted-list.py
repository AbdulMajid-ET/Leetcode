class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        # Make sure both current and the next node exist before comparing
        while current and current.next:
            if current.val == current.next.val:
            # Skip the duplicate node by pointing to the node after it
                current.next = current.next.next
            else:
            # Values differ, so safely move current forward
                current = current.next

        return head