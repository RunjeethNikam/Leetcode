from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        freq = {}
        temp = head
        while temp:
            freq[temp.val] = temp.random.val if temp.random else None
        print(freq)
        return head