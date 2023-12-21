# HEADER
# name: Coppersmith's Attack
# prefix: coppersmith
# description: ある整数 N と次数 d のモニック多項式 f∈ Z[x] に対し、f(x) ≡ 0 (mod N) を満たすすべての |x| < N^{1/d-ε} を求める
# author: keymoon
# template: false

# VARIABLES
# _N: 
# _f: x
# _bits: 512

# BODY
PR.<x> = PolynomialRing(Zmod(_N))
f = _f
f = f.monic()

x_cand = f.small_roots(X=2**_bits, beta=1)
