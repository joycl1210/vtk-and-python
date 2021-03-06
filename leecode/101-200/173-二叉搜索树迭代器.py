# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.tree = []
        if not root:
            return
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                self.tree.append(cur.val)
                cur = cur.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.tree.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.tree else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
