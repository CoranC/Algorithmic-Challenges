def rev_word_pythonic(s):
  """
  Pythonic implementation of string reversal.

  Args:
    s: (str) The string to be reversed

  Returns:
    (str) The reversed string
  """
  return " ".join(s.split()[::-1])

def rev_word_non_pythonic(s):
  """
  Non pythonic implementation of string reversal.

  Args:
    s: (str) The string to be reversed

  Returns:
    (str) The reversed string
  """
  words = []
  current_word = ""
  space = " "
  final_string = ""
  for i, char in enumerate(s):
    if char == space:
      if current_word == "": # ignore spaces if no current_word exists
        continue
      else:
        words.append(current_word) # append current word and reset
        current_word = ""
    else:
      current_word += char
      if i == len(s) - 1: # reached end of string
        words.append(current_word)
  i = len(words) - 1
  while i > -1:
    if i == 0:
      final_string += words[i]
    else:
      final_string += words[i] + " "
    i -= 1
  return final_string