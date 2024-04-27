
#
# Tiny Basic Python Edition v2021.08.29
#
# v2022.11.23
#


A = 0                               # temp
B = 0                               # temp
characterPointer = 0                # character index in line
errorLineNumber = 0                 # line number for error msg
# I = 0                             # temp (loops)
K = 0                               # temp
programMemoryPointer = 0            # number of lines
N = 0                               # number
mathStackMemoryPointer = 0          # expression stack index
T = 0                               # temp
variableStackMemoryPointer = 0      # variable index

As = ""                             # temp
Bs = ""                             # temp
character = ""                      # character
Ds = ""                             # single statement
errorMessage = ""                   # error message
Zs = ""                             # statement input

EMPTY_STRING = ""
SPACE = " "
COLON = ":"
COMMA = ","
SEMI_COLON = ""

LINE_NUMBER_PADDING = "     "


# operators
OP_EQUALS = "="
OP_PLUS = "+"
OP_MINUS = "-"
OP_LESS_THAN = "<"
OP_GREATER_THAN = ">"
OP_MULTIPLY = "*"
OP_DIVIDE = "/"
OP_MODULUS = "%"
OP_LEFT_PARENTHESIS = "("
OP_RIGHT_PARENTHESIS = ")"

END_OF_LINE_CHARACTER = '\n'
NEWLINE = '\n'


# characters
CH_DOUBLE_QUOTE = 34
CH_PERCENT = 37
CH_ASTERISK = 42
CH_PLUS = 43
CH_MINUS = 45
CH_DECIMAL_POINT = 46
CH_FORWARD_SLASH = 47
CH_ZERO = 48
CH_NINE = 57
CH_LESS_THAN = 60
CH_GREATER_THAN = 62
CH_UPPERCASE_A = 65
CH_UPPERCASE_Z = 90
CH_BACK_SLASH = 92
CH_LOWERCASE_A = 97
CH_LOWERCASE_Z = 122


PROGRAM_MEMORY_TOP = 256
PROGRAM_MEMORY_START = 27
PROGRAM_MEMORY_WORKSPACE = 26

PROCESSOR_STACK_MEMORY_TOP = 82

VARIABLE_STACK_MEMORY_START = 27
VARIABLE_STACK_MEMORY_TOP = 52

MATH_STACK_MEMORY_START = 53
MATH_STACK_MEMORY_TOP = 82

CHARACTERS_PER_LINE = 59


# [27-125] = 99 program lines
programCode = []

# [27 - 52] = 26 variables
variableStack = []

# [53 - 82] = 30 items math stack
mathStack = []
processorStack = []


inputText = ""
outputText = ""
welcomeMessage = ""
totalMemoryMessage = ""
freeMemoryMessage = ""
promptMessage = ""
subroutine = ""


characterArray = []
asciiCode = 0


def Start():
    global outputText

    # cls
    outputText = EMPTY_STRING

    Initialise()

# def Update():

    CaptainOnTheBridge()


def Initialise():
    global subroutine, freeMemoryMessage

    ColdStart()

    WarmStart()

    WriteLineToConsole(NEWLINE)

    WriteLineToConsole(welcomeMessage)
    # WriteLineToConsole(str(NEWLINE))

    GetTotalMemory()

    GetFreeMemory()

    WriteLineToConsole(totalMemoryMessage + freeMemoryMessage)
    # WriteLineToConsole(str(NEWLINE))

    WriteLineToConsole(promptMessage)
    # WriteLineToConsole(str(NEWLINE))

    subroutine = "Report"


def ColdStart():
    global programCode, variableStack, mathStack, processorStack
    global welcomeMessage, promptMessage

    programCode = []

    variableStack = []

    mathStack = []

    processorStack = []

    welcomeMessage = "Tiny Basic Python Edition" + END_OF_LINE_CHARACTER

    promptMessage = "Ready" + END_OF_LINE_CHARACTER


