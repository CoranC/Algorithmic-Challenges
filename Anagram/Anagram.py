def anagram(s1,s2):
  """
  An algorithm that runs in O(n) time by comparing sorted strings.

  Args:
    s1: (str) Input string assumed to contain no punctuation.
    s2: (str) Input string assumed to contain no punctuation.

  Returns:
    A bool indicating whether s1 and s2 are anagrams of each other.
  """
  s1_sort = sorted(s1.lower().replace(" ", ""))
  s2_sort = sorted(s2.lower().replace(" ", ""))
  if len(s1_sort) != len(s2_sort):
    return False
  for i, _ in enumerate(s1_sort):
    if s1_sort[i] != s2_sort[i]:
      return False
  return True