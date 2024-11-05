from BinSrchTree import *

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def preorder(n):
    if n is not None:
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=' ')

class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)
        # return search_bst_iter(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg = "BSTMap :", order = 1):
        if order == 1 :
            print(msg, end='')
            inorder(self.root)
            print()
        elif order == 2:
            print(msg, end='')
            preorder(self.root)
            print()
        elif order == 3:
            print(msg, end='')
            postorder(self.root)
            print()

if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value = ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map1 = BSTMap()
    for i in range(len(data)):
        map1.insert(data[i], value[i])
    map1.display("[중위 탐색] : ", 1)

    map2 = BSTMap()
    for i in range(len(data)):
        map2.insert(data[i], value[i])
    map2.display("[전위 탐색] : ", 2)

    map3 = BSTMap()
    for i in range(len(data)):
        map3.insert(data[i], value[i])
    map3.display("[후위 탐색] : ", 3)