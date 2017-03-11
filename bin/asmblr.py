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
SRAI = 17
ADDI = 18
XORI = 19
XOR = 20
OR = 21
AND = 22
SLTI = 23
SLTIU = 24
SLT = 25
SLTU = 26
LB = 27
SB = 28
SH = 29
LBU = 30
LHU = 31
SRL = 32
SRA = 33
LABEL = 34
AUIPC = 35
ID = 36
COLON = 37
DW = 38

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
                           "SRLI",
                           "SRAI",
                           "ADDI", 
                           "XORI", 
                           "XOR",
                           "OR",
                           "AND",
                           "SLTI",
                           "SLTIU",
                           "SLT",
                           "SLTU",
                           "LB",
                           "SB",
                           "SH",
                           "LBU",
                           "LHU",
                           "SRL",
                           "SRA",
                           "LABEL",
                           "AUIPC",
                           "ID",
                           "COLON",
                           "DW"]
          
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
        elif (k == 17):
            return "SRAI"
        elif (k == 18):
            return "ADDI"
        elif (k == 19):
            return "XORI"
        elif (k == 20):
            return "XOR"
        elif (k == 21):
            return "OR"
        elif (k == 22):
            return "AND"
        elif (k == 23):
            return "SLTI"
        elif (k == 24):
            return "SLTIU"
        elif (k == 25):
            return "SLT"
        elif (k == 26):
            return "SLTU"
        elif (k == 27):
            return "LB"
        elif (k == 28):
            return "SB"
        elif (k == 29):
            return "SH"
        elif (k == 30):
            return "LBU"
        elif (k == 31):
            return "LHU"
        elif (k == 32):
            return "SRL"
        elif (k == 33):
            return "SRA"
        elif (k == 34):
            return "LABEL"
        elif (k == 35):
            return "AUIPC"
        elif (k == 36):
            return "ID"
        elif (k == 37):
            return "COLON"
        elif (k == 38):
            return "DW"
        else:
            return "UNKNOWN"

class CodeGenerator:
    def __init__(self, outFile):
        self.outFile = outFile
        self.memarray = []
        #print "[ start ] CodeGenerator"

    def __del__(self):
        for index in range(len(self.memarray)):
            print "+" + "{0:0{1}X}".format(index,8) + " " + self.memarray[index]
            self.outFile.write("+" + "{0:0{1}X}".format(index,8) + " " + self.memarray[index] + "\n")
        
    def emitInstruction(self, cnt, op):
        #self.outFile.write("+" + "{0:0{1}X}".format(cnt,8) + " " + op + "\n")
        #print "+" + "{0:0{1}X}".format(cnt,8) + " " + op
        #self.memdic["{0:0{1}X}".format(cnt,8)] = op
        self.memarray.append(op)

        #print "--------------------"
        #for index in range(len(self.memarray)):
        #    print "+" + "{0:0{1}X}".format(index,8) + " " + self.memarray[index]
        #print "--------------------"
        
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

    def restartread(self):
        self.inFileHandle.seek(0)
        self.currentChar = "\n"
        self.currentColumnNumber = 0
        self.currentLineNumber = 0
        self.inputLine = ""
        self.buff = ""
        self.getNextChar()

    def __del__(self):
        self.inFileHandle.close()
        self.outFileHandle.close()
        #print "finished"

    def is_hex(self,s):
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
                        if not (self.is_hex(self.currentChar) or self.currentChar == "x"):
                            break
                    tkn.image = self.buff
                    tkn.kind = HEX
            elif self.currentChar.isalnum() or self.currentChar == "_" or self.currentChar == '@':
                self.buff = ""
                while True:
                    self.buff = self.buff + self.currentChar
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    self.getNextChar()
                    if not self.currentChar.isalnum():
                        break
                #print "self.buff:" + self.buff
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
                elif tkn.image == "SRAI":
                    tkn.kind = SRAI
                elif tkn.image == "ADDI":
                    tkn.kind = ADDI
                elif tkn.image == "XORI":
                    tkn.kind = XORI
                elif tkn.image == "XOR":
                    tkn.kind = XOR
                elif tkn.image == "OR":
                    tkn.kind = OR
                elif tkn.image == "AND":
                    tkn.kind = AND
                elif tkn.image == "SLTI":
                    tkn.kind = SLTI
                elif tkn.image == "SLTIU":
                    tkn.kind = SLTIU
                elif tkn.image == "SLT":
                    tkn.kind = SLT
                elif tkn.image == "SLTU":
                    tkn.kind = SLTU
                elif tkn.image == "LB":
                    tkn.kind = LB
                elif tkn.image == "SB":
                    tkn.kind = SB
                elif tkn.image == "SH":
                    tkn.kind = SH
                elif tkn.image == "LBU":
                    tkn.kind = LBU
                elif tkn.image == "LHU":
                    tkn.kind = LHU
                elif tkn.image == "SRL":
                    tkn.kind = SRL
                elif tkn.image == "SRA":
                    tkn.kind = SRA
                elif tkn.image == "AUIPC":
                    tkn.kind = AUIPC
                elif tkn.image == "dw":
                    tkn.kind = DW
                elif tkn.image[0] == "x" and tkn.image[1:].isdigit():
                    tkn.kind = REGISTER
                else:
                    tkn.kind = ID
            elif self.currentChar == ":":
                tkn.endLine = self.currentLineNumber
                tkn.endColumn = self.currentColumnNumber
                tkn.image = self.currentChar
                tkn.kind = COLON
                self.getNextChar()
            elif self.currentChar == ",":
                tkn.endLine = self.currentLineNumber
                tkn.endColumn = self.currentColumnNumber
                tkn.image = self.currentChar
                tkn.kind = COMMA
                self.getNextChar()
            else:
                tkn.kind = ERROR

        #print "tkn.image: " + tkn.image + " tkn.kind: " + tkn.getKind(tkn.kind) + " line: " + str(self.currentLineNumber)

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

