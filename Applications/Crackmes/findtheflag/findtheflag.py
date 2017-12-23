from z3 import *

serial = [ BitVec('serial{}'.format(i), 8) for i in range(32) ]

s = Solver()

s.add(serial[31] == 0)

# 1st constraint
s.add(serial[0] + serial[22] + serial[26] + serial[20] + serial[10] + serial[7] + 3 * serial[14] + 2 * (serial[23] + serial[24] + serial[17] + serial[21] + serial[12] + serial[18]) == 2024)

# 2nd constraint 
s.add(serial[0] + serial[22] + serial[23] + serial[26] + serial[14] + serial[24] + serial[17] + serial[12] + serial[10] + serial[15] + serial[4] + serial[2] + serial[6] + serial[1] + serial[29] + serial[11] + 2 * (serial[9] + serial[19]) == 1927)

# 3rd constraint
s.add(serial[14] + serial[10] == 148)

# 4th constraint
s.add(serial[0] + serial[14] + serial[10] + serial[11] + serial[3] + serial[25] + 2 * (serial[22] + serial[27]) == 741) 

s.add(serial[24] + serial[29] == 229 )

s.add( serial[0] + serial[26] + serial[20] + serial[21] + serial[12] + serial[7] + serial[9] + serial[15] + serial[4] + serial[1] + serial[29] + serial[11] + serial[3] + serial[27] + serial[25] + serial[5] + serial[8] + serial[16] + 2 * (serial[6] + serial[19]) == 2133 )

s.add( serial[14] + serial[17] + serial[7] + serial[15] + serial[11] + serial[8] == 619 )

s.add( serial[0] + serial[22] + serial[26] + serial[21] + serial[12] + serial[7] + serial[11] + serial[16] + serial[28] + 2 * serial[23] == 996 )

s.add( serial[24] + serial[17] + serial[6] + serial[1] + serial[29] + 2 * serial[21] == 717 )

s.add( serial[24] + serial[21] + serial[12] + serial[18] + serial[6] + serial[29] + serial[11] + serial[8] + serial[16] + 3 * serial[26] + 2 * (serial[0]  + serial[17]  + serial[2]  + serial[19]  + serial[5]  + serial[28]  + serial[13]) == 2308 )

s.add( serial[20] + serial[17] + serial[21] + serial[7] + serial[9] + serial[1] + serial[19] + serial[11] + serial[27] + serial[8] + serial[28] + 3 * (serial[14] + serial[3]) + 2 * (serial[0] + serial[23] + serial[18] + serial[6]) == 2347 )

s.add( serial[0] + serial[26] + serial[20] + serial[24] + serial[10] + serial[9] + serial[6] + serial[11] + serial[25] + 2 * (serial[23] + serial[28]) == 1041 )

s.add( serial[23] + serial[6] + serial[27] == 184 )

s.add( serial[23] + serial[18] + serial[9] + serial[19] + serial[11] + serial[25] + serial[5] + serial[16] + 2 * serial[1] == 1076 )

s.add( serial[0] + serial[22] + serial[26] + serial[20] + serial[24] + serial[10] + serial[7] + serial[4] + serial[2] + serial[6] + serial[19] + serial[11] == 1040 )

s.add( serial[0] + serial[22] + serial[23] + serial[14] + serial[18] + serial[10] + serial[4] + serial[6] + serial[1] + serial[19] + serial[11] + serial[8] + serial[16] + serial[28] + 5 * serial[21] + 3 * serial[13] + 2 * (serial[26] + serial[24]) == 2393 )

s.add( serial[0] + serial[23] + serial[26] + serial[24] + serial[9] + serial[15] + serial[29] + serial[11] + serial[25] == 901 )

s.add( serial[0] + serial[22] + serial[18] + serial[10] + serial[7] + serial[9] + serial[29] + serial[11] + serial[28] + 3 * serial[26] == 893 )

s.add( serial[18] + serial[11] + serial[3] == 308 )

s.add( serial[22] + serial[14] + serial[20] + serial[12] + serial[10] + serial[4] + serial[2] + serial[19] + serial[29] + serial[5] + serial[8] + serial[13] + 2 * serial[18] == 1350 )

s.add( serial[0] + serial[26] + serial[14] + serial[20] + serial[17] + serial[7] + serial[9] + serial[1] + serial[19] + serial[5] + serial[8] + 2 * (serial[15] + serial[29] + serial[28]) == 0x62C )

