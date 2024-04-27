
#
# Tiny Basic Python Edition
#
# Adapted for Python
#
# v2023.02.06
#


# ---------------------------------
# tinyBasic.iBas
#
# tinyBasic v1.2
#   Copyleft 2005-2007
#     by Laurent DUVEAU
#   http://www.aldweb.com/
#
# This file is an iziBasic for
# Palm sample Tiny Basic
# interpreter, loosely adapted
# from the original Tiny Basic
# version by Li Chen Wang.
# ---------------------------------


# A          temp
# B          temp
# C          character index in line
# E          line number for error msg
# I          temp (loops)
# K          temp
# L          number of lines
# N          number
# S          expression stack index
# T          temp
# V          variable index

# A$         temp
# B$         temp
# C$         character
# D$         single statement
# E$         error message
# G$         string code (")
# H$         HALT code (Line Feed)
# I$-R$      Help
# Z$=A$(26)  statement input


EMPTY_STRING = ""

# print formatting characters
CHR_SPACE = " "
CHR_COLON = ":"
CHR_COMMA = ","
CHR_SEMI_COLON = ";"


# math / conditional operators
class OpCodes:
    OP_EQUALS = "="
    OP_ADD = "+"
    OP_SUBTRACT = "-"
    OP_MINUS = "-"
    OP_LESS_THAN = "<"
    OP_GREATER_THAN = ">"
    OP_MULTIPLY = "*"
    OP_DIVIDE = "/"
    OP_MODULUS = "%"
    OP_LEFT_PARENTHESIS = "("
    OP_RIGHT_PARENTHESIS = ")"


CHR_END_OF_LINE = chr(171)
CHR_DOUBLE_QUOTE = chr(34)


# character ascii codes
ASC_SPACE = 32
ASC_DOUBLE_QUOTE = 34
ASC_PERCENT = 37
ASC_ASTERISK = 42
ASC_PLUS = 43
ASC_MINUS = 45
ASC_DECIMAL_POINT = 46
ASC_FORWARD_SLASH = 47
ASC_ZERO = 48
ASC_NINE = 57
ASC_LESS_THAN = 60
ASC_GREATER_THAN = 62
ASC_UPPERCASE_A = 65
ASC_UPPERCASE_Z = 90
ASC_BACK_SLASH = 92
ASC_LOWERCASE_A = 97
ASC_LOWERCASE_Z = 122


# error codes
ERROR_CODE_STOP = -1
ERROR_CODE_PROGRAM_OVERFLOW = 8
ERROR_CODE_GOSUB_STACK_OVERFLOW = 188
ERROR_CODE_RETURN_WITHOUT_GOSUB = 133
ERROR_CODE_LINE_NOT_FOUND = 32
ERROR_CODE_UNTERMINATED_STRING = 62
ERROR_CODE_END_OF_STATEMENT_EXPECTED = 0
ERROR_CODE_INVALID_FACTOR = 0
ERROR_CODE_INVALID_NUMBER = 0
ERROR_CODE_INVALID_LABEL = 0
ERROR_CODE_INVALID_LINE_NUMBER = 9
ERROR_CODE_FUNCTION_EXPECTED = 0
ERROR_CODE_VARIABLE_EXPECTED = 0
ERROR_CODE_EQUALS_EXPECTED = 20
ERROR_CODE_THEN_EXPECTED = 0
ERROR_CODE_SYNTAX_ERROR = 0
ERROR_CODE_MISTAKE = 0
ERROR_CODE_NO_SUCH_VARIABLE = 0
ERROR_CODE_DIVISION_BY_ZERO = 224
ERROR_CODE_MISSING_RIGHT_PARENTHESIS = 296
ERROR_CODE_FILE_NOT_FOUND = 0


# error messages
ERROR_MESSAGE_STOP = "STOP"
ERROR_MESSAGE_PROGRAM_OVERFLOW = "Program overflow"  # 8
ERROR_MESSAGE_GOSUB_STACK_OVERFLOW = "GOSUB stack overflow"  # 188
ERROR_MESSAGE_RETURN_WITHOUT_GOSUB = "RETURN without GOSUB"  # 133
ERROR_MESSAGE_LINE_NOT_FOUND = "Line not found"  # 32
ERROR_MESSAGE_UNTERMINATED_STRING = "Missing """  # 62
ERROR_MESSAGE_END_OF_STATEMENT_EXPECTED = "End of statement expected"
ERROR_MESSAGE_INVALID_FACTOR = "Invalid factor"
ERROR_MESSAGE_INVALID_NUMBER = "Invalid number"
ERROR_MESSAGE_INVALID_LABEL = "Invalid label"
ERROR_MESSAGE_INVALID_LINE_NUMBER = "Invalid line number"  # 9
ERROR_MESSAGE_FUNCTION_EXPECTED = "Function expected"
ERROR_MESSAGE_VARIABLE_EXPECTED = "Variable expected"
ERROR_MESSAGE_EQUALS_EXPECTED = "= expected"  # 20
ERROR_MESSAGE_THEN_EXPECTED = "THEN expected"
ERROR_MESSAGE_SYNTAX_ERROR = "Syntax error"
ERROR_MESSAGE_MISTAKE = "Mistake"
ERROR_MESSAGE_NO_SUCH_VARIABLE = "No such variable"
ERROR_MESSAGE_DIVISION_BY_ZERO = "Division by zero"  # 224
ERROR_MESSAGE_MISSING_RIGHT_PARENTHESIS = "Missing )"  # 296
ERROR_MESSAGE_FILE_NOT_FOUND = "File not found"


