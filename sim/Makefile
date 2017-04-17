# vpi
IVERILOG_LIB_PATH=$(IVERILOG_LIB_PATH_)
IVERILOG_INCLUDE_PATH=$(IVERILOG_INCLUDE_PATH_)
COPTS=-g -Wall -I$(IVERILOG_INCLUDE_PATH) -L$(IVERILOG_LIB_PATH) -I../vpi/
#COPTS=-I$(IVERILOG_INCLUDE_PATH) -L$(IVERILOG_LIB_PATH) -I../vpi/ -Wall
#COPTS=-L/data/local/KTDP/silladore/files/build/install/lib -I/data/local/KTDP/silladore/files/build/install/include/iverilog -I../vpi/ -Wall
#COPTS=-L/data/local/KTDP/silladore/files/build/install/lib -I/data/local/KTDP/silladore/files/build/install/include/iverilog -I../vpi/ -Wall

TESTFILE=tstPattern0067.asm
#TESTFILEC=../asm/global/global.c
#TESTFILE=../asm/global/global.asm

#all: asm comp run

#all: vpi5
#all: vpi6

#all: vpi_dynmem
all: output2.txt

asm: $(TESTFILE)
	python2 ../bin/asmblr.py $(TESTFILE)

comp:
	iverilog -f files -o lanzones

run:
	vvp lanzones

clean:
	rm -fr lanzones sim.vcd
	rm -fr *.vvp *.o *.vpi

testvpi: bst.o vpi_dynmem.o
	gcc -c -fpic ../vpi/vpi_dynmem.c -o vpi_dynmem.o $(COPTS)
	gcc -shared -o vpi_dynmem.vpi vpi_dynmem.o bst.o -lvpi $(COPTS)
	iverilog -o tstvpiassoc.vvp tstvpiassoc.v
	vvp -M. -m vpi_dynmem tstvpiassoc.vvp

vpi5: output.txt bst.o vpi_dynmem.o vpi_dynmem.vpi
	iverilog -f files -o lanzones.vvp
	vvp -M. -m vpi_dynmem lanzones.vvp

vpi_dynmem: bst.o vpi_dynmem.o vpi_dynmem.vpi
	iverilog -f files -o lanzones.vvp
	vvp -M. -m vpi_dynmem lanzones.vvp

output.txt:
	python2 ../bin/asmblr.py $(TESTFILE)

output2.txt: 
#	riscv32-unknown-elf-gcc -c -S -o global.s ../asm/global/global.c
	riscv32-unknown-elf-gcc -c -o global.o ../asm/global/global.c
	riscv32-unknown-elf-objcopy -O binary global.o
#	gcc -save-temps ../asm/global/global.c
	python2 ../bin/asmblr2.py global.s

bst.o: ../vpi/bst.c ../vpi/bst.h
	gcc -c -fpic $^ -o $@ $(COPTS)

vpi_dynmem.o: ../vpi/vpi_dynmem.c
	gcc -c -fpic $^ -o $@ $(COPTS)

vpi_dynmem.vpi:
#	gcc -shared -o $@ vpi_dynmem.o bst.o $(COPTS) -lvpi 
	iverilog-vpi vpi_dynmem.o bst.o

dbgbst:
	gcc -g ../vpi/bst.c -o bst $(COPTS) -D DEBUG_BST
#	valgrind --leak-check=full -v ./bst
	./bst