s.add( serial[14] + serial[20] + serial[24] + serial[12] + serial[18] + serial[10] + serial[15] + serial[6] + serial[29] + serial[3] + serial[25] + 3 * serial[21] + 2 * (serial[0] + serial[7] + serial[4]) == 0x81B )

s.add( serial[23] + serial[26] + serial[24] + serial[17] + serial[21] + serial[18] + serial[10] + serial[6] + serial[11] + serial[5] + serial[8] + serial[13] + 3 * serial[22] + 2 * (serial[7] + serial[9] + serial[27]) == 0x6B9 )

s.add( serial[11] + serial[28] == 141 )

s.add( serial[26] + serial[24] + serial[17] + serial[12] + serial[7] + serial[4] + serial[29] + serial[5] + serial[16] + serial[13] + 2 * (serial[22] + serial[15] + serial[25]) == 0x60E )

s.add( serial[0] + serial[22] + serial[20] + serial[17] + serial[18] + serial[15] + serial[2] + serial[1] + serial[19] + serial[27] + serial[5] + serial[16] + serial[13] + 2 * (serial[14]  + serial[24]  + serial[10]  + serial[7]  + serial[6]  + serial[11]  + serial[25]) == 0x9B4 )

s.add( serial[22] + serial[17] + serial[10] + serial[5] + serial[16] + 2 * (serial[20] + serial[24]) == 0x324 )

s.add( serial[7] + serial[4] + serial[2] + serial[27] + serial[25] + serial[5] + serial[8] + serial[16] + serial[13] + 3 * (serial[22] + serial[24] + serial[9]) + 2 * (serial[0] + serial[1] + serial[28] + 2 * serial[10]) == 0x941 )

s.add( serial[23] + serial[17] + serial[12] + serial[27] + serial[16] + 2 * serial[9] == 0x2C0 )

s.add( serial[0] + serial[26] + serial[24] + serial[10] + serial[7] + serial[4] + serial[6] + serial[1] + serial[29] + serial[11] + serial[3] + serial[27] + serial[5] + serial[8] + serial[13] + 3 * serial[20] + 2 * (serial[22] + serial[14] + serial[15]) == 0x83E )

s.add( serial[26] + serial[14] + serial[21] + serial[18] + serial[9] + serial[15] + serial[2] + serial[29] + serial[3] + serial[5] == 968 )

s.add( serial[24] + serial[12] + serial[4] + serial[1] + serial[19] + serial[3] + serial[16] + 2 * (serial[26] + serial[21] + serial[6] + serial[5]) == 1356 )

s.add( serial[0] + serial[22] + serial[21] + serial[9] + serial[15] + serial[29] + serial[3] + serial[5] + 3 * serial[23] + 2 * (serial[12] + serial[7] + serial[19] + serial[27]) == 0x74D )

s.add( serial[26] + serial[14] + serial[18] + serial[7] + serial[9] + serial[2] + serial[1] + serial[3] + serial[5] + serial[8] + serial[28] + 2 * (serial[0]  + serial[20]  + serial[17]  + serial[21]  + serial[15]  + serial[6]  + serial[19]  + serial[25]  + serial[13]) == 2769 )

s.add( serial[22] + serial[23] + serial[10] + serial[15] + serial[19] + serial[11] + serial[8] + serial[28] + 2 * (serial[0]  + serial[24]  + serial[1]  + serial[3]  + serial[27]  + 2 * (serial[26] + serial[7])) == 2147 )

s.add( serial[23] + serial[14] + serial[20] + serial[24] + serial[17] + serial[19] + serial[11] + serial[3] + serial[25] + serial[13] + 2 * (serial[0]  + serial[21]  + serial[9]  + serial[2]  + serial[6]  + serial[1]  + serial[16]) == 2450 )

s.add( serial[0] + serial[26] + serial[24] + serial[17] + serial[21] + serial[18] + serial[10] + serial[9] + serial[19] + serial[27] + serial[25] + 3 * (serial[11] + serial[13]) + 2 * (serial[12] + serial[28] + 2 * (serial[1] + serial[3])) == 2755 )

s.add( serial[0] + serial[23] + serial[26] + serial[20] + serial[21] + serial[12] + serial[7] + serial[9] + serial[2] + serial[1] + serial[11] + serial[5] + serial[16] + 3 * (serial[6] + serial[25]) + 2 * (serial[24] + serial[18] + serial[10] + serial[15] + serial[28]) == 2561 )

