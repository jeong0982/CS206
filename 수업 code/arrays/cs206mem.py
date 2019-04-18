#
# Defines a function slots that returns the number of slots of capacity
# in a Python list
#

import sys as _sys

def slots(obj):
  m0 = _sys.getsizeof([])
  ss = _sys.getsizeof([ None ] * 1) - m0
  return (_sys.getsizeof(obj) - m0) // ss

