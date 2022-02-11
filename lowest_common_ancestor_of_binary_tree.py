class Solution:
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left==None and right==None:
            return None
        elif left==None and right!=None:
            return right
        elif left!=None and right==None:
            return left
        else:
            return root
    
    '''
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    pathp = []
    pathq = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pathp = []
        self.pathq = []
        self.helper(root,p,q,[])
        for i in range(len(self.pathp)):
            if self.pathp[i]!=self.pathq[i]:
                return self.pathp[i-1]
        return -1
        
    def helper(self,root,p,q,path):
        # base
        if root==None:
            return
        if root.val==p.val:
            temp = path.copy()
            self.pathp = temp
            self.pathp.append(root)
            self.pathp.append(root)
        if root.val==q.val:
            temp = path.copy()
            self.pathq = temp
            self.pathq.append(root)
            self.pathq.append(root)
        # logic
        path.append(root)
        self.helper(root.right,p,q,path)
        if len(self.pathp)==0 or len(self.pathq)==0:
            self.helper(root.left,p,q,path)
        path.pop()'''
