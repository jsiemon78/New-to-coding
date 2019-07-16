import math
def FastModular(b, k, m):
  c = b % m
  for i in range(k):
    c = c**2 % m
  return c
print(FastModular(7, 7, 11))

def dec_to_bin(x):
    return int(bin(x)[2:])

def FastModularExponentiation(b, e, m):
  exponent = []
  a = FastModular(b, int(math.log(e, 2)), m)

  d = dec_to_bin(a)
  return d


print(FastModularExponentiation(7, 128, 11))
