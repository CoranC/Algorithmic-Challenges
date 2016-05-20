class Queue2Stacks(object):

  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, element):
    self.stack1.append(element)

  def dequeue(self):
    stack1_len = len(self.stack1)
    while len(self.stack2) < stack1_len:
      self.stack2.append(self.stack1.pop())
    return self.stack2.pop()
