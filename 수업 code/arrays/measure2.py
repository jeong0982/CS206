#
# Measure how Python increases capacity of lists
# Trying to reverse-engineer the Python strategy
#

import sys
from cs206mem import slots

l = []
maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

nslots = slots(l)
print("Size %4d: %d slots" % (len(l), slots(l)))
for i in range(maxn):
  l.append(1)
  nslots1 = slots(l)
  if nslots1 != nslots:
    guess = int((nslots + 1) * 1.125 + 6)
    nslots = nslots1
    valid = "Yes" if guess == nslots else "--"
    print("Size %4d: %d slots, guess %d %s" % (len(l), slots(l), guess, valid))
