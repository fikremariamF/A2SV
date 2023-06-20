# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        neighbours = defaultdict(list)
        def builder(node, parentVal):
            neighbours[node.val].append(parentVal)
            if node.left:
                neighbours[node.val].append(node.left.val)
                builder(node.left, node.val)
            if node.right:
                neighbours[node.val].append(node.right.val)
                builder(node.right, node.val)
        if root.left:
            builder(root.left, root.val)
            neighbours[root.val].append(root.left.val)
        if root.right:
            builder(root.right, root.val)
            neighbours[root.val].append(root.right.val)
        
        # print(neighbours)
        level = 0
        curr = neighbours[target.val][:]
        visited = {*curr, target.val}
        while level < k-1:
            # print("curr",curr, visited)
            temp = []
            for num in curr:
                for i in neighbours[num]:
                    if i not in visited:
                        temp.append(i)
                        visited.add(i)
            curr = temp[:]
            
            # print("level",temp)
            level += 1
        
        return curr