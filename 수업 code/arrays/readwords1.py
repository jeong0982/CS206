# readwords1.py
# read many words from a file and store in a Python list

import time

fname = "words.txt"

def readWords():
  f = open(fname, "r")
  words = []
  for line in f.readlines():
    s = line.strip()
    #words.append(s)
    #words.insert(0, s)
    words = words + [s]
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



