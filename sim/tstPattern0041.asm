;	   LW x4,x0,xxx1
;      SB x4,x0,xxx2
;      LW x4,x0,xxx3
;      SB x4,x0,xxx4
;xxx1:   dw 0xAAAAAAAA
;xxx2:   dw 0xBBBBBBBB
;xxx3:   dw 0xCCCCCCCC
;xxx4:   dw 0xDDDDDDDD
;xxx5:   dw 0xEEEEEEEE
;xxx6:   dw 0xFFFFFFFF
;xxx7:   dw 0xABCDEFAB
	

label1:   LUI x5,0x123
	       SW x5,x0,xx1
label2:   LW x4,x0,xx2
label3:   LUI x5,xx2
label4:   LW x3,x0,xx3
   LW x4,x0,xx4
   LW x5,x0,xx5
   LW x6,x0,xx6
   LW x7,x0,xx7
   SB x5,x0,xx1
   SB x4,x0,xx2
   SB x3,x0,xx3
   SB x2,x0,xx4
   SB x1,x0,xx5
   SB x3,x0,xx6
   SB x2,x0,xx7
   dw 0xFFFFFFFF
xx1:   dw 0xAAAAAAAA
xx2:   dw 0xBBBBBBBB
xx3:   dw 0xCCCCCCCC
xx4:   dw 0xDDDDDDDD
xx5:   dw 0xEEEEEEEE
xx6:   dw 0xFFFFFFFF
xx7:   dw 0xABCDEFAB