# used to calculate/estimate available memory
STRING_OBJECT_DATA_LENGTH = 20
BYTES_PER_CHARACTER_BUFFER = 2

# input line length
MAXIMUM_LINE_LENGTH = 80

# [27-125] = 99 program lines
PROGRAM_CODE_MEMORY = 125
PROGRAM_CODE_MEMORY_START = 27
PROGRAM_CODE_MEMORY_WORKSPACE = 26

# [27-52] = 26 variables
# [53-82] = 30 items math stack
VARIABLE_STACK_MEMORY = 26
MATH_STACK_MEMORY = 30
PROCESSOR_STACK_MEMORY = 82
VARIABLE_STACK_MEMORY_START = 27
PROCESSOR_STACK_MEMORY_START = 53

GOSUB_STACK_MEMORY = 26

COMMAND_HELP_MEMORY = 10

# file i/o
FILE_NOT_FOUND = 0
FILE_EXTENSION = ".txt"

# carriage return / line feed
CRLF = True


# program variables
tempA = 0
# asciiCode = 0
tempB = 0
C_characterPointer = 0
errorCode = 0
E_errorLineNumber = 0
gosubStackPointer = 0
tempI = 0
tempK = 0
L_programCodeMemoryPointer = 0
lineNumber = 0
N_numericData = 0
S_processorStackPointer = 0
tempT = 0
V_variableStackPointer = 0

As = ""
Bs = ""
character = ""
Ds = ""
errorMessage = ""
Zs = ""


programCode = []

A_processorStack = []

gosubLineNumberPointer = []
returnLineNumberPointer = []

commandHelp = []


welcomeMessage = ""
promptMessage = ""
totalMemoryMessage = ""
freeMemoryMessage = ""
fileName = ""
subroutine = ""

dataInput = False
savingFile = False
loadingFile = False
fileNameOkay = False

programRunning = True


def Start():

    TinyBasic_Cls()

    Initialise()

    PowerOn()

    ProgramLoop()


def ProgramLoop():

    while programRunning:

        ControlLoop()


def ControlLoop():

    if subroutine == "Ready":

        Ready()

    if subroutine == "GetInput":

        GetInput()

    if subroutine == "AutoRun":

        AutoRun()

    if subroutine == "Exec":

        Exec()

    if subroutine == "NextStatement":

        NextStatement()

    if subroutine == "FinishStatement":

        FinishStatement()

    if subroutine == "FinishStatement2":

        FinishStatement2()

    if subroutine == "NextChar":

        NextChar()

    if subroutine == "EndPrint":

        EndPrint()


def PowerOn():

    global subroutine

    ColdStart()

    WarmStart()

    InitialiseCommandHelp()

    WriteTextToConsole(EMPTY_STRING, CRLF)

    WriteTextToConsole(welcomeMessage, CRLF)

    WriteTextToConsole(EMPTY_STRING, CRLF)

    GetTotalMemory()

    GetFreeMemory()

    WriteTextToConsole(totalMemoryMessage + freeMemoryMessage, CRLF)

    WriteTextToConsole(EMPTY_STRING, CRLF)

    WriteTextToConsole(promptMessage, CRLF)

    # goto Ready
    subroutine = "Ready"


def Initialise():

    global programCode, A_processorStack
    global gosubLineNumberPointer, returnLineNumberPointer, commandHelp

    programCode = []

    A_processorStack = []

    gosubLineNumberPointer = []

    returnLineNumberPointer = []

    commandHelp = []


def ColdStart():

    global gosubStackPointer
    global welcomeMessage, promptMessage

    for programCodePointer in range(0, PROGRAM_CODE_MEMORY):

        programCode.append(EMPTY_STRING)

    for processorStackPointer in range(0, PROCESSOR_STACK_MEMORY):

        A_processorStack.append(0)

    for gosubStackPointer in range(0, GOSUB_STACK_MEMORY):

        gosubLineNumberPointer.append(0)
        returnLineNumberPointer.append(0)

    welcomeMessage = CHR_SPACE + "**** Tiny Basic Python Edition ****"

    promptMessage = "Ready"


def WarmStart():

    global tempA, tempB, tempI, N_numericData, tempT, C_characterPointer, errorCode, E_errorLineNumber
    global L_programCodeMemoryPointer, lineNumber, S_processorStackPointer
    global V_variableStackPointer, gosubStackPointer
    global savingFile, loadingFile, fileNameOkay, programRunning
    global As, Bs, Ds, character, errorMessage, fileName

    tempA = 0
    tempB = 0

    C_characterPointer = 0

    errorCode = 0
    E_errorLineNumber = 0

    L_programCodeMemoryPointer = 0

    lineNumber = 0

    N_numericData = 0

    S_processorStackPointer = 0

    tempT = 0

    V_variableStackPointer = 0

    gosubStackPointer = 0

    # asciiCode = 0

    As = EMPTY_STRING

    Bs = EMPTY_STRING

    character = EMPTY_STRING

    Ds = EMPTY_STRING

    errorMessage = EMPTY_STRING

    fileName = EMPTY_STRING

    savingFile = False

    loadingFile = False

    fileNameOkay = False

    programRunning = True


