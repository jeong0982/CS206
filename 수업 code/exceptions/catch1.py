s = input("Enter an integer> ")

try:
  x = int(s)
  print("You said: %g" % x)
except ValueError:
  print("'%s' is not a number" % s)
