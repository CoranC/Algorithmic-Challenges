class Node(object):
  """
  A Singley Linked List Node object.
  """
  def __init__(self, value):
    self.value = value
    self.next = None

def nth_to_last_node(n, head):
  """
  Fetches the value of the nth last node in a linked list.

  Args:
    n: (int) An int to specify the nth node from the last in a linked list.
    head: (Node) The head node object in a linked list.

  Returns:
    (Node.value) The value of the nth node.
  """
  left = head
  right = head
  count = 1
  while right.next:
    if count >= n:
      left = left.next
    count += 1
    right = right.next
  if count < n:
    raise Exception("N is greater than amount of Nodes")
  return left.value