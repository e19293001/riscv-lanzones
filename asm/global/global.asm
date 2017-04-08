ADDI    sp,sp,0x3FFFFFF0
SW      ra,sp,0xC
SW      s0,sp,0x8
ADDI    s0,sp,0xF
;; jal     ra,0x101dc <fb>
LW      a5,gp,0x3FFFF8D8
ADDI    a1,a5,0x0
LUI     a5,0x1C
ADDI    a0,a5,0x3FFFF380
;; jal     ra,0x104cc <printf>
LW      a5,gp,0x3FFFF854
ADDI      a1,a5,0x0
LUI     a5,0x1C
ADDI    a0,a5,0x3FFFFE8C
;; jal     ra,0x104cc <printf>
LUI      a5,0x0
ADDI      a0,a5,0x0
LW      ra,sp,0xC
LW      s0,sp,0x8
ADDI    sp,sp,0xF
JALR    x0,x1,0x0
