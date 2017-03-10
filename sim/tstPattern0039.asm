label1:   LUI x5,0x123
	       SW x5,x0,0x108
label2:   LW x4,x0,0x108       ;005
label3:   LUI x5,xx2
label4:   LW x4,x0,xx3
   LW x4,x0,xx4
   LW x5,x0,xx5
   LW x6,x0,xx6
   LW x7,x0,xx7
xx1:   dw 0xAA
xx2:   dw 0xAB
xx3:   dw 0xAC
xx4:   dw 0xAD
xx5:   dw 0xAE
xx6:   dw 0xAF
xx7:   dw 0xBB

