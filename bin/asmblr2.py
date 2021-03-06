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
JAL = 39
JALR = 40
BEQ = 41
BNE = 42
BLT = 43
BGE = 44
BLTU = 45
BGEU = 46
ORG = 47
SIGNED = 48
STRING = 49

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
                           "DW",
                           "JAL",
                           "JALR",
                           "BEQ",
                           "BNE",
                           "BLT",
                           "BGE",
                           "BLTU",
                           "BGEU",
                           "ORG",
                           "SIGNED",
                           "STRING"]
          
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
        elif (k == 39):
            return "JAL"
        elif (k == 40):
            return "JALR"
        elif (k == 41):
            return "BEQ"
        elif (k == 42):
            return "BNE"
        elif (k == 43):
            return "BLT"
        elif (k == 44):
            return "BGE"
        elif (k == 45):
            return "BLTU"
        elif (k == 46):
            return "BGEU"
        elif (k == 47):
            return "ORG"
        elif (k == 48):
            return "SIGNED"
        elif (k == 49):
            return "STRING"
        else:
            return "UNKNOWN"

class CodeGenerator:
    def __init__(self, outFile):
        self.outFile = outFile
        self.memarray = []
        self.memaddr = []
        #print "[ start ] CodeGenerator"

    def __del__(self):
        for index in range(len(self.memarray)):
            #print "+" + "{0:0{1}X}".format(index,8) + " " + self.memarray[index]
            print "+" + "{0:0{1}X}".format(self.memaddr[index],8) + " " + self.memarray[index]
            #self.outFile.write("+" + "{0:0{1}X}".format(index,8) + " " + self.memarray[index] + "\n")
            self.outFile.write("+" + "{0:0{1}X}".format(self.memaddr[index],8) + " " + self.memarray[index] + "\n")
        
    def emitInstruction(self, cnt, op):
        #self.outFile.write("+" + "{0:0{1}X}".format(cnt,8) + " " + op + "\n")
        #print "+" + "{0:0{1}X}".format(cnt,8) + " " + op
        #self.memdic["{0:0{1}X}".format(cnt,8)] = op
        self.memarray.append(op)
        self.memaddr.append(cnt)

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
        #self.getNextChar()

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
                    self.buff = self.buff + self.currentChar
                    self.getNextChar()
                    if self.currentChar == "x":
                        while True:
                            self.buff = self.buff + self.currentChar
                            tkn.endLine = self.currentLineNumber
                            tkn.endColumn = self.currentColumnNumber
                            self.getNextChar()
                            if not (self.is_hex(self.currentChar) or self.currentChar == "x"):
                                break
                        tkn.image = self.buff
                        tkn.kind = HEX
                    else:
                        self.buff = "0"
                        #self.getNextChar()
                        while True:
                            self.buff = self.buff + self.currentChar
                            tkn.endLine = self.currentLineNumber
                            tkn.endColumn = self.currentColumnNumber
                            self.getNextChar()
                            if not self.currentChar.isdigit():
                                break
                        #tkn.image = self.buff
                        #print "signed int: " + self.buff + "\n"
                        #print "      converting to hex: " + hex(int(self.buff) & 0xFFFFFFFF) + "\n"
                        tkn.image = hex(int(self.buff) & 0xFFFFFFFF)
                        tkn.kind = HEX
                else:
                    self.buff = ""
                    #self.getNextChar()
                    while True:
                        self.buff = self.buff + self.currentChar
                        tkn.endLine = self.currentLineNumber
                        tkn.endColumn = self.currentColumnNumber
                        self.getNextChar()
                        if not self.currentChar.isdigit():
                            break
                    tkn.image = self.buff
                    #print "signed int: " + self.buff + "\n"
                    #print "      converting to hex: " + hex(int(self.buff) & 0xFFFFFFFF) + "\n"
                    tkn.image = hex(int(self.buff) & 0xFFFFFFFF)
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
                if tkn.image == "LUI" or tkn.image == "lui":
                    tkn.kind = LUI
                elif tkn.image == "ADD" or tkn.image == "add":
                    tkn.kind = ADD
                elif tkn.image == "SW" or tkn.image == "sw":
                    tkn.kind = SW
                elif tkn.image == "LW" or tkn.image == "lw":
                    tkn.kind = LW
                elif tkn.image == "LH" or tkn.image == "lh":
                    tkn.kind = LH
                elif tkn.image == "SUB" or tkn.image == "sub":
                    tkn.kind = SUB
                elif tkn.image == "SLL" or tkn.image == "sll":
                    tkn.kind = SLL
                elif tkn.image == "ORI" or tkn.image == "ori":
                    tkn.kind = ORI
                elif tkn.image == "ANDI" or tkn.image == "andi":
                    tkn.kind = ANDI
                elif tkn.image == "SLLI" or tkn.image == "slli":
                    tkn.kind = SLLI
                elif tkn.image == "SRLI" or tkn.image == "srli":
                    tkn.kind = SRLI
                elif tkn.image == "SRAI" or tkn.image == "srai":
                    tkn.kind = SRAI
                elif tkn.image == "ADDI" or tkn.image == "addi":
                    tkn.kind = ADDI
                elif tkn.image == "XORI" or tkn.image == "xori":
                    tkn.kind = XORI
                elif tkn.image == "XOR" or tkn.image == "xor":
                    tkn.kind = XOR
                elif tkn.image == "OR" or tkn.image == "or":
                    tkn.kind = OR
                elif tkn.image == "AND" or tkn.image == "and":
                    tkn.kind = AND
                elif tkn.image == "SLTI" or tkn.image == "slti":
                    tkn.kind = SLTI
                elif tkn.image == "SLTIU" or tkn.image == "sltiu":
                    tkn.kind = SLTIU
                elif tkn.image == "SLT" or tkn.image == "slt":
                    tkn.kind = SLT
                elif tkn.image == "SLTU" or tkn.image == "sltu":
                    tkn.kind = SLTU
                elif tkn.image == "LB" or tkn.image == "lb":
                    tkn.kind = LB
                elif tkn.image == "SB" or tkn.image == "sb":
                    tkn.kind = SB
                elif tkn.image == "SH" or tkn.image == "sh":
                    tkn.kind = SH
                elif tkn.image == "LBU" or tkn.image == "lbu":
                    tkn.kind = LBU
                elif tkn.image == "LHU" or tkn.image == "lhu":
                    tkn.kind = LHU
                elif tkn.image == "SRL" or tkn.image == "srl":
                    tkn.kind = SRL
                elif tkn.image == "SRA" or tkn.image == "sra":
                    tkn.kind = SRA
                elif tkn.image == "AUIPC" or tkn.image == "auipc":
                    tkn.kind = AUIPC
                elif tkn.image == "dw":
                    tkn.kind = DW
                elif tkn.image == "JAL" or tkn.image == "jal":
                    tkn.kind = JAL
                elif tkn.image == "JALR" or tkn.image == "jalr":
                    tkn.kind = JALR
                elif tkn.image == "BEQ" or tkn.image == "beq":
                    tkn.kind = BEQ
                elif tkn.image == "BNE" or tkn.image == "bne":
                    tkn.kind = BNE
                elif tkn.image == "BLT" or tkn.image == "blt":
                    tkn.kind = BLT
                elif tkn.image == "BGE" or tkn.image == "bge":
                    tkn.kind = BGE
                elif tkn.image == "BLTU" or tkn.image == "bltu":
                    tkn.kind = BLTU
                elif tkn.image == "BGEU" or tkn.image == "bgeu":
                    tkn.kind = BGEU
                elif tkn.image == "org":
                    tkn.kind = ORG
                elif tkn.image == "zero":
                    tkn.image = "x0"
                    tkn.kind = REGISTER
                elif tkn.image == "ra":
                    tkn.image = "x1"
                    tkn.kind = REGISTER
                elif tkn.image == "sp":
                    tkn.image = "x2"
                    tkn.kind = REGISTER
                elif tkn.image == "gp":
                    tkn.image = "x3"
                    tkn.kind = REGISTER
                elif tkn.image == "tp":
                    tkn.image = "x4"
                    tkn.kind = REGISTER
                elif tkn.image == "t0":
                    tkn.image = "x5"
                    tkn.kind = REGISTER
                elif tkn.image == "t1":
                    tkn.image = "x6"
                    tkn.kind = REGISTER
                elif tkn.image == "t2":
                    tkn.image = "x7"
                    tkn.kind = REGISTER
                elif tkn.image == "s0" or tkn.image == "fp":
                    tkn.image = "x8"
                    tkn.kind = REGISTER
                elif tkn.image == "s1":
                    tkn.image = "x9"
                    tkn.kind = REGISTER
                elif tkn.image == "a0":
                    tkn.image = "x10"
                    tkn.kind = REGISTER
                elif tkn.image == "a1":
                    tkn.image = "x11"
                    tkn.kind = REGISTER
                elif tkn.image == "a2":
                    tkn.image = "x12"
                    tkn.kind = REGISTER
                elif tkn.image == "a3":
                    tkn.image = "x13"
                    tkn.kind = REGISTER
                elif tkn.image == "a4":
                    tkn.image = "x14"
                    tkn.kind = REGISTER
                elif tkn.image == "a5":
                    tkn.image = "x15"
                    tkn.kind = REGISTER
                elif tkn.image == "a6":
                    tkn.image = "x16"
                    tkn.kind = REGISTER
                elif tkn.image == "a7":
                    tkn.image = "x17"
                    tkn.kind = REGISTER
                elif tkn.image == "s2":
                    tkn.image = "x18"
                    tkn.kind = REGISTER
                elif tkn.image == "s3":
                    tkn.image = "x19"
                    tkn.kind = REGISTER
                elif tkn.image == "s4":
                    tkn.image = "x20"
                    tkn.kind = REGISTER
                elif tkn.image == "s5":
                    tkn.image = "x21"
                    tkn.kind = REGISTER
                elif tkn.image == "s6":
                    tkn.image = "x22"
                    tkn.kind = REGISTER
                elif tkn.image == "s7":
                    tkn.image = "x23"
                    tkn.kind = REGISTER
                elif tkn.image == "s8":
                    tkn.image = "x24"
                    tkn.kind = REGISTER
                elif tkn.image == "s9":
                    tkn.image = "x25"
                    tkn.kind = REGISTER
                elif tkn.image == "s10":
                    tkn.image = "x26"
                    tkn.kind = REGISTER
                elif tkn.image == "s11":
                    tkn.image = "x27"
                    tkn.kind = REGISTER
                elif tkn.image == "t3":
                    tkn.image = "x28"
                    tkn.kind = REGISTER
                elif tkn.image == "t4":
                    tkn.image = "x29"
                    tkn.kind = REGISTER
                elif tkn.image == "t5":
                    tkn.image = "x30"
                    tkn.kind = REGISTER
                elif tkn.image == "t6":
                    tkn.image = "x31"
                    tkn.kind = REGISTER
                elif tkn.image[0] == "x" and tkn.image[1:].isdigit():
                    tkn.kind = REGISTER
                else:
                    tkn.kind = ID
            elif self.currentChar == "-":
                self.buff = ""
                #self.getNextChar()
                while True:
                    self.buff = self.buff + self.currentChar
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    self.getNextChar()
                    if not self.currentChar.isdigit():
                        break
                #tkn.image = self.buff
                #print "signed int: " + self.buff + "\n"
                #print "      converting to hex: " + hex(int(self.buff) & 0xFFFFFFFF) + "\n"
                tkn.image = hex(int(self.buff) & 0xFFFFFFFF)
                tkn.kind = HEX
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
            elif self.currentChar == "\"":
                self.buff = ""
                self.getNextChar()
                while True:
                    self.buff = self.buff + self.currentChar
                    #print "buff: " + self.buff
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    self.getNextChar()
                    if self.currentChar == "\"":
                        #print "BREAK!"
                        break
                tkn.image = self.buff
                tkn.kind = STRING
                self.getNextChar()
            else:
                tkn.kind = ERROR

        #print "self.currentChar: " + self.currentChar
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

        if self.currentChar == ";" or self.currentChar == "#":
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
        self.asmblrstate = PARSESTATE_NONE
        
    def instformat(self,s,i):
        return "{0:0{1}X}".format(int(s,2),i)

    def binformat(self,s,i):
