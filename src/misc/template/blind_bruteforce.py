# HEADER
# name: Template for Blind Attack(bruteforce)
# prefix: blind-bruteforce
# description: Template for Blind Attack
# author: keymoon
# template: true

# VARIABLES

# BODY
from ctf import *

def test_prefix(cur: str):
  return False
 
alphabet = set(string.printable) - set(" ")

cur = ""
while True:
  print(f"[+] {cur=}")
  for c in tqdm(list(alphabet)):
    nxt = cur + c
    if not test_prefix(nxt): continue
    print("\n")
    cur = nxt
    break
  else:
    break

print(cur)
