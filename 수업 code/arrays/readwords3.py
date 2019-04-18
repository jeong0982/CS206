# readwords3.py
# read many words from a file and 
# store using an array with some reserve capacity 

import sys,time
from cs206array import Array

fname = sys.argv[1]

class GrowArray():
  def __init__(self):
    self._a = Array(32)
    self._size = 0

  def __len__(self):
    return self._size

  def __getitem__(self, i):
    return self._a[i]

  def append(self, el):
    if self._size == len(self._a):
      # array is full, make a new one
      oldA = self._a
      n = len(oldA)
      #self._a = Array(n + 32)
      self._a = Array(2 * n)
      for i in range(n):
        self._a[i] = oldA[i]
    self._a[self._size] = el
    self._size += 1

def readWords():
  f = open(fname, "r")
  words = GrowArray()
  for line in f.readlines():
    s = line.strip()
    words.append(s)
  f.close()
  return words

print("Starting...")
t0 = time.time()
words = readWords()
t1 = time.time()
print("Reading all %d words took %g seconds\n" % (len(words), t1 - t0))

print("The first ten words are:")
for i in range(10):
  print(words[i])
