# HEADER
# name: decrypt rsa
# prefix: decrypt-rsa
# description: Decrypt RSA from e, phi, n
# author: keymoon
# template: false

# VARIABLES
#   _c: c
#   _e: e
# _phi: phi

# BODY
pow(c, pow(e, -1, phi), n)
