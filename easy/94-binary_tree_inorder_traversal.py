from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

# Recursive Solution
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         in_order = []
        
#         if root:
#             in_order = self.inorderTraversal(root.left)
#             in_order.append(root.val)
#             in_order = in_order + self.inorderTraversal(root.right)

#         return in_order

# Iterative Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

class TreeNodeExample:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNodeExample(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNodeExample(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True



tree = TreeNode(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(8)
tree.insert(6)
tree.insert(7)
tree.insert(9)

a = Solution()

print(a.inorderTraversal(tree))


# tree.inorder_traversal()