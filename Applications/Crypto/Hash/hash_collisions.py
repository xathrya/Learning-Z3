# A simple collisions with Z3
#
# Use: 
#    python hash_collisions.py 
# 
from z3 import *

# The hash algorithm has a weak algorithm which can be decomposed as a series of operations

def H(input_bytes):
    '''This idea comes directly from awesome James Forshaw, read his blogpost:
    http://tyranidslair.blogspot.co.uk/2014/09/generating-hash-collisions.html'''
    h = 0
    for byte in input_bytes:
        h = h * 31 + ZeroExt(24, byte)
    return h

def ascii_printable(x):
    '''Adds the constraints to have an ascii printable byte'''
    return And(0x20 <= x, x <= 0x7f)

def generate_ascii_printable_string(base_name, size, solver):
    '''Generates a sequence of byte you can use as something to simulate C strings,
    and also adds to the solver the required constraints to have an ascii printable string'''
    bytes = [BitVec('%s%d' % (base_name, i), 8) for i in range(size)]
    solver.add(And(list(map(ascii_printable, bytes))))
    return bytes

def str_to_BitVecVals8(s):
    '''Generates a list of BitVecVal8 from a python string'''
    return list(map(lambda x: BitVecVal(ord(x), 8), s))

def collide(target_str, base_str):
    '''Generates a string with the following properties:
        * strcmp(res, base_str) = 0
        * H(res) == H(target_str)'''
    size_suffix = 7
    s = Solver()
    # We can even impress girls by having an ascii printable suffix :-)))
    res = str_to_BitVecVals8(base_str) + [BitVecVal(0, 8)] + generate_ascii_printable_string('res', size_suffix, s)
    s.add(H(res) == H(str_to_BitVecVals8(target_str)))
    if s.check() == sat:
        x = s.model()
        return base_str + '\x00' + ''.join(chr(x[i].as_long()) for i in res[-size_suffix:])
    raise Exception('Unsat!')

a = 'xyz'
b = 'abc'
c = collide(a, b)
print('c = %r' % c)
print('H(%r) == H(%r)' % (a, c))
print('strcmp(%r, %r) = 0' % (c, b))
