#
# A class representing a piecewise linear function
#
# --------------------------------------------------------------------

class PieceWiseLinear(object):
  """A piecewise linear function"""
  def __init__(self, x0, y0, x1, y1):
    if x1 <= x0:
      raise ValueError("x1 must be larger than x0")
    self.a = ((x0,y0),(x1,y1))
    self.b = None
 
  def domain(self):
    """Return domain interval as a pair."""
    return (self.a[0][0], self.a[1][0])
                           
  def __str__(self):
    st = "(%g,%g)."%(self.a[0][0],self.a[0][1])
    i=0
    if self.b!=None:
      while i<=len(self.b)-1:
        st = st + ".(%g,%g)."%(self.b[i][0],self.b[i][1])
        i+=1
    st = st + ".(%g,%g)"%(self.a[1][0],self.a[1][1])
    return st

  def __call__(self, x):
    """Evaluate this function at x-coordinate x."""
    d = self.domain()
    if x < d[0] or x > d[1]:
      raise ValueError("argument is not in domain")
    if self.b==None:
      gdt=((float)((self.a[1][1]-self.a[0][1])/(self.a[1][0]-self.a[0][0])))
      return gdt*x+self.a[0][1]-gdt*self.a[0][0]
    if x < self.b[0][0]:
      gdt=((float)((self.a[0][1]-self.b[0][1])/(self.a[0][0]-self.b[0][0])))
      return gdt*x+self.a[0][1]-gdt*self.a[0][0]
    i = 0
    last = self.a[0]
    if self.b!=None :
      while x > last[0]:
        i+=1
        if i>len(self.b)-1:
          break
        last = self.b[i]
      if i>len(self.b)-1:
          gdt=((float)((self.a[1][1]-self.b[i-1][1])/(self.a[1][0]-self.b[i-1][0])))
          return gdt*x+self.b[i-1][1]-gdt*self.b[i-1][0]
      elif i <= len(self.b)-1:
        gdt=((float)((self.b[i-1][1]-self.b[i][1])/(self.b[i-1][0]-self.b[i][0])))
        return gdt*x+self.b[i][1]-gdt*self.b[i][0]

  def join(self, rhs):
    """Join two piecewise linear functions."""
    d1= self.domain()
    d2 = rhs.domain()
    if d1[1] != d2[0]:
      raise ValueError("domains are not contiguous")
    if abs(self(d1[1]) - rhs(d2[0])) > 1e-13:
      raise ValueError("discontinuity at connection point")
    new_func = PieceWiseLinear(self.a[0][0],self.a[0][1],rhs.a[1][0],rhs.a[1][1])
    if self.b == None:
      if rhs.b==None:
        new_func.b = (self.a[1:])
        return new_func
      else:
        new_func.b = (self.a[1:]+rhs.b[:])
        return new_func
    elif rhs.b == None:
        new_func.b = (self.b[:] + self.a[1:])
        return new_func
    else:
      new_func.b = (self.b[:] + self.a[1:] + rhs.b[:])
    return new_func

  def __rmul__(self, lhs):
    """Multiplication of a number lhs with a piecewise linear function.
Returns a new function, this function remains unchanged."""
    n = PieceWiseLinear(self.a[0][0],self.a[0][1]*lhs,self.a[1][0],self.a[1][1]*lhs)
    i = 0
    if self.b==None:
      return n
    n.b = list(self.b)
    while i<=len(n.b)-1:
      n.b[i] = (n.b[i][0], n.b[i][1] *lhs)
      i+=1
    n.b = tuple(n.b)
    return n

  def add_pwlf(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is another piecewise linear function.
The domain of the result is the intersection of the two domains.
Returns a new function, this function remains unchanged."""
    x0a, x1a = self.domain()
    x0b, x1b = rhs.domain()
    x0 = max(x0a, x0b)
    x1 = min(x1a, x1b)
    if x0 >= x1:
      raise ValueError("domains do not overlap")
    if x0==x0a:
      if x1==x1a:
        y0 = self(x0) + rhs(x0)*factor
        y1 = self(x1) + rhs(x1)*factor
      else:
        y0 = self(x0) + rhs(x0)*factor
        y1 = rhs(x1)*factor + self(x1)
    else:
      y0 = rhs(x0)*factor + self(x0)
      y1 = rhs(x1)*factor + self(x1)
    n = PieceWiseLinear(x0,y0,x1,y1)
    n.b = []
    index_a = 0
    index_b = 0
    if self.b!=None:
     while self.b[index_a][0] < x0:
       index_a+=1
       if index_a > len(self.b)-1:
         break
    if rhs.b!=None:
      while rhs.b[index_b][0] < x0:
        index_b+=1
        if index_b > len(rhs.b)-1:
          break
    last = n.a[0]
    while last[0] < x1:
      if self.b ==None:
        if rhs.b==None:
          break
        else:
          if len(rhs.b)-1 < index_b:
            break
          elif self.a[1][0] > rhs.b[index_b][0]:
            n.b.append((rhs.b[index_b][0],self(rhs.b[index_b][0])+rhs.b[index_b][1]*factor))
            index_b+=1
          else:
            break
      elif rhs.b==None:
        if index_a > len(self.b)-1:
          break
        if rhs.a[1][0] > self.b[index_a][0]:
          n.b.append((self.b[index_a][0],self.b[index_a][1]+rhs(self.b[index_a][0])*factor))
          index_a+=1
        else:
          break
      elif index_a > len(self.b)-1:
        if index_b > len(rhs.b)-1:
          break
        if self.a[1][0] < rhs.b[index_b][0]:
          break
        elif self.a[1][0] > rhs.b[index_b][0]:
          n.b.append((rhs.b[index_b][0],self(rhs.b[index_b][0])+rhs.b[index_b][1]*factor))
          index_b+=1
          last = n.b[len(n.b)-1]
          continue
      elif index_b > len(rhs.b)-1:
        if rhs.a[1][0] < self.b[index_a][0]:
          break
        else:
          n.b.append((self.b[index_a][0],self.b[index_a][1]+rhs(self.b[index_a][0])*factor))
          index_a+=1
          last = n.b[len(n.b)-1]
          continue
      elif self.b[index_a][0] < rhs.b[index_b][0]:
        n.b.append((self.b[index_a][0], self.b[index_a][1] + rhs(self.b[index_a][0]) *factor))
        index_a+=1
        last = n.b[len(n.b)-1]
      elif self.b[index_a][0] > rhs.b[index_b][0]:
        n.b.append((rhs.b[index_b][0], self(rhs.b[index_b][0]) + rhs.b[index_b][1]*factor))      
        index_b+=1
        last = n.b[len(n.b)-1]
      else:
        n.b.append((rhs.b[index_b][0], self.b[index_a][1] + rhs.b[index_b][1]*factor))      
        index_b+=1
        index_a+=1
        last = n.b[len(n.b)-1]
    n.b=tuple(n.b)
    return n

  def add_number(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is a number.
This function remains unchanged."""
    n = PieceWiseLinear(self.a[0][0],self.a[0][1]+factor*rhs,self.a[1][0],self.a[1][1]+factor*rhs)
    i = 0
    if self.b==None:
      return n
    n.b = list(self.b)
    while i<=len(n.b)-1:
      n.b[i] = (n.b[i][0], n.b[i][1] +rhs*factor)
      i+=1
    n.b = tuple(n.b)
    return n

  def __add__(self, rhs):
    """Addition of a piecewise linear function with a number or 
with another piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, +1)
    else:
      return self.add_number(rhs, +1)

  def __sub__(self, rhs):
    """Subtraction of a number or of another piecewise linear function
from this piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, -1)
    else:
      return self.add_number(rhs, -1)
  
