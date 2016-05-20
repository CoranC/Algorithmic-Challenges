from ReverseString import rev_word_pythonic, rev_word_non_pythonic
import unittest

class ReverseStringTest(unittest.TestCase):

  def testA(self):
    self.assertEquals(rev_word_pythonic("Hello how are you"),
                      "you are how Hello")
    self.assertEquals(rev_word_non_pythonic("Hello how are you"),
                      "you are how Hello")

  def testB(self):
    self.assertEquals(rev_word_pythonic("  Hello   how  are you  "),
                      "you are how Hello")
    self.assertEquals(rev_word_non_pythonic("  Hello   how  are you  "),
                      "you are how Hello")

  def testC(self):
    self.assertEquals(rev_word_pythonic(""),
                      "")
    self.assertEquals(rev_word_non_pythonic(""),
                      "")


if __name__ == '__main__':
  unittest.main()