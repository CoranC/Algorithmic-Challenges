import Anagram
import unittest

class AnagramTest(unittest.TestCase):

  def setUp(self):
    self.anagram = Anagram.anagram

  def testA(self):
    self.assertEquals(self.anagram('go go go','gggooo'), True)

  def testOrder(self):
    self.assertEquals(self.anagram('abc','cba'), True)

  def testMultipleSpaces(self):
    self.assertEquals(self.anagram('hi man','hi     man'), True)

  def testDifferentStrings(self):
    self.assertEquals(self.anagram('aabbcc','aa2bbc'), False)

  def testNumbers(self):
    self.assertEquals(self.anagram('123','1 2'), False)

if __name__ == '__main__':
  unittest.main()