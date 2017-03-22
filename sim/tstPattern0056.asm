	ANDI x4,x4,0x0
   ORI  x4,x0,label5
	ANDI x3,x3,0x5
   ORI  x3,x3,0x5               ;x3 = 5
	ANDI x2,x2,0x5
   ORI  x2,x2,0x3               ;x2 = 3
	BLT  x3,x2,label4            ;branch should not be taken
	BLT  x3,x2,label4            ;branch should be taken
	JALR x1,x3,label4
	ADDI x5,x0,label2
label1:   LUI x5,0x123
	       SH x5,x0,0x108
label2:   LHU x4,x0,0x108       ;005
label3:   LUI x5,xx2
   JAL x2,label5
label4:
   LHU x4,x0,xx3
   LHU x4,x0,xx4
	SLTIU x4,x0,xx1
   LHU x5,x0,xx5
	JAL x1,label1
label5:  SH x5,x0,xx2
   LHU x6,x0,xx6
	SH x6,x0,xx3
   LHU x7,x0,xx7
	SH x7,x0,xx1
label6:  JAL x1,label6
xx1:   dw 0xAAAAAA
xx2:   dw 0xAAAAAB
xx3:   dw 0xAAAAAC
xx4:   dw 0xAAAAAD
xx5:   dw 0xAAAAAE
xx6:   dw 0xAAAAAF
xx7:   dw 0xAAAABB
