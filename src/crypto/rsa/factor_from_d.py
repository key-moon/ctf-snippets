# HEADER
# name: Factor from d and e
# prefix: factor-from-d
# description: Factor $N$ if $d$ and $e$ is known
# author: keymoon

# BODY
def factor_from_d(d, e, N):
  k = d * e - 1
  g = 2
  while True:
    t = k
    while t % 2 == 0:
      t //= 2
      x = pow(g, t, N)
      if 1 < x and gcd(x - 1, N) != 1:
        return int(gcd(x - 1, N))
    g += 1
