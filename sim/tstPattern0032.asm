abc:  LUI x3,0xFFF
abc1: 
   LUI x3,0x3
   LUI x2,0x2
   ADD x4,x3,x2
_abc2: 
   SW x2,x0,0x108
@labelhere:
   SW x3,x0,0x107
   LW x4,x0,0x108
   LW x5,x0,0x107