def InitialiseCommandHelp():

    commandHelp.insert(0, "CLS, CLEAR, END")
    commandHelp.insert(1, "HELP, MEM, NEW, RUN")
    commandHelp.insert(2, "GOTO | GOSUB | RETURN")
    commandHelp.insert(3, "LOAD | SAVE <exp>")
    commandHelp.insert(4, "if <exp> THEN <statement>")
    commandHelp.insert(5, "INPUT <var>")
    commandHelp.insert(6, "[LET] <var>=<exp>")
    commandHelp.insert(7, "LIST [<exp>|PAUSE]")
    commandHelp.insert(8, "PRINT <exp|str>[,<exp|str>][;]")
    commandHelp.insert(9, "REM <any>")


def GetTotalMemory():

    global totalMemoryMessage

    totalMemory = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * PROGRAM_CODE_MEMORY

    totalMemory = int(totalMemory / 1024)

    totalMemoryMessage = CHR_SPACE + CHR_SPACE + CHR_SPACE + CHR_SPACE + str(totalMemory) + "K Memory"


def GetFreeMemory():

    global freeMemoryMessage

    freeMemoryStart = PROGRAM_CODE_MEMORY_START

    for memoryPointer in range(PROGRAM_CODE_MEMORY - 1, PROGRAM_CODE_MEMORY_START, -1):

        memoryLocation = programCode[memoryPointer]

        if memoryLocation == EMPTY_STRING:

            freeMemoryStart = memoryPointer

    memoryTopBytes = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * PROGRAM_CODE_MEMORY

    memoryBottomBytes = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * freeMemoryStart

    freeMemory = memoryTopBytes - memoryBottomBytes

    freeMemoryMessage = CHR_SPACE + CHR_SPACE + CHR_SPACE + str(freeMemory) + " Bytes Free"


def Ready():

    global subroutine

    ErrorHandler()

    # goto GetInput
    subroutine = "GetInput"


def GetInput():

    global subroutine, Zs

    if dataInput:

        DataInput()

    else:

        CodeInput()

        OnScreen()

        if Zs != EMPTY_STRING:

            Zs = Zs + CHR_END_OF_LINE


def OnScreen():

    global Zs, subroutine

    if Zs == EMPTY_STRING:

        subroutine = "Ready"

    else:

        WriteTextToConsole(">" + Zs, CRLF)

        subroutine = "AutoRun"


def CodeInput():

    global Zs

    WriteTextToConsole(">", not CRLF)

    Zs = input()


def DataInput():

    global N_numericData
    global dataInput
    global subroutine

    WriteTextToConsole("?", not CRLF)

    N_numericData = input()

    A_processorStack.insert(V_variableStackPointer, N_numericData)

    dataInput = False

    subroutine = "FinishStatement"


def AutoRun():

    global programCode
    global tempB, C_characterPointer, E_errorLineNumber, L_programCodeMemoryPointer
    global N_numericData, lineNumber
    global character, subroutine, errorMessage

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_WORKSPACE

    C_characterPointer = 0

    programCode.insert(L_programCodeMemoryPointer, Zs)

    GetNumber()

    lineNumber = N_numericData

    E_errorLineNumber = N_numericData

    if lineNumber == 0:

        if character == EMPTY_STRING:

            subroutine = "Ready"

        else:

            subroutine = "NextStatement"

        return

    if lineNumber > 0:

        EnterLine()

        if errorMessage != EMPTY_STRING:

            subroutine = "Ready"

            return

        subroutine = "GetInput"

        return

    if lineNumber < 0:

        E_errorLineNumber = 0

        ErrorMessage(ERROR_CODE_INVALID_LINE_NUMBER, ERROR_MESSAGE_INVALID_LINE_NUMBER)

        subroutine = "Ready"

        return

    subroutine = "Exec"


def Exec():

    global E_errorLineNumber, N_numericData
    global subroutine

    GetNumber()

    E_errorLineNumber = N_numericData

    subroutine = "NextStatement"


def NextStatement():

    global tempT, C_characterPointer, N_numericData, V_variableStackPointer, gosubStackPointer
    global Ds, character, subroutine, errorMessage

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    if Ds == "IF" or Ds == "if":

        TinyBasic_If()

        return

    if Ds == "REM" or Ds == "rem":

        TinyBasic_Rem()

        return

    if Ds == "INPUT" or Ds == "input":

        TinyBasic_Input()

        return

    if Ds == "PRINT" or Ds == "print":

        TinyBasic_Print()

        return

    if Ds == "CLEAR" or Ds == "clear":

        TinyBasic_Clear()

        return

    if Ds == "RUN" or Ds == "run":

        gosubStackPointer = -1

        TinyBasic_Run()

        return

    if Ds == "GOTO" or Ds == "goto":

        TinyBasic_Goto()

        return

    if Ds == "GOSUB" or Ds == "gosub":

        TinyBasic_Gosub()

        return

    if Ds == "RETURN" or Ds == "return":

        TinyBasic_Return()

        return

    if Ds == "NEW" or Ds == "new":

        TinyBasic_New()

        return

    if Ds == "CLS" or Ds == "cls":

        TinyBasic_Cls()

        return

    if Ds == "HELP" or Ds == "help":

        TinyBasic_Help()

        return

    if Ds == "MEM" or Ds == "mem":

        TinyBasic_Mem()

        return

    if Ds == "END" or Ds == "end":

        TinyBasic_End()

        return

    if Ds == "STOP" or Ds == "stop":

        TinyBasic_Stop()

        return

    if Ds == "LIST" or Ds == "list":

        TinyBasic_List()

        return

    if Ds == "SAVE" or Ds == "save":

        # TinyBasic_Save()

        return

    if Ds == "LOAD" or Ds == "load":

        # TinyBasic_Load()

        return

    if Ds == "LET" or Ds == "let":

        TinyBasic_Let()

    ReturnVar()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    SkipSpace()

    GetChar()

    if character != OpCodes.OP_EQUALS:

        ErrorMessage(ERROR_CODE_EQUALS_EXPECTED, ERROR_MESSAGE_EQUALS_EXPECTED)

        subroutine = "Ready"

        return

    C_characterPointer = C_characterPointer + 1

    stackPointer = V_variableStackPointer

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    A_processorStack.insert(stackPointer, N_numericData)

    subroutine = "FinishStatement"


