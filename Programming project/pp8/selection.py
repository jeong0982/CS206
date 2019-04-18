#
# select returns the k-th smallest element of a
#
def select(a, k):
  b = sorted(a)
  return b[k]

# Implement the function quick_select.
# It also returns the k-th smallest element of a.
def quick_select(a, k):
  if len(a) == 1 and k == 1 :
    return a[0]
  pivot = a[len(a) // 2]
  small = []
  equal = []
  large = []
  for x in a:
    if x < pivot:
      small.append(x)
    elif x == pivot:
      equal.append(x)
    else:
      large.append(x)
  if len(small) + len(equal) -1  >= k and len(small)-1 < k:
    return pivot
  if len(small)-1 >= k:
    return quick_select(small, k)
  if len(small) + len(equal) -1 < k:
    return quick_select(large, k-len(small)-len(equal))

