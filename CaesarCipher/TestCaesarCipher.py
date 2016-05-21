import CaesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):

  TEST_TEXT_1 = "ABC DEF."
  TEST_TEXT_2 = "XYZ ABC."
  TEST_TEXT_EMPTY = ""
  TEST_TEXT_PUNCTUATION = "><?:"

  def setUp(self):
    print(' In setUp()')
    self.cipher = CaesarCipher.CaesarCipher(3)

  def tearDown(self):
    print(' In tearDown()')
    del self.cipher

  def testRotationGetter(self):
    print "running test_rotation"
    self.assertEquals(self.cipher.rotation, CaesarCipher.ROTATION_CONSTANT + 3)

  def testRotationSetter(self):
    print "running test_rotation_setterself"
    self.cipher.rotation = 10
    self.assertEquals(self.cipher.rotation, CaesarCipher.ROTATION_CONSTANT + 10)

  def testRotationDeleter(self):
    print "running test_rotation_deleter"
    with self.assertRaises(Exception) as context:
      del self.cipher.rotation
    self.assertTrue("can't delete attribute" in context.exception)

  def test_code(self):
    print "running test_code"
    expected_text = "XYZ ABC."
    self.assertEquals(expected_text,
                      self.cipher._code(self.TEST_TEXT_1,
                                        self.cipher.rotation))

  def test_codeRotation20(self):
    print "running test_code_rotation_20"
    self.cipher.rotation = 20
    expected_text = "GHI JKL."
    self.assertEquals(expected_text,
                      self.cipher._code(self.TEST_TEXT_1,
                                        self.cipher.rotation))

  def test_codeEmptyString(self):
    print "running test_codeEmptyString"
    self.assertEquals(self.TEST_TEXT_EMPTY,
                      self.cipher._code(self.TEST_TEXT_EMPTY,
                                        self.cipher.rotation))

  def test_codeOnlyPunctuation(self):
    print "running test_codeEmptyString"
    self.assertEquals(self.TEST_TEXT_PUNCTUATION,
                      self.cipher._code(self.TEST_TEXT_PUNCTUATION,
                                        self.cipher.rotation))

  def testEncode(self):
    print "running testEncode"
    self.assertEquals(self.TEST_TEXT_2,
                      self.cipher.encode(self.TEST_TEXT_1))

  def testDecode(self):
    print "running testEncode"
    self.assertEquals(self.TEST_TEXT_1,
                      self.cipher.decode(self.TEST_TEXT_2))

if __name__ == '__main__':
  unittest.main()
