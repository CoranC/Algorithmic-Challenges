import BalanceCheck
import unittest

class BalanceCheckTest(unittest.TestCase):

  def setUp(self):
    self.balance_check = BalanceCheck.balance_check

  def testOneBracket(self):
    self.assertEquals(self.balance_check("["), False)

  def testOnlySquareBrackets(self):
    self.assertEquals(self.balance_check("[]"), True)

  def testLongBalancedString(self):
    self.assertEquals(self.balance_check("[](){([[[]]])}"), True)

  def testLongUnbalancedString(self):
    self.assertEquals(self.balance_check("[](){([[[}]])}"), False)

  def testEmptyString(self):
    self.assertEquals(self.balance_check(""), True)

  def testIncludeAsciiChars(self):
    self.assertEquals(self.balance_check("(a,b)"), True)

if __name__ == '__main__':
  unittest.main()