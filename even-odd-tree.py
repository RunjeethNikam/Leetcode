from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def process_odd(self, nodes):
        q = deque()
        lt = float('inf')
        for node in nodes:
            if node.val % 2 == 0 and node.val < lt:
                lt = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                return None, False
        return q, True

    def process_even(self, nodes):
        q = deque()
        lt= -1
        for node in nodes:
            if node.val % 2 == 1 and node.val > lt:
                lt = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                return None, False
        return q, True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while len(q):
            if level % 2 == 0:
                q, check = self.process_even(q)
            else:
                q, check = self.process_odd(q)
            print(level)
            if not check:
                return False
            level += 1
        
        return True
    



    # 4 questions
    # 1 from slides
    # 1 creative problem(medium level)
    # 2 practise problem(or similar to practise problem)(easy level)
    # one questions to calculate the time complexity


    # what is an autograder