# HEADER
# name: Demangle ShiftXOR
# prefix: demangle-shiftxor
# author: keymoon

def demangle_shiftxor(mangle: int, shift: int):
  recovered = 0
  for i in range(0, mangle.bit_length())[::-1]:
    recovered *= 2
    recovered ^= (mangle >> i & 1) ^ (recovered >> shift & 1)
  assert (recovered ^ (recovered >> shift)) == mangle
  return recovered