#        print "s: " + s + ",i: " + str(i)
#        print "returning: " + s.zfill(i)
#        return s.zfill(i)[len(s)-i:len(s)]
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

    def roundOffString(self, imm, n):
        return imm[len(imm)-n:len(imm)]        

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
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + imm.image[0:5]
                    #imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                    print "         ---- imm.image: " + imm.image
                    print "         ---- immstr: " + immstr
                else:
                    print "imm.image: " + imm.image
                    immstr = self.hextobinstr(imm.image[2:])
                    print "immstr: " + immstr

                #immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])

                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)

                #immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + imm.image[0:5]
                    #imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "010" + immstr[15:20] + self.binformat(op,7)
        
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
                if len(imm.image[2:]) > 5:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + imm.image[0:7]
                    #print "         this will be rounded to 0x" + imm.image[len(imm.image)-5:len(imm.image)]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,5)
                    #imm.image = imm.image[0:5]
                    imm.image = self.roundOffString(imm.image,5)
                    #imm.image = imm.image[0:7]
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 5:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:7] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:7]
                                 
                immstr = self.hextobinstr(labelvalue)

                #immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "110" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "110" + self.binformat(rdstr,5) + self.binformat(op,7)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
        
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
        
                instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))

                instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "001" + self.binformat(rdstr,5) + self.binformat(op,7)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + imm.image[0:5]
                    #imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
        
                instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))

                instruction = "0000000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:3]
