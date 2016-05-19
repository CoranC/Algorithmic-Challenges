import LargestContinuousSum
import unittest

class LargestContinuousSumTest(unittest.TestCase):

  def setUp(self):
    self.large_cont_sum = LargestContinuousSum.large_cont_sum

  def testA(self):
    self.assertEquals(self.large_cont_sum([1,2,-1,3,4,-1]),9)

  def testB(self):
    self.assertEquals(self.large_cont_sum([1,2,-1,3,4,10,10,-10,-1]),29)

  def testC(self):
    self.assertEquals(self.large_cont_sum([-1,1]),1)

  def testEmptyInput(self):
    self.assertEquals(self.large_cont_sum([]),0)

  def testAllNegative(self):
    self.assertEquals(self.large_cont_sum([-1,-3, -8, -5]),-1)


if __name__ == '__main__':
  unittest.main()