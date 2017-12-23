# Generate bits which having certain CRC32 with Z3
#
# Use: 
#    python crc32.py 
# 
from z3 import *
import sys

# The polynomial "magic number" used for computing CRC32
polynomial = 0xEDB88320

def crc32(data, size, prev=0):
    crc = prev ^ 0xFFFFFFFF
    for i in range(0, size, 8):
        crc = crc ^ (LShR(data, i) & 0xFF)
        for _ in range(8):
            crc = If(crc & 1 == BitVecVal(1, size), LShR(crc,1) ^ polinomial, LShR(crc,1))
    return crc ^ 0xFFFFFFFF

if len(sys.argv) < 3:
    print("Usage: crc32.py target_crc input_length_in_bytes")
else:
    solver = Solver()

    print("Target: {}".format(sys.argv[1]))
    print("Length: {}".format(sys.argv[2]))
    size = int(sys.argv[2])
    target = int(sys.argv[1], 16)

    data = BitVec('data', size)
    solver.add(crc32(data, size) == target)
    if s.check() == sat:
        print(hex(int(str(s.model()[data]))))
    else:
        print("UNSAT")