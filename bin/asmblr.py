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
                    #print "buff:" + self.buff
                    tkn.endLine = self.currentLineNumber
                    tkn.endColumn = self.currentColumnNumber
                    #if not (self.currentChar.isalnum() and self.currentChar == "x"):
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
                print "\ninputLine:" + self.inputLine
                self.currentColumnNumber = 0
                self.currentLineNumber = self.currentLineNumber + 1
            else:
                self.currentChar = "EOF"
                return

        self.currentChar = self.inputLine[self.currentColumnNumber]
        self.currentColumnNumber = self.currentColumnNumber + 1
        #print "currentChar:" + self.currentChar
        

tmgr = TokenMgr("tstPattern0003.asm", "outfile.txt")
tmgr.getNextChar()

for i in range(50):
    tkn = tmgr.getNextToken()
    print "Token.image:" + tkn.image + " Token.kind:" + tkn.getKind(tkn.kind)

