class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)

        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)