s.add( serial[21] + serial[4] + serial[19] + serial[5] + 2 * serial[14] == 642 )

s.add( serial[20] + serial[24] + serial[17] + serial[4] + serial[27] + serial[25] + serial[8] + serial[16] + 3 * serial[19] + 2 * (serial[26] + serial[14] + serial[7] + serial[13] + 2 * serial[29]) == 0x920 )

s.add( serial[20] + serial[24] + serial[12] + serial[18] + serial[10] + 3 * serial[3] + 2 * (serial[17]  + serial[21]  + serial[9]  + serial[15]  + serial[2]  + serial[1]  + serial[19]  + serial[29]  + serial[11]  + serial[8]) == 2925 )

s.add( serial[23] + serial[20] + serial[24] + serial[10] + serial[15] + serial[6] + serial[19] + serial[29] + serial[3] + serial[8] + serial[16] + serial[28] + 3 * serial[7] + 2 * (serial[14]  + serial[17]  + serial[12]  + serial[9]  + serial[1]  + serial[25]  + serial[13]) == 2956 )

s.add( serial[22] + serial[26] + serial[24] + serial[7] + serial[15] + serial[2] + serial[11] + serial[3] + serial[25] + serial[5] + serial[13] + 2 * (serial[20] + serial[21] + serial[12] + serial[18] + serial[8]) == 2050 )

s.add( serial[0] + serial[9] + serial[11] + serial[25] + serial[5] + 2 * serial[22] == 628 )

s.add( serial[0] + serial[26] + serial[20] + serial[12] + serial[2] + serial[6] + serial[29] + serial[11] + serial[3] + serial[25] + serial[5] + serial[16] + 2 * (serial[22] + serial[9] + serial[19] + 2 * serial[28]) == 1842 )

s.add( serial[24] + serial[10] + serial[9] + serial[11] + serial[16] == 491 )

s.add( serial[22] + serial[23] + serial[24] + serial[17] + serial[12] + serial[6] + serial[29] + serial[27] + serial[5] + serial[16] + serial[28] + 3 * serial[4] + 2 * (serial[21]  + serial[15]  + serial[2]  + serial[1]  + serial[3]  + serial[25]) == 2557 )

s.add( serial[26] + serial[7] + serial[27] + 3 * serial[2] == 474 )

s.add( serial[23] + serial[14] + serial[21] + serial[12] + serial[7] + serial[15] + serial[2] + serial[11] + serial[3] + serial[8] + 2 * (serial[18] + serial[6] + serial[27] + serial[28]) == 1472 )

s.add( serial[17] + serial[7] + serial[2] + serial[25] + serial[5] + serial[13] + 3 * serial[28] == 723 )

s.add( serial[0] + serial[22] + serial[23] + serial[14] + serial[24] + serial[21] + serial[12] + serial[10] + serial[7] + serial[15] + serial[19] + serial[29] + serial[3] + serial[16] + 3 * (serial[6] + serial[1]) + 2 * (serial[18] + serial[25]) == 2304 )

s.add( serial[20] + serial[24] + serial[17] + serial[21] + serial[10] + serial[15] + serial[2] + serial[6] + serial[1] + serial[19] + serial[3] + serial[25] + serial[8] + serial[28] + 3 * serial[12] + 2 * (serial[22] + serial[26] + serial[18] + serial[4]) == 2234 )

s.add( serial[22] + serial[12] + serial[10] + serial[4] + serial[29] == 463 )

s.add( serial[21] + serial[18] == 211 )

s.add( serial[0] + serial[22] + serial[23] + serial[21] + serial[18] + serial[7] + serial[4] + serial[11] + serial[8] + serial[28] + serial[13] + 3 * serial[12] + 2 * (serial[26] + serial[9] + serial[29] + serial[27]) == 2008 )

s.add( serial[20] + serial[12] + serial[18] + serial[15] + serial[29] + serial[5] + serial[28] + 3 * serial[10] + 2 * (serial[14] + serial[25]) == 1228 )

s.add( serial[0] + serial[24] + serial[21] + serial[9] + serial[4] + serial[2] + serial[1] + serial[11] + serial[3] + serial[5] + serial[8] + serial[28] == 1191 )

s.add( serial[0] + serial[14] + serial[20] + serial[24] + serial[15] + serial[4] + serial[1] + serial[5] + serial[16] + 3 * serial[29] + 2 * (serial[2] + serial[8]) == 1691 )

