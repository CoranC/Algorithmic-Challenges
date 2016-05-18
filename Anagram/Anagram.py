def anagram(s1,s2):
  s1_sort = sorted(s1.lower().replace(" ", ""))
  s2_sort = sorted(s2.lower().replace(" ", ""))
  if len(s1_sort) != len(s2_sort):
    return False
  for i, _ in enumerate(s1_sort):
    if s1_sort[i] != s2_sort[i]:
      return False
  return True