#                    imm.image = imm.image[0:3]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,5)
                immstr = immstr[len(immstr)-5:len(immstr)]
        
                instruction = "0100000" + immstr + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)
                #instruction = self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 3:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:4]
                                 
                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                instruction = "0100000" + self.binformat(immstr,5) + self.binformat(rs1str,5) + "101" + self.binformat(rdstr,5) + self.binformat(op,7)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 3:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + imm.image[0:5]
                    #print "         this will be rounded to 0x" + imm.image[len(imm.image)-3:len(imm.image)]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
        
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    #print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
#                immstr = self.hextobinstr(imm.image[2:])
            
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "010" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
        
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "011" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "011" + self.binformat(rdstr,5) + self.binformat(op,7)

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
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)
                
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + immstr[15:20] + self.binformat(op,7)
        
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
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "001" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])

                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "100" + self.binformat(rdstr,5) + self.binformat(op,7)

                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                if len(str(hex(self.symboltablename[imm.image]))) > 3:
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + str(hex(self.symboltablename[imm.image]))[0:3]
                    imm.image = str(hex(self.symboltablename[imm.image]))[0:3]
                immstr = self.hextobinstr(imm.image)
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
                if len(str(hex(self.symboltablename[imm.image]))) > 3:
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + str(hex(self.symboltablename[imm.image]))[0:3]
                    imm.image = str(hex(self.symboltablename[imm.image]))[0:3]
                immstr = self.hextobinstr(imm.image)
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
                #print "found label programcounter: " + str(self.programcounter)
                self.symboltablename[lbl.image] = self.programcounter
            else:
                print "Error. Symbol [" + lbl.image + "] already exists."
                exit(1)

    def DWpattern(self):
        if self.asmblrstate == PARSESTATE_ASM:
            self.consume(DW)
            imm = self.currentToken
            if self.currentToken.kind == HEX:
                immstr = self.hextobinstr(imm.image[2:])
                instruction = self.binformat(immstr,32)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif self.currentToken.kind == STRING:
                strdata = imm.image
                self.consume(STRING)
                #print "self.currentToken.image: " + strdata
                #print "strdata[0:8]: [" + strdata[0:8] + "]"
                #print "strdata[8:16]: [" + strdata[8:16] + "]"
                for i in range(0,len(strdata),4):
                    #print "i: " + str(i) + " loop strdata: [i:i+4]: [" + strdata[i:i+4] + "]"
                    inst = "".join([ str(hex(ord(c))[2:]) for c in strdata[i:i+4] ])
                    #instruction = [ str(hex(ord(c))[2:]) for c in strdata[i:i+4] ]

                    #print "len: " + str(len(inst))
                    if (len(inst) < 8) :
                        for j in range(8 - len(inst)):
                            inst = inst + "0"

                    self.cg.emitInstruction(self.programcounter, inst)
                    
        elif self.asmblrstate == PARSESTATE_LABELS:
            self.consume(DW)
            if self.currentToken.kind == HEX:
                self.consume(HEX)
            elif self.currentToken.kind == STRING:
                self.consume(STRING)
    
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
                if len(imm.image[2:]) > 6:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:7]