def WarmStart():
    global A, B, characterPointer, errorLineNumber, programMemoryPointer
    global N, mathStackMemoryPointer, T, variableStackMemoryPointer, asciiCode
    global As, Bs, character, Ds, errorMessage

    global programCode, variableStack, mathStack, processorStack
    global PROGRAM_MEMORY_TOP, VARIABLE_STACK_MEMORY_TOP, MATH_STACK_MEMORY_TOP, PROCESSOR_STACK_MEMORY_TOP

    global EMPTY_STRING

    for programCodePointer in range(PROGRAM_MEMORY_TOP):

        programCode.append(EMPTY_STRING)

    for variableStackPointer in range(VARIABLE_STACK_MEMORY_TOP):

        variableStack.append(0)

    for mathStackPointer in range(MATH_STACK_MEMORY_TOP):

        mathStack.append(0)

    for processorStackPointer in range(PROCESSOR_STACK_MEMORY_TOP):

        processorStack.append(0)

    programCode[9] = "BYE, CLEAR, CLS, END"
    programCode[10] = "HELP, MEM, NEW, RUN"
    programCode[11] = "GOTO | LOAD | SAVE <exp>"
    programCode[12] = "IF <exp> THEN <statement>"
    programCode[13] = "INPUT <var>"
    programCode[14] = "[LET] <var>=<exp>"
    programCode[15] = "LIST [<exp>|PAUSE]"
    programCode[16] = "PRINT <exp|str>[,<exp|str>][]"
    programCode[17] = "REM <any>"

    A = 0
    B = 0
    characterPointer = 0
    errorLineNumber = 0
    programMemoryPointer = 0
    N = 0
    mathStackMemoryPointer = 0
    T = 0
    variableStackMemoryPointer = 0

    asciiCode = 0

    As = EMPTY_STRING
    Bs = EMPTY_STRING
    character = EMPTY_STRING
    Ds = EMPTY_STRING
    errorMessage = EMPTY_STRING


def GetTotalMemory():
    global totalMemoryMessage

    totalMemory = int(((10 + 2 * CHARACTERS_PER_LINE) * PROGRAM_MEMORY_TOP) / 1024)

    totalMemoryMessage = str(totalMemory) + "K Memory"


def GetFreeMemory():
    global Bs
    global freeMemoryMessage

    freeMemoryStart = PROGRAM_MEMORY_START

    for memoryPointer in range(PROGRAM_MEMORY_TOP - 1, PROGRAM_MEMORY_START):

        Bs = programCode[memoryPointer]

        if Bs == EMPTY_STRING:

            freeMemoryStart = memoryPointer

    memoryTopBytes = (10 + (2 * CHARACTERS_PER_LINE)) * PROGRAM_MEMORY_TOP

    memoryBottomBytes = (10 + (2 * CHARACTERS_PER_LINE)) * freeMemoryStart

    freeMemory = memoryTopBytes - memoryBottomBytes

    freeMemoryMessage = "  " + str(freeMemory) + " Bytes Free" + END_OF_LINE_CHARACTER


def CaptainOnTheBridge():

    while True:
        if subroutine == "Report":
            Report()

        if subroutine == "Command":
            Command()

        if subroutine == "MakeItSo":
            MakeItSo()

        if subroutine == "Engage":
            Engage()

        if subroutine == "RunCommandInterpreter":
            RunCommandInterpreter()

        if subroutine == "FinishStatement":
            FinishStatement()

        if subroutine == "FinishStatement2":
            FinishStatement2()

        if subroutine == "Print":
            TB_Print()

        if subroutine == "NextChar":
            NextChar()

        if subroutine == "EndPrint":
            EndPrint()


def Report():
    global subroutine

    ErrorHandler()

    subroutine = "Command"


def Command():
    global Zs, inputText

    inputText = input(">")
    
    Zs = inputText + END_OF_LINE_CHARACTER
    
    OnScreen()


def OnScreen():
    global subroutine

    WriteLineToConsole(">" + Zs)

    subroutine = "MakeItSo"


