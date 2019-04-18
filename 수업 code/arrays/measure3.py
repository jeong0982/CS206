#
# Measure some Python list operations
#

from cs206mem import slots

def show(l):
  print("List: %s" % str(l[:10]))
  print("Length: %d, Slots: %d" % (len(l), slots(l)))
  
print("List literal:")
show([1, 2, 3, 4, 5, 6])
print("From range:")
show(list(range(1, 7)))
print("Fixed length:")
show( [ 7 ] * 97)

l = [17] * 1000
r = [13] * 1000
show(l)
show(r)

print("Extending:")
l.extend(r)
show(l)
m = [17] * 1000
m.append(19)
show(m)
m.extend( [ 23 ] * 100)
show(m)

print("Slicing:")
l1 = l[100:1400]
show(l1)



