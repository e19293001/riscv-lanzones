# vpi
IVERILOG_LIB_PATH=$(IVERILOG_LIB_PATH_)
IVERILOG_INCLUDE_PATH=$(IVERILOG_INCLUDE_PATH_)
COPTS=-g -Wall -I$(IVERILOG_INCLUDE_PATH) -L$(IVERILOG_LIB_PATH)

TESTFILE=tstPattern0061.asm

all: asm comp run

asm: $(TESTFILE)
	python2 ../bin/asmblr.py $(TESTFILE)

comp:
	iverilog -f files -o lanzones

run:
	vvp lanzones

clean:
	rm -fr lanzones sim.vcd

vpi:
	gcc -c -fpic ../vpi/vpi_dynmem.c -o vpi_dynmem.o $(COPTS)
	gcc -shared -o vpi_dynmem.vpi vpi_dynmem.o -lvpi $(COPTS)
	iverilog -o tstvpiassoc.vvp tstvpiassoc.v
	vvp -M. -m vpi_dynmem tstvpiassoc.vvp
