class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                tato = root
                strem = root.right
                while strem.left:
                    tato = strem
                    strem = strem.left
                if tato != root:
                    tato.left = strem.right
                else:
                    root.right = strem.right
                root.val = strem.val
        return root