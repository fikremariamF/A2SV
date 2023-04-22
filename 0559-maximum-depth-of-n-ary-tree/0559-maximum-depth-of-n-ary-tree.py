"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        depth = 0
        def traverse(node):
            nonlocal depth
            nonlocal max_depth
            nodes = None
            if node:
                nodes = node.children
            else:
                return
            depth += 1
            if not nodes:
                max_depth = max(depth, max_depth)
                return
            for child in nodes:
                traverse(child)
                depth -= 1
            return
        traverse(root)
        return max_depth