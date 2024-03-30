#========= CLASSES

class Tree:
    
    def __init__(self, label, *children):
        self.label = label
        self.children = children 
        
    def alabel(self):
        return self.label
    
    def achildren(self):
        return self.children
    
    def nb_children(self):
        return len(self.children)
    
    def child(self, i):
        return self.children[i]
    
    def is_leaf(self):
        if self.children == ():
            return True
        else:
            return False
        
    def depth(self):
        if not self.is_leaf():
            return (1 + max([i.depth() for i in self.children]))
        return 0

    def __str__(self):
        r =""
        if self.is_leaf():
            return self.label
        r = self.label
        r += "("
        for i in self.children:
            r += str(i) + ","
        return r[:-1]+")"

    def __eq__(self, t):
        if self.depth() != t.depth():
            return False
        if self.nb_children() != t.nb_children():
            return False
        if len(self.children) == 0 :
            if self.label == t.label:
                return True
            return False
        for i in range(len(self.children)): 
            if (self.children[i] != t.children[i]):
                return False
        return True       

    def deriv(self, var):
        if self.label == var:
            return Tree("1")
        elif (self.label != "+")&(self.label != "*"):
            return Tree("0")
        if self.label == "+":
            return Tree("+",*[t.deriv(var) for t in self.children])
        #if self.label =="*":
            #return Tree("+", 
        #je ne sais pas comment faire pour la dérivée d'une multiplication

# -*- coding: utf-8 -*-

import unittest


class TestTree(unittest.TestCase):

    def test_create_tree1(self):
        a = Tree('a')
        a1 = Tree('a1', a)
        a2 = Tree('a1', a, a)
        self.assertIsNotNone(a)
        self.assertIsNot(a, a1)
        self.assertIsNot(a1, a2)

    def test_create_tree2(self):
        a = Tree('a')
        b = Tree('b')
        fab = Tree('f', a, b)
        ga = Tree('g', a)
        gb = Tree('g', b)

        self.assertEqual(a.alabel(), 'a')
        self.assertEqual(len(a.achildren()), 0)
        self.assertEqual(b.alabel(), 'b')
        self.assertEqual(len(b.achildren()), 0)

        self.assertEqual(fab.alabel(), 'f')
        self.assertEqual(fab.child(0), a)
        self.assertEqual(fab.child(1), b)

    def test_leaf(self):
        a = Tree('a')
        ga = Tree('g', a)

        self.assertTrue(a.is_leaf())
        self.assertFalse(ga.is_leaf())

    def test_depth(self):
        a = Tree('a')
        b = Tree('b')
        fab = Tree('f', a, b)
        ga = Tree('g', a)
        gb = Tree('g', b)
        fagb = Tree('f', a, gb)

        self.assertEqual(a.depth(), 0)
        self.assertEqual(fab.depth(), 1)
        self.assertEqual(ga.depth(), 1)
        self.assertEqual(gb.depth(), 1)
        self.assertEqual(fagb.depth(), 2)

    def test_eq_tree(self):
        a1 = Tree('a')
        a2 = Tree('a')
        fab1 = Tree('f', Tree('a'), Tree('b'))
        fab2 = Tree('f', Tree('a'), Tree('b'))

        self.assertEqual(a1, a2)
        self.assertEqual(fab1, fab2)
        
#========= MAIN 

t1 = Tree("a")
t2 = Tree("b")
t3 = Tree("f", t1, t2)

print(t1.label)
print([i.alabel() for i in t3.achildren()])
print(t3.is_leaf())
print(t3.depth())

print(str(t3))

print(t1.__eq__(t2))
print(str(t1))

t4 = Tree("a")
print(str(t4))

print(t1.__eq__(t4))
print(t1.__eq__(t3))

t5 = Tree("+", Tree("1"), Tree("X"))
print(str(t5.deriv("X")))
print(str(t5))

unittest.main()