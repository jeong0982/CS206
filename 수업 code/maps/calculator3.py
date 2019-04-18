#
# Calculator, version 3
# with variables
#

import tokens

# start with no variables defined
variables = { }  

class InputError(Exception):
  def __init__(self, msg, token):
    self.msg = msg
    self.token = token

def parse_item(tok):
  t = tok[0]
  tok.pop(0)
  if t.isNumber():
    return t.value
  if t.isIdentifier():
    if t.value in variables:
      return variables[t.value]
    else:
      raise InputError("Variable '%s' undefined" % t.value, t)
  if not t.isSymbol("("):
    raise InputError("Expected number, variable, or '('", t)
  expr = parse_expression(tok)
  if not tok[0].isSymbol(")"):
    raise InputError("Expected operator or ')'")
  tok.pop(0)
  return expr

def parse_factor(tok):
  t = tok[0]
  sign = -1 if t.isSymbol("-") else +1
  if t.isSymbol("+") or sign < 0:
    tok.pop(0)
  result = parse_item(tok)
  while tok[0].isSymbol("^"):
    tok.pop(0)
    rhs = parse_factor(tok)
    result = result ** rhs
  return sign * result
  
def parse_term(tok):
  result = parse_factor(tok)
  t = tok[0]
  while t.isSymbol("*") or t.isSymbol("/"):
    tok.pop(0)
    rhs = parse_factor(tok)
    if t.isSymbol("/"):
      result = result / rhs
    else:
      result = result * rhs
    t = tok[0]
  return result

def parse_expression(tok):
  result = parse_term(tok)
  t = tok[0]
  while t.isSymbol("+") or t.isSymbol("-"):
    tok.pop(0)
    rhs = parse_term(tok)
    if t.isSymbol("+"):
      result = result + rhs
    else:
      result = result - rhs
    t = tok[0]
  return result

def parse(s):
  toks = tokens.tokenize(s)
  if (len(toks) >= 4 and toks[0].isIdentifier() and
      toks[1].isSymbol("=")):
    varname = toks[0].value
    toks.pop(0)
    toks.pop(0)    
    value = parse_expression(toks)
    if not toks[0].isStop():
      raise InputError("Expected operator or end of input", toks[0])
    variables[varname] = value
    print("%s = %g" % (varname, value))
  else:
    result = parse_expression(toks)
    if not toks[0].isStop():
      raise InputError("Expected operator or end of input", toks[0])
    print("==> %g" % result)

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Welcome to KAIST Supercalculator v0.3")
  while True:
    s = input("Enter an expression or a variable assignment: ")
    if s is None or s.strip() == "":
      break
    try:
      parse(s)
    except InputError as e:
      print("Error:", e.msg)
      print(s)
      print(" " * e.token.pos + "^")

# --------------------------------------------------------------------
