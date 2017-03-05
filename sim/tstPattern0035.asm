	LUI x3,0xABCDE
   ORI x3,x3,0xFDE
   SW x3,x0,0x108
   LW x4,x0,0x108
@labelhere:   LB x5,x0,@labelhere
   LB x6,x0,abc1
   LB x7,x0,_abc2
abc:  LUI x3,_abc2
abc1: 
   AUIPC x3,_abc2
   LUI x2,@labelhere
_abc2:
   AUIPC x3,@labelhere
   LUI x3,_abc2	
   LUI x3,_abc2
   LUI x3,_abc2
   
