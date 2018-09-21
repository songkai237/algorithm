class binaryTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = binaryTree(newNode)
        else:
            n = binaryTree(newNode)
            n.left = self.left
            self.left = n

    def insertRight(self, newNode):
        if self.right is None:
            self.right = binaryTree(newNode)
        else:
            n = binaryTree(newNode)
            n.right = self.right
            self.right = n

    def getLeft(self):
        if type(self.left) is binaryTree:
            return self.left.getRoot()
        else:
            return self.left

    def getRight(self):
        if type(self.right) is binaryTree:
            return self.right.getRoot()
        else:
            return self.right

    def getRoot(self):
        return self.root

    def setRoot(self, value):
        self.key = value

    def preorder(self):
        print(self.key, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=' ')

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right:
            self.right.inorder()


if __name__ == '__main__':
    tree = binaryTree(1)
    tree.left = binaryTree(2)
    tree.right = binaryTree(3)
    tree.left.left = binaryTree(4)
    tree.left.right = binaryTree(5)
    tree.left.left.left = binaryTree(6)
    tree.right.left = binaryTree(7)
    tree.right.right = binaryTree(8)
    tree.right.right.left = binaryTree(9)
    tree.right.right.right = binaryTree(10)
    print('---前序遍历---')
    tree.preorder()
    print('\n')
    print('---后序遍历---')
    tree.postorder()
    print('\n')
    print('---中序遍历---')
    tree.inorder()
