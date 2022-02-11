class Solution:
    # Time Complexity - O(logn)
    # Space Complexity - O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return root
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
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
        
        
    def helper(self,root,p,q,path):
        #base
        if root==None:
            return
        if root==p:
            temp = path.copy()
            self.pathp = temp
            self.pathp.append(root)
            self.pathp.append(root)
        if root==q:
            temp = path.copy()
            self.pathq = temp
            self.pathq.append(root)
            self.pathq.append(root)
        if len(self.pathp)!=0 and len(self.pathq)!=0:
            return
        #logic
        path.append(root)
        self.helper(root.left,p,q,path)
        self.helper(root.right,p,q,path)
        path.pop()'''
