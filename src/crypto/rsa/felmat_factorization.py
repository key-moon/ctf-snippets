# HEADER
# name: Felmat factorization method
# prefix: felmat-factorization
# description: felmat factorization method
# author: keymoon

# BODY
def felmat_factor(N):
  a = ceil(sqrt(N))
  while not is_square(a^2 - N):
    a = a + 1
  b = sqrt(a^2 - N)
  return a - b
