class dict():
  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)

  def __getitem__(self, k):
    i = self._findkey(k)
    if i >= 0:
      return self._data[i][1]
    else:
      raise KeyError(k)

  def get(self, k, v0 = None):
    i = self._findkey(k)
    if i >= 0:
      return self._data[i][1]
    else:
      return v0

  def __setitem__(self, k, value):
    i = self._findkey(k)
    if i >= 0:
      self._data[i] = (k, value)
    else:
      self._data.append((k, value))

  def __contains__(self, k):
    return self._findkey(k) >= 0

  def _findkey(self, k):
    for i in range(len(self._data)):
      if k == self._data[i][0]:
        return i
    return -1

  def keys(self):
    return _MapIterator(self._data)

  def __repr__(self):
    s = "ListMap("
    sep = ""
    for k, v in self._data:
      s += sep + repr(k) + ": " + repr(v)
      sep = ","
    return s + ")"

  def __iter__(self):
    return _MapIterator(self._data)
    
class _MapIterator():
  def __init__(self, d):
    self._d = d
    self._current = 0
  
  def __iter__(self):
    return self
    
  def __next__(self):
    if self._current < len(self._d):
      key = self._d[self._current][0]
      self._current += 1
      return key
    else:      
      raise StopIteration

