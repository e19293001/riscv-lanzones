label1:   LUI x5,0x123
	       SH x5,x0,0x108
label2:   LHU x4,x0,0x108       ;005
label3:   LUI x5,xx2
label4:   LHU x4,x0,xx3
   LHU x4,x0,xx4
	SLTI x4,x0,xx1
   LHU x5,x0,xx5
	SH x5,x0,xx2
   LHU x6,x0,xx6
	SH x6,x0,xx3
   LHU x7,x0,xx7
	SH x7,x0,xx1
xx1:   dw 0xAAAAAA
xx2:   dw 0xAAAAAB
xx3:   dw 0xAAAAAC
xx4:   dw 0xAAAAAD
xx5:   dw 0xAAAAAE
xx6:   dw 0xAAAAAF
xx7:   dw 0xAAAABB
