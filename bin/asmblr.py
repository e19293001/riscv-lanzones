import sys
import re

EOF = 0
UNSIGNED = 1
HEX = 2
LUI = 3
ADD = 4
SW = 5
LW = 6
ERROR = 7
COMMA = 8
REGISTER = 9
LH = 10
SUB = 11
SLL = 12
ORI = 13
ANDI = 14
SLLI = 15
SRLI = 16

class Token:
    def __init__(self):
        self.kind = EOF
        self.beginLine = 0
        self.beginColumn = 0
        self.endLine = 0
        self.endColumn = 0
        self.image = ""

        self.tokenImage = ["EOF",
                           "UNSIGNED",
                           "HEX",
                           "LUI",
                           "ADD",
                           "SW",
                           "LW",
                           "ERROR",
                           "COMMA",
                           "REGISTER",
                           "LH",
                           "SUB",
                           "SLL",
                           "ORI",
                           "ANDI",
                           "SLLI",
                           "SRLI"]
          
    def getKind(self,k):
        if (k == 0):
            return "EOF"
        elif (k == 1):
            return "UNSIGNED"
        elif (k == 2):
            return "HEX"
        elif (k == 3):
            return "LUI"
        elif (k == 4):
            return "ADD"
        elif (k == 5):
            return "SW"
        elif (k == 6):
            return "LW"
        elif (k == 7):
            return "ERROR"
        elif (k == 8):
            return "COMMA"
        elif (k == 9):
            return "REGISTER"
        elif (k == 10):
            return "LH"
        elif (k == 11):
            return "SUB"
        elif (k == 12):
            return "SLL"
        elif (k == 13):
            return "ORI"
        elif (k == 14):
            return "ANDI"
        elif (k == 15):
            return "SLLI"
        elif (k == 16):
            return "SRLI"
        else:
            return "UNKNOWN"
    

class CodeGenerator:
    def __init__(self, outFile):
        self.outFile = outFile
        #print "[ start ] CodeGenerator"

    def emitInstruction(self, cnt, op):
        self.outFile.write("+" + "{0:0{1}X}".format(cnt,8) + " " + op + "\n")
        print "+" + "{0:0{1}X}".format(cnt,8) + " " + op
        #self.outFile.write(

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
        #print "started"

    def __del__(self):
        self.inFileHandle.close()
        self.outFileHandle.close()
        #print "finished"

    def is_hex(self,s):
        print "[is_hex]=" + s
        hex_digits = set("0123456789abcdefABCDEF")
        for char in s:
            if not (char in hex_digits):
                return False
        return True

    def getNextToken(self):
        while self.currentChar.isspace():
            self.getNextChar()
            
        tkn = Token()
        tkn.beginLine = self.currentLineNumber
        tkn.beginColumn = self.currentColumnNumber

        if self.currentChar == "EOF":
            tkn.image = "<EOF>"
            tkn.endLine = self.currentLineNumber
            tkn.endColumn = self.currentColumnNumber
            tkn.kind = EOF
            return tkn
        else:
            if self.currentChar.isdigit():
                if self.currentChar == "0":
                    self.buff = ""
                    while True:
                        self.buff = self.buff + self.currentChar
                        tkn.endLine = self.currentLineNumber
                        tkn.endColumn = self.currentColumnNumber
                        self.getNextChar()
                        print "currentChar:" + currentChar
                        if not (self.is_hex(self.currentChar) or self.currentChar == "x"):
                            break
                    tkn.image = self.buff
                    tkn.kind = HEX
            elif self.currentChar.isalnum():
                self.buff = ""
                while True:
                    self.buff = self.buff + self.currentChar
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    self.getNextChar()
                    if not self.currentChar.isalnum():
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
                elif tkn.image == "LH":
                    tkn.kind = LH
                elif tkn.image == "SUB":
                    tkn.kind = SUB
                elif tkn.image == "SLL":
                    tkn.kind = SLL
                elif tkn.image == "ORI":
                    tkn.kind = ORI
                elif tkn.image == "ANDI":
                    tkn.kind = ANDI
                elif tkn.image == "SLLI":
                    tkn.kind = SLLI
                elif tkn.image == "SRLI":
                    tkn.kind = SRLI
                elif tkn.image[0] == "x" and tkn.image[1:].isdigit():
                    tkn.kind = REGISTER
                else:
                    tkn.kind = ERROR
            elif self.currentChar == ",":
                tkn.endLine = self.currentLineNumber
                tkn.endColumn = self.currentColumnNumber
                tkn.image = self.currentChar
                tkn.kind = COMMA
                self.getNextChar()
            else:
                tkn.kind = ERROR
        return tkn

    def getNextChar(self):
        if self.currentChar == "EOF":
            print "reached EOF"
            return

        if self.currentChar == "\n":
            self.inputLine = self.inFileHandle.readline()
            if self.inputLine:
                #print "inputLine:" + self.inputLine[:len(self.inputLine)-1]
                #print "; " + self.inputLine[:len(self.inputLine)-1]
                self.currentColumnNumber = 0
                self.currentLineNumber = self.currentLineNumber + 1
            else:
                self.currentChar = "EOF"
                return

        self.currentChar = self.inputLine[self.currentColumnNumber]
        self.currentColumnNumber = self.currentColumnNumber + 1
        #print "currentChar:" + self.currentChar

        if self.currentChar == ";":
            self.currentChar = "\n"

