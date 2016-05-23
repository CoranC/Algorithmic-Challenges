from nthToLastNode import Node, nth_to_last_node
import unittest

class LinkedListNthToLastNodeTest(unittest.TestCase):

  def setUp(self):
    self.a = Node(1)
    self.b = Node(2)
    self.c = Node(3)
    self.d = Node(4)
    self.e = Node(5)
    self.f = Node(6)
    self.a.next = self.b
    self.b.next = self.c
    self.c.next = self.d
    self.d.next = self.e
    self.e.next = self.f

  def testNthToLastNode_LastNode(self):
    self.assertEquals(nth_to_last_node(1, self.a), 6)

  def testNthToLastNode_FirstNode(self):
    self.assertEquals(nth_to_last_node(6, self.a), 1)

  def testNthToLastNode_2ndLastNode(self):
    self.assertEquals(nth_to_last_node(2, self.a), 5)

  def testNthToLast_TooManyNodes(self):
    with self.assertRaises(Exception) as context:
      nth_to_last_node(11, self.a)
    self.assertTrue("N is greater than amount of Nodes" in context.exception)


if __name__ == '__main__':
  unittest.main()