def MakeItSo():
    global errorLineNumber, characterPointer, programMemoryPointer
    global subroutine

    programMemoryPointer = PROGRAM_MEMORY_WORKSPACE

    characterPointer = 0

    programCode[programMemoryPointer] = Zs

    GetNumber()

    errorLineNumber = N

    # if no line number
    if N == 0:

        if character == END_OF_LINE_CHARACTER:

            subroutine = "Report"

        else:

            subroutine = "RunCommandInterpreter"

        return

    if N > 0:

        EnterLine()

        subroutine = "Report"

        return

    if N < 0:

        errorLineNumber = 0

        ErrorMessage("Invalid line number")

        subroutine = "Report"

        return

    subroutine = "Engage"


def Engage():
    global errorLineNumber
    global subroutine

    GetNumber()

    errorLineNumber = N

    subroutine = "RunCommandInterpreter"


def RunCommandInterpreter():
    global T, characterPointer
    global subroutine

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    if Ds == "IF":

        TB_If()

        return

    if Ds == "REM":

        TB_Rem()

        return

    if Ds == "INPUT":

        TB_Input()

        return

    if Ds == "PRINT":

        subroutine = "Print"

        return

    if Ds == "RUN":

        TB_Run()

        return

    if Ds == "GOTO":

        TB_Goto()

        return

    if Ds == "GOSUB":

        TB_Gosub()

        return

    if Ds == "RETURN":

        TB_Return()

        return

    if Ds == "NEW":

        TB_New()

        return

    if Ds == "CLS":

        TB_Cls()

        return

    if Ds == "HELP":

        TB_Help()

        return

    if Ds == "MEM":

        TB_Mem()

        return

    if Ds == "END":

        TB_End()

        return

    if Ds == "STOP":

        TB_Stop()

        return

    if Ds == "LIST":

        TB_List()

        return

    if Ds == "SAVE":

        TB_Save()

        return

    if Ds == "LOAD":

        TB_Load()

        return

    if Ds == "LET":

        TB_Let()

    ReturnVar()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    SkipSpace()

    GetChar()

    if character != OP_EQUALS:

        ErrorMessage("= expected")

        subroutine = "Report"

        return

    characterPointer += 1

    T = variableStackMemoryPointer

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    processorStack[T] = N

    subroutine = "FinishStatement"


def FinishStatement():
    global characterPointer, programMemoryPointer
    global subroutine

    SkipSpace()

    GetChar()

    if character == COLON:

        characterPointer += 1

        subroutine = "RunCommandInterpreter"

        return

    else:

        if character != END_OF_LINE_CHARACTER:

            ErrorMessage("End of statement expected")

            subroutine = "Report"

            return

    if programMemoryPointer == PROGRAM_MEMORY_WORKSPACE:

        subroutine = "Report"

        return

    programMemoryPointer += 1

    characterPointer = 0

    if programMemoryPointer == PROGRAM_MEMORY_TOP + 1:

        ErrorMessage("Program Overflow")

        subroutine = "Report"

        return

    subroutine = "FinishStatement2"


def FinishStatement2():
    global Bs, subroutine

    Bs = programCode[programMemoryPointer]

    if Bs == EMPTY_STRING:

        subroutine = "Report"

        return

    subroutine = "Engage"


def NextChar():
    global characterPointer
    global Bs, subroutine, character

    characterPointer += 1

    character = As[characterPointer]

    if character == END_OF_LINE_CHARACTER:

        ErrorMessage("Unterminated string")

        subroutine = "Report"

        return

    else:

        if character != CH_DOUBLE_QUOTE:

            Bs += character

            subroutine = "NextChar"

            return

    characterPointer += 1

    character = As[characterPointer]

    if character == CH_DOUBLE_QUOTE:

        Bs += character

        subroutine = "NextChar"

        return

    WriteLineToConsole(Bs)

    subroutine = "EndPrint"


def EndPrint():
    global characterPointer
    global subroutine

    SkipSpace()

    GetChar()

    if character == COMMA:

        characterPointer += 1

        subroutine = "Print"

        return

    SkipSpace()

    GetChar()

    if character == SEMI_COLON:

        characterPointer += 1

        return

    WriteLineToConsole(str(NEWLINE))

    subroutine = "FinishStatement"


def PauseList():

    linesToDisplay = (programMemoryPointer - PROGRAM_MEMORY_WORKSPACE) % 10

    if linesToDisplay == 0:

        pass
        # INPUT "" P$


