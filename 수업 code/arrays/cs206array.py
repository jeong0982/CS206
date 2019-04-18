# cs206array.py
# implements a basic Array type for Python

class Array():
  """An array with size slots"""
  def __init__(self, size):               
    assert size > 0, "Array size must be > 0"
    self._size = size    
    self._elements = [ None ] * size
    
  def __len__(self):
    return self._size
    
  def __getitem__(self, i):
    assert i >= 0 and i < len(self), "Array subscript out of range"
    return self._elements[i]
    
  def __setitem__(self, i, v):
    assert i >= 0 and i < len(self), "Array subscript out of range"
    self._elements[i] = v

  def __repr__(self):
    s = "Array("
    sep = ""
    for i in range(len(self)):
      s += sep + repr(self._elements[i])
      sep = ", "
    s += ")"
    return s

  def __iter__(self):
    return _ArrayIterator(self._elements)
        
class _ArrayIterator:
  def __init__(self, theArray):
    self._arrayRef = theArray
    self._curNdx = 0
    
  def __iter__(self):
    return self
    
  def __next__(self):
    if self._curNdx < len(self._arrayRef):
      entry = self._arrayRef[self._curNdx]
      self._curNdx += 1
      return entry
    else:      
      raise StopIteration               