s.add( serial[0] + serial[23] + serial[14] + serial[17] + serial[12] + serial[10] + serial[9] + serial[15] + serial[19] + serial[3] + 2 * (serial[21]  + serial[7]  + serial[1]  + serial[27]  + serial[8]  + 2 * serial[26]) == 2070 )

s.add( serial[0] + serial[17] + serial[18] + serial[10] + serial[2] + serial[19] + serial[11] + serial[28] + 3 * (serial[14] + serial[20] + serial[1]) + 2 * (serial[26] + serial[7]                      + serial[4]                      + serial[3]                      + serial[25]                      + serial[5]) == 2776 )

s.add( serial[20] + serial[10] + serial[2] + serial[1] + serial[19] + serial[11] + serial[3] + serial[27] + serial[16] + serial[28] + 3 * (serial[14] + serial[12]) + 2 * (serial[0] + serial[24] + serial[4]) == 2169 )

s.add( serial[22] + serial[7] + serial[29] + serial[11] + serial[27] + serial[16] + serial[28] + serial[13] + 2 * (serial[23] + serial[6] + serial[25] + serial[5]) == 1394 )

s.add( serial[0] + serial[22] + serial[14] + serial[24] + serial[21] + serial[18] + serial[4] + serial[6] + serial[29] + serial[3] + 3 * serial[2] + 2 * (serial[17] + 2 * serial[25]) == 1928 )

s.add( serial[0] + serial[23] + serial[24] + serial[25] + serial[5] == 514 )

s.add( serial[26] + serial[17] + serial[21] + serial[19] + serial[25] + serial[16] + serial[13] == 700 )

s.add( serial[0] + serial[26] + serial[14] + serial[17] + serial[18] + serial[15] + serial[2] + serial[19] + serial[27] + serial[25] + serial[13] + 2 * serial[20] == 1184 )

s.add( serial[0] + serial[23] + serial[20] + serial[24] + serial[12] + serial[15] + serial[4] + serial[29] + serial[3] + serial[5] + 2 * serial[11] == 1273 )

s.add( serial[0] + serial[26] + serial[14] + serial[21] + serial[12] + serial[4] + serial[6] + serial[1] + serial[19] + serial[29] + serial[5] + serial[16] == 1192 )

s.add( serial[22] + serial[21] + serial[12] + serial[15] + serial[11] + serial[8] + serial[28] + serial[13] + 2 * serial[14] == 913 )

s.add( serial[24] + serial[18] + serial[10] + serial[25] + 2 * serial[20] == 555 )

s.add( serial[26] + serial[1] + serial[16] == 257 )

s.add( serial[12] + serial[18] + serial[7] + serial[9] + serial[15] + serial[4] + serial[3] + serial[13] + 2 * (serial[22] + serial[14] + serial[10] + serial[19] + serial[27]) == 1561 )

s.add( serial[20] + serial[17] + serial[18] + serial[6] + serial[1] + serial[19] + serial[29] + serial[3] + serial[13] + 2 * serial[11] == 1113 )

s.add( serial[20] + serial[24] + serial[10] + serial[15] + serial[6] + serial[13] + 2 * serial[22] == 589 )

s.add( serial[23] + serial[26] + serial[14] + serial[17] + serial[21] + serial[18] + serial[10] + serial[3] + serial[25] + 3 * (serial[4] + serial[19] + serial[27]) + 2 * (serial[22] + serial[15] + serial[11]) == 2138 )

s.add( serial[15] + serial[2] + serial[8] == 287 )

s.add( serial[15] + serial[4] + serial[27] + serial[8] + serial[28] + 3 * serial[6] + 2 * serial[23] == 729 )

s.add( serial[0] + serial[2] == 199 )

s.add( serial[0] + serial[23] + serial[17] + serial[10] + serial[6] + serial[19] + serial[3] + serial[25] + serial[8] + 3 * (serial[21] + serial[1] + serial[11]) + 2 * (serial[22] + serial[14] + serial[12] + serial[29] + serial[5]) == 2787 )

s.add( serial[21] + serial[10] + serial[7] + serial[9] + serial[4] + serial[19] + serial[11] + serial[3] + serial[28] + 2 * serial[2] == 1071 )

s.add( serial[14] + serial[20] + serial[18] + serial[15] + serial[6] + serial[11] + serial[3] + serial[25] + serial[8] + serial[13] == 958 )

