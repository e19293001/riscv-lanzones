LUI x3,0x32
LUI x2,0x23
ADD x4,x3,x2
ADD x5,x4,x2
SW x2,x0,0x108
SW x3,x0,0x107
SW x4,x0,0x105
SW x5,x0,0x106
LW x4,x0,0x108
LW x5,x0,0x107
SW x4,x0,0x105
SW x5,x0,0x106
LUI x3,0x1
SW x5,x3,0x108
