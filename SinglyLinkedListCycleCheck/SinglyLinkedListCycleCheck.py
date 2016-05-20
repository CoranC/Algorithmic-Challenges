class Node(object):
  """
  A Singley Linked List Node object.
  """
  def __init__(self, value):
    self.value = value
    self.next = None

def cycle_check(node):
  """
  Checks to see if a cycle exists in a linked list

  Args:
    node: (Node) A node object.

  Returns:
    True if a cycle exists else False.
  """
  marker1 = node
  marker2 = node
  while marker2.next:
    marker1 = marker1.next
    marker2 = marker2.next.next
    print marker1.value, marker2.value
    if marker1 == marker2:
      return True
  return False