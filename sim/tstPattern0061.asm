	BGEU    tp,tp,0x888888888888888
   BGEU    tp,tp,biglabel
	BGE    tp,tp,0x999999999999999
   BGE    tp,tp,biglabel
	BLTU    tp,tp,0xAAAAAAAAAAAAAA
   BLTU    tp,tp,biglabel
	BLT    tp,tp,0xBBBBBBBBBBBBBB
   BLT    tp,tp,biglabel
	BNE    tp,tp,0xCCCCCCCCCCCCCC
   BNE    tp,tp,biglabel
	BEQ    tp,tp,0xDDDDDDDDDDDDDD
   BEQ    tp,tp,biglabel
	JALR    tp,tp,0xEEEEEEEEEEE
   JALR    tp,tp,biglabel
	AUIPC    tp,0xFFFFFFFFFFFF
   AUIPC    tp,biglabel
	LBU    tp,tp,0xEEEEEEEEEE
   LBU    tp,tp,biglabel
	SH    tp,tp,0xDDDDDDDDD
   SH    tp,tp,biglabel
	SB    tp,tp,0xDDDDDDDDDD
   SB    tp,tp,biglabel
	LB    tp,tp,0xCCCCCCCCCC
   LB    tp,tp,biglabel
	SLTIU tp,tp,0xBBBBBBBBBB
   SLTIU tp,tp,biglabel
	SLTI tp,tp,0xAAAAAAAAAA
   SLTI tp,tp,biglabel
	XORI tp,tp,0x9999999999
   XORI tp,tp,biglabel
	ADDI tp,tp,0x8888888888
   ADDI tp,tp,biglabel
	SRAI tp,tp,0x7777777777
   SRAI tp,tp,biglabel
	SRLI tp,tp,0x6666666666
   SRLI tp,tp,biglabel
	SLLI tp,tp,0x5555555555
   SLLI tp,tp,biglabel
	ANDI tp,tp,0x4444444444
	ANDI tp,tp,biglabel
	ORI tp,tp,0x3333333333
	ORI tp,tp,biglabel
	LH tp,tp,0x2222222222
   LH tp,tp,biglabel
	LW tp,tp,0x1111111111
   LW tp,tp,biglabel
	SW tp,tp,0x123456789
	LUI  tp,0x987654321
   LUI  tp,biglabel
	JAL  tp,0x123456789
	JAL  tp,biglabel
org 0x12345
	;; ORI  tp,zero,label5
	LUI  tp,0xFFFFF
   ORI tp,tp,0xFFF              ;x4 = -1
   ANDI gp,gp,0x0               ;x3 = 0
	ANDI tp,tp,0x0
;; org 0x3
   ;; ORI  tp,zero,label5
	ANDI gp,gp,0x5
   ORI  gp,gp,0x5               ;x3 = 5
	ANDI sp,sp,0x5
   ORI  sp,sp,0x3               ;x2 = 3
	BGEU  sp,gp,label4            ;branch should not be taken
	BGEU  gp,sp,label4            ;branch should be taken
	;; JALR ra,gp,label4
	;; ADDI x5,zero,label2
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
   ;; LHU tp,zero,xx4
	;; SLTIU tp,zero,xx1
   ;; LHU x5,zero,xx5
	;; JAL ra,label1
;; org 0x111
label5:
   SH x5,zero,xx2
   LHU x6,zero,xx6
	;; SH x6,zero,xx3
   ;; LHU x7,zero,xx7
	;; SH x7,zero,xx1
label6:  JAL ra,label6
this1:
   JAL ra,this2
org 0x12345678
biglabel:   
xx1:   dw 0xAAAAAA
xx2:   dw 0xAAAAAB
xx3:   dw 0xAAAAAC
xx4:   dw 0xAAAAAD
xx5:   dw 0xAAAAAE
xx6:   dw 0xAAAAAF
xx7:   dw 0xAAAABB
