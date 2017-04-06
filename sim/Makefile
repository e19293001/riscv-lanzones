# vpi
IVERILOG_LIB_PATH=$(IVERILOG_LIB_PATH_)
IVERILOG_INCLUDE_PATH=$(IVERILOG_INCLUDE_PATH_)
COPTS=-g -Wall -I$(IVERILOG_INCLUDE_PATH) -L$(IVERILOG_LIB_PATH) -I../vpi/

TESTFILE=tstPattern0062.asm

all: asm comp run

asm: $(TESTFILE)
	python2 ../bin/asmblr.py $(TESTFILE)

comp:
	iverilog -f files -o lanzones

run:
	vvp lanzones

clean:
	rm -fr lanzones sim.vcd
	rm -fr *.vvp *.o *.vpi

vpi: bst.o
	gcc -c -fpic ../vpi/vpi_dynmem.c -o vpi_dynmem.o $(COPTS)
	gcc -shared -o vpi_dynmem.vpi vpi_dynmem.o bst.o -lvpi $(COPTS)
	iverilog -o tstvpiassoc.vvp tstvpiassoc.v
	vvp -M. -m vpi_dynmem tstvpiassoc.vvp

vpi2:
	iverilog-vpi ../vpi/vpi_dynmem.c ../vpi/bst.c -I../vpi/

vpi3: bst.o vpi_dynmem.o
	iverilog-vpi vpi_dynmem.o bst.o

vpi4: vpi3
	iverilog -f files -o lanzones
	vvp -M. -m vvp_dynmem lanzones

vpi5: output.txt bst.o vpi_dynmem.o vpi_dynmem.vpi #working
	iverilog -f files -o lanzones.vvp
	vvp -M. -m vpi_dynmem lanzones.vvp

output.txt:
	python2 ../bin/asmblr.py $(TESTFILE)

bst.o: ../vpi/bst.c
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
