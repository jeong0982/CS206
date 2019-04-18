
class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None):
    self.el = el
    self.next = next
  def __repr__(self):
    return "<" + repr(self.el) + ">"

class LinkedList:
  def __init__(self):
    self._front = None
  
  def first(self):
    if self._front is None:
      raise EmptyListError
    return self._front

  def is_empty(self):
    return self._front is None

  def __repr__(self):
    if self.is_empty():
      return "[]"
    res = "["
    p = self._front
    while p is not None:
      res += repr(p.el)
      if p.next is not None:
        res += ", "
      p = p.next
    res += "]"
    return res

