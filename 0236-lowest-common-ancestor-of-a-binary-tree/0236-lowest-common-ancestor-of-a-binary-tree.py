class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q: return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        if L and R: return root
        return L or R 