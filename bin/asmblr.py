import sys
import re

def instformat(s,i):
    return "{0:0{1}x}".format(int(s,2),i)

def binformat(s,i):
    return s.zfill(i)

def tobinstr(spltd):
    return str(bin(int(spltd)))[2:]

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
        rs1 = ""
        rs2 = ""

        if (spltd[0] == "LUI"):
            opcode = "0110111"
            rd = tobinstr(getReg(spltd[1]))
            if (spltd[2][0] == "0" and spltd[2][1] == "x"):
                imm = tobinstr(spltd[2][2:])
            else:
                imm = "0"
            #print imm, rd, opcode
            #print binformat(imm,12), binformat(rd,5), binformat(opcode,7)
            instruction = binformat(imm,12) + binformat(rd,5) + binformat(opcode,7)
            print instformat(instruction,8)
        elif (spltd[0] == "ADD"):
            opcode = "0110011"
            rd = tobinstr(getReg(spltd[1]))
            rs1 = tobinstr(getReg(spltd[2]))
            rs2 = tobinstr(getReg(spltd[3]))
            #instruction = binformat(rd,5) + binformat(rs1,5) + binformat(rs2,5) + binformat(opcode,7)
            instruction = "0000000" + binformat(rs2,5) + binformat(rs1,5) + "000" + binformat(rd,5) + binformat(opcode,7)
            print instruction
            #print opcode, rd, rs1, rs2
            print instformat(instruction,8)

