# HEADER
# name: Template for Interactive(pwnable)
# prefix: interactive-pwn
# description: Template for Interactive(pwnable)
# author: keymoon
# template: true

# VARIABLES
# bin_name: ./binname
# nc_string: nc hogenet 3141592

# BODY
from ctf import *

BIN_NAME = "bin_name"
REMOTE_LIBC_PATH = "./lib/libc.so.6"
LOCAL = not (("REMOTE" in os.environ) or ("REMOTE" in sys.argv))

chall = ELF(BIN_NAME)

if LOCAL: stream = process(BIN_NAME)
else: stream = remote("nc_string")

#cursor
# chall.base = ???_addr - chall.symbol("???")

libc = ELF(REMOTE_LIBC_PATH)
# libc.base = ???_addr - libc.symbol("???")

stream.interactive()
