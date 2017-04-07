      JAL tp,main

fa:
      LW tp,tp,x
fb:
	   XORI tp,tp,0x0
      ORI tp,tp,0x5
main:
      JAL tp,fb
finish:
      JAL tp,finish
x: dw 0x0
y: dw 0x3