def FinishStatement():

    global C_characterPointer, L_programCodeMemoryPointer
    global character, subroutine

    SkipSpace()

    GetChar()

    if character == CHR_COLON:

        C_characterPointer = C_characterPointer + 1

        subroutine = "NextStatement"

        return

    else:

        if character == EMPTY_STRING or character == CHR_END_OF_LINE:

            ErrorMessage(ERROR_CODE_END_OF_STATEMENT_EXPECTED, ERROR_MESSAGE_END_OF_STATEMENT_EXPECTED)

            subroutine = "Ready"

            return

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY_WORKSPACE:

        subroutine = "Ready"

        return

    L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

    C_characterPointer = 0

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY:

        ErrorMessage(ERROR_CODE_PROGRAM_OVERFLOW, ERROR_MESSAGE_PROGRAM_OVERFLOW)

        subroutine = "Ready"

        return

    subroutine = "FinishStatement2"


def FinishStatement2():

    global programCode
    global L_programCodeMemoryPointer
    global Bs, subroutine

    if programCode[L_programCodeMemoryPointer] == EMPTY_STRING:

        subroutine = "Ready"

        return

    subroutine = "Exec"


def EnterLine():

    global tempT, N_numericData, C_characterPointer, L_programCodeMemoryPointer

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    C_characterPointer = 0

    tempT = N_numericData

    NextLine()


def NextLine():

    global programCode
    global tempI, tempB, tempT, N_numericData, C_characterPointer, L_programCodeMemoryPointer
    global Zs

    nextLine = True

    while nextLine:

        GetNumber()

        isNextLine = (N_numericData < tempT) and (N_numericData != 0) and (L_programCodeMemoryPointer < PROGRAM_CODE_MEMORY + 1)

        if isNextLine:

            L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

            C_characterPointer = 0

            # goto NextLine
            nextLine = True

        else:

            nextLine = False

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY:

        ErrorMessage(ERROR_CODE_PROGRAM_OVERFLOW, ERROR_MESSAGE_PROGRAM_OVERFLOW)

        return

    if tempT != N_numericData:

        for tempI in range(PROGRAM_CODE_MEMORY - 1, L_programCodeMemoryPointer, -1):

            programCode.insert(tempI, programCode[tempI - 1])

    programCode.insert(L_programCodeMemoryPointer, Zs)

    SkipSpace()

    if character == EMPTY_STRING or character == CHR_END_OF_LINE:

        for tempI in range(L_programCodeMemoryPointer, PROGRAM_CODE_MEMORY):

            programCode.insert(tempI, programCode[tempI + 1])


def GetExpression():

    global A_processorStack
    global N_numericData, S_processorStackPointer

    S_processorStackPointer = PROCESSOR_STACK_MEMORY_START

    A_processorStack.insert(S_processorStackPointer, 0)

    BoolExpression()

    N_numericData = A_processorStack[S_processorStackPointer]


def BoolExpression():

    AddExpression()

    SkipSpace()

    GetChar()

    NextBool()


def NextBool():

    global character

    nextBool = True

    while nextBool:

        if character == OpCodes.OP_EQUALS:

            TinyBasic_Equals()

        if character == OpCodes.OP_GREATER_THAN:

            TinyBasic_Greater_Than()

        if character == OpCodes.OP_LESS_THAN:

            TinyBasic_Less_Than()

        SkipSpace()

        GetChar()

        asciiCode = ord(character)

        nextBool = (asciiCode >= ASC_LESS_THAN) and (asciiCode <= ASC_GREATER_THAN)


def AddExpression():

    MulExpression()

    SkipSpace()

    GetChar()

    NextAdd()


def NextAdd():

    global character

    nextAdd = True

    while nextAdd:

        if character == OpCodes.OP_ADD:

            TinyBasic_Add()

        if character == OpCodes.OP_SUBTRACT:

            TinyBasic_Subtract()

        SkipSpace()

        GetChar()

        asciiCode = ord(character)

        nextAdd = (asciiCode == ASC_PLUS) or (asciiCode == ASC_MINUS)


def MulExpression():

    GroupExpression()

    SkipSpace()

    GetChar()

    NextMul()


def NextMul():

    global character

    nextMul = True

    while nextMul:

        if character == OpCodes.OP_MULTIPLY:

            TinyBasic_Multiply()

        if character == OpCodes.OP_DIVIDE:

            TinyBasic_Divide()

        if character == OpCodes.OP_MODULUS:

            TinyBasic_Modulus()

        SkipSpace()

        GetChar()

        asciiCode = ord(character)

        nextMul = (asciiCode == ASC_ASTERISK) or (asciiCode == ASC_FORWARD_SLASH) or (asciiCode == ASC_BACK_SLASH)


