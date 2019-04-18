
class EmptyQueueError(Exception):
  pass

class FullQueueError(Exception):
  pass

class Queue():
  def __init__(self, capacity):
    self._data = [ None ] * capacity
    self._front = 0
    self._rear = 0

  def is_empty(self):
    return self._front == self._rear
  
  # we always keep one slot empty to distinguish full from empty
  def is_full(self):
    return ((self._rear + 1) % len(self._data)) == self._front
  
  def front(self):
    if self.is_empty():
      raise EmptyQueueError
    return self._data[self._front]

  def dequeue(self):
    el = self.front()
    self._front = (self._front + 1) % len(self._data)
    return el

  def enqueue(self, x):
    if self.is_full():
      raise FullQueueError
    self._data[self._rear] = x
    self._rear = (self._rear + 1) % len(self._data)
