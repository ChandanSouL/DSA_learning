class TreeNode():
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
#depth first search
def in_order(root):
    #root,left,right
    if root is None:
        return root
    print(root.val,end = ' ')
    in_order(root.left)
    in_order(root.right)

def pre_order(root):
    #left,root,right
    if root is None:
        return root
    pre_order(root.left)
    print(root.val,end =' ')
    pre_order(root.right)

def post_order(root):
    if root is None:
        return root
    #left,right and root
    post_order(root.left)
    post_order(root.right)
    print(root.val,end= ' ')


#bredth forst search or level order traversing
def bfs(root):
    queue = []
    if root is None:
        return root
    while queue:
        node = queue.pop(0)
        print(node.val,end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#maximum depth of the tree using dfs/bfs
def maximumDepth(root):
    if not root:
        return 
    lp = maximumDepth(root.left)
    rp = maximumDepth(root.right)
    return 1+max(lp,rp)

#minimum depth of the tree by bfs
def minimumDepth(root):
    if not root:
        return
    queue = [(root,1)]
    while queue:
        node,level = queue.pop(0)
        if not node.left  and not node.right :
            return level
        if node.left:
            queue.append(node.right,level+1)
        if node.right:
            queue.append(node.right,level+1)

#Convert Sorted Array to Binary Search Tree

def bst(self,nums,low,high):
    if not nums:
        return 
    mid = low + (high-low) //2
    node = TreeNode(nums[mid])
    node.left = self.bst(nums,low,mid-1)
    node.right = self.bst(nums,mid+1,high)

def SortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    return self.bst(nums,0,len(nums)-1)

    