def GroupExpression():

    global A_processorStack
    global tempB, N_numericData, C_characterPointer, S_processorStackPointer
    global character, errorMessage

    SkipSpace()

    GetChar()

    #  "("
    if character == OpCodes.OP_LEFT_PARENTHESIS:

        C_characterPointer = C_characterPointer + 1

        BoolExpression()

        SkipSpace()

        GetChar()

        # ")"
        if character != OpCodes.OP_RIGHT_PARENTHESIS:

            if errorMessage == EMPTY_STRING:

                ErrorMessage(ERROR_CODE_MISSING_RIGHT_PARENTHESIS, ERROR_MESSAGE_MISSING_RIGHT_PARENTHESIS)

            return

        C_characterPointer = C_characterPointer + 1

        return

    if character == EMPTY_STRING or character == CHR_END_OF_LINE:  # "":

        if errorMessage == EMPTY_STRING:

            ErrorMessage(ERROR_CODE_INVALID_FACTOR, ERROR_MESSAGE_INVALID_FACTOR)

        return

    # otherwise / else
    # else:

    asciiCode = ord(character)

    tempB = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_MINUS) and (asciiCode != ASC_DECIMAL_POINT)

    if tempB:

        GetNumber()

        if errorMessage != EMPTY_STRING:

            return

        S_processorStackPointer = S_processorStackPointer + 1

        A_processorStack.insert(S_processorStackPointer, N_numericData)

    else:

        GetLabel()

        if errorMessage != EMPTY_STRING:

            return

        if len(Ds) == 1:

            ReturnVar()

            S_processorStackPointer = S_processorStackPointer + 1

            A_processorStack.insert(S_processorStackPointer, A_processorStack[V_variableStackPointer])

        else:

            if Ds == "ticks":

                S_processorStackPointer = S_processorStackPointer + 1

                A_processorStack.insert(S_processorStackPointer, 0)  # TICKS)

                return

            if Ds == "tickspersec":

                S_processorStackPointer = S_processorStackPointer + 1

                A_processorStack.insert(S_processorStackPointer, 1)  # = TICKSPERSEC

                return

            if errorMessage == EMPTY_STRING:

                ErrorMessage(ERROR_CODE_FUNCTION_EXPECTED, ERROR_MESSAGE_FUNCTION_EXPECTED)


def GetNumber():

    global tempA, tempB, C_characterPointer
    global Bs, character, errorMessage

    SkipSpace()

    GetChar()

    tempA = 0

    if character == OpCodes.OP_MINUS:

        Bs = OpCodes.OP_MINUS

        C_characterPointer = C_characterPointer + 1

        GetChar()

        asciiCode = ord(character)

        isValidNumber = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_DECIMAL_POINT)

        if isValidNumber:

            if errorMessage == EMPTY_STRING:

                ErrorMessage(ERROR_CODE_INVALID_NUMBER, ERROR_MESSAGE_INVALID_NUMBER)

            return

    else:

        Bs = EMPTY_STRING

    NextNumber()


def NextNumber():

    global tempA, tempB, N_numericData, C_characterPointer
    global Bs, character

    nextNumber = True

    tempA = 0

    while nextNumber:

        if character == EMPTY_STRING or character == CHR_END_OF_LINE:

            GetNumberCalc()

            nextNumber = False

        if nextNumber:

            asciiCode = ord(character)

            if asciiCode == ASC_DECIMAL_POINT:

                tempA = tempA + 1

                if tempA > 1:

                    if errorMessage == EMPTY_STRING:

                        ErrorMessage(ERROR_CODE_INVALID_NUMBER, ERROR_MESSAGE_INVALID_NUMBER)

                    nextNumber = False

        if nextNumber:

            isSpace = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_DECIMAL_POINT)

            if isSpace:

                GetNumberCalc()

                nextNumber = False

        if nextNumber:

            Bs = Bs + character

            C_characterPointer = C_characterPointer + 1

            GetChar()


def GetNumberCalc():

    global N_numericData
    global Bs

    if Bs == EMPTY_STRING:

        N_numericData = 0

    else:

        N_numericData = int(Bs)


def GetVar():

    global errorMessage

    GetLabel()

    if errorMessage != EMPTY_STRING:

        return

    ReturnVar()


def ReturnVar():

    global tempA, V_variableStackPointer
    global Ds, errorMessage

    asciiCode = ord(Ds)

    # tempA = len(Ds)
    variableNameLength = len(Ds)

    isValidVariable = (variableNameLength == 1) and (asciiCode >= ASC_LOWERCASE_A) and (asciiCode <= ASC_LOWERCASE_Z)

    if isValidVariable:

        V_variableStackPointer = asciiCode - 70

    else:

        if errorMessage == EMPTY_STRING:

            ErrorMessage(ERROR_CODE_VARIABLE_EXPECTED, ERROR_MESSAGE_VARIABLE_EXPECTED)


def GetLabel():

    global tempB
    global Ds, character, errorMessage

    SkipSpace()

    GetChar()

    Ds = EMPTY_STRING

    asciiCharacter = ord(character)

    if character == EMPTY_STRING or asciiCharacter == CHR_END_OF_LINE:

        if errorMessage == EMPTY_STRING:

            ErrorMessage(ERROR_CODE_INVALID_LABEL, ERROR_MESSAGE_INVALID_LABEL)

        return

    asciiCode = ord(character)

    tempB = (asciiCode < ASC_LOWERCASE_A) or (asciiCode > ASC_LOWERCASE_Z)

    if tempB:

        if errorMessage == EMPTY_STRING:

            ErrorMessage(ERROR_CODE_INVALID_LABEL, ERROR_MESSAGE_INVALID_LABEL)

        return

    GetNextLabel()