# --------------------------------------------------------------------

if __name__ == "__main__":
  f1 = PieceWiseLinear(1, -1, 3, 1)
  f2 = PieceWiseLinear(3, 1, 7, -5)
  print("f1 = %s" % f1)
  print("f2 = %s" % f2)  
  for x in [1, 2, 3]:
    print("f1(%g) = %g" % (x, f1(x)))
  for x in [3, 5, 7]:
    print("f2(%g) = %g" % (x, f2(x)))
  f = f1.join(f2)
  print("f = %s" % f)  
  for x in [1, 2, 3, 5, 7]:
    print("f(%g) = %g" % (x, f(x)))
  print("Domain of f1 = %s, domain of f2 = %s, domain of f = %s" %
        (f1.domain(), f2.domain(), f.domain()))
  g11 = f + 2
  print("g1 = f + 2 = %s" % g11)
  g2 = f - 6
  print("g2 = f - 6 = %s" % g2)
  g3 = 3 * f
  print("g3 = 3 * f = %s" % g3)
  h1 = 5 * f + 3
  h2 = 0.5 * f - 2
  print("h1 = 5 * f + 3 = %s" % h1)
  print("h2 = 0.5 * f - 2 = %s" % h2)
  g = h1 + h2
  print("g = h1 + h2 = %s" % g)
  d1 = PieceWiseLinear(0, 0, 2, 19)
  d = d1.join(PieceWiseLinear(2, 19, 6, 12))
  print("d = %s" % d)
  e1 = g + d
  e2 = g - d
  print("e1 = g + d = %s" % e1)
  print("e2 = g - d = %s" % e2)
  for x in [1, 2, 3, 4, 5, 6]:
    print("g(%g) = %g, d(%g) = %g, e1(%g) = %g, e2(%g) = %g" %
          (x, g(x), x, d(x), x, e1(x), x, e2(x)))
# --------------------------------------------------------------------
