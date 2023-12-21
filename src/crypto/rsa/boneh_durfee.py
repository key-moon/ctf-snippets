# HEADER
# name: Boneh-Durfee Attack
# prefix: boneh-durfee
# description: find $\phi$ if $d$ satisfies $d<N^{0.292}$ 
# author: keymoon

# BODY
def boneh_durfee(e, N, max_ppq=None):
  if max_ppq is None:
    max_ppq = int(N).bit_length() // 2 + 1
  P.<k, s> = PolynomialRing(Zmod(e))
  f = (N - s + 1)*k + 1

  ppq = small_roots(f, (floor(N**0.292), 2**max_ppq), m=3, d=4)[0][1]
  return N - ppq + 1