def EnterLine():
    global B, T, characterPointer, programMemoryPointer

    programMemoryPointer = PROGRAM_MEMORY_START

    characterPointer = 0

    T = N

    # NextLine
    while True:

        GetNumber()

        if (N < T) and (N != 0) and (programMemoryPointer < PROGRAM_MEMORY_TOP + 1):

            programMemoryPointer += 1

            characterPointer = 0

        else:

            break

    if programMemoryPointer == PROGRAM_MEMORY_TOP + 1:

        ErrorMessage("Program Overflow")

        return

    if T != N:

        for i in range(PROGRAM_MEMORY_TOP, programMemoryPointer):

            B = i - 1

            programCode[i] = programCode[B]

        programCode[programMemoryPointer] = Zs

        GetChar()

    if character == END_OF_LINE_CHARACTER:

        for i in range(programMemoryPointer, PROGRAM_MEMORY_TOP - 1):

            B = i + 1

            programCode[i] = programCode[B]


def GetExpression():
    global N, mathStackMemoryPointer

    mathStackMemoryPointer = MATH_STACK_MEMORY_START

    processorStack[mathStackMemoryPointer] = 0

    BoolExpression()

    N = processorStack[mathStackMemoryPointer]


def BoolExpression():
    global asciiCode

    AddExpression()

    SkipSpace()

    GetChar()

    # NextBool
    while (asciiCode >= CH_LESS_THAN) and (asciiCode <= CH_GREATER_THAN):

        if character == OP_EQUALS:

            TB_Equals()

        if character == OP_GREATER_THAN:

            TB_Greater_Than()

        if character == OP_LESS_THAN:

            TB_Less_Than()

        SkipSpace()

        GetChar()

        asciiCode = ord(character)


def AddExpression():
    global asciiCode

    MulExpression()

    SkipSpace()

    GetChar()

    # NextAdd
    while (asciiCode == CH_PLUS) or (asciiCode == CH_MINUS):

        if character == OP_PLUS:

            TB_Add()

        if character == OP_MINUS:

            TB_Subtract()

        SkipSpace()

        GetChar()

        asciiCode = character


def MulExpression():
    global asciiCode

    GroupExpression()

    SkipSpace()

    GetChar()

    # NextMul
    while (asciiCode == CH_ASTERISK) or (asciiCode == CH_FORWARD_SLASH) or (asciiCode == CH_PERCENT):

        if character == OP_MULTIPLY:

            TB_Multiply()

        if character == OP_DIVIDE:

            TB_Divide()

        if character == OP_MODULUS:

            TB_Modulus()

        SkipSpace()

        GetChar()

        asciiCode = character


def GroupExpression():
    global B, characterPointer, asciiCode, mathStackMemoryPointer

    SkipSpace()

    GetChar()

    if character == OP_LEFT_PARENTHESIS:

        characterPointer += 1

        BoolExpression()

        SkipSpace()

        GetChar()

        if character != OP_RIGHT_PARENTHESIS:

            ErrorMessage("Missing )")

            return

        characterPointer += 1

        return

    if character == END_OF_LINE_CHARACTER:

        ErrorMessage("Invalid factor")

        return

    # default: \
    asciiCode = ord(character)

    if not (((asciiCode < CH_ZERO) or (asciiCode > CH_NINE)) and (asciiCode != CH_MINUS) and (asciiCode != CH_DECIMAL_POINT)):

        GetNumber()

        if errorMessage != EMPTY_STRING:

            return

        mathStackMemoryPointer += 1

        processorStack[mathStackMemoryPointer] = N

    else:

        GetLabel()

        if errorMessage != EMPTY_STRING:

            return

    B = len(Ds)

    if B == 1:

        ReturnVar()

        mathStackMemoryPointer += 1

        processorStack[mathStackMemoryPointer] = processorStack[variableStackMemoryPointer]

    else:

        if Ds == "ticks":

            #                  S = S + 1
            #                  processorStack(S)=TICKS
            return

        if Ds == "tickspersec":

            #                  S = S + 1
            #                  processorStack(S)=TICKSPERSEC
            return

    # default: \
    ErrorMessage("Function expected")


