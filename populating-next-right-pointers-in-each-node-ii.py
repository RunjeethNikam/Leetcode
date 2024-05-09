from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root is None:
            return None
        
        current = root
        dummy = Node(-1999)
        head = root

        while head:
            current = head
            prev = dummy

            while current:
                if current.left:
                    prev.next = current.left
                    prev = prev.next
                if current.right:
                    prev.next = current.right
                    prev = prev.next
                current = current.next
            head = dummy.next
            dummy.next = None
        return root

        # q = deque()
        # q.append(root)
        # q.append(None)
        # while len(q):
        #     item = q.popleft()
        #     if item:
        #         if item.left:
        #             if q[-1]:
        #                 q[-1].next = item.left
        #             q.append(item.left)
        #         if item.right:
        #             if q[-1]:
        #                 q[-1].next = item.right
        #             q.append(item.right)
        #     elif not item and len(q):
        #         q.append(item)
        # return root
    


Solution().connect(root)
            