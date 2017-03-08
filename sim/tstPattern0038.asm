label1:   LUI x5,0x123
          SW x5,x0,0x108
label2:   LW x4,x0,label4       ;005
label3:   LUI x5,0x123
          SW x5,x0,0x108
label4:   LW x4,x0,label3
   LW x4,x0,label1
   LW x5,x0,label2
   LW x6,x0,label3
   LW x7,x0,label4
xx1: dw 0x5
yy1: dw 0x5
