def balance_check(s):
  """
  Checks to see if a string of brackets is balanced correctly.

  Args:
    s: (str) A string potentially containing brackets.

  Returns:
    True if the brackets in s are balanced else False.
  """
  stack = []
  brackets = {")":"(", "]":"[", "}":"{"}
  for i, b in enumerate(s):
    # starting bracket is not an opening bracket
    if i == 0 and b not in brackets.values():
      return False
    # ignore any non bracket characters
    if b not in brackets.keys() and b not in brackets.values():
      continue
    # append opening brackets to stack
    if b in brackets.values():
      stack.append(b)
    # pop corresponding closing bracket form stack
    elif brackets[b] == stack[-1]:
      stack.pop()
    else:
      return False
  return True if len(stack) == 0 else False