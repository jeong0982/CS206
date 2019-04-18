def f(n):
  print("Starting f(%d) ... " % n)
  g(n)
  print("Ending f(%d) ... " % n)

def g(n):
  print("Starting g(%d) ... " % n)
  if n < 0:
    raise ValueError("Cannot handle negative numbers")
  print("The result is %d" % n)
  print("Ending g(%d) ... " % n)

def main():
  while True:
    s = input("Enter a number> ")
    if s.strip() == "":
      return
    try:
      print("Beginning of try block")
      n = int(s)
      f(n)
      print("End of try block")
    except ValueError as e:
      print("Cannot handle this input: %s" % e)

main()
