
class Node:
  def __init__(self, el, next=None):
    self.el = el
    self.next = next
  def __repr__(self):
    return "<" + repr(self.el) + ">"