def GetNextLabel():

    global C_characterPointer
    global Ds, character

    getNextLabel = True

    while getNextLabel:

        Ds = Ds + character

        C_characterPointer = C_characterPointer + 1

        GetChar()

        if character == EMPTY_STRING or character == CHR_END_OF_LINE:  # "":

            # return
            break

        asciiCode = ord(character)

        getNextLabel = (asciiCode >= ASC_LOWERCASE_A) and (asciiCode <= ASC_LOWERCASE_Z)


def SkipSpace():

    global C_characterPointer
    global character

    GetChar()

    while character == CHR_SPACE:

        C_characterPointer = C_characterPointer + 1

        GetChar()


def GetChar():

    global programCode
    global C_characterPointer
    global As, character

    As = programCode[L_programCodeMemoryPointer]

    character = As[C_characterPointer:C_characterPointer + 1]


# **** support routines ****
def NextChar():

    global C_characterPointer
    global Bs, subroutine, character

    C_characterPointer = C_characterPointer + 1

    character = As[C_characterPointer:1]

    asciiCharacter = chr(character)

    asciiCode = ord(asciiCharacter)

    if character == CHR_END_OF_LINE:  # "":

        ErrorMessage(ERROR_CODE_UNTERMINATED_STRING, ERROR_MESSAGE_UNTERMINATED_STRING)

        # GOTO Ready
        subroutine = "Ready"

        return

    else:

        if character != CHR_DOUBLE_QUOTE:

            Bs = Bs + character

            # GOTO NextChar
            subroutine = "NextChar"

            return

    C_characterPointer = C_characterPointer + 1

    character = As[C_characterPointer:1]

    if character == CHR_DOUBLE_QUOTE:

        Bs = Bs + character

        # GOTO NextChar
        subroutine = "NextChar"

        return

    WriteTextToConsole(Bs)  # ;

    subroutine = "EndPrint"


def EndPrint():

    global C_characterPointer
    global subroutine

    SkipSpace()

    GetChar()

    if character == CHR_COMMA:

        C_characterPointer = C_characterPointer + 1

        TinyBasic_Print()

        return

    SkipSpace()

    GetChar()

    if character != CHR_SEMI_COLON:

        WriteTextToConsole(EMPTY_STRING)

    else:

        C_characterPointer = C_characterPointer + 1

    subroutine = "FinishStatement"


def WriteTextToConsole(text, crlf):

    text = ConvertToUppercase(text)

    if crlf:

        print(text)

    else:

        print(text)


def ConvertToUppercase(textStringToConvert):

    global tempI
    global character

    for tempI in range(0, len(textStringToConvert)):

        # get character to convert
        character = textStringToConvert[tempI:1]

        # check if character is lowercase
        if character >= "a" and character <= "z":

            # it is, so convert it
            # get code for character - offset 'A'
            asciiCode = ord(character) - ord("a")

            # add value to offset for 'A'
            textStringToConvert[tempI:1] = chr(ord("A") + asciiCode)

    return textStringToConvert


# **** error handler ****
def ErrorMessage(code, message):

    global errorMessage, errorCode

    if errorMessage == EMPTY_STRING:

        errorCode = code

        errorMessage = message


def ErrorHandler():

    global errorMessage, errorCode

    if errorMessage != EMPTY_STRING:

        if E_errorLineNumber > 0 and errorCode == ERROR_CODE_STOP:

            errorMessage = errorMessage + " at line " + str(E_errorLineNumber)

            DisplayErrorMessage()

            return

        if E_errorLineNumber > 0:

            errorMessage = "Error in line " + str(E_errorLineNumber) + ": " + errorMessage

        else:

            errorMessage = "Error: " + errorMessage

        DisplayErrorMessage()


def DisplayErrorMessage():

    global subroutine, errorMessage

    WriteTextToConsole(EMPTY_STRING, CRLF)

    WriteTextToConsole(errorMessage, CRLF)

    errorMessage = EMPTY_STRING


# **** tiny basic commands ****
def TinyBasic_If():

    global C_characterPointer
    global Bs, subroutine

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    # N<1 THEN
    if N_numericData < 1:

        Bs = programCode[L_programCodeMemoryPointer]

        C_characterPointer = len(Bs) - 1

        subroutine = "FinishStatement"

        return

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    if Ds != "THEN" and Ds != "then":

        ErrorMessage(ERROR_CODE_THEN_EXPECTED, ERROR_MESSAGE_THEN_EXPECTED)

        subroutine = "Ready"

        return

    subroutine = "NextStatement"


def TinyBasic_Rem():

    global C_characterPointer
    global Bs, subroutine

    Bs = programCode[L_programCodeMemoryPointer]

    C_characterPointer = len(Bs) - 1

    subroutine = "FinishStatement"


def TinyBasic_Clear():

    global tempI
    global subroutine

    for tempI in range(VARIABLE_STACK_MEMORY_START, VARIABLE_STACK_MEMORY_START + VARIABLE_STACK_MEMORY):

        A_processorStack.insert(tempI, 0)

    subroutine = "FinishStatement"


def TinyBasic_Input():

    global N_numericData
    global dataInput
    global subroutine

    GetVar()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    dataInput = True

    subroutine = "GetInput"


