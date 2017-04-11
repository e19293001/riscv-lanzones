lbu a5,a5,0x13
lbu a5,a5,16
lbu a5,a5,016   
lbu a5,a5,-16   
	
;sh a5,a5,0x13
;sh a5,a5,16
;sh a5,a5,016   
;sh a5,a5,-16   
	
;sb a5,a5,0x13
;sb a5,a5,16
;sb a5,a5,016   
;sb a5,a5,-16   
	
;lb a5,a5,0x13
;lb a5,a5,16
;lb a5,a5,016   
;lb a5,a5,-16   
	
;sltiu a5,a5,0x13
;sltiu a5,a5,16
;sltiu a5,a5,016   
;sltiu a5,a5,-16   
	
;slti a5,a5,0x13
;slti a5,a5,16
;slti a5,a5,016   
;slti a5,a5,-16   
;xori a5,a5,0x13
;xori a5,a5,16
;xori a5,a5,016   
;xori a5,a5,-16   
;srai a5,a5,0x13
;srai a5,a5,16
;srai a5,a5,016   
;srai a5,a5,-16   
;srli a5,a5,0x13
;srli a5,a5,16
;srli a5,a5,016   
;srli a5,a5,-16   
;slli a5,a5,0x13
;slli a5,a5,16
;slli a5,a5,016   
;slli a5,a5,-16   
;andi a5,a5,0x13
;andi a5,a5,16
;andi a5,a5,016   
;andi a5,a5,-16   
;ori a5,a5,0x13
;ori a5,a5,16
;ori a5,a5,016   
;ori a5,a5,-16   
;lh a5,a5,0x13
;lh a5,a5,-16   
;lh a5,a5,16
;lh a5,a5,016   
;lw a5,a5,0x13
;lw a5,a5,-16   
;lw a5,a5,16
;lw a5,a5,016   
;addi    sp,sp,0x13
;addi    sp,sp,-16
;addi    sp,sp,16
;addi    sp,sp,016
;lui a5,0x13	
;lui a5,-16
;lui a5,16
;lui a5,016
   
	
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
