#
# Measure how Python increases capacity of lists
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
    nslots = nslots1
    print("Size %4d: %d slots" % (len(l), slots(l)))
    
