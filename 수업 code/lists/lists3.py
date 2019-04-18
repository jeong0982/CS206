
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

  def prepend(self, el):
    self._front = Node(el, self._front)

  def remove_first(self):
    if self._front is None:
      raise EmptyListError
    self._front = self._front.next

  def insert_after(self, n, el):
    n.next = Node(el, n.next)

  def remove_after(self, n):
    if n.next is None:
      raise ValueError(n)
    n.next = n.next.next

  def before(self, n):
    p = self._front
    while p.next != n:
      p = p.next
    return p

  def last(self):
    p = self._front
    while p.next != null:
      p = p.next
    return p
  
  def __len__(self):
    if self.is_empty():
      return 0
    p = self._front
    count = 0
    while p is not None:
      count += 1
      p = p.next
    return count