#                    imm.image = imm.image[0:7]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,5)
                    imm.image = self.roundOffString(imm.image,5)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 6:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:7] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:7]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

    def JALpattern(self):
        op = "1101111"
        self.consume(JAL)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 5:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:7]
#                    imm.image = imm.image[0:7]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,5)
                    imm.image = self.roundOffString(imm.image,5)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
#                immstr = self.hextobinstr(imm.image[2:])
                print "len(immstr.image[2:] -> " + str(len(immstr))
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 5:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:7] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:7]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,5)
                    imm.image = self.roundOffString(labelvalue,5)
#                    immstr = self.hextobinstr(imm.image)
#                else:
#                    immstr = self.hextobinstr(imm.image[2:])
                                 
                immstr = self.hextobinstr(labelvalue)
                
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)
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

    def JALRpattern(self):
        op = "1100111"
        self.consume(JALR)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                rs1str = self.tobinstr(rs1.image[1:])
                rdstr = self.tobinstr(rd.image[1:])
                instruction = self.binformat(immstr,12) + self.binformat(rs1str,5) + "000" + self.binformat(rdstr,5) + self.binformat(op,7)
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    immstr = self.hextobinstr(labelvalue)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
                                 
#                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

    def BEQpattern(self):
        op = "1100011"
        self.consume(BEQ)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                immstr = ""
                if len(labelvalue) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    labelvalue = self.roundOffString(labelvalue,3)
