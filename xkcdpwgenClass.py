import sys
import random

f = open("lowercaseDict.txt", "r")

HELP_TEXT = """usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]

Generate a secure, memorable password using the XKCD method
                
optional arguments:
    -h, --help            show this help message and exit
    
    -w WORDS, --words WORDS         include WORDS words in the password (default=4)

    -c CAPS, --caps CAPS        capitalize the first letter of CAPS random words
                                (default=0)

    -n NUMBERS, --numbers NUMBERS
                          insert NUMBERS random numbers in the password
                          (default=0)

    -s SYMBOLS, --symbols SYMBOLS
                          insert SYMBOLS random symbols in the password
                          (default=0)
"""

class XKCD:
    def __init__(self):
        self.WORDS = f.read().splitlines()
        self.SYMBOLS = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":" ";"]
        self.ARGS = ["-h", "-help", "-w", "--words", "-c", "--caps", "-n", "--numbers", "-s", "symbols"]

        self.ChosenWords = []
        self.ChosenSymbols = []
        self.ChosenNumbers = []

    "FIXED THIS so no repeats"
    def chooseNwords(self, n = 4):
        print(n, "words chosen")
        for i in range(0, n):
            chosenWord = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
            self.ChosenWords.append(chosenWord)

    def capN(self, n = 0):
        if n <= 0:
            return
        
        for i in range(0, n if n <= len(self.ChosenWords) else len(self.ChosenWords)):
            self.ChosenWords[i] = self.ChosenWords[i].capitalize()

        if n > len(self.ChosenWords):
            print("ATTENTION: Number of capitalisations exceeds number of words chosen. All chosen words have been capitalised.")

    def chooseNnumbers(self, n = 0):
        if (n <= 0):
            return
        
        for i in range(0, n):
            self.ChosenNumbers.append(str(random.randint(0, 9)))

    def chooseNSymbols(self, n = 0):
        if (n <= 0):
            return
        
        for i in range(0, n):
            randSymb = self.SYMBOLS[random.randint(0, len(self.SYMBOLS) - 1)]
            self.ChosenSymbols.append(randSymb)

    """"""""

    def addWords(self, i):
        if (i + 1 >= len(sys.argv)):
            """if out of bounds then choose 4 (default)"""
            self.chooseNwords()
        elif ((sys.argv[i + 1] in self.ARGS) == True):
            """if next is in list of valid args then choose 4 (default)"""
            self.chooseNwords()
        else:
            self.chooseNwords(int(sys.argv[i + 1]))

    def makeCaps(self, i):
        if (len(self.ChosenWords) <= 0):
            self.chooseNwords()
            
        if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
            ""

        if (i + 1 >= len(sys.argv)):
            """if out of bounds"""
            self.capN()
        elif ((sys.argv[i + 1] in self.ARGS) == True):
            """if next is in list of valid args then"""
            self.capN()
        else:
            self.capN(int(sys.argv[i + 1]))

    def addNums(self, i):
        if (len(self.ChosenWords) <= 0):
            self.chooseNwords()
            
        if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
            ""

        if (i + 1 >= len(sys.argv)):
            """if out of bounds"""
            self.chooseNnumbers()
        elif ((sys.argv[i + 1] in self.ARGS) == True):
            """if next is in list of valid args then"""
            self.chooseNnumbers()
        else:
            self.chooseNnumbers(int(sys.argv[i + 1]))

    def addSymbols(self, i):
        if (len(self.ChosenWords) <= 0):
            self.chooseNwords()

        if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
            ""

        if (i + 1 >= len(sys.argv)):
            """if out of bounds"""
            self.chooseNSymbols()
        elif ((sys.argv[i + 1] in self.ARGS) == True):
            """if next is in list of valid args then"""
            self.chooseNSymbols()
        else:
            self.chooseNSymbols(int(sys.argv[i + 1]))

    def makePassword(self):
        self.checkArgs()
        all_Lists = self.ChosenWords + self.ChosenNumbers + self.ChosenSymbols
        random.shuffle(all_Lists)
        print("".join(all_Lists))

    def checkArgs(self):
        if len(sys.argv) <= 1:
            self.chooseNwords()
        elif ((sys.argv[1] in self.ARGS) == False):
            print(HELP_TEXT)
            return
        else:
            for i in range(len(sys.argv)):
                arg = sys.argv[i]
                if arg == "-h" or arg == "--help":
                    print(HELP_TEXT)
                    return
                elif (arg == "-w" or arg == "--words"):
                    self.addWords(i)
                elif (arg == "-c" or arg == "--caps"):
                    self.makeCaps(i)
                elif (arg == "-n" or arg == "--numbers"):
                    self.addNums(i)
                elif (arg == "-s" or arg == "--symbols"):
                    self.addSymbols(i)
        
        print(self.ChosenWords)
        print(self.ChosenNumbers)
        print(self.ChosenSymbols)
        "self.makePassword()"

pwGen = XKCD()
pwGen.makePassword()