PARSESTATE_NONE = 0
PARSESTATE_LABELS = 1
PARSESTATE_ASM = 2

SYMBOLTYPE_LABEL = 0
SYMBOLTYPE_DW = 0

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
        self.symboltablename = {}
        self.symboltabletype = {}
        self.asmblrstate = PARSESTATE_NONE
        
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
            print "at line: " + str(self.currentToken.beginLine) + ". Near [" + self.currentToken.image + "]"
            print "Error. Expecting " + self.currentToken.getKind(expected)
            exit(1)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])

                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])

                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])

                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
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
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "010" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

    def LUIpattern(self):
        op = "0110111"
        self.consume(LUI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                print "LUIpattern: " + self.instformat(instruction,8)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

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

    def SRAIpattern(self):
        op = "0010011"
        self.consume(SRAI)
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
        
        instruction = "0100000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def ADDIpattern(self):
        op = "0010011"
        self.consume(ADDI)
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
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def XORIpattern(self):
        op = "0010011"
        self.consume(XORI)
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
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def XORpattern(self):
        op = "0110011"
        self.consume(XOR)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def ORpattern(self):
        op = "0110011"
        self.consume(OR)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "110" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def ANDpattern(self):
        op = "0110011"
        self.consume(AND)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "111" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def SLTIpattern(self):
        op = "0010011"
        self.consume(SLTI)
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
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SLTIUpattern(self):
        op = "0010011"
        self.consume(SLTIU)
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
        
        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "011" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SLTpattern(self):
        op = "0110011"
        self.consume(SLT)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def SLTUpattern(self):
        op = "0110011"
        self.consume(SLTU)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "011" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def LBpattern(self):
        op = "0000011"
        self.consume(LB)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)

        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                
                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

    def SBpattern(self):
        op = "0100011"
        self.consume(SB)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        immstr = self.hextobinstr(imm.image[2:])
        immstr = self.binformat(immstr,20)
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])

        instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + immstr[15:20] + self.binformat(op,7)
        
        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def SHpattern(self):
        op = "0100011"
        self.consume(SH)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "001" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "001" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

    def LBUpattern(self):
        op = "0000011"
        self.consume(LBU)
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

        instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(HEX)

    def LHUpattern(self):
        op = "0000011"
        self.consume(LHU)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value or a label is expected."
                exit(1)
        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

    def SRLpattern(self):
        op = "0110011"
        self.consume(SRL)
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
        
        instruction = "0000000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def SRApattern(self):
        op = "0110011"
        self.consume(SRA)
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
        
        instruction = "0100000" + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
        self.consume(REGISTER)

    def LABELpattern(self):
        lbl = self.currentToken
        self.consume(ID)
        self.consume(COLON)
        if self.asmblrstate == PARSESTATE_LABELS:
            #print "adding label:" + lbl.image
            if lbl.image not in self.symboltablename:
                print "found label programcounter: " + str(self.programcounter)
                self.symboltablename[lbl.image] = self.programcounter
                self.symboltabletype[lbl.image] = SYMBOLTYPE_LABEL
            else:
                print "Error. Symbol [" + lbl.image + "] already exists."
                exit(1)

    def DWpattern(self):
        if self.asmblrstate == PARSESTATE_ASM:
            self.consume(DW)
            imm = self.currentToken
            immstr = self.hextobinstr(imm.image[2:])
            instruction = self.binformat(immstr,32)
            self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
            self.consume(HEX)
        elif self.asmblrstate == PARSESTATE_LABELS:
            self.consume(DW)
            self.consume(HEX)
    
    def AUIPCpattern(self):
        op = "0010111"
        self.consume(AUIPC)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        #self.binformat(imm,12)

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                #print "imm.image[2:]=" + imm.image
                immstr = self.hextobinstr(imm.image[2:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(ID)
            else:
                print "Error. Hex value is expected."
                exit(1)

        elif self.asmblrstate == PARSESTATE_LABELS:
            if imm.kind == HEX:
                self.consume(HEX)
            elif imm.kind == ID:
                self.consume(ID)
        else:
            print "Error. Invalid state"
            exit(1)

    def program(self,labels = 0):
        while self.currentToken.kind != EOF:
            if self.currentToken.kind == ID:
                self.LABELpattern()
            elif self.currentToken.kind == DW:
                self.DWpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LUI:
                self.LUIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == ADD:
                self.ADDpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SW:
                self.SWpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LW:
                self.LWpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LH:
                self.LHpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SUB:
                self.SUBpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLL:
                self.SLLpattern()
                self.programcounter += 1
            elif self.currentToken.kind == ORI:
                self.ORIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == ANDI:
                self.ANDIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLLI:
                self.SLLIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SRLI:
                self.SRLIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SRAI:
                self.SRAIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == ADDI:
                self.ADDIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == XORI:
                self.XORIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == XOR:
                self.XORpattern()
                self.programcounter += 1
            elif self.currentToken.kind == OR:
                self.ORpattern()
                self.programcounter += 1
            elif self.currentToken.kind == AND:
                self.ANDpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLTI:
                self.SLTIpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLTIU:
                self.SLTIUpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLT:
                self.SLTpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SLTU:
                self.SLTUpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LB:
                self.LBpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SB:
                self.SBpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SH:
                self.SHpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LBU:
                self.LBUpattern()
                self.programcounter += 1
            elif self.currentToken.kind == LHU:
                self.LHUpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SRL:
                self.SRLpattern()
                self.programcounter += 1
            elif self.currentToken.kind == SRA:
                self.SRApattern()
            elif self.currentToken.kind == AUIPC:
                self.AUIPCpattern()
                self.programcounter += 1
            elif self.currentToken.kind == ERROR:
                print "Line: " + str(self.currentToken.beginLine)
                print "syntax Error"
                print "Unexpected: " + self.currentToken.image
                exit(1)
            else:
                print "unexpected termination"
                exit(1)

    def parse(self):
        self.tmgr.restartread()
        self.tmgr.getNextChar()
        self.currentToken = self.tmgr.getNextToken()
        self.programcounter = 0
        self.asmblrstate = PARSESTATE_ASM
        print "start"
        self.program()
        print "finish"
        self.cg.emitInstruction(self.programcounter, "FFFFFFFF")
        print self.symboltabletype

    def parseLabels(self):
        self.programcounter = 0
        self.asmblrstate = PARSESTATE_LABELS
        self.program()
        print "symboltable:"
        print self.symboltablename

def printHelp():
    print "usage: python2 ../bin/asmblr.py <asm file>"

# let's start the assembler
if len(sys.argv) == 1:
    printHelp()
    sys.exit(1)

asmfile = sys.argv[1]

ass = asmblr(asmfile)
ass.parseLabels()
ass.parse()