#                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(labelvalue)
                                 
#                immstr = self.hextobinstr(labelvalue)

#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "000" + immstr[15:20] + self.binformat(op,7)
        
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

    def BNEpattern(self):
        op = "1100011"
        self.consume(BNE)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "001" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                immstr = ""
                if len(labelvalue) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    labelvalue = self.roundOffString(labelvalue,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])
                                 
#                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
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

    def BLTpattern(self):
        op = "1100011"
        self.consume(BLT)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "100" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                immstr = ""
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    labelvalue = self.roundOffString(labelvalue,3)
                    immstr = self.hextobinstr(labelvalue)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

                                 
#                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "100" + immstr[15:20] + self.binformat(op,7)
        
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

    def BLTUpattern(self):
        op = "1100011"
        self.consume(BLTU)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "111" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                immstr = ""
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    labelvalue = self.roundOffString(labelvalue,3)
                    immstr = self.hextobinstr(labelvalue)
                else:
                    immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "111" + immstr[15:20] + self.binformat(op,7)
        
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

    def BGEpattern(self):
        op = "1100011"
        self.consume(BGE)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "101" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                immstr = ""
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
#                    labelvalue = labelvalue[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(labelvalue,3)
                    imm.image = self.roundOffString(labelvalue,3)
                    immstr = self.hextobinstr(labelvalue)
                else:
                    immstr = self.hextobinstr(labelvalue)
                                 
#                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "101" + immstr[15:20] + self.binformat(op,7)
        
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

    def BGEUpattern(self):
        op = "1100011"
        self.consume(BGEU)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        if self.asmblrstate == PARSESTATE_ASM:
            if imm.kind == HEX:
                if len(imm.image[2:]) > 4:
                    print "Line: " + str(self.currentToken.beginLine)
                    print "Warning: " + imm.image + " exceeds the maximum immediate value."
