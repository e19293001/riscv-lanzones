TESTFILE=tstPattern0031.asm

all: asm comp run

asm: $(TESTFILE)
	python2 ../bin/asmblr.py $(TESTFILE)

comp:
	iverilog -f files -o lanzones

run:
	vvp lanzones

clean:
	rm -fr lanzones sim.vcd