def TinyBasic_Print():

    global Bs, subroutine

    if character == CHR_END_OF_LINE:

        WriteTextToConsole(EMPTY_STRING, CRLF)

        subroutine = "FinishStatement"

        return

    SkipSpace()

    GetChar()

    if character == CHR_DOUBLE_QUOTE:

        Bs = EMPTY_STRING

        subroutine = "NextChar"

        return

    else:

        GetExpression()

        if errorMessage != EMPTY_STRING:

            subroutine = "Ready"

            return

    WriteTextToConsole(str(N_numericData), not CRLF)  # ;

    subroutine = "EndPrint"


def TinyBasic_Run():

    global C_characterPointer, L_programCodeMemoryPointer, gosubStackPointer
    global subroutine

    TinyBasic_Clear()

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    gosubStackPointer = -1

    C_characterPointer = 0

    subroutine = "FinishStatement2"


def TinyBasic_Goto():

    global tempT, C_characterPointer, L_programCodeMemoryPointer
    global subroutine

    GetExpression()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    if E_errorLineNumber >= N_numericData:

        L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    C_characterPointer = 0

    tempT = N_numericData

    NextGoto()


def NextGoto():

    global C_characterPointer, E_errorLineNumber, L_programCodeMemoryPointer
    global subroutine

    nextGoto = True

    while nextGoto:

        GetNumber()

        if N_numericData == tempT:

            E_errorLineNumber = N_numericData

            nextGoto = False

            subroutine = "NextStatement"

        else:

            L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

            C_characterPointer = 0

            if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY:

                nextGoto = False

                ErrorMessage(ERROR_CODE_LINE_NOT_FOUND, ERROR_MESSAGE_LINE_NOT_FOUND)

                subroutine = "Ready"


def TinyBasic_Gosub():

    global gosubStackPointer
    global subroutine

    if gosubStackPointer < GOSUB_STACK_MEMORY:

        gosubStackPointer = gosubStackPointer + 1

        gosubLineNumberPointer.insert(gosubStackPointer, L_programCodeMemoryPointer)

        returnLineNumberPointer.insert(gosubStackPointer, L_programCodeMemoryPointer + 1)

        TinyBasic_Goto()

    else:

        ErrorMessage(ERROR_CODE_GOSUB_STACK_OVERFLOW, ERROR_MESSAGE_GOSUB_STACK_OVERFLOW)

        subroutine = "Ready"


def TinyBasic_Return():

    global tempI, gosubStackPointer, L_programCodeMemoryPointer, E_errorLineNumber, C_characterPointer
    global subroutine

    if gosubStackPointer < 0:

        ErrorMessage(ERROR_CODE_RETURN_WITHOUT_GOSUB, ERROR_MESSAGE_RETURN_WITHOUT_GOSUB)

        subroutine = "Ready"

        return

    for tempI in range(0, gosubStackPointer):

        L_programCodeMemoryPointer = gosubLineNumberPointer[tempI]

        canReturn = True

        while canReturn:

            GetNumber()

            if L_programCodeMemoryPointer == returnLineNumberPointer[tempI]:

                E_errorLineNumber = N_numericData

                subroutine = "NextStatement"

                canReturn = False

                tempI = gosubStackPointer

            else:

                L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

                C_characterPointer = 0


def TinyBasic_New():

    global tempI, E_errorLineNumber
    global subroutine

    for tempI in range(PROGRAM_CODE_MEMORY_START, PROGRAM_CODE_MEMORY):

        programCode.insert(tempI, EMPTY_STRING)

    if E_errorLineNumber == 0:

        subroutine = "FinishStatement"

    else:

        subroutine = "Ready"


def TinyBasic_Cls():

    global subroutine

    # CLS

    subroutine = "FinishStatement"


def TinyBasic_Help():

    global subroutine

    for commands in range(0, COMMAND_HELP_MEMORY):

        WriteTextToConsole(commandHelp[commands], CRLF)

    subroutine = "FinishStatement"


def TinyBasic_Mem():

    global subroutine

    GetFreeMemory()

    WriteTextToConsole(freeMemoryMessage, CRLF)

    subroutine = "FinishStatement"


def TinyBasic_End():

    global subroutine

    subroutine = "Ready"


def TinyBasic_Stop():

    global subroutine

    ErrorMessage(ERROR_CODE_STOP, ERROR_MESSAGE_STOP)

    subroutine = "Ready"


def TinyBasic_List():

    global tempB, tempT, tempK, tempI, C_characterPointer, L_programCodeMemoryPointer
    global errorMessage, subroutine

    GetNumber()

    tempT = N_numericData

    tempK = L_programCodeMemoryPointer

    tempI = C_characterPointer

    if tempT == 0:

        GetLabel()

        if errorMessage == EMPTY_STRING:

            if Ds == "pause":

                tempI = C_characterPointer

        errorMessage = EMPTY_STRING

    for L_programCodeMemoryPointer in range(PROGRAM_CODE_MEMORY_START, PROGRAM_CODE_MEMORY):

        C_characterPointer = 0

        GetNumber()

        tempB = (tempT == 0) or (N_numericData == tempT)

        if tempB:

            if programCode[L_programCodeMemoryPointer] != EMPTY_STRING:

                code = programCode[L_programCodeMemoryPointer]

                WriteTextToConsole(code, CRLF)

                if Ds == "pause":

                    tempB = (L_programCodeMemoryPointer - PROGRAM_CODE_MEMORY_WORKSPACE) % 10

                    if tempB == 0:

                        WriteTextToConsole("Pause...", not CRLF)

                        # WAIT

    L_programCodeMemoryPointer = tempK

    C_characterPointer = tempI

    subroutine = "FinishStatement"


