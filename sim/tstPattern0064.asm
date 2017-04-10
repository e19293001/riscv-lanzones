lh a5,a5,0x13
lh a5,a5,-16   
lh a5,a5,16
lh a5,a5,016   
lw a5,a5,0x13
lw a5,a5,-16   
lw a5,a5,16
lw a5,a5,016   
addi    sp,sp,0x13
addi    sp,sp,-16
addi    sp,sp,16
addi    sp,sp,016
lui a5,0x13	
lui a5,-16
lui a5,16
lui a5,016
   
	
;sw      ra,12(sp)
;sw      s0,8(sp)
;addi    s0,sp,16
;auipc   t1,0x0
;jalr    t1
;lui     a5,0x0
;lw      a5,0(a5) # 0 <fa>
;mv      a1,a5
;lui     a5,0x0
;mv      a0,a5
;auipc   t1,0x0
;jalr    t1
;lui     a5,0x0
;lw      a5,0(a5) # 0 <fa>
;mv      a1,a5
;lui     a5,0x0
;mv      a0,a5
;auipc   t1,0x0
;jalr    t1
;li      a5,0
;mv      a0,a5
;lw      ra,12(sp)
;lw      s0,8(sp)
;addi    sp,sp,16
;ret   
