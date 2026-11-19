
class Solution:
    def hasCycle(self, head):
        # Start both pointers at the beginning of the linked list
        slow = head
        fast = head

        # Keep moving while fast can move forward
        while fast and fast.next:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle
        return False

'''
In this problem, we need to check whether a linked list contains a cycle or not. We use two pointers: slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If both pointers meet, it means a cycle exists, so we return True. If the fast pointer reaches None, there is no cycle, so we return False. This approach is called Floyd's Cycle Detection Algorithm.
'''