#                    print "         this will be rounded to " + imm.image[0:5]
#                    imm.image = imm.image[0:5]
                    print "         this will be rounded to 0x" + self.roundOffString(imm.image,3)
                    imm.image = self.roundOffString(imm.image,3)
                    immstr = self.hextobinstr(imm.image)
                else:
                    immstr = self.hextobinstr(imm.image[2:])

#                immstr = self.hextobinstr(imm.image[2:])
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "111" + immstr[15:20] + self.binformat(op,7)
        
                self.cg.emitInstruction(self.programcounter, self.instformat(instruction,8))
                self.consume(HEX)
            elif imm.kind == ID:
                labelvalue = str(hex(self.symboltablename[imm.image]))
                if len(labelvalue) > 4:
                    print "Warning: " + labelvalue[2:0] + " exceeds the maximum immediate value."
                    print "         this will be rounded to " + labelvalue[0:5] + " address of label: " + imm.image
                    labelvalue = labelvalue[0:5]
                                 
                immstr = self.hextobinstr(labelvalue)
#                immstr = self.hextobinstr(str(hex(self.symboltablename[imm.image])))
                immstr = self.binformat(immstr,20)
                rs1str = self.tobinstr(rs1.image[1:])
                rs2str = self.tobinstr(rs2.image[1:])

                instruction =  immstr[8:15] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "111" + immstr[15:20] + self.binformat(op,7)
        
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

    def ORGpattern(self):
        self.consume(ORG)
        lprogcounter = self.currentToken
        self.consume(HEX)
        self.programcounter = int(lprogcounter.image[2:], 16)

    def program(self,labels = 0):
        while self.currentToken.kind != EOF:
            if self.currentToken.kind == ID:
                self.LABELpattern()
            elif self.currentToken.kind == DW:
                self.DWpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LUI:
                self.LUIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == ADD:
                self.ADDpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SW:
                self.SWpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LW:
                self.LWpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LH:
                self.LHpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SUB:
                self.SUBpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLL:
                self.SLLpattern()
                self.programcounter += 4
            elif self.currentToken.kind == ORI:
                self.ORIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == ANDI:
                self.ANDIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLLI:
                self.SLLIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SRLI:
                self.SRLIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SRAI:
                self.SRAIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == ADDI:
                self.ADDIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == XORI:
                self.XORIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == XOR:
                self.XORpattern()
                self.programcounter += 4
            elif self.currentToken.kind == OR:
                self.ORpattern()
                self.programcounter += 4
            elif self.currentToken.kind == AND:
                self.ANDpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLTI:
                self.SLTIpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLTIU:
                self.SLTIUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLT:
                self.SLTpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SLTU:
                self.SLTUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LB:
                self.LBpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SB:
                self.SBpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SH:
                self.SHpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LBU:
                self.LBUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == LHU:
                self.LHUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SRL:
                self.SRLpattern()
                self.programcounter += 4
            elif self.currentToken.kind == SRA:
                self.SRApattern()
            elif self.currentToken.kind == AUIPC:
                self.AUIPCpattern()
                self.programcounter += 4
            elif self.currentToken.kind == JAL:
                self.JALpattern()
                self.programcounter += 4
            elif self.currentToken.kind == JALR:
                self.JALRpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BEQ:
                self.BEQpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BNE:
                self.BNEpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BLT:
                self.BLTpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BGE:
                self.BGEpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BLTU:
                self.BLTUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == BGEU:
                self.BGEUpattern()
                self.programcounter += 4
            elif self.currentToken.kind == ORG:
                self.ORGpattern()
            elif self.currentToken.kind == ERROR:
                print "Line: " + str(self.currentToken.beginLine)
                print "syntax Error"
                print "Unexpected: " + self.currentToken.image
                exit(1)
            else:
                print "Line: " + str(self.currentToken.beginLine) + " syntax Error"
                print "unexpected termination near: " + self.currentToken.image
                exit(1)

    def parse(self):
        self.tmgr.restartread()
        self.tmgr.getNextChar()
        self.currentToken = self.tmgr.getNextToken()
        self.programcounter = 0
        self.asmblrstate = PARSESTATE_ASM
        #print "start"
        self.program()
        #print "finish"
        self.cg.emitInstruction(self.programcounter, "FFFFFFFF")

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