def TinyBasic_Save():

    global tempI, file
    global Bs, fileName, subroutine

    # GOSUB GetExpression

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    # A$ = "tinyBas" + STR$(N)
    fileName = input("Filename: ")

    fileName = fileName + FILE_EXTENSION

    file = open(fileName, "a")

    for tempI in range(PROGRAM_CODE_MEMORY_START, PROGRAM_CODE_MEMORY):

        Bs = programCode[tempI]

        if Bs != "":

            file.write(Bs)

            # tempA = TRUE

    file.close()

    subroutine = "FinishStatement"


def TinyBasic_Load():

    global tempI, file
    global Bs, fileName, subroutine

    # GOSUB GetExpression

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    # A$ = "tinyBas" + STR$(N)
    fileName = input("Filename: ")

    fileName = fileName + FILE_EXTENSION

    file = open(fileName, "r")

    if file == FILE_NOT_FOUND:

        ErrorMessage(ERROR_CODE_FILE_NOT_FOUND, ERROR_MESSAGE_FILE_NOT_FOUND)

        subroutine = "Ready"

        return

    tempI = PROGRAM_CODE_MEMORY_START

    endOfFile = False

    # while NOT endOfFile

    # endOfFile = EOF#(file)

    file.readline(Bs)

    programCode.insert(tempI, Bs)

    tempI = tempI + 1

    file.close()

    while tempI <= PROGRAM_CODE_MEMORY:

        programCode.insert(tempI, EMPTY_STRING)

        tempI = tempI + 1

    if E_errorLineNumber == 0:

        subroutine = "FinishStatement"

        return

    subroutine = "Ready"


def TinyBasic_Let():

    global subroutine

    GetLabel()

    if errorMessage != EMPTY_STRING:

        subroutine = "Ready"


# **** tiny basic conditional operators ****
def TinyBasic_Equals():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AddExpression()

    condition = A_processorStack[S_processorStackPointer - 1] == A_processorStack[S_processorStackPointer]

    A_processorStack.insert(S_processorStackPointer - 1, condition)

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Greater_Than():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GetChar()

    # >=
    if character == OpCodes.OP_EQUALS:

        TinyBasic_Greater_Than_Equal_To()

    else:

        AddExpression()

        condition = A_processorStack[S_processorStackPointer - 1] > A_processorStack[S_processorStackPointer]

        A_processorStack.insert(S_processorStackPointer - 1, condition)

        S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Greater_Than_Equal_To():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AddExpression()

    condition = A_processorStack[S_processorStackPointer - 1] >= A_processorStack[S_processorStackPointer]

    A_processorStack.insert(S_processorStackPointer - 1, condition)

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Less_Than():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GetChar()

    # <=
    if character == OpCodes.OP_EQUALS:

        TinyBasic_Less_Than_Equal_To()

    # !=
    elif character == OpCodes.OP_GREATER_THAN:

        TinyBasic_Not_Equal_To()

    # otherwise / else
    else:

        AddExpression()

        condition = A_processorStack[S_processorStackPointer - 1] < A_processorStack[S_processorStackPointer]

        A_processorStack.insert(S_processorStackPointer - 1, condition)

        S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Less_Than_Equal_To():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AddExpression()

    condition = A_processorStack[S_processorStackPointer - 1] <= A_processorStack[S_processorStackPointer]

    A_processorStack.insert(S_processorStackPointer - 1, condition)

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Not_Equal_To():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AddExpression()

    condition = A_processorStack[S_processorStackPointer - 1] != A_processorStack[S_processorStackPointer]

    A_processorStack.insert(S_processorStackPointer - 1, condition)

    S_processorStackPointer = S_processorStackPointer - 1


# **** tiny basic math operators ****
def TinyBasic_Add():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    MulExpression()

    A_processorStack.insert(S_processorStackPointer - 1, A_processorStack[S_processorStackPointer - 1] + A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Subtract():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    MulExpression()

    A_processorStack.insert(S_processorStackPointer - 1, A_processorStack[S_processorStackPointer - 1] - A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Multiply():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GroupExpression()

    A_processorStack.insert(S_processorStackPointer - 1, A_processorStack[S_processorStackPointer - 1] * A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Divide():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GroupExpression()

    if A_processorStack[S_processorStackPointer] == 0:

        ErrorMessage(ERROR_CODE_DIVISION_BY_ZERO, ERROR_MESSAGE_DIVISION_BY_ZERO)

        S_processorStackPointer = S_processorStackPointer - 1

        return

    else:

        A_processorStack.insert(S_processorStackPointer - 1, A_processorStack[S_processorStackPointer - 1] / A_processorStack[S_processorStackPointer])

        S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Modulus():

    global tempB, C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GroupExpression()

    if A_processorStack[S_processorStackPointer] == 0:

        ErrorMessage(ERROR_CODE_DIVISION_BY_ZERO, ERROR_MESSAGE_DIVISION_BY_ZERO)

        S_processorStackPointer = S_processorStackPointer - 1

        return

    else:

        A_processorStack.insert(S_processorStackPointer - 1, A_processorStack[S_processorStackPointer - 1] % A_processorStack[S_processorStackPointer])

        S_processorStackPointer = S_processorStackPointer - 1


Start()
