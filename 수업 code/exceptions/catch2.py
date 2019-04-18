def test(s):
  return int(100 * float(s))

def show(s):
  try:
    print(test(s))
  except ValueError:
    print("'%s' is not a number" % s)