class asmblr:
    def __init__(self, infile):
        self.currentToken = Token()
        self.previousToken = Token()
        #self.tmgr = TokenMgr("tstPattern0003.asm", "outfiletstPattern0003.txt")
        #outfile = "outfile" + infile[0:len(infile)-4] + ".txt"
        outfile = "outfile.txt"
        print "input file: " + infile
        print "output file: " + outfile
        self.tmgr = TokenMgr(infile, outfile)
        self.tmgr.getNextChar()
        self.currentToken = self.tmgr.getNextToken()
        self.cg = CodeGenerator(self.tmgr.outFileHandle)
        self.programcounter = 0
        
    def instformat(self,s,i):
        return "{0:0{1}X}".format(int(s,2),i)

    def binformat(self,s,i):
        return s.zfill(i)

    def hextobinstr(self, h):
        return str(bin(int(h,16)))[2:]

    def tobinstr(self,spltd):
        return str(bin(int(spltd)))[2:]

    def advance(self):
        self.previousToken = self.currentToken
        self.currentToken = self.tmgr.getNextToken()

    def consume(self,expected):
        #print "currentToken:" + self.currentToken.image
        if (self.currentToken.kind == expected):
            self.advance()
        else:
            print "Error. Expecting" + self.currentToken.getKind(expected)

    def LWpattern(self):
        op = "0000011"
        self.consume(LW)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        immstr = self.hextobinstr(imm.image[2:])
        rs1str = self.tobinstr(rs1.image[1:])
        rdstr = self.tobinstr(rd.image[1:])

        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def LHpattern(self):
        op = "0000011"
        self.consume(LH)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        immstr = self.hextobinstr(imm.image[2:])
        rs1str = self.tobinstr(rs1.image[1:])
        rdstr = self.tobinstr(rd.image[1:])

        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SWpattern(self):
        op = "0100011"
        self.consume(SW)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        immstr = self.hextobinstr(imm.image[2:])
        immstr = self.binformat(immstr,20)
        #print "immstr[3]: " + immstr[len(immstr)-3]
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])

        #imm = {inst[31:25],inst[11:7]}
        #rs2 = inst[24:20]
        #rs1 = inst[19:15]
        #funct3 = inst[14:12]
        #opcode = inst[6:0]
        #
        #0001000 00000 00010010010000100011
        #0001000 00010 00000 010 01000 0100011
        #
        #0001 0000 0010 0000 0010 0100 0010 0011
        #   0    0    2    0    2    4    2    3

        # 0001000 01000
        # imm[5:11] 0001000
        # imm[0:4] 01000
        instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "010" + immstr[15:20] + self.binformat(op,7)

        #print "self.binformat(rs2str,5): " + self.binformat(rs2str,5) + " rs2.image[1:]: " + rs2.image[1:]
        #print "instruction: " + instruction
        
        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def LUIpattern(self):
        op = "0110111"
        self.consume(LUI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        #self.binformat(imm,12)

        print "imm.image[2:]=" + imm.image[2:]
        immstr = self.hextobinstr(imm.image[2:])
        rdstr = self.tobinstr(rd.image[1:])
        instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def ADDpattern(self):
        op = "0110011"
        self.consume(ADD)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs2 = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def SUBpattern(self):
        op = "0110011"
        self.consume(SUB)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs2 = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])
        
        instruction = "0100000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def SLLpattern(self):
        op = "0110011"
        self.consume(SLL)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs2 = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def ORIpattern(self):
        op = "0010011"
        self.consume(ORI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        immstr = self.hextobinstr(imm.image[2:])
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "110" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def ANDIpattern(self):
        op = "0010011"
        self.consume(ANDI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        immstr = self.hextobinstr(imm.image[2:])
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SLLIpattern(self):
        op = "0010011"
        self.consume(SLLI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        immstr = self.hextobinstr(imm.image[2:])
        
        instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SRLIpattern(self):
        op = "0010011"
        self.consume(SRLI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        rdstr = self.tobinstr(rd.image[1:])
        rs1str = self.tobinstr(rs1.image[1:])
        immstr = self.hextobinstr(imm.image[2:])
        
        instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def program(self):
        while self.currentToken.kind != EOF:
            if self.currentToken.kind == LUI:
                self.LUIpattern()
            elif self.currentToken.kind == ADD:
                self.ADDpattern()
            elif self.currentToken.kind == SW:
                self.SWpattern()
            elif self.currentToken.kind == LW:
                self.LWpattern()
            elif self.currentToken.kind == LH:
                self.LHpattern()
            elif self.currentToken.kind == SUB:
                self.SUBpattern()
            elif self.currentToken.kind == SLL:
                self.SLLpattern()
            elif self.currentToken.kind == ORI:
                self.ORIpattern()
            elif self.currentToken.kind == ANDI:
                self.ANDIpattern()
            elif self.currentToken.kind == SLLI:
                self.SLLIpattern()
            elif self.currentToken.kind == SRLI:
                self.SRLIpattern()
            elif self.currentToken.kind == ERROR:
                print "syntax Error"
                exit()
            else:
                print "unexpected termination"
                exit()
            self.programcounter += 1

    def parse(self):
        self.program()
        self.cg.emitInstruction(self.programcounter, "FFFFFFFF")

def printHelp():
    print "usage: python2 ../bin/asmblr.py <asm file>"

# let's start the assembler
if len(sys.argv) == 1:
    printHelp()
    sys.exit()

asmfile = sys.argv[1]

ass = asmblr(asmfile)
ass.parse()
