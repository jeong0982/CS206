import sys

def make_concordance(fname):
  fd = open(fname, "r")

  concordance = dict()
  lineNumber = 0

  for s in fd.readlines():
    line = s.rstrip()
    lineNumber += 1
    print("%4d: %s" % (lineNumber, line))
    words = line.split()
    for w in words:
      word = w.rstrip(",:;.?!-").upper()
      lns = concordance.get(word, [])
      if lns == [] or lns[-1] != lineNumber:
        lns.append(lineNumber)
      concordance[word] = lns

  for w in concordance:
    lns = concordance[w]
    print("%-10s : %d" % (w, lns[0]), end='')
    for ln in lns[1:]:
      print(", %d" % ln, end="")
    print()
  print("lines: ", lineNumber)
  print("distinct words: ", len(concordance))

make_concordance(sys.argv[1])
