# HEADER
# name: Template for Blind Attack(binarysearch)
# prefix: blind-binarysearch
# description: Template for Blind Attack(BinarySearch)
# author: keymoon
# template: true

# VARIABLES

# BODY
from ctf import *

def test_nxt_char(cur: str, nxt_lower: int, nxt_upper: int):
  return False

cur = ""
while True:
  print(f"[+] {cur=}")
  valid, invalid = 0x20, 0x100 # printable
  while invalid - valid > 1:
      mid = (invalid + valid) // 2
      if test_nxt_char(cur, mid, invalid): valid = mid
      else: invalid = mid
  cur += chr(valid)
