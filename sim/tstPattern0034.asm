abc:  LUI x3,_abc2
abc1: 
   AUIPC x3,_abc2
   LUI x2,@labelhere
_abc2:
   AUIPC x3,@labelhere
   LUI x3,_abc2
@labelhere:	
   LUI x3,_abc2
   LUI x3,_abc2
   
