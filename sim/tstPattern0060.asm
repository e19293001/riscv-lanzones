	LUI  tp,0xFFFFF
   ORI tp,tp,0xFFF              ;x4 = -1
   ANDI gp,gp,0x0               ;x3 = 0
	ANDI tp,tp,0x0
   ORI  tp,zero,label5
	ANDI gp,gp,0x5
   ORI  gp,gp,0x5               ;x3 = 5
	ANDI sp,sp,0x5
   ORI  sp,sp,0x3               ;x2 = 3
	BGEU  sp,gp,label4            ;branch should not be taken
	BGEU  gp,sp,label4            ;branch should be taken
	JALR ra,gp,label4
	ADDI x5,zero,label2
label1:   LUI x5,0x123
	       SH x5,zero,0x108
label2:   LHU tp,zero,0x108       ;005
label3:   LUI x5,xx2
   JAL sp,label5
label4:
   ANDI tp,tp,0x0
   ORI tp,tp,0x5
   BGEU sp,gp,label4             ;3 >= 5 --> false
   BGEU gp,tp,this1              ;5 >= 5 --> true
this2:
   LHU tp,zero,xx3
   LHU tp,zero,xx4
	SLTIU tp,zero,xx1
   LHU x5,zero,xx5
	JAL ra,label1
label5:  SH x5,zero,xx2
   LHU x6,zero,xx6
	SH x6,zero,xx3
   LHU x7,zero,xx7
	SH x7,zero,xx1
label6:  JAL ra,label6
this1:
   JAL ra,this2
xx1:   dw 0xAAAAAA
xx2:   dw 0xAAAAAB
xx3:   dw 0xAAAAAC
xx4:   dw 0xAAAAAD
xx5:   dw 0xAAAAAE
xx6:   dw 0xAAAAAF
xx7:   dw 0xAAAABB