def GetNumber():
    global A, asciiCode, characterPointer
    global Bs

    SkipSpace()

    GetChar()

    A = 0

    if character == OP_MINUS:

        Bs = OP_MINUS

        characterPointer += 1

        GetChar()

        asciiCode = ord(character)

        if ((asciiCode < CH_ZERO) or (asciiCode > CH_NINE)) and (asciiCode != CH_DECIMAL_POINT):

            ErrorMessage("Invalid number")

            return

    else:

        Bs = EMPTY_STRING

    if character == EMPTY_STRING:

        GetNumberCalc()

        return

    # NextNumber
    while True:

        if character == END_OF_LINE_CHARACTER:

            GetNumberCalc()

            return

        asciiCode = ord(character)

        if asciiCode == CH_DECIMAL_POINT:

            A += 1

            if A > 1:

                ErrorMessage("Invalid number")

            return

        if ((asciiCode < CH_ZERO) or (asciiCode > CH_NINE)) and (asciiCode != CH_DECIMAL_POINT):

            GetNumberCalc()

            return

        Bs += character

        characterPointer += 1

        GetChar()


def GetNumberCalc():
    global N

    if Bs == EMPTY_STRING:

        N = 0

    else:

        N = int(Bs)


def GetVar():

    GetLabel()

    if errorMessage != EMPTY_STRING:

        return

    ReturnVar()


def ReturnVar():
    global asciiCode, variableStackMemoryPointer

    asciiCode = ord(character)

    variableLength = len(Ds)

    if not ((variableLength != 1) or (asciiCode < CH_UPPERCASE_A) or (asciiCode > CH_UPPERCASE_Z)):

        # [27 - 52]
        variableStackMemoryPointer = asciiCode - 38

    else:

        ErrorMessage("Variable expected")


def GetLabel():
    global asciiCode, characterPointer
    global Ds

    SkipSpace()

    GetChar()

    Ds = EMPTY_STRING

    if character == END_OF_LINE_CHARACTER:

        ErrorMessage("Invalid label")

        return

    asciiCode = ord(character)

    if (asciiCode < CH_UPPERCASE_A) or (asciiCode > CH_UPPERCASE_Z):

        ErrorMessage("Invalid label")

        return

    # GetNextLabel
    while (asciiCode >= CH_UPPERCASE_A) and (asciiCode <= CH_UPPERCASE_Z):

        Ds += character

        characterPointer += 1

        GetChar()

        if character == END_OF_LINE_CHARACTER:

            return

        asciiCode = character


def SkipSpace():
    global characterPointer
    global character

    GetChar()

    if character != EMPTY_STRING:

        while character == SPACE:

            characterPointer += 1

        character = As[characterPointer]


def GetChar():
    global As, character

    As = programCode[programMemoryPointer]

    if As != EMPTY_STRING:

        character = As[characterPointer]

    else:

        character = EMPTY_STRING


def TB_If():
    global characterPointer
    global Bs, subroutine

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    if N == 0:

        Bs = programCode[programMemoryPointer]

        characterPointer = Bs.Length + 1

        subroutine = "FinishStatement"

        return

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    if Ds != "THEN":

        ErrorMessage("Then expected")

        subroutine = "Report"

        return

    subroutine = "RunCommandInterpreter"


def TB_Rem():
    global characterPointer
    global Bs, subroutine

    Bs = programCode[programMemoryPointer]

    characterPointer = Bs.Length  # + 1

    subroutine = "FinishStatement"


def TB_Input():

    pass
    # GOSUB(GetVar)

    # IF errorMessage$ <> EMPTY_STRING$ THEN
    # subroutine$ = "Report"
    # RETURN
    # ENDIF
    # INPUT N
    # processorStack(variableStackMemoryPointer) = N
    # subroutine$ = "FinishStatement"


def TB_Print():
    global character
    global Bs, subroutine

    SkipSpace()

    GetChar()

    if character != END_OF_LINE_CHARACTER:

        if character == CH_DOUBLE_QUOTE:

            Bs = EMPTY_STRING

            subroutine = "NextChar"

            return

    else:

        GetExpression()

        if errorMessage != EMPTY_STRING:

            subroutine = "Report"

            return

    WriteLineToConsole(str(N))

    subroutine = "EndPrint"


