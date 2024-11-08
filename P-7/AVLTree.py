from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A) :
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A) :
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A) :
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A) :
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance (parent) :
    hDiff = calc_height_diff(parent)

    if hDiff > 1 :
        if calc_height_diff( parent.left ) > 0 :
            parent = rotateLL( parent )
        else :
            parent = rotateLR( parent )
    elif hDiff < -1 :
        if calc_height_diff( parent.right ) < 0 :
            parent = rotateRR( parent )
        else :
            parent = rotateRL( parent )
    return parent

def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")


def delete_min_avl(parent):
    if parent.left is None:
        return parent.right

    parent.left = delete_min_avl(parent.left)

    return reBalance(parent)

from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    # node = [0,1,2,3,4,5,6,7,8,9]

    root = None
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = insert_avl(root, n)

        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    print("모든 노드 삭제 과정:")
    while root is not None:
        print(" 최소값 삭제:", end=' ')
        levelorder(root)
        print()
        root = delete_min_avl(root)

    print("모든 노드 삭제 후:")
    if root is None:
        print(" 트리가 비어 있습니다.")
