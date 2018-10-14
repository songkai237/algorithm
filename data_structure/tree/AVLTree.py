from data_structure.tree.binarySearchTree import *


class AVLTree(BinarySearchTree):

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = treeNode(key, value, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = treeNode(key, value, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        # 更新完平衡因子的节点如果大于1或者小于-1，则不平衡，需要进行调整
        if node.balanceFactor not in [-1, 1, 0]:
            self._rebalance(node)
        # 更新当前节点的父节点的平衡因子
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            # 当当前节点的父节点平衡因子为0，那么其长辈节点的平衡因子不会改变。
            # 若不为0，则递归更新其父节点的平衡因子
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def _rebalance(self, node):
        # 以当前node为根的子树左重，平衡因子大于0
        if node.balanceFactor > 0:
            # 左子树左重，node只需要做一次右旋转
            if node.leftChild.balanceFactor > 0:
                self._rotateRight(node)
            # 左子树右重，则左子树的根节点需要先做一次左旋转，然后node做右旋转
            else:
                self._rotateLeft(node.leftChild)
                self._rotateRight(node)
        # 以当前node为根的子树右重，平衡因子小于0
        else:
            # 右子树右重，node只需要做一次左旋转
            if node.rightChild.balanceFactor < 0:
                self._rotateLeft(node)
            # 右子树左重，则右子树的根节点需要先做一次右旋转，然后node做左旋转
            else:
                self._rotateRight(node.rightChild)
                self._rotateLeft(node)

    # 对节点进行左旋转
    def _rotateLeft(self, node):
        # 用newNode来跟踪旋转后的根节点，也就是node的右孩子
        newNode = node.rightChild
        node.balanceFactor = self.treeHeight(node.leftChild) - self.treeHeight(newNode.leftChild)
        newNode.balanceFactor = node.balanceFactor - self.treeHeight(newNode.rightChild)
        node.rightChild = newNode.leftChild
        if newNode.leftChild:
            newNode.leftChild.parent = node
        newNode.leftChild = node
        if node.parent:
            newNode.parent = node.parent
            if node.isLeftChild():
                node.parent.leftChild = newNode
            else:
                node.parent.rightChild = newNode
        else:
            newNode.parent = None
            self.root = newNode
        node.parent = newNode

    def _rotateRight(self, node):
        newNode = node.leftChild
        node.balanceFactor = self.treeHeight(newNode.rightChild) - self.treeHeight(node.rightChild)
        newNode.balanceFactor = self.treeHeight(newNode.leftChild) - node.balanceFactor
        node.leftChild = newNode.rightChild
        if newNode.rightChild:
            newNode.rightChild.parent = node
        newNode.rightChild = node
        if node.parent:
            newNode.parent = node.parent
            if node.isLeftChild():
                node.parent.leftChild = newNode
            else:
                node.parent.rightChild = newNode
        else:
            newNode.parent = None
            self.root = newNode
        node.parent = newNode


if __name__ == '__main__':
    tree = AVLTree()
    tree.put(1, 1)
    tree.put(2, 2)
    tree.put(3, 3)
    # print(f'root={tree.root.value},rootblc={tree.root.balanceFactor}')
    tree.put(2.5, 2.5)
    tree.put(2.7, 2.7)
    print("前序")
    tree.preOrder(tree.root)
    print(f'root:{tree.root.key}')
    print("中序")
    tree.inOrder(tree.root)

