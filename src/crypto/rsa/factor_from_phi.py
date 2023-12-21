import math
# HEADER
# name: Factor from phi
# prefix: factor-from-phi
# description: Factor $N$ if $\phi$ is known
# author: keymoon

# BODY
def factor_from_phi(phi, N):
  b = N - phi + 1
  d = b * b - 4 * N
  sqrtd = math.isqrt(d)
  if sqrtd * sqrtd != d:
    return None
  p = (b + sqrtd) // 2
  assert N % p == 0
  return p
