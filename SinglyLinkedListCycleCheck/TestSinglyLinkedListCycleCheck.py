from SinglyLinkedListCycleCheck import cycle_check
import SinglyLinkedListCycleCheck
import unittest

class SinglyLinkedListCycleCheckTest(unittest.TestCase):

  def setUp(self):
    self.a = SinglyLinkedListCycleCheck.Node(1)
    self.b = SinglyLinkedListCycleCheck.Node(2)
    self.c = SinglyLinkedListCycleCheck.Node(3)

  def testNoCycle(self):
    print "testNoCycle"
    self.a.next = self.b
    self.b.next = self.c
    self.assertEquals(cycle_check(self.a), False)

  def testCycle(self):
    print "testCycle"
    self.a.next = self.b
    self.b.next = self.c
    self.c.next = self.a
    self.assertEquals(cycle_check(self.a), True)

if __name__ == '__main__':
  unittest.main()