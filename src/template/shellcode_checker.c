// HEADER
// name: Template for Running Shellcode(pwnable)
// prefix: shellcode-checker
// description: Run shellcode(pwnable)
// author: keymoon
// template: true

// VARIABLES
// _shellcode: 

// BODY
// gcc -fno-stack-protector -z execstack shellcode.c -o shellcode
int main() {
  unsigned char shellcode[] = {_shellcode};
  int (*ret)() = (int(*)())shellcode;
  ret();
}
