import string

class CaesarCipher(object):
  """
  A CaesarCipher class that encodes or decodes a string based on a specified
  rotation integer.
  """
  ALPHABET = string.ascii_uppercase
  SIZE = len(ALPHABET)

  def __init__(self, rotation=0):
    self._rotation = rotation

  @property
  def rotation(self):
    return self._rotation

  @rotation.setter
  def rotation(self, rotation):
    self._rotation = rotation

  def char_rotate_pos(self, char, rotate):
    """
    Finds a new text character based on the rotate amount.

    Args:
      char: (char) The charcater to be rotated from.
      rotate: (int) The amount of charcaters to rotate from.

    Returns:
      The new character based on the rotation amount.
    """
    return self.ALPHABET[(self.ALPHABET.find(char) - rotate) % self.SIZE]

  def _code(self, text, rotate):
    """
    Creates a string from the rotated characters.

    Args:
      text: (string) The original to be encoded or decoded.
      rotate: (int) The amount of charcaters to rotate from.

    Returns:
      The modified string that has been encoded or decoded.
    """
    text_array = []
    for char in text:
      char = char.upper()
      if char in string.ascii_uppercase:
        text_array.append(self.char_rotate_pos(char, rotate))
      else:
        text_array.append(char)
    return ''.join(text_array)

  def encode(self, text):
    """
    Encodes a string by calling _code.

    Args:
      text: (string) The original to be encoded or decoded.

    Returns:
      The result from _code.
    """

  def decode(self, text):
    """
    Decodes a string by calling _code.

    Args:
      text: (string) The original to be encoded or decoded.

    Returns:
      The result from _code.
    """
    return self._code(text, self._rotation * -1)