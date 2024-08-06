class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node, result):
        if not node:
            return
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)

# Example usage:
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# sol = Solution()
# print(sol.inorderTraversal(root))  # Output: [1, 3, 2]

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

# Example usage:
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# sol = Solution()
# print(sol.inorderTraversal(root))  # Output: [1, 3, 2]