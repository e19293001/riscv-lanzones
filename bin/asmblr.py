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
                           "REGISTER"]
          
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
        else:
            return "UNKNOWN"
    

class CodeGenerator:
    def __init__(self, outFile):
        self.outFile = outFile
        #print "[ start ] CodeGenerator"

    def emitInstruction(self, op):
        print op
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
                        if not (self.currentChar.isdigit() or self.currentChar == "x"):
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
                print "; " + self.inputLine[:len(self.inputLine)-1]
                self.currentColumnNumber = 0
                self.currentLineNumber = self.currentLineNumber + 1
            else:
                self.currentChar = "EOF"
                return

        self.currentChar = self.inputLine[self.currentColumnNumber]
        self.currentColumnNumber = self.currentColumnNumber + 1
        #print "currentChar:" + self.currentChar

class asmblr:
    def __init__(self):
        self.currentToken = Token()
        self.previousToken = Token()
        self.tmgr = TokenMgr("tstPattern0003.asm", "outfile.txt")
        self.tmgr.getNextChar()
        self.currentToken = self.tmgr.getNextToken()
        self.cg = CodeGenerator(self.tmgr.outFileHandle)
        
    def instformat(self,s,i):
        return "{0:0{1}x}".format(int(s,2),i)

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
        self.cg.emitInstruction(op + rd.image + rs1.image + imm.image)
        self.consume(HEX)

    def SWpattern(self):
        op = "0100011"
        self.consume(SW)
        rs1 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        rs2 = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        immstr = self.hextobinstr(imm.image[2:])
        rs1str = self.tobinstr(rs1.image[1:])
        rs2str = self.tobinstr(rs2.image[1:])

        #immstr = self.binformat(immstr,12)
        print "immstr - " + immstr
        #print "immstr[0:4] - " + immstr[0:4]
        #print "immstr[5:] - " + immstr[5:11]
        print "immstr[0:4]: " + immstr[0:5]
        print "immstr[5:11]: " + immstr[6:12]
        instruction = immstr[6:12] + self.binformat(rs2str,5) + self.binformat(rs1str,5) + "010" + immstr[0:5] + self.binformat(op,7)
        
        self.cg.emitInstruction(self.instformat(instruction,8))
        self.consume(HEX)

    def LUIpattern(self):
        op = "0110111"
        self.consume(LUI)
        rd = self.currentToken
        self.consume(REGISTER)
        self.consume(COMMA)
        imm = self.currentToken

        #self.binformat(imm,12)

        immstr = self.hextobinstr(imm.image[2:])
        rdstr = self.tobinstr(rd.image[1:])
        instruction = self.binformat(immstr,20) + self.binformat(rdstr,5) + self.binformat(op,7)

        self.cg.emitInstruction(self.instformat(instruction,8))
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

        self.cg.emitInstruction(self.instformat(instruction,8))
        self.consume(REGISTER)

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
            elif self.currentToken.kind == ERROR:
                print "syntax Error"
                exit()
            else:
                print "unexpected termination"
                exit()

    def parse(self):
        self.program()

ass = asmblr()
ass.parse()    

#for i in range(50):
#    tkn = tmgr.getNextToken()
#    print "Token.image:" + tkn.image + " Token.kind:" + tkn.getKind(tkn.kind)

