import os, sys, numpy.random as R


class rbnode(object):

    def __init__(self, key):
        self._key = key
        self._red = False
        self._left = None
        self._right = None
        self._p = None

    key = property(fget=lambda self: self._key, doc="The node's key")
    red = property(fget=lambda self: self._red, doc="Is the node red?")
    left = property(fget=lambda self: self._left, doc="The node's left child")
    right = property(fget=lambda self: self._right, doc="The node's right child")
    p = property(fget=lambda self: self._p, doc="The node's parent")

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class rbtree(object):

    def __init__(self, create_node=rbnode):

        self._nil = create_node(key=None)

        self._root = self.nil

        self._create_node = create_node

    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")

    def search(self, key, x=None):
        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x=None):
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x=None):
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, key):
        self.insert_node(self._create_node(key=key))

    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False

    def _left_rotate(self, x):
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y

    def _right_rotate(self, y):
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x

    def check_invariants(self):

        def is_red_black_node(node):
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            if not node.left and not node.right and node.red:
                return 0, False

            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False

            if node.left and node.right:

                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True

        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root._red


    def inorder_tree_walk(self):
        print("inorder tree walk")
        def _inorder_tree_walk(node = self.root):
            if self._nil != node:
                _inorder_tree_walk(node.left)
                print("key = {0}, left = {1}, right = {2}, color = {3},"
                      " root = {4}".format(node.key, node.left, node.right, node.red, self.root == node))
                _inorder_tree_walk(node.right)

        _inorder_tree_walk()


    def preorder_tree_walk(self):
        print("preorder tree walk")
        def _preorder_tree_walk(node = self.root):
            if self._nil != node:
                print("key = {0}, left = {1}, right = {2}, color = {3},"
                      " root = {4}".format(node.key, node.left, node.right, node.red, self.root == node))
                _preorder_tree_walk(node.left)
                _preorder_tree_walk(node.right)

        _preorder_tree_walk()


    def postorder_tree_walk(self):
        print("postorder tree walk")

        def _postorder_tree_walk(node=self.root):
            if self._nil != node:
                _postorder_tree_walk(node.left)
                _postorder_tree_walk(node.right)
                print("key = {0}, left = {1}, right = {2}, color = {3},"
                    " root = {4}".format(node.key, node.left, node.right, node.red, self.root == node))
        _postorder_tree_walk()


def test_tree(t, keys):
    assert t.check_invariants()
    for i, key in enumerate(keys):
        for key2 in keys[:i]:
            assert t.nil != t.search(key2)
        for key2 in keys[i:]:
            assert (t.nil == t.search(key2)) ^ (key2 in keys[:i])
        t.insert_key(key)
        assert t.check_invariants()


# test the rbtree
# R.seed(2)
# n = 5
# size = n
# keys = R.randint(-50, 50, size=size)

keys = []

while(True):
    testKey = int(input("1)Add 2)Remove 3)Show 4)Exit"))
    if(testKey == 1):
        keys.append(int(input("Enter number")))
    elif(testKey == 2):
        keys.remove(int(input("Enter number")))
    elif(testKey == 3):
        t = rbtree()
        test_tree(t, keys)
        t.preorder_tree_walk()
        t.inorder_tree_walk()
        t.postorder_tree_walk()
    elif(testKey == 4):
        break
