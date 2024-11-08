class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

def search_bst(n, key) :
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n, key) :
    while n != None :
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value) :
    if n == None :
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None :
       return res
    return search_value_bst(n.right, value)

def search_max_bst(n) :
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n) :
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n) :
    if n.key < r.key:
        if r.left is None :
           r.left = n
           return True
        else :
           return insert_bst(r.left, n)
    elif n.key > r.key :
        if r.right is None :
           r.right = n
           return True
        else :
           return insert_bst(r.right, n)
    else :
        return False

def delete_bst_case1 (parent, node, root) :
    if parent is None:
        root = None
    else :
        if parent.left == node:
            parent.left = None
        else :
            parent.right = None
    return root

def delete_bst_case2 (parent, node, root) :
    if node.left is not None :
        child = node.left
    else :
        child = node.right

    if node == root :
        root = child
    else :
        if node is parent.left :
            parent.left = child
        else :
            parent.right = child
    return root

def delete_bst_case3 (parent, node, root) :
    succp = node
    succ = node.right
    while (succ.left != None) :
        succp = succ
        succ = succ.left

    if (succp.left == succ) :
        succp.left = succ.right
    else :
        succp.right = succ.right

    node.key = succ.key
    node.value= succ.value
    node = succ

    return root

def delete_bst (root, key) :
    if root == None : return None

    parent = None
    node = root
    while node != None and node.key != key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;
    if node == None : return root

    if node.left == None and node.right == None :
        root = delete_bst_case1 (parent, node, root)

    elif node.left==None or node.right==None :
        root = delete_bst_case2 (parent, node, root)

    else :
        root = delete_bst_case3 (parent, node, root)

    return root