def TB_List():
    global T, K, characterPointer, programMemoryPointer
    global subroutine, errorMessage

    GetNumber()

    T = N

    K = programMemoryPointer

    i = characterPointer

    if T == 0:

        GetLabel()

        if errorMessage == EMPTY_STRING:

            if Ds == "PAUSE":

                i = characterPointer

            errorMessage = EMPTY_STRING

    for programMemoryPointer in range(PROGRAM_MEMORY_START, PROGRAM_MEMORY_TOP):

        characterPointer = 0

        GetNumber()

        if (T == 0) or (N == T):

            if As != EMPTY_STRING:

                lineNumberLength = len(str(N))

                lineNumberPadding = LINE_NUMBER_PADDING[len(LINE_NUMBER_PADDING) - lineNumberLength]

                WriteLineToConsole(lineNumberPadding + As)

                if Ds == "PAUSE":

                    PauseList()

    programMemoryPointer = K

    characterPointer = i

    subroutine = "FinishStatement"


def TB_Run():
    global programMemoryPointer, characterPointer
    global subroutine

    # clear variable stack
    for i in range(VARIABLE_STACK_MEMORY_START, VARIABLE_STACK_MEMORY_TOP):

        processorStack[i] = 0

    programMemoryPointer = PROGRAM_MEMORY_START

    characterPointer = 0

    subroutine = "FinishStatement2"


def TB_Goto():
    global T, errorLineNumber, characterPointer, programMemoryPointer
    global subroutine

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"

        return

    if errorLineNumber >= N:

        programMemoryPointer = PROGRAM_MEMORY_START

    characterPointer = 0

    T = N

    # NextGoto
    while True:

        if programMemoryPointer == PROGRAM_MEMORY_TOP + 1:

            ErrorMessage("Line not found")

            subroutine = "Report"

            return

        GetNumber()

        if N == T:

            errorLineNumber = N

            subroutine = "RunCommandInterpreter"

            return

        programMemoryPointer += 1

        characterPointer = 0


def TB_Gosub():

    pass
    # GOSUB(GetExpression)

    # IF errorMessage$ <> EMPTY_STRING$ THEN
    # subroutine$ = "Report" : REM GOTO(Ready)
    # RETURN
    # ENDIF

    # IF errorLineNumber >= N THEN
    # programMemoryPointer = PROGRAM_MEMORY_START
    # ENDIF

    # characterPointer = 0

    # T = N

    # (NextGosub)
    # WHILE TRUE
    # IF programMemoryPointer = PROGRAM_MEMORY_TOP + 1 THEN
    #  errorMessage$ = "Line not found"
    #  subroutine$ = "Report"
    #  RETURN
    # NDIF
    # GOSUB(GetNumber)
    # IF N = T THEN
    #  errorLineNumber = N
    #  subroutine$ = "RunCommandInterpreter"
    #  RETURN
    # ENDIF
    # programMemoryPointer = programMemoryPointer + 1
    # characterPointer = 0
    # ENDWHILE : REM GOTO(NextGoto)


def TB_Return():

    pass


def TB_New():
    global subroutine

    WarmStart()

    subroutine = "Report"


def TB_Cls():
    global subroutine, outputText

    outputText = EMPTY_STRING

    subroutine = "FinishStatement"


def TB_Help():
    global Bs, subroutine

    for i in range(9, 17):

        Bs = programCode[i]

        WriteLineToConsole(Bs)

    subroutine = "FinishStatement"


def TB_Mem():
    global subroutine

    GetFreeMemory()

    WriteLineToConsole(freeMemoryMessage)

    subroutine = "FinishStatement"


def TB_End():
    global subroutine

    subroutine = "Report"


def TB_Stop():
    global subroutine

    ErrorMessage("STOP")

    subroutine = "Report"


