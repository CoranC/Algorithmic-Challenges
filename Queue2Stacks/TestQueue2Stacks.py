import Queue2Stacks
import unittest

class Queue2StacksTest(unittest.TestCase):

  def setUp(self):
    self.q = Queue2Stacks.Queue2Stacks()

  def testA(self):
    result = []
    for i in xrange(5):
      self.q.enqueue(i)
    for i in xrange(5):
      result.append(self.q.dequeue())

    self.assertEquals(result, [0,1,2,3,4])

if __name__ == '__main__':
  unittest.main()