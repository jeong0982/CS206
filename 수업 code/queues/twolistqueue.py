
class EmptyQueueError(Exception):
  pass

class Queue():
  def __init__(self):
    self._in = []
    self._out = []

  def is_empty(self):
    return len(self._in) == 0 and len(self._out) == 0
  
  def _ensure_out(self):
    if self.is_empty():
      raise EmptyQueueError
    if len(self._out) == 0:
      self._out = self._in
      self._in = []
      self._out.reverse()

  def front(self):
    self._ensure_out()
    return self._out[-1]

  def dequeue(self):
    self._ensure_out()
    return self._out.pop()

  def enqueue(self, x):
    self._in.append(x)
