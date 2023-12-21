import subprocess
from typing import *
# HEADER
# name: flatter
# prefix: flatter
# description: call flatter to perform lattice reduction
# author: keymoon
# template: false

# VARIABLES

# BODY
def flatter(mat: List[List[int]]):
    mat_s = "[" + "\n".join([f"[{' '.join(map(str, row))}]" for row in mat]) + "]"
    ret = subprocess.check_output(["flatter"], input=mat_s.encode())
    return [[int(elem) for elem in row.strip(b"[]").split()] for row in ret.strip(b'[]\n').split(b"\n")]
