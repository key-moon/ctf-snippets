from sage.all import GF
import zlib
# HEADER
# name: SageMath implementation of CRC32
# prefix: crc32-sage-polynomial-implementation
# description: SageMath implementation of CRC32
# author: keymoon
# template: false

R = GF(2)['x']
_x = R.gen()
# or: R.<x> = GF(2)["x"]

def int_to_poly(n, x): # F.fetch_int は範囲以上の値を受け付けない
  return sum([(n >> bit & 1) * x**bit for bit in range(int(n).bit_length())])

F = GF(2**32, name='a', modulus=int_to_poly(0x01_04_C1_1D_B7, _x))
x = F.gen()

def reverse_bit(val: int, bits: int):
  return int(bin(val)[2:].zfill(bits)[::-1], 2)

def sage_crc32(data):
  data_val = reverse_bit(int.from_bytes(data, "little"), len(data) * 8)
  data_poly = int_to_poly(data_val, x)

  res = 0
  res += data_poly * x**32
  res += F.fetch_int(2**32-1) * x**(len(data)*8)
  res += F.fetch_int(2**32-1)
  return reverse_bit(res.integer_representation(), 32)

assert sage_crc32(b"Hello, world!") == zlib.crc32(b"Hello, world!")