def TB_Save():

    pass
    # GOSUB(GetExpression)
    # IF errorMessage$ <> EMPTY_STRING$ THEN
    # subroutine$ = "Report" : REM GOTO(Ready)
    # RETURN
    # ENDIF
    # A$="tinyBas"+STR$(N,0)
    # A=FALSE
    # REM OPEN A$ FOR OUTPUT AS #1
    # FOR I=27 TO 125
    # B$=programCode$(I)
    # IF B$<>"" THEN
    #  PRINT #1,B$
    #  A=TRUE
    # ENDIF
    # NEXT
    # CLOSE #1
    # IF A = FALSE THEN
    #  REM KILL A$
    # ENDIF
    # subroutine$ = "FinishStatement" : REM GOTO(FinishStatement)


def TB_Load():

    pass
    # GOSUB(GetExpression)
    # IF errorMessage$ <> EMPTY_STRING$ THEN
    # subroutine$ = "Report" : REM GOTO(Ready)
    # RETURN
    # ENDIF
    # A$ = "tinyBas" + STR$(N)
    # REM B=FILEEXISTS(A$)
    # IF B = FALSE THEN
    #  errorMessage$="File "+A$+" not found"
    # subroutine$ = "Report" : REM GOTO(Ready)
    # RETURN
    # ENDIF
    # REM OPEN A$ FOR INPUT AS #1
    # B = FALSE
    # I = PROGRAM_MEMORY_START
    # WHILE B=FALSE
    # B = EOF(#1)
    # INPUT #1,B$
    # programCode$(I) = B$
    # INC I
    # ENDWHILE
    # CLOSE #1
    # WHILE I <= PROGRAM_MEMORY_TOP
    # programCode$(I) = ""
    # I = I + 1
    # ENDWHILE
    # IF errorLineNumber = 0 THEN
    # subroutine$ = "FinishStatement" : REM GOTO(FinishStatement)
    # RETURN
    # ENDIF
    # subroutine$ = "Report" : REM GOTO(Ready)


def TB_Let():
    global subroutine

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Report"


def TB_Equals():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] = processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Greater_Than():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    GetChar()

    if character == OP_EQUALS:

        TB_Greater_Than_Equal_To()

        return

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] > processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Greater_Than_Equal_To():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] >= processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Less_Than():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    GetChar()

    if character == OP_EQUALS:

        TB_Less_Than_Equal_To()

        return

    if character == OP_GREATER_THAN:

        TB_Not_Equal_To()

        return

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] < processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Less_Than_Equal_To():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] <= processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Not_Equal_To():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    AddExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] != processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Add():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    MulExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] + processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Subtract():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    MulExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] - processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Multiply():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    GroupExpression()

    B = mathStackMemoryPointer - 1

    processorStack[B] = processorStack[B] * processorStack[mathStackMemoryPointer]

    mathStackMemoryPointer -= 1


def TB_Divide():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    GroupExpression()

    B = processorStack[mathStackMemoryPointer]

    if B == 0:

        ErrorMessage("Division by zero")

        mathStackMemoryPointer -= 1

        return

    else:

        B = mathStackMemoryPointer - 1

        processorStack[B] = processorStack[B] / processorStack[mathStackMemoryPointer]

        mathStackMemoryPointer -= 1


def TB_Modulus():
    global B, characterPointer, mathStackMemoryPointer

    characterPointer += 1

    GroupExpression()

    B = processorStack[mathStackMemoryPointer]

    if B == 0:

        ErrorMessage("Division by zero")

        mathStackMemoryPointer -= 1

        return

    else:

        B = mathStackMemoryPointer - 1

        processorStack[B] = processorStack[B] % processorStack[mathStackMemoryPointer]

        mathStackMemoryPointer -= 1


def WriteLineToConsole(text):
    global outputText

    outputText = text  # += text

    print(outputText)


def ErrorMessage(message):
    global errorMessage

    if errorMessage == EMPTY_STRING:

        errorMessage = message


def ErrorHandler():
    global errorMessage

    if errorMessage != EMPTY_STRING:

        if errorLineNumber > 0:

            errorMessage = errorMessage + " at line " + str(errorLineNumber)

        errorMessage += END_OF_LINE_CHARACTER

        WriteLineToConsole(str(NEWLINE))
        WriteLineToConsole(errorMessage)

        errorMessage = EMPTY_STRING


Start()
