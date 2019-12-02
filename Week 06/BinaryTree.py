from random import *

class TreeNode:
    def __init__(self, val):
        self.Left = None
        self.Right = None
        self.Value = val
    
    def printNode(self, depth = 0):
       me = self.Value
       for x in range(depth):
        me = " " + str(me)
       if not self.Left is None:
           self.Left.printNode(depth + 1)
       print(me)
       if not self.Right is None:
           self.Right.printNode(depth + 1)
    
class BinaryTree:
    def __init__(self):
        self.Root = None
    
    def Insert(self, val, node):
        if node == None:
            self.Root = TreeNode(val)
        elif val <= node.Value:
            if node.Left is None:
                node.Left = TreeNode(val)
            else:
                self.Insert(val, node.Left)
        else:
            
            if node.Right is None:
                node.Right = TreeNode(val)
            else:
                self.Insert(val, node.Right)
    
    def InsertList(self, list):
        for x in list:
            self.Insert(x, self.Root)

    def printTree(self):
        self.Root.printNode()

def main():
    listSize = randrange(1, 100)
    list = []
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    for x in range(listSize):
        nextVal = randint(-50,50)
        list.append(nextVal)
        tree1.Insert(nextVal, tree1.Root)
    tree2.InsertList(list)
    print("Tree1 - Inerting Elements one at a time")
    tree1.printTree()
    print("Tree2 - Inserting a Whole List")
    tree2.printTree()
    print("List")
    print(list)
main()