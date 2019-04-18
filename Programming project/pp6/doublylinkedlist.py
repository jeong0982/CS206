
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
  def __init__(self):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
  
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

  def find_first(self, x):
    node = self._front
    while node != None:
      if node.el == x:
        return node
      else:
        node = node.next
    return None

  def find_last(self, x):
    node = self._rear
    while node != None:
      if node.el == x:
        return node
      else:
        node = node.prev
    return None

  def count(self, x):
    node = self._front
    cnt = 0
    while node != None:
      if node.el == x:
        cnt += 1
      node = node.next
    return cnt

  def remove_first(self, x):
    node = (self._front).next
    while node != None:
      p_node = node.prev
      n_node = node.next
      if node.el == x:
        if n_node != None:
          if p_node != None:
            p_node.next = n_node
            n_node.prev = p_node
            return self
          else:
            (self._front).next = n_node
            n_node.prev = None
            return self
        else:
          if p_node == None:
            return None
          else:
            p_node.next = None
            (self._rear).prev = p_node
            return self
      node = n_node
    return self
        

  def remove_last(self, x):
    node = (self._rear).prev
    while node != None:
      p_node = node.prev
      n_node = node.next
      if node.el == x:
        if n_node != None:
          if p_node != None:
            p_node.next = n_node
            n_node.prev = p_node
            return self
          else:
            (self._front).next = n_node
            n_node.prev = None
            return self
        else:
          if p_node == None:
            return None
          else:
            p_node.next = None
            (self._rear).prev = p_node
            return self
      node = p_node
    return self   

  def remove_all(self, x):
    node = (self._front).next
    while node != None:
      p_node = node.prev
      n_node = node.next
      if node.el == x:
        if n_node != None:
          if p_node != None:
            p_node.next = n_node
            n_node.prev = p_node
          else:
            (self._front).next = n_node
            n_node.prev = None
        else:
          if p_node == None:
            return None
          else:
            p_node.next = None
            (self._rear).prev = p_node
      node = n_node
    return self   

  def takeout(self, n, m):
    new_l = DoublyLinkedList()
    pnode = n.prev
    f = new_l._front
    f.next = n
    n.prev = new_l._front
    nnode = m.next
    nnode.prev = pnode
    pnode.next = nnode
    m.next = new_l._rear
    new_l._rear.prev = m
    return new_l