s.add( serial[10] + serial[4] + serial[16] + 2 * serial[8] == 477 )

s.add( serial[0] + serial[17] + serial[9] + serial[15] + serial[4] + serial[3] + serial[27] + serial[8] + 3 * serial[28] + 2 * (serial[14]  + serial[20]  + serial[7]  + serial[2]  + serial[6]  + serial[16]) == 2015 )

s.add( serial[0] + serial[22] + serial[26] + serial[14] + serial[20] + serial[10] + serial[7] + serial[15] + serial[1] + serial[27] + serial[28] + 2 * (serial[21] + serial[18] + serial[2] + serial[29]) == 1679 )

s.add( serial[0] + serial[22] + serial[20] + serial[24] + serial[7] + serial[15] + serial[19] + serial[11] + serial[3] + serial[27] + serial[5] + serial[16] + serial[13] + 3 * serial[14] + 2 * (serial[12] + serial[10] + serial[4] + serial[25] + serial[28]) == 2404 )

s.add( serial[12] + serial[18] + serial[1] + serial[29] + serial[8] + serial[28] + 3 * serial[13] + 2 * (serial[0]  + serial[21]  + serial[10]  + serial[15]  + serial[4]  + serial[6]  + serial[19]  + serial[11]  + serial[27]) == 2453 )

s.add( serial[0] + serial[26] + serial[14] + serial[20] + serial[7] + serial[9] + serial[1] + serial[29] + serial[11] + serial[27] + serial[5] + serial[16] + serial[13] + 2 * (serial[17] + serial[3] + serial[28]) == 1722 )

s.add( serial[12] + serial[18] + serial[7] + serial[15] + serial[4] + serial[2] + serial[6] + serial[1] + 3 * (serial[5] + serial[13]) + 2 * (serial[22]  + serial[26]  + serial[10]  + serial[3]  + serial[27]  + serial[28]) == 1971 )

s.add( serial[11] + serial[28] == 141 )

s.add( serial[22] + serial[14] + serial[17] + serial[10] + serial[1] + serial[27] + 3 * (serial[20] + serial[7]) + 2 * (serial[18] + serial[4] + serial[19] + serial[25] + serial[13]) == 2184 )

s.add( serial[24] + serial[17] + serial[21] + serial[10] + serial[7] + serial[2] + serial[29] + serial[11] + serial[3] + serial[25] + serial[16] + 3 * (serial[22] + serial[14]) + 2 * (serial[0]  + serial[18]  + serial[15]  + serial[1]  + serial[19]  + serial[8]) == 2825 )

s.add( serial[17] + serial[9] + serial[2] + serial[3] + serial[5] == 508 )

s.add( serial[0] + serial[14] + serial[24] + serial[21] + serial[12] + serial[9] + serial[1] + serial[19] + serial[29] + serial[28] + 3 * (serial[18] + serial[13]) + 2 * serial[16] == 1861 )

s.add( serial[20] + serial[15] + serial[29] + serial[11] + serial[27] + serial[16] + serial[13] == 673 )

s.add( serial[23] + serial[24] + serial[17] + serial[21] + serial[18] + serial[9] + serial[15] + serial[4] + serial[19] + serial[3] + serial[16] + 3 * serial[29] + 2 * (serial[11] + serial[27] + serial[28] + 2 * serial[5]) == 2269 )

s.add( serial[22] + serial[6] + serial[25] + serial[8] == 308 )

s.add( serial[24] + serial[12] + serial[7] + serial[15] + serial[6] + serial[5] + serial[8] + serial[16] + 2 * serial[9] == 1012 )

s.add( serial[14] + serial[16] == 216 )

s.add( serial[0] + serial[24] + serial[17] + serial[21] + serial[12] + serial[7] + serial[9] + serial[6] + serial[1] + serial[27] + serial[16] + serial[13] + 3 * serial[8] + 2 * (serial[26] + serial[14] + serial[4] + serial[2] + serial[28]) == 2237 )

s.add( serial[23] + serial[20] + serial[15] + serial[4] + serial[6] + serial[1] + serial[27] + 3 * serial[10] + 2 * serial[12] == 985 )

if s.check() == sat:
    model = s.model()
    print("Key is {}".format( "".join([ chr(model[serial[i]].as_long()) for i in range(30) ])))
else:
    print("Unsatisfied!")