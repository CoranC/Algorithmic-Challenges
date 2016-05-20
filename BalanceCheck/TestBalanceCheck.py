from BalanceCheck import balance_check
import unittest

class BalanceCheckTest(unittest.TestCase):

  def testOneBracket(self):
    self.assertEquals(balance_check("["), False)

  def testOnlySquareBrackets(self):
    self.assertEquals(balance_check("[]"), True)

  def testLongBalancedString(self):
    self.assertEquals(balance_check("[](){([[[]]])}"), True)

  def testLongUnbalancedString(self):
    self.assertEquals(balance_check("[](){([[[}]])}"), False)

  def testEmptyString(self):
    self.assertEquals(balance_check(""), True)

  def testIncludeAsciiChars(self):
    self.assertEquals(balance_check("(a,b)"), True)

if __name__ == '__main__':
  unittest.main()