EOF = 0
UNSIGNED = 1
HEX = 2
LUI = 3
ADD = 4
SW = 5
LW = 6
ERROR = 7
COMMA = 8

class Token:
    def __init__(self):
        self.kind = EOF
        self.beginLine = 0
        self.beginColumn = 0
        self.endLine = 0
        self.endColumn = 0
        self.image = ""
    

class TokenMgr:

    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile
        self.inFileHandle = open(inFile, "r")
        self.outFileHandle = open(outFile, "w")
        self.currentChar = "\n"
        self.currentColumnNumber = 0
        self.currentLineNumber = 0
        self.inputLine = ""
        self.buff = ""
        print "started"

    def __del__(self):
        self.inFileHandle.close()
        self.outFileHandle.close()
        print "finished"

    def getNextToken(self):
        while self.currentChar.isspace():
            self.getNextChar()
            
        tkn = Token()
        tkn.beginLine = self.currentLineNumber
        tkn.beginColumn = self.currentColumnNumber
        tkn.kind = EOF

        if self.currentChar == EOF:
            tkn.image = "<EOF>"
            tkn.endLine = self.currentLineNumber
            tkn.endColumn = self.currentColumnNumber
            tkn.kind = EOF
        else:
            if self.currentChar.isdigit():
                if self.currentChar == "0":
                    self.buff = ""
                    while True:
                        self.buff = self.buff + self.currentChar
                        tkn.endLine = self.currentLineNumber
                        tkn.endColumn = self.currentColumnNumber
                        self.getNextChar()
                        if not self.currentChar.isdigit():
                            break
                        tkn.image = self.buff
                        tkn.kind = HEX
            elif self.currentChar.isalnum():
                self.buff = ""
                while True:
                    self.buff = self.buff + self.currentChar
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    #if not (self.currentChar.isalnum() and self.currentChar == "x"):
                    if self.currentChar.isalnum():
                        break
                tkn.image = self.buff
                if tkn.image == "LUI":
                    tkn.kind = LUI
                elif tkn.image == "ADD":
                    tkn.kind = ADD
                elif tkn.image == "SW":
                    tkn.kind = SW
                elif tkn.image == "LW":
                    tkn.kind = LW
                else:
                    tkn.kind = ERROR
            elif self.currentChar == ",":
                tkn.endLine = self.currentLineNumber
                tkn.endColumn = self.currentColumnNumber
                self.getNextChar()
                tkn.image = self.currentChar
                tkn.kind = COMMA
            else:
                tkn.kind = ERROR
        return tkn

    def getNextChar(self):
        if self.currentChar == EOF:
            print "reached EOF"
            return

        if self.currentChar == "\n":
            self.inputLine = self.inFileHandle.readline()
            if self.inputLine:
                print "inputLine:" + self.inputLine
                self.currentColumnNumber = 0
                self.currentLineNumber = self.currentLineNumber + 1
            else:
                self.currentChar = EOF
                return

        self.currentChar = self.inputLine[self.currentColumnNumber]
        self.currentColumnNumber = self.currentColumnNumber + 1
        #print "currentChar:" + self.currentChar
        

tmgr = TokenMgr("tstPattern0003.asm", "outfile.txt")
tmgr.getNextChar()

for i in range(10):
    tkn = tmgr.getNextToken()
    print "Token.image:" + tkn.image
    print "Token.kind:" + str(tkn.kind)

#import sys
#import re
#
#def instformat(s,i):
#    return "{0:0{1}x}".format(int(s,2),i)
#
#def binformat(s,i):
#    return s.zfill(i)
#
#def tobinstr(spltd):
#    return str(bin(int(spltd)))[2:]
#
#def printHelp():
#    print "usage: python2 ../bin/asmblr.py <asm file>"
#
#def getReg(ireg):
#    for i in range(32):
##        print "x" + str(i)
#        if ireg == ("x" + str(i)):
##            print "Match:" + ireg
#            return i
#
#print "number of arguments:", len(sys.argv)
#
#if len(sys.argv) == 1:
#    printHelp()
#    sys.exit()
#
#asmfile = sys.argv[1]
#
#print "asmfile:" + asmfile
#
#with open(asmfile, "r") as asmhandle:
#    for line in asmhandle:
#        linestrp = line.strip()
#        print "; " + line
#        spltd = re.split(',| ',linestrp)
#        opcode = ""
#        rd = ""
#        imm = ""
#        rs1 = ""
#        rs2 = ""
#
#        if (spltd[0] == "LUI"):
#            opcode = "0110111"
#            rd = tobinstr(getReg(spltd[1]))
#            if (spltd[2][0] == "0" and spltd[2][1] == "x"):
#                imm = tobinstr(spltd[2][2:])
#            else:
#                imm = "0"
#            #print imm, rd, opcode
#            #print binformat(imm,12), binformat(rd,5), binformat(opcode,7)
#            instruction = binformat(imm,12) + binformat(rd,5) + binformat(opcode,7)
#            print instformat(instruction,8)
#        elif (spltd[0] == "ADD"):
#            opcode = "0110011"
#            rd = tobinstr(getReg(spltd[1]))
#            rs1 = tobinstr(getReg(spltd[2]))
#            rs2 = tobinstr(getReg(spltd[3]))
#            #instruction = binformat(rd,5) + binformat(rs1,5) + binformat(rs2,5) + binformat(opcode,7)
#            instruction = "0000000" + binformat(rs2,5) + binformat(rs1,5) + "000" + binformat(rd,5) + binformat(opcode,7)
#            print instruction
#            #print opcode, rd, rs1, rs2
#            print instformat(instruction,8)

