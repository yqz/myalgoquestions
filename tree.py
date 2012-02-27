#!/usr/bin/python
import pdb

class TreeNode(list):
    """A TreeNode is represented by list of list"""
    def __init__(self, iterable=(), **attr):
        """iterable should be all the child"""
        self.__dict__.update(attr)
        list.__init__(self, iterable)

    def __getattr__(self, name):
        """special attribute handling for binary tree"""
        if name == 'left':
            return self[0] if len(self) > 0 else None
        elif name == "right":
            return self[1] if len(self) > 1 else None
        else:
            raise AttributeError()
    def __repr__(self):
        return "[" + str(self.data) + ",".join([repr(x) for x in self]) + "]"

def inorder_traversal(node, func):
    if node.left is not None:
        inorder_traversal(node.left, func)
    func(node)
    if node.right is not None:
        inorder_traversal(node.right, func)

    
def preorder_traversal(node, func):
    func(node)
    if node.left is not None:
        preorder_traversal(node.left, func)
    if node.right is not None:
        preorder_traversal(node.right, func)


def postorder_traversal(node, func):
    if node.left is not None:
        postorder_traversal(node.left, func)
    if node.right is not None:
        postorder_traversal(node.right, func)
    func(node)


def inorder_traversal_iterative_1(node, func):
    """iteratively tranverse a tree this function
    use a stack to keep the path from root to the 
    current node. it's the same as if you have a 
    parent pointer on each node"""
    path = []
    # Firstly find the left most node.
    while node.left is not None:
        path.append(node)
        node = node.left
    func(node)
    # Iteratively find successor of the current
    # node.
    while True:
        node = inorder_successor(node, path)
        if node is not None:
            func(node)
        else:
            return

def inorder_traversal_iterative_2(node, func):
    """iteratively tranverse a tree. This function
    use a stack to mimic the call stack which keeps
    all the node of the ancestors of the current node
    that could appear afterwards"""
    stack = []
    while node is not None:
        # push all left child to stack
        while node is not None:
            stack.append(node)
            node = node.left
        # pop out
        while True:
            node = stack.pop()
            func(node)
            if len(stack) == 0 or node.right is not None:
                break
        node = node.right

def postrder_traversal_iterative_2(node):
    stack = []
    needpush = True
    while node is not None:
        if needpush:
            while node is not None:
                stack.append(node)
                node = node.left
        while len(stack) > 0:
            parent = stack.pop()
            if parent.left is node:
                if parent.right is not None:
                    stack.append(parent)
                    node = parent.right
                    needpush = True
                    break
                else:
                    needpush = False
                    node = None if len(stack) == 0 else parent
                    yield parent
            else:
                needpush = False
                node = None if len(stack) == 0 else parent
                yield parent


def traversal_helper(node, first_func, successor_func):
    path = []
    node = first_func(node, path)
    while node is not None:
        yield node
        node = successor_func(node, path)

def left_most(node, path):
    while node.left is not None:
        path.append(node)
        node = node.left
    return node

def inorder_successor(node, path):
    """given the path to the node, find the succssor.
    if the current noe has right child, successor is
    always the left most node of the right sub tree.
    otherwise, trace back until the first ancestor that
    has the current node as left side. """
    if node.right is not None:
        path.append(node)
        return left_most(node.right, path)
    else:
        while len(path) > 0:
            parent = path.pop()
            if parent.left is node:
                return parent 
            node = parent
        return None

def postorder_successor(node, path):
    """the succssor of the current node when doing post
    order traversal is:
    if parent has right chlid: 
        1. current nodde is left child of parent: left_most of right child.
        2. current node is right child of parent: parent
    if parent hasn't right child: parent
    if parent is None: None """
    if len(path) == 0:
        return None
    parent = path.pop()
    if parent.right is None:
        return parent
    elif parent.right is node:
        return parent
    else:
        path.append(parent)
        return left_most(parent.right, path)


def inorder_iterator(node):
    return traversal_helper(node, left_most, inorder_successor)

def postorder_iterator(node):
    return traversal_helper(node, left_most, postorder_successor)



import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        t = TreeNode((TreeNode((), data=2), TreeNode((), data=3)), data = 1)
        self.assertEqual(1, t.data)
        self.assertEqual(2, t.left.data)
        self.assertEqual(3, t.right.data)
        self.assertEqual(None, t.left.left)

    def test_traversal(self):
        t = TreeNode((TreeNode((), data=2), TreeNode((), data=3)), data = 1)
        t2 = TreeNode((TreeNode((), data=5), None), data = 4)
        t = TreeNode((t,t2), data = 6)
        """
              6
            /  \
           1    4
          / \  /
         2   3 5
        """
        x = []
        def func(n):
            x.append(n.data)
        inorder_traversal(t, func)
        self.assertEqual([2,1,3,6,5,4], x)
        x = []
        preorder_traversal(t, func)
        self.assertEqual([6,1,2,3,4,5], x)
        x = []
        postorder_traversal(t, func)
        self.assertEqual([2,3,1,5,4,6], x)
        x = []
        inorder_traversal_iterative_1(t, func)
        self.assertEqual([2,1,3,6,5,4], x)
        x = []
        inorder_traversal_iterative_2(t, func)
        self.assertEqual([2,1,3,6,5,4], x)
        x = [y.data for y in inorder_iterator(t)]
        self.assertEqual([2,1,3,6,5,4], x)
        x = [y.data for y in postorder_iterator(t)]
        self.assertEqual([2,3,1,5,4,6], x)
        x = [y.data for y in postrder_traversal_iterative_2(t)]
        self.assertEqual([2,3,1,5,4,6], x)
        print t


        

if __name__ == '__main__':
    unittest.main()
