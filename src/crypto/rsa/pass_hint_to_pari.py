# HEADER
# name: Pass hint to PARI/GP
# prefix: pass-hint-to-pari
# description: Pass Hint to PARI/GP
# author: keymoon
# template: false

# VARIABLES
# _p: p

# BODY
pari(f"addprimes({_p})")
