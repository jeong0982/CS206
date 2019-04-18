def f(n):
  print("Starting f(%d) ... " % n)
  g(n)
  print("Ending f(%d) ... " % n)

def g(n):
  print("Starting g(%d) ... " % n)
  m = 100 // n
  print("The result is %d" % m)
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
    except ValueError:
      print("Please enter a number!")
    except ZeroDivisionError:
      print("I can't handle this value!")

main()
