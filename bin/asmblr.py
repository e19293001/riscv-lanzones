import sys
import re

def printHelp():
    print "usage: python2 ../bin/asmblr.py <asm file>"

def getReg(ireg):
    for i in range(32):
#        print "x" + str(i)
        if ireg == ("x" + str(i)):
#            print "Match:" + ireg
            return i

print "number of arguments:", len(sys.argv)

if len(sys.argv) == 1:
    printHelp()
    sys.exit()

asmfile = sys.argv[1]

print "asmfile:" + asmfile

with open(asmfile, "r") as asmhandle:
    for line in asmhandle:
        linestrp = line.strip()
        print "; " + line
        spltd = re.split(',| ',linestrp)
        opcode = ""
        rd = ""
        imm = ""

        if (spltd[0] == "LUI"):
            opcode = "0110111"
            rd = getReg(spltd[1])
            imm = spltd[2]

        print opcode, rd, imm
        
