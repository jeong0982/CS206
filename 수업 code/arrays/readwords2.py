# readwords2.py
# read many words from a file and store using an array

import sys,time
from cs206array import Array

fname = sys.argv[1]

class GrowArray():
  def __init__(self):
    self._a = None

  def __len__(self):
    return len(self._a)

  def __getitem__(self, i):
    return self._a[i]

  def append(self, el):
    if self._a == None:
      self._a = Array(1)
      self._a[0] = el
    else:
      oldA = self._a
      n = len(oldA)
      self._a = Array(n + 1)
      for i in range(n):
        self._a[i] = oldA[i]
      self._a[n] = el

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
