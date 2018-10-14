class treeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None

    def hasAnyChildren(self):
        return self.leftChild is not None or self.rightChild is not None

    def hasBothChildren(self):
        return self.leftChild is not None and self.rightChild is not None

    def replaceNodeData(self, key, value, left, right):
        self.key = key
        self.value = value
        self.rightChild = left
        self.rightChild = right
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._getNode(key, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def inOrder(self, node):
        if node.leftChild:
            self.inOrder(node.leftChild)
        print(node.key)
        if node.rightChild:
            self.inOrder(node.rightChild)

    def preOrder(self, node):
        print(node.key)
        if node.leftChild:
            self.preOrder(node.leftChild)

        if node.rightChild:
            self.preOrder(node.rightChild)

    def length(self):
        return self.size

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = treeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = treeNode(key, value, parent=currentNode)

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = treeNode(key, value)
        self.size += 1

    def _getNode(self, key, currentNode):
        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._getNode(key, currentNode.leftChild)
        else:
            return self._getNode(key, currentNode.rightChild)

    def get(self, key):
        if not self.root:
            return None
        else:
            node = self._getNode(key, self.root)
            if node:
                return node.value
            else:
                return None

    def delete(self, key):
        if self.__contains__(key):
            if self.size == 1 and self.root.key == key:
                self.root = None
                self.size -= 1
            else:
                node = self._getNode(key, self.root)
                self._deleteNode(node)
                self.size -= 1
        else:
            print("The key is not in tree")

    def _deleteNode(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            node = self._findMax(currentNode.leftChild)
            if node.isLeaf():
                currentNode.key = node.key
                currentNode.value = node.value
                node.parent.rightChild = None
            else:
                currentNode.key = node.key
                currentNode.value = node.value
                node.parent.rightChild = node.leftChild
                node.leftChild.parent = node.parent
        else:
            if currentNode.isLeftChild():
                if currentNode.hasLeftChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
            elif currentNode.isRightChild():
                if currentNode.hasLeftCHild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
            else:
                if currentNode.hasLeftChild():
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.value,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.value,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )

    def _findMax(self, currentNode):
        if currentNode.rightChild is None:
            return currentNode
        else:
            return self._findMin(currentNode.rightChild)

    def _findMin(self, currentNode):
        if currentNode.leftChild is None:
            return currentNode
        else:
            return self._findMax(currentNode.leftChild)

    def treeHeight(self, node):
        if node is None:
            return 0
        return max(self.treeHeight(node.leftChild), self.treeHeight(node.rightChild)) + 1

# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     tree.put(10, 10)
#     tree.put(78, 78)
#     tree.put(5, 5)
#     tree.put(42, 42)
#     tree.put(8, 8)
#     tree.put(3, 3)
#     tree.put(4, 4)
#     tree.put(1, 1)
#     tree.put(100, 100)
#
#     # tree.inOrder(tree.root)
#     tree.delete(10)
#     print(tree.root.key)
#     print(tree.root.leftChild.key)
#     print(tree.root.rightChild.key)
#     tree.inOrder(tree.root)
