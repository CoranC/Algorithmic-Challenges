import ReverseString
import unittest

class ReverseStringTest(unittest.TestCase):

  def setUp(self):
    self.rev_word_pythonic = ReverseString.rev_word_pythonic
    self.rev_word_non_pythonic = ReverseString.rev_word_non_pythonic

  def testA(self):
    self.assertEquals(self.rev_word_pythonic("Hello how are you"),
                      "you are how Hello")
    self.assertEquals(self.rev_word_non_pythonic("Hello how are you"),
                      "you are how Hello")

  def testB(self):
    self.assertEquals(self.rev_word_pythonic("     Hello   how  are you  "),
                      "you are how Hello")
    self.assertEquals(self.rev_word_non_pythonic("     Hello   how  are you  "),
                      "you are how Hello")

  def testC(self):
    self.assertEquals(self.rev_word_pythonic(""),
                      "")
    self.assertEquals(self.rev_word_non_pythonic(""),
                      "")


if __name__ == '__main__':
  unittest.main()