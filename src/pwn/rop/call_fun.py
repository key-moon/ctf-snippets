# HEADER
# name: Call Function(x64)
# prefix: rop-call-fun-x64
# description: fun(rdi, rsi, rdx, rcx, r8, r9)
# author: keymoon

# VARIABLES
# _rop: rop
# _fun_name: function
# _bin: bin
# arg1: 
# arg2: 
# arg3: 
# arg4: 
# arg5: 
# arg6: 

# BODY
_rop += p64(next(_bin.gadget("pop rdi; ret;")))
_rop += p64(arg1)
_rop += p64(next(_bin.gadget("pop rsi; ret;")))
_rop += p64(arg2)
_rop += p64(next(_bin.gadget("pop rdx; ret;")))
_rop += p64(arg3)
_rop += p64(next(_bin.gadget("pop rcx; ret;")))
_rop += p64(arg4)
_rop += p64(next(_bin.gadget("pop r8; ret;")))
_rop += p64(arg5)
_rop += p64(next(_bin.gadget("pop r9; ret;")))
_rop += p64(arg6)
_rop += p64(_bin.symbol("_fun_name"))
