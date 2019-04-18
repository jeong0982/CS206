
class EmptyQueueError(Exception):
  pass

class _Node():
  def __init__(self, el, next):
    self.el = el
    self.next = next

class Queue():
  def __init__(self):
    self._front = None
    self._rear = None

  def is_empty(self):
    return self._front is None
  
  def front(self):
    if self.is_empty():
      raise EmptyQueueError
    return self._front.el

  def dequeue(self):
    if self.is_empty():
      raise EmptyQueueError
    el = self._front.el
    self._front = self._front.next
    return el

  def enqueue(self, x):
    if self._front is None:
      self._front = _Node(x, None)
      self._rear = self._front
    else:
      self._rear.next = _Node(x, None)
      self._rear = self._rear.next
