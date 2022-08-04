import sys
import random

FinalPassword = ""

ARGS = ["-h", "-help", "-w", "--words", "-c", "--caps", "-n", "--numbers", "-s", "symbols"]

f = open("lowercaseDict.txt", "r")
WORDS = f.read().splitlines()
SYMBOLS = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":" ";"]

ChosenWords = []
ChosenNumbers = []
ChosenSymbols = []

helpText = """usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n

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

"FIXED THIS so no repeats"
def chooseNwords(n = 4):
    print(n, "words chosen")
    for i in range(0, n):
        chosenWord = WORDS[random.randint(0, len(WORDS) - 1)]
        ChosenWords.append(chosenWord)

def capN(n = 0):
    if n <= 0:
        return
    
    for i in range(0, n if n <= len(ChosenWords) else len(ChosenWords)):
        ChosenWords[i] = ChosenWords[i].capitalize()

    if n > len(ChosenWords):
        print("ATTENTION: Number of capitalisations exceeds number of words chosen. All chosen words have been capitalised.")

def chooseNnumbers(n = 0):
    if (n <= 0):
        return
    
    for i in range(0, n):
        ChosenNumbers.append(str(random.randint(0, 9)))

def chooseNSymbols(n = 0):
    if (n <= 0):
        return
    
    for i in range(0, n):
        randSymb = SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        ChosenSymbols.append(randSymb)

""""""""

def addWords(i):
    if (i + 1 >= len(sys.argv)):
        """if out of bounds then choose 4 (default)"""
        chooseNwords()
    elif ((sys.argv[i + 1] in ARGS) == True):
        """if next is in list of valid args then choose 4 (default)"""
        chooseNwords()
    else:
        chooseNwords(int(sys.argv[i + 1]))

def makeCaps(i):
    if (len(ChosenWords) <= 0):
        chooseNwords()
        
    if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
        ""

    if (i + 1 >= len(sys.argv)):
        """if out of bounds"""
        capN()
    elif ((sys.argv[i + 1] in ARGS) == True):
        """if next is in list of valid args then"""
        capN()
    else:
        capN(int(sys.argv[i + 1]))

def addNums(i):
    if (len(ChosenWords) <= 0):
        chooseNwords()
        
    if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
        ""

    if (i + 1 >= len(sys.argv)):
        """if out of bounds"""
        chooseNnumbers()
    elif ((sys.argv[i + 1] in ARGS) == True):
        """if next is in list of valid args then"""
        chooseNnumbers()
    else:
        chooseNnumbers(int(sys.argv[i + 1]))

def addSymbols(i):
    if (len(ChosenWords) <= 0):
        chooseNwords()

    if (("-w" in sys.argv) == False or ("--words" in sys.argv) == False):
        ""

    if (i + 1 >= len(sys.argv)):
        """if out of bounds"""
        chooseNSymbols()
    elif ((sys.argv[i + 1] in ARGS) == True):
        """if next is in list of valid args then"""
        chooseNSymbols()
    else:
        chooseNSymbols(int(sys.argv[i + 1]))

def makePassword():
    all_Lists = ChosenWords + ChosenNumbers + ChosenSymbols
    random.shuffle(all_Lists)
    print("".join(all_Lists))

def checkArgs():
    if len(sys.argv) <= 1:
        chooseNwords()
        print("".join(ChosenWords))
    else:
        for i in range(len(sys.argv)):
            arg = sys.argv[i]
            if arg == "-h" or arg == "--help":
                print(helpText)
            elif (arg == "-w" or arg == "--words"):
                addWords(i)
            elif (arg == "-c" or arg == "--caps"):
                makeCaps(i)
            elif (arg == "-n" or arg == "--numbers"):
                addNums(i)
            elif (arg == "-s" or arg == "--symbols"):
                addSymbols(i)
    
    print(ChosenWords)
    print(ChosenNumbers)
    print(ChosenSymbols)
    makePassword()

checkArgs()
