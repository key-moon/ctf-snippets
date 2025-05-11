# HEADER
# name: Template for pwntools Interactive(pwnable)
# prefix: interactive-pwn-pwntools
# description: Template for pwntools Interactive(pwnable)
# author: keymoon
# template: true

# VARIABLES
# bin_name: ./binname
# nc_host: hogenet
# nc_port: 3141592

# BODY
from pwn import *

BIN_NAME = "bin_name"
REMOTE_LIBC_PATH = "./lib/libc.so.6"
LOCAL = "REMOTE" not in args

chall = ELF(BIN_NAME)

if LOCAL: stream = process(BIN_NAME)
else: stream = remote("nc_host", nc_port)

#cursor
# chall.base = ???_addr - chall.symbol("???")

libc = ELF(REMOTE_LIBC_PATH)
# libc.base = ???_addr - libc.symbol("???")

stream.interactive()
