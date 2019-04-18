#
# Implementation of dict using a Binary Search Tree
#  WITHOUT recursion for insertion and deletion
#

class _Node():
  def __init__(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  # This method is still recursive
  # We will only use it for small trees to test your methods
  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    p = self
    if key == p.key:
      return p
    while key != p.key:
      if key < p.key:
        p = p.left
      else:
        p = p.right
      if key == p.key:
        return p
    return None
      
  def _insert(self, key, value):
    temp = self
    while temp.key != key:
      if key < temp.key:
        if temp.left is None:
          temp.left = _Node(key, value)
        else:
          temp = temp.left
      else:
        if temp.right is None:
          temp.right = _Node(key, value)
        else:
          temp = temp.right

  # Remove node with smallest key in the subtree rooted at this node
  # Returns the new root.
  def _remove_first(self):
    temp = self
    if temp.left is None:
      return temp.right
    while temp.left is not None:
      anode = temp
      temp = temp.left
      if temp.left is None:
        if temp.right != None:
          anode.left = temp.right
          return self
        else:
          anode.left = None
          return self

  # Returns the new root.
  def _remove(self, key):
    p = self
    b = None
    if p.key == key:
      if p.right is not None and p.left is not None:
        n = p.right._find_first()
        p.key = n.key
        p.value = n.value
        p.right = p.right._remove_first()
        return p
      elif p.left is not None:
        return p.left
      elif p.right is not None:
        return p.right
      else:
        return None
    while p.key != key:
      if key < p.key:
        if p.left is not None:
          b = p
          p = p.left
        else:
          return self
      elif key > p.key:
        if p.right is not None:
          b = p
          p = p.right
        else:
          return self
      if key == p.key:
        if p.left is not None and p.right is not None:
          n = p.right._find_first()
          p.key = n.key
          p.value = n.value
          p.right = p.right._remove_first()
          return self
        else:
          if p.left != None:
            if p == b.left:
              b.left = p.left
            else:
              b.right = p.left
            return self
          else:
            if p == b.left:
              b.left = p.right
            else:
              b.right = p.right
            return self
    return self
# --------------------------------------------------------------------

class dict():
  def __init__(self):
    self._root = None

  def __str__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def __getitem__(self, key):
    n = self._find(key)
    if n is None:
      raise KeyError(key)
    return n.value 

  def get(self, key, v = None):
    n = self._find(key)
    return n.value if n else v

  def __contains__(self, key):
    return self._find(key) is not None

  def __setitem__(self, key, value):
    if self._root is None:
      self._root = _Node(key, value)
    else:
      self._root._insert(key, value)

  def firstkey(self):
    return self._root._find_first().key if self._root else None

  def lastkey(self):
    return self._root._find_last().key if self._root else None

  def __delitem__(self, key):
    if self._root:
      self._root = self._root._remove(key)

# --------------------------------------------------------------------
