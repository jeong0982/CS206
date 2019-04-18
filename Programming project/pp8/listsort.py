#
# DoublyLinkedList with Mergesort
#

class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class DoublyLinkedList:
  def __init__(self, *els):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
    for el in els:
      self.append(el)
  
  def is_empty(self):
    return self._front.next == self._rear

  def first(self):
    if self.is_empty():
      raise EmptyListError
    return self._front.next

  def last(self):
    if self.is_empty():
      raise EmptyListError
    return self._rear.prev

  def __repr__(self):
    res = "["
    p = self._front.next
    while p != self._rear:
      res += str(p.el)
      if p.next != self._rear:
        res += ", "
      p = p.next
    res += "]"
    return res

  def __len__(self):
    p = self._front.next
    count = 0
    while p != self._rear:
      count += 1
      p = p.next
    return count

  def insert_after(self, n, el):
    p = Node(el, n.next, n)
    n.next.prev = p
    n.next = p

  def prepend(self, el):
    self.insert_after(self._front, el)
  
  def append(self, el):
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

# --------------------------------------------------------------------

  def median(self):
    "Returns the node in the middle of the list."
    a = self._front
    b = self._rear
    while a != b:
      if a.prev == b:
        return a.prev
      a = a.next
      b = b.prev
    return a
    

  def split(self, n):
    "Removes all nodes after n from this list and returns them in a new DoublyLinkedList object."
    newlist = DoublyLinkedList()
    if n == self._rear.prev:
      return newlist
    newlist._front.next = n.next
    newlist._rear.prev = self._rear.prev
    n.next.prev = newlist._front
    newlist._rear.prev.next = newlist._rear
    n.next = self._rear
    self._rear.prev = n
    return newlist

  def steal(self, other):
    "Moves first node in other list to the end of this list."
    self._rear.prev.next = other._front.next
    other._front.next.prev = self._rear.prev
    other._front.next = other._front.next.next
    self._rear.prev = self._rear.prev.next
    other._front.next.prev = other._front
    self._rear.prev.next = self._rear

  def merge(self, other):
    "Merges elements from sorted other list into this sorted list."
    left = self.split(self._front)  # move all elements to a new list
    # now merge left and other
    while not left.is_empty() or not other.is_empty():
      if left._front.next == left._rear:
        self.steal(other)
      elif other._front.next == other._rear:
        self.steal(left)
      elif left._front.next.el > other._front.next.el:
        self.steal(other)
      else:
        self.steal(left)
    

# --------------------------------------------------------------------

  def sort(self):
    # is length <= 1 ?
    if self.is_empty() or self._front.next.next == self._rear:
      return
    other = self.split(self.median())
    self.sort()
    other.sort()
    self.merge(other)

# --------------------------------------------------------------------
