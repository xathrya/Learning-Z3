import wmi
from z3 import *

def get_HddSerial():
    c = wmi.WMI()
    hdd_serial = c.Win32_PhysicalMedia()[0].SerialNumber
    
    if len(hdd_serial) < 32:
        hdd_serial = ' ' * (32 - len(hdd_serial)) + hdd_serial
    
    return list(map(ord, hdd_serial))

def get_Hardcoded():
    return list(map(ord, "0how4zdy81jpe5xfu92kar6cgiq3lst7"))

def solve():
    #hdd_serial = get_HddSerial()
    #print(hdd_serial)

    solver = Solver()

    #hdd  = get_HddSerial()
    #code = get_Hardcoded()
    hdd  = [0xB7, 0x68, 0x83, 0x6E, 0x97, 0x20, 0xD1, 0xF2, 0xAF, 0x9E, 0x35, 0xCF, 0x1C, 0xCA, 0x96, 0x99, 0xAB, 0x05, 0xCC, 0x9A, 0xCB, 0x46, 0xBF, 0x74, 0x49, 0x38, 0x13, 0x57, 0xA4, 0xA3, 0xD5, 0x76]
    code = [0x30, 0x68, 0x6f, 0x77, 0x34, 0x7a, 0x64, 0x79, 0x38, 0x31, 0x6a, 0x70, 0x65, 0x35, 0x78, 0x66, 0x75, 0x39, 0x32, 0x6b, 0x61, 0x72, 0x36, 0x63, 0x67, 0x69, 0x71, 0x33, 0x6c, 0x73, 0x74, 0x37]
    x, y   = BitVecs('x y',32)

    # Check for constraint
    for i in range(32):
        solver.add((hdd[i] - (x & 0xFF)) ^ (y & 0xFF) == code[i])
        x = RotateLeft(x, 1)
        y = RotateLeft(y, 1)
    
    if solver.check() == sat:
        print("Yeah")
    else:
        print("No!")


if __name__ == '__main__':
    solve()