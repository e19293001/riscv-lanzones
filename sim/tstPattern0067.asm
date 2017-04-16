addi    sp,sp,-16
sw      s0,sp,12
addi    s0,sp,16
ori     a5,a5,0
add     a0,a0,a5
lw      s0,sp,12
addi    sp,sp,16

loop:
   jal t0,loop
