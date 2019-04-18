
class EmptyQueueError(Exception):
  pass

class Queue():
  def __init__(self):
    self._data = []

  def is_empty(self):
    return len(self._data) == 0
  
  def front(self):
    if self.is_empty():
      raise EmptyQueueError
    return self._data[0]

  def dequeue(self):
    if self.is_empty():
      raise EmptyQueueError
    return self._data.pop(0)

  def enqueue(self, x):
    self._data.append(x)


