#
# A few examples using recursion
#

def number_of_threes(n):
	if n<10:
		if n==3:
			return 1
		else:
			return 0
	else:
		r=n%10
		if r==3:
			return 1+number_of_threes(n//10)
		else:
			return 0+number_of_threes(n//10)
def palindrome(s):
        if len(s)<2:
                return True
        if s[0]!=s[-1]:
                return False
        return palindrome(s[1:-1])

def bin_log(n):
  if n<2:
    return 0
  else:
    return 1+bin_log(n/2)

if __name__ == "__main__":
  for n in [ 0, 7, 3, 13, 33333, 123454321, 12333983393893 ]:
    print("%d contains %d threes" % (n, number_of_threes(n)))
  print()
  for s in ["abba", "omma", "a", "", "ere", "era", 
            "amanaplanacanalpanama" ]:
    print("'%s' is a palindrome? %s" % (s, palindrome(s)))
  print()
  for n in [7, 8, 17, 1000, 1024, 2500, 1000000, 1000000000]:
    print("binLog(%d) = %d" % (n, bin_log(n)))

