#
# Tiny Basic Python Edition
#
# Mk2 v1
#
# v2022.12.02
#

# Loosely adapted from the original Tiny Basic
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
SPACE = " "
COLON = ":"
COMMA = ","
SEMI_COLON = ";"

LINE_NUMBER_PADDING = "     "

TAB_SPACING = "        "

# math/conditional operators
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

CHR_END_OF_LINE = chr(10)
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
ERROR_CODE_MEMORY_OVERFLOW = 8
ERROR_CODE_GOSUB_STACK_OVERFLOW = 188
ERROR_CODE_LINE_NOT_FOUND = 32
ERROR_CODE_MISSING_DOUBLE_QUOTE = 62
ERROR_CODE_NO_MATCHING_GOSUB = 133
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


# error messages
ERROR_MESSAGE_STOP = "STOP"
ERROR_MESSAGE_MEMORY_OVERFLOW = "MEMORY OVERFLOW"  # 8
ERROR_MESSAGE_GOSUB_STACK_OVERFLOW = "GOSUB STACK OVERFLOW"  # 188
ERROR_MESSAGE_LINE_NOT_FOUND = "LINE NOT FOUND"  # 32
ERROR_MESSAGE_MISSING_DOUBLE_QUOTE = "MISSING """  # 62
ERROR_MESSAGE_NO_MATCHING_GOSUB = "RETURN HAS NO MATCHING GOSUB"  # 133
ERROR_MESSAGE_END_OF_STATEMENT_EXPECTED = "END OF STATEMENT EXPECTED"
ERROR_MESSAGE_INVALID_FACTOR = "INVALID FACTOR"
ERROR_MESSAGE_INVALID_NUMBER = "INVALID NUMBER"
ERROR_MESSAGE_INVALID_LABEL = "INVALID LABEL"
ERROR_MESSAGE_INVALID_LINE_NUMBER = "INVALID LINE NUMBER"  # 9
ERROR_MESSAGE_FUNCTION_EXPECTED = "FUNCTION EXPECTED"
ERROR_MESSAGE_VARIABLE_EXPECTED = "VARIABLE EXPECTED"
ERROR_MESSAGE_EQUALS_EXPECTED = "= EXPECTED"  # 20
ERROR_MESSAGE_THEN_EXPECTED = "THEN EXPECTED"
ERROR_MESSAGE_SYNTAX_ERROR = "SYNTAX ERROR"
ERROR_MESSAGE_MISTAKE = "MISTAKE"
ERROR_MESSAGE_NO_SUCH_VARIABLE = "NO SUCH VARIABLE"
ERROR_MESSAGE_DIVISION_BY_ZERO = "DIVISION BY ZERO"  # 224
ERROR_MESSAGE_MISSING_RIGHT_PARENTHESIS = "MISSING )"  # 296


STRING_OBJECT_DATA_LENGTH = 20
BYTES_PER_CHARACTER_BUFFER = 2

PROGRAM_CODE_MEMORY_TOP = 125
PROGRAM_CODE_MEMORY_START = 27
PROGRAM_CODE_MEMORY_WORKSPACE = 26

VARIABLE_STACK_MEMORY_TOP = 53
VARIABLE_STACK_MEMORY_START = 27

# ACCUMULATOR_MEMORY_START = 54

PROCESSOR_STACK_MEMORY_TOP = 84
GOSUB_STACK_MEMORY_TOP = 26
COMMAND_HELP_MEMORY = 10
MAXIMUM_LINE_LENGTH = 72


programCode = []
commandHelp = []
A_processorStack = []
gosubLineNumberStack = []
returnLineNumberStack = []


welcomeMessage = ""
promptMessage = ""
totalMemoryMessage = ""
freeMemoryMessage = ""

subroutine = ""


A = 0
B = 0
C_characterPointer = 0
errorCode = 0
E_errorLineNumber = 0
L_programCodeMemoryPointer = 0
lineNumber = 0
N_numericData = 0
S_processorStackPointer = 0
T = 0
V_variableStackMemoryPointer = 0
gosubStackMemoryPointer = 0
asciiCode = 0

As_programCodeWorkspace = ""
Bs_stringData = ""
Cs_character = ""
Ds_statementLabel = ""
Es_errorMessage = ""
Zs_command = ""

fileName = ""

F = False
savingFile = False
loadingFile = False
fileNameOkay = False


def Start():

    Initialise()

    while True:

        if subroutine == "Ready":
            Ready()

        if subroutine == "EnterCommand":
            EnterCommand()

        if subroutine == "MakeItSo":
            MakeItSo()

        if subroutine == "Engage":
            Engage()

        if subroutine == "RunCommandInterpreter":
            RunCommandInterpreter()

        if subroutine == "FinishStatement":
            FinishStatement()
    
        if subroutine == "Print":
            TinyBasic_Print()

        if subroutine == "NextCharacter":
            NextCharacter()
    
        # WHEN "PrintBufferController" : PrintBufferController)
        # WHEN "GetString" : GetString)
        # WHEN "GetNumeric" : GetNumeric)
    
        # WHEN "Save" : SaveFile)
        # WHEN "Load" : LoadFile)


def Initialise():

    global subroutine

    ColdStart()
    WarmStart()

    print(welcomeMessage)
    print()

    GetTotalMemory()
    GetFreeMemory()

    print(totalMemoryMessage + freeMemoryMessage)
    print()
    print(promptMessage, end="")

    subroutine = "Ready"


def InitialiseCommandHelp():

    commandHelp.insert(0, "CLS, END")
    commandHelp.insert(1, "HELP, MEM, NEW, RUN")
    commandHelp.insert(2, "GOTO | GOSUB | LOAD | SAVE <exp>")
    commandHelp.insert(3, "if <exp> THEN <statement>")
    commandHelp.insert(4, "INPUT <var>")
    commandHelp.insert(5, "[LET] <var>=<exp>")
    commandHelp.insert(6, "LIST [<exp>|PAUSE]")
    commandHelp.insert(7, "print <exp|str>[,<exp|str>][;]")
    commandHelp.insert(8, "REM <any>")


def ColdStart():

    global programCode, A_processorStack, gosubLineNumberStack, returnLineNumberStack
    global welcomeMessage, promptMessage

    # [27-125] = 99 program lines
    # DIM A$(125)
    programCode = []

    # [27 - 53] = 26 variables
    # [54 - 84] = 30 items math stack
    A_processorStack = []

    # gosub stack
    gosubLineNumberStack = []
    returnLineNumberStack = []

    InitialiseCommandHelp()

    welcomeMessage = SPACE + "**** TINY BASIC PYTHON EDITION ****"
    promptMessage = "READY"


def WarmStart():

    global A, B, C_characterPointer, errorCode, E_errorLineNumber, L_programCodeMemoryPointer
    global lineNumber, N_numericData, S_processorStackPointer, T, V_variableStackMemoryPointer
    global gosubStackMemoryPointer, asciiCode

    global As_programCodeWorkspace, Bs_stringData, Cs_character
    global Ds_statementLabel, Es_errorMessage, fileName

    global savingFile, loadingFile, fileNameOkay

    for programCodePointer in range(PROGRAM_CODE_MEMORY_TOP + 1):

        programCode.insert(programCodePointer, EMPTY_STRING)

    for processorStackPointer in range(PROCESSOR_STACK_MEMORY_TOP):

        A_processorStack.insert(processorStackPointer, 0)

    for gosubStackPointer in range(GOSUB_STACK_MEMORY_TOP):

        gosubLineNumberStack.insert(gosubStackPointer, 0)

        returnLineNumberStack.insert(gosubStackPointer, 0)

    A = 0
    B = 0

    C_characterPointer = 0

    errorCode = 0
    E_errorLineNumber = 0

    L_programCodeMemoryPointer = 0

    lineNumber = 0

    N_numericData = 0

    S_processorStackPointer = 0

    T = 0

    V_variableStackMemoryPointer = 0

    gosubStackMemoryPointer = 0

    asciiCode = 0

    As_programCodeWorkspace = EMPTY_STRING
    Bs_stringData = EMPTY_STRING
    Cs_character = EMPTY_STRING
    Ds_statementLabel = EMPTY_STRING
    Es_errorMessage = EMPTY_STRING

    fileName = EMPTY_STRING

    savingFile = False
    loadingFile = False
    fileNameOkay = False


def GetTotalMemory():

    global totalMemoryMessage

    totalMemory = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * PROGRAM_CODE_MEMORY_TOP

    totalMemory = int(totalMemory / 1024)

    totalMemoryMessage = SPACE + str(totalMemory) + "K MEMORY"


def GetFreeMemory():

    global freeMemoryMessage

    freeMemoryStart = PROGRAM_CODE_MEMORY_START

    for memoryPointer in range(PROGRAM_CODE_MEMORY_TOP - 1, PROGRAM_CODE_MEMORY_START, -1):

        memoryLocation = programCode[memoryPointer]

        if memoryLocation == EMPTY_STRING:

            freeMemoryStart = memoryPointer

    memoryTopBytes = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * PROGRAM_CODE_MEMORY_TOP

    memoryBottomBytes = (STRING_OBJECT_DATA_LENGTH + MAXIMUM_LINE_LENGTH * BYTES_PER_CHARACTER_BUFFER) * freeMemoryStart

    freeMemory = memoryTopBytes - memoryBottomBytes

    freeMemoryMessage = "  " + str(freeMemory) + " BYTES FREE"


def Ready():

    global subroutine

    ErrorHandler()

    subroutine = "EnterCommand"


def EnterCommand():

    global Zs_command, subroutine

    Zs_command = input(">")

    if Zs_command == EMPTY_STRING:

        subroutine = "Ready"

    else:

        Zs_command = ConvertToUppercase(Zs_command)

        Zs_command = Zs_command + CHR_END_OF_LINE

        subroutine = "MakeItSo"


def MakeItSo():

    global L_programCodeMemoryPointer, C_characterPointer, E_errorLineNumber
    global lineNumber, subroutine

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_WORKSPACE

    C_characterPointer = 0

    programCode.insert(PROGRAM_CODE_MEMORY_WORKSPACE, Zs_command)

    GetNumber()

    lineNumber = N_numericData

    E_errorLineNumber = N_numericData

    if lineNumber == 0:

        if Cs_character == CHR_END_OF_LINE:

            subroutine = "Ready"

        else:

            subroutine = "RunCommandInterpreter"

            return

    if lineNumber > 0:

        EnterLine()

        subroutine = "Ready"

        return

    if lineNumber < 0:

        E_errorLineNumber = 0

        ErrorMessage(ERROR_CODE_INVALID_LINE_NUMBER, ERROR_MESSAGE_INVALID_LINE_NUMBER)

        subroutine = "Ready"

    else:

        subroutine = "Engage"


def Engage():
    
    global E_errorLineNumber, subroutine
    
    GetNumber()
    
    E_errorLineNumber = N_numericData
    
    subroutine = "RunCommandInterpreter"


def RunCommandInterpreter():
    
    global T, subroutine, C_characterPointer, gosubStackMemoryPointer
    
    GetStatementLabel()
    
    if Es_errorMessage != EMPTY_STRING:
        
        subroutine = "Ready"
        
        return 

    if Ds_statementLabel == "IF":

        TinyBasic_If()
        
        return
    
    if Ds_statementLabel == "REM":

        TinyBasic_Rem()

        return
    
    if Ds_statementLabel == "INPUT":

        TinyBasic_Input()

        return
    
    if Ds_statementLabel == "PRINT":

        TinyBasic_Print()

        return
    
    if Ds_statementLabel == "RUN":

        gosubStackMemoryPointer = -1

        TinyBasic_Run()

        return

    if Ds_statementLabel == "GOTO":

        TinyBasic_Goto()

        return

    if Ds_statementLabel == "GOSUB":

        TinyBasic_Gosub()

        return

    if Ds_statementLabel == "RETURN":

        TinyBasic_Return()

        return

    if Ds_statementLabel == "NEW":

        TinyBasic_New()

        return

    if Ds_statementLabel == "CLS":

        TinyBasic_Cls()

        return

    if Ds_statementLabel == "HELP":

        TinyBasic_Help()

        return

    if Ds_statementLabel == "MEM":

        TinyBasic_Mem()

        return

    if Ds_statementLabel == "END":

        TinyBasic_End()

        return

    if Ds_statementLabel == "STOP":

        TinyBasic_Stop()

        return

    if Ds_statementLabel == "LIST":

        TinyBasic_List()

        return

    if Ds_statementLabel == "SAVE":

        TinyBasic_Save()

        return

    if Ds_statementLabel == "LOAD":

        TinyBasic_Load()

        return

    if Ds_statementLabel == "LET":

        TinyBasic_Let()

    ReturnVariable()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    SkipSpace()

    GetCharacter()

    if Cs_character != OP_EQUALS:

        ErrorMessage(ERROR_CODE_EQUALS_EXPECTED, ERROR_MESSAGE_EQUALS_EXPECTED)

        subroutine = "Ready"

        return

    C_characterPointer = C_characterPointer + 1

    T = V_variableStackMemoryPointer

    GetExpression()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    A_processorStack.insert(T, N_numericData)

    subroutine = "FinishStatement"


def FinishStatement():

    global L_programCodeMemoryPointer, C_characterPointer, subroutine
    global Bs_stringData

    SkipSpace()

    GetCharacter()

    if Cs_character == COLON:

        C_characterPointer = C_characterPointer + 1

        subroutine = "RunCommandInterpreter"

        return

    if Cs_character != CHR_END_OF_LINE:

        ErrorMessage(ERROR_CODE_END_OF_STATEMENT_EXPECTED, ERROR_MESSAGE_END_OF_STATEMENT_EXPECTED)

        subroutine = "Ready"

        return

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY_WORKSPACE:

        subroutine = "Ready"

        return

    L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

    C_characterPointer = 0

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY_TOP + 1:

        ErrorMessage(ERROR_CODE_MEMORY_OVERFLOW, ERROR_MESSAGE_MEMORY_OVERFLOW)

        subroutine = "Ready"

        return

    Bs_stringData = programCode[L_programCodeMemoryPointer]

    if Bs_stringData == EMPTY_STRING:

        subroutine = "Ready"

    else:

        subroutine = "Engage"


def EnterLine():
    
    global B, F, T, L_programCodeMemoryPointer, C_characterPointer

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    C_characterPointer = 0

    T = N_numericData

    # (NextLine)

    canLoop = True

    # REPEAT
    while canLoop:

        GetNumber()

        F = (N_numericData < T) and (N_numericData != 0) and (L_programCodeMemoryPointer < PROGRAM_CODE_MEMORY_TOP + 1)

        if F:

            L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

            C_characterPointer = 0

        else:

            canLoop = False

    # UNTIL F = FALSE

    if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY_TOP + 1:

        ErrorMessage(ERROR_CODE_MEMORY_OVERFLOW, ERROR_MESSAGE_MEMORY_OVERFLOW)

        return

    if T != N_numericData:

        for i in range(PROGRAM_CODE_MEMORY_TOP, L_programCodeMemoryPointer, -1):

            B = i - 1

            programCode.insert(i, programCode[B])

    programCode.insert(L_programCodeMemoryPointer, Zs_command)

    GetCharacter()

    if Cs_character == CHR_END_OF_LINE:

        for i in range(L_programCodeMemoryPointer, PROGRAM_CODE_MEMORY_TOP - 1):

            B = i + 1

            programCode.insert(i, programCode[B])


def GetExpression():
    
    global S_processorStackPointer, N_numericData

    S_processorStackPointer = VARIABLE_STACK_MEMORY_TOP  # ACCUMULATOR_MEMORY_START

    A_processorStack.insert(S_processorStackPointer, 0)

    BoolExpression()

    N_numericData = A_processorStack[S_processorStackPointer]


def BoolExpression():

    global F, asciiCode

    AdditionSubtractionExpression()

    SkipSpace()

    GetCharacter()

    # (NextBool)

    canLoop = True

    # REPEAT
    while canLoop:

        if Cs_character == OP_EQUALS:

            TinyBasic_Equals()

        if Cs_character == OP_GREATER_THAN:

            TinyBasic_Greater_Than()

        if Cs_character == OP_LESS_THAN:

            TinyBasic_Less_Than()

        SkipSpace()

        GetCharacter()

        asciiCode = ord(Cs_character)

        F = (asciiCode >= ASC_LESS_THAN) and (asciiCode <= ASC_GREATER_THAN)

        if not F:

            canLoop = False

    # UNTIL F = FALSE


def AdditionSubtractionExpression():

    global F, asciiCode

    MultiplyDivideModulusExpression()
    
    SkipSpace()
    
    GetCharacter()

    # (NextAdditionSubraction)

    canLoop = True

    # REPEAT
    while canLoop:

        if Cs_character == OP_PLUS:

            TinyBasic_Add()

        if Cs_character == OP_MINUS:

            TinyBasic_Subtract()

        SkipSpace()

        GetCharacter()

        asciiCode = ord(Cs_character)

        F = (asciiCode == ASC_PLUS) or (asciiCode == ASC_MINUS)

        if not F:

            canLoop = False

    # UNTIL F = FALSE


def MultiplyDivideModulusExpression():

    global F, asciiCode

    GroupExpression()

    SkipSpace()

    GetCharacter()

    # (NextMultiplyDivideModulus)

    canLoop = True

    # REPEAT
    while canLoop:

        if Cs_character == OP_MULTIPLY:

            TinyBasic_Multiply()

        if Cs_character == OP_DIVIDE:

            TinyBasic_Divide()

        if Cs_character == OP_MODULUS:

            TinyBasic_Modulus()

        SkipSpace()

        GetCharacter()

        asciiCode = ord(Cs_character)

        F = (asciiCode == ASC_ASTERISK) or (asciiCode == ASC_FORWARD_SLASH) or (asciiCode == ASC_PERCENT)

        if not F:

            canLoop = False

    # UNTIL F = FALSE


def GroupExpression():

    global B, F, C_characterPointer, S_processorStackPointer, asciiCode
    global Cs_character

    TICKS = 0
    TICKSPERSEC = 0

    SkipSpace()

    GetCharacter()

    if Cs_character == OP_LEFT_PARENTHESIS:

        C_characterPointer = C_characterPointer + 1

        BoolExpression()

        SkipSpace()

        GetCharacter()

        if Cs_character != OP_RIGHT_PARENTHESIS:

            ErrorMessage(ERROR_CODE_MISSING_RIGHT_PARENTHESIS, ERROR_MESSAGE_MISSING_RIGHT_PARENTHESIS)

            return

        C_characterPointer = C_characterPointer + 1

        return

    if Cs_character == CHR_END_OF_LINE:

        ErrorMessage(ERROR_CODE_INVALID_FACTOR, ERROR_MESSAGE_INVALID_FACTOR)

        return

    # ELSE
    asciiCode = ord(Cs_character)

    F = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_MINUS) and (asciiCode != ASC_DECIMAL_POINT)

    if not F:

        GetNumber()

        if Es_errorMessage != EMPTY_STRING:

            return

        S_processorStackPointer = S_processorStackPointer + 1

        A_processorStack.insert(S_processorStackPointer, N_numericData)

    else:

        GetStatementLabel()

        if Es_errorMessage != EMPTY_STRING:

            return

        B = len(Ds_statementLabel)

        if B == 1:

            ReturnVariable()

            S_processorStackPointer = S_processorStackPointer + 1

            A_processorStack.insert(S_processorStackPointer, A_processorStack[V_variableStackMemoryPointer])

        else:

            if Ds_statementLabel == "ticks":

                S_processorStackPointer = S_processorStackPointer + 1

                A_processorStack.insert(S_processorStackPointer, TICKS)

                return

            if Ds_statementLabel == "tickspersec":

                S_processorStackPointer = S_processorStackPointer + 1

                A_processorStack.insert(S_processorStackPointer, TICKSPERSEC)

                return

            ErrorMessage(ERROR_CODE_FUNCTION_EXPECTED, ERROR_MESSAGE_FUNCTION_EXPECTED)


def GetNumber():

    global F, C_characterPointer, asciiCode
    global Bs_stringData

    SkipSpace()

    GetCharacter()

    decimalPlaces = 0

    if Cs_character == OP_MINUS:

        Bs_stringData = OP_MINUS

        C_characterPointer = C_characterPointer + 1

        GetCharacter()

        asciiCode = ord(Cs_character)

        print(asciiCode)

        F = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_DECIMAL_POINT)

        if F:

            ErrorMessage(ERROR_CODE_INVALID_NUMBER, ERROR_MESSAGE_INVALID_NUMBER)

            return

    else:

        Bs_stringData = EMPTY_STRING

    # (NextNumber)

    canLoop = True

    # REPEAT
    while canLoop:

        asciiCode = ord(Cs_character)

        if asciiCode == ASC_DECIMAL_POINT:

            decimalPlaces = decimalPlaces + 1

        if decimalPlaces > 1:

            ErrorMessage(ERROR_CODE_INVALID_NUMBER, ERROR_MESSAGE_INVALID_NUMBER)

            return

        F = ((asciiCode < ASC_ZERO) or (asciiCode > ASC_NINE)) and (asciiCode != ASC_DECIMAL_POINT)

        if F:

            GetNumberCalc()

            return

        Bs_stringData = Bs_stringData + Cs_character

        C_characterPointer = C_characterPointer + 1

        GetCharacter()

    # UNTIL Cs_character$ = CHR_END_OF_LINE$

    GetNumberCalc()


def GetNumberCalc():

    global N_numericData

    N_numericData = int(Bs_stringData)


def GetVariable():

    GetStatementLabel()

    if Es_errorMessage != EMPTY_STRING:

        return

    ReturnVariable()


def ReturnVariable():

    global A, F, asciiCode, V_variableStackMemoryPointer

    asciiCode = ord(Ds_statementLabel)

    A = len(Ds_statementLabel)

    # F = (A != 1) OR (asciiCode < CHR_UPPERCASE_A) OR (asciiCode > CHR_UPPERCASE_Z)
    F = (A == 1) and (asciiCode >= ASC_UPPERCASE_A) and (asciiCode <= ASC_UPPERCASE_Z)

    if F:

        # [27 - 53]
        V_variableStackMemoryPointer = asciiCode - 38

    else:

        ErrorMessage(ERROR_CODE_VARIABLE_EXPECTED, ERROR_MESSAGE_VARIABLE_EXPECTED)


def GetStatementLabel():

    global F, C_characterPointer, asciiCode, subroutine
    global Ds_statementLabel

    SkipSpace()

    GetCharacter()

    Ds_statementLabel = EMPTY_STRING

    # if Cs_character$ = "" THEN
    if Cs_character == CHR_END_OF_LINE:

        ErrorMessage(ERROR_CODE_INVALID_LABEL, ERROR_MESSAGE_INVALID_LABEL)

        return

    asciiCode = ord(Cs_character)

    F = (asciiCode < ASC_UPPERCASE_A) or (asciiCode > ASC_UPPERCASE_Z)

    if F:

        ErrorMessage(ERROR_CODE_INVALID_LABEL, ERROR_MESSAGE_INVALID_LABEL)

        return

    GetNextLabel()


def GetNextLabel():

    global F, C_characterPointer, asciiCode
    global Ds_statementLabel

    canLoop = True

    # REPEAT
    while canLoop:

        Ds_statementLabel = Ds_statementLabel + Cs_character

        C_characterPointer = C_characterPointer + 1

        GetCharacter()

        # if Cs_character$ = "" THEN
        if Cs_character == CHR_END_OF_LINE:

            return

        asciiCode = ord(Cs_character)

        F = (asciiCode >= ASC_UPPERCASE_A) and (asciiCode <= ASC_UPPERCASE_Z)

        if not F:

            canLoop = False

    # UNTIL F = FALSE


def SkipSpace():

    global C_characterPointer, Cs_character

    GetCharacter()

    while Cs_character == SPACE:

        C_characterPointer = C_characterPointer + 1

        Cs_character = As_programCodeWorkspace[C_characterPointer]


def GetCharacter():

    global As_programCodeWorkspace, Cs_character

    As_programCodeWorkspace = programCode[L_programCodeMemoryPointer]

    Cs_character = As_programCodeWorkspace[C_characterPointer]


# tiny basic commands
def TinyBasic_If():

    global C_characterPointer, subroutine
    global Bs_stringData

    GetExpression()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    # if N < 1 THEN
    if N_numericData == 0:

        Bs_stringData = programCode[L_programCodeMemoryPointer]

        C_characterPointer = len(Bs_stringData)  # + 1

        subroutine = "FinishStatement"

        return

    GetStatementLabel()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    if Ds_statementLabel != "THEN":

        ErrorMessage(ERROR_CODE_THEN_EXPECTED, ERROR_MESSAGE_THEN_EXPECTED)

        subroutine = "Ready"

    else:

        subroutine = "RunCommandInterpreter"


def TinyBasic_Rem():

    global C_characterPointer, subroutine
    global Bs_stringData

    Bs_stringData = programCode[L_programCodeMemoryPointer]

    C_characterPointer = len(Bs_stringData)  # + 1

    subroutine = "FinishStatement"


def TinyBasic_Input():

    global N_numericData, subroutine

    GetVariable()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    N_numericData = input()

    A_processorStack.insert(V_variableStackMemoryPointer, int(N_numericData))

    subroutine = "FinishStatement"


def TinyBasic_Print():

    global C_characterPointer, subroutine
    global Bs_stringData

    SkipSpace()

    GetCharacter()

    if Cs_character == CHR_DOUBLE_QUOTE:

        Bs_stringData = EMPTY_STRING

        subroutine = "NextCharacter"

        return

    else:

        GetExpression()

        # if E$!="" GOTO _Ready
        if Es_errorMessage != EMPTY_STRING:

            subroutine = "Ready"

            return

        print(N_numericData)

    SkipSpace()

    GetCharacter()

    # if C$="," INC C : GOTO _Print
    if Cs_character == COLON:

        C_characterPointer = C_characterPointer + 1

        subroutine = "Print"

        return

    SkipSpace()

    GetCharacter()

    # if C$!=";" THEN
    if Cs_character != SEMI_COLON:

        print()

    else:

        C_characterPointer = C_characterPointer + 1

    subroutine = "FinishStatement"


def NextCharacter():

    global Cs_character, C_characterPointer, subroutine
    global Bs_stringData

    C_characterPointer = C_characterPointer + 1

    Cs_character = As_programCodeWorkspace[C_characterPointer]

    if Cs_character == CHR_END_OF_LINE:

        ErrorMessage(ERROR_CODE_MISSING_DOUBLE_QUOTE, ERROR_MESSAGE_MISSING_DOUBLE_QUOTE)

        subroutine = "Ready"

        return

    else:

        # if C$!=G$ THEN
        if Cs_character != CHR_DOUBLE_QUOTE:

            Bs_stringData = Bs_stringData + Cs_character

            # GOTO _NextChar
            subroutine = "NextCharacter"

            return

    C_characterPointer = C_characterPointer + 1

    Cs_character = As_programCodeWorkspace[C_characterPointer]

    # if C$=G$ THEN
    if Cs_character == CHR_DOUBLE_QUOTE:

        Bs_stringData = Bs_stringData + Cs_character

        # GOTO _NextChar
        subroutine = "NextCharacter"

        return

    print(Bs_stringData)


def TinyBasic_List():

    global B, F, T, C_characterPointer, L_programCodeMemoryPointer, subroutine
    global Es_errorMessage

    GetNumber()
    # N_numericData = FN_GetNumber

    T = N_numericData

    K = L_programCodeMemoryPointer

    J = C_characterPointer

    if T == 0:

        GetNextLabel()

        if Es_errorMessage == EMPTY_STRING:

            if Ds_statementLabel == "PAUSE":

                J = C_characterPointer

        Es_errorMessage = EMPTY_STRING

    for L_programCodeMemoryPointer in range(PROGRAM_CODE_MEMORY_START, PROGRAM_CODE_MEMORY_TOP):

        C_characterPointer = 0

        GetNumber()
        # N_numericData = FN_GetNumber

        F = (T == 0) or (N_numericData == T)

        if F:

            if As_programCodeWorkspace != EMPTY_STRING:

                lineNumberLength = len(str(N_numericData))

                lineNumberPadding = LINE_NUMBER_PADDING[:5 - lineNumberLength]

                # removes end of line character from string
                print(lineNumberPadding + As_programCodeWorkspace[:len(As_programCodeWorkspace) - 1])

                """
                if Ds_statementLabel == "PAUSE":

                    B = (L_programCodeMemoryPointer - PROGRAM_CODE_MEMORY_WORKSPACE) % 10

                    if B == 0:

                        # print("Pause...")

                        P = input("...")
                """

    L_programCodeMemoryPointer = K

    C_characterPointer = J

    subroutine = "FinishStatement"


def TinyBasic_Run():

    global L_programCodeMemoryPointer, C_characterPointer, subroutine

    # clear variable stack
    for i in range(VARIABLE_STACK_MEMORY_START, VARIABLE_STACK_MEMORY_TOP):

        A_processorStack.insert(i, 0)

    L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    C_characterPointer = 0

    # Bs_stringData$ = programCode$(L_programCodeMemoryPointer)

    if programCode[L_programCodeMemoryPointer] == EMPTY_STRING:

        subroutine = "Ready"

    else:

        subroutine = "Engage"


def TinyBasic_Goto():

    global T, L_programCodeMemoryPointer, C_characterPointer, subroutine

    GetExpression()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"

        return

    if E_errorLineNumber >= N_numericData:

        L_programCodeMemoryPointer = PROGRAM_CODE_MEMORY_START

    C_characterPointer = 0

    T = N_numericData

    GotoLineNumber()


def GotoLineNumber():

    global C_characterPointer, L_programCodeMemoryPointer, E_errorLineNumber, subroutine

    while True:

        if L_programCodeMemoryPointer > PROGRAM_CODE_MEMORY_TOP:

            ErrorMessage(ERROR_CODE_LINE_NOT_FOUND, ERROR_MESSAGE_LINE_NOT_FOUND)

            subroutine = "Ready"

            return

        GetNumber()

        if N_numericData == T:

            E_errorLineNumber = N_numericData

            subroutine = "RunCommandInterpreter"

            return

        L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

        C_characterPointer = 0


def TinyBasic_Gosub():

    global gosubStackMemoryPointer, subroutine

    if gosubStackMemoryPointer < GOSUB_STACK_MEMORY_TOP:

        gosubStackMemoryPointer = gosubStackMemoryPointer + 1

        gosubLineNumberStack.insert(gosubStackMemoryPointer, L_programCodeMemoryPointer)

        returnLineNumberStack.insert(gosubStackMemoryPointer, L_programCodeMemoryPointer + 1)

        TinyBasic_Goto()

    else:

        ErrorMessage(ERROR_CODE_GOSUB_STACK_OVERFLOW, ERROR_MESSAGE_GOSUB_STACK_OVERFLOW)

        subroutine = "Ready"


def TinyBasic_Return():

    global L_programCodeMemoryPointer, C_characterPointer, E_errorLineNumber, subroutine

    gosubStackPointer = 0

    if gosubStackMemoryPointer < 0:

        ErrorMessage(ERROR_CODE_NO_MATCHING_GOSUB, ERROR_MESSAGE_NO_MATCHING_GOSUB)

        subroutine = "Ready"

        return

    for gosubStackPointer in range(gosubStackMemoryPointer):

        L_programCodeMemoryPointer = gosubLineNumberStack[gosubStackPointer]

    while True:

        if L_programCodeMemoryPointer == PROGRAM_CODE_MEMORY_TOP + 1:

            # ErrorMessage("Line not found")
            ErrorMessage(ERROR_CODE_LINE_NOT_FOUND, ERROR_MESSAGE_LINE_NOT_FOUND)

            subroutine = "Ready"

            return

        GetNumber()
        # N_numericData = FN_GetNumber

        if L_programCodeMemoryPointer == returnLineNumberStack[gosubStackPointer]:

            E_errorLineNumber = N_numericData

            subroutine = "RunCommandInterpreter"

            return

        L_programCodeMemoryPointer = L_programCodeMemoryPointer + 1

        C_characterPointer = 0


def TinyBasic_New():

    global subroutine

    WarmStart()

    subroutine = "Ready"


def TinyBasic_Cls():
    """
    global subroutine

    CLS

    subroutine = "FinishStatement"
    """
    

def TinyBasic_Help():

    global subroutine

    for i in range(COMMAND_HELP_MEMORY):

        print(commandHelp[i])

    subroutine = "FinishStatement"


def TinyBasic_Mem():

    global subroutine

    GetFreeMemory()

    print(freeMemoryMessage)

    subroutine = "FinishStatement"


def TinyBasic_End():

    global subroutine

    subroutine = "Ready"


def TinyBasic_Stop():

    global subroutine

    ErrorMessage(ERROR_CODE_STOP, ERROR_MESSAGE_STOP)

    subroutine = "Ready"


def TinyBasic_Save():
    """
    GetExpression()
    if Es_errorMessage$ != EMPTY_STRING THEN
    subroutine = "Ready"
    RETURN
    ENDIF
    As_programCodeWorkspace$="tinyBas"+STR$(N_numericData,0)
    A=FALSE
    # OPEN As_programCodeWorkspace$ FOR OUTPUT AS #1
    FOR I=27 TO 125
    Bs_stringData$=programCode$(I)
    if Bs_stringData$!="" THEN
    print #1,Bs_stringData$
    A=TRUE
    ENDIF
    NEXT
    CLOSE #1
    if A=FALSE THEN
    # KILL As_programCodeWorkspace$
    ENDIF
    subroutine = "FinishStatement"
    RETURN
    """


def TinyBasic_Load():
    """
    GetExpression)
    if Es_errorMessage$ != EMPTY_STRING THEN
    subroutine = "Ready"
    RETURN
    ENDIF
    As_programCodeWorkspace$ = "tinyBas" + STR$(N_numericData)
    # B=FILE_EXISTS(As_programCodeWorkspace)
    if B=FALSE THEN
    Es_errorMessage$="File "+As_programCodeWorkspace$+" not found"
    subroutine = "Ready"
    RETURN
    ENDIF
    # OPEN As_programCodeWorkspace$ FOR INPUT AS #1
    B=FALSE
    I = PROGRAM_CODE_MEMORY_START
    WHILE B=FALSE
    B=EOF(#1)
        INPUT #1,Bs_stringData$
    programCode$(I)=Bs_stringData$
    INC I
    #ENDWHILE
    CLOSE #1
    WHILE I <= PROGRAM_CODE_MEMORY_TOP
    programCode$(I) = ""
    I = I + 1
    #ENDWHILE
    if E_errorLineNumber = 0 THEN
    subroutine = "FinishStatement"
    RETURN
    ENDIF
    subroutine = "Ready"
    RETURN
    """


def TinyBasic_Let():

    global subroutine

    GetStatementLabel()

    if Es_errorMessage != EMPTY_STRING:

        subroutine = "Ready"


# tiny basic math/conditional operators
def TinyBasic_Equals():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AdditionSubtractionExpression()

    B_stackpointer = S_processorStackPointer - 1

    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] == A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Greater_Than():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GetCharacter()

    if Cs_character == OP_EQUALS:

        TinyBasic_Greater_Than_Equal_To()

        return

    AdditionSubtractionExpression()

    B_stackpointer = S_processorStackPointer - 1

    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] > A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Greater_Than_Equal_To():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    AdditionSubtractionExpression()

    B_stackpointer = S_processorStackPointer - 1

    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] >= A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Less_Than():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1

    GetCharacter()

    if Cs_character == OP_EQUALS:

        TinyBasic_Less_Than_Equal_To()

        return

    if Cs_character == OP_GREATER_THAN:

        TinyBasic_Not_Equal_To()

        return

    AdditionSubtractionExpression()

    B_stackpointer = S_processorStackPointer - 1

    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] < A_processorStack[S_processorStackPointer])

    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Less_Than_Equal_To():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    AdditionSubtractionExpression()
    
    B_stackpointer = S_processorStackPointer - 1
    
    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] <= A_processorStack[S_processorStackPointer])
    
    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Not_Equal_To():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    AdditionSubtractionExpression()
    
    B_stackpointer = S_processorStackPointer - 1
    
    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] != A_processorStack[S_processorStackPointer])
    
    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Add():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    MultiplyDivideModulusExpression()
    
    B_stackpointer = S_processorStackPointer - 1
    
    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] + A_processorStack[S_processorStackPointer])
    
    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Subtract():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    MultiplyDivideModulusExpression()
    
    B_stackpointer = S_processorStackPointer - 1
    
    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] - A_processorStack[S_processorStackPointer])
    
    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Multiply():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    GroupExpression()
    
    B_stackpointer = S_processorStackPointer - 1
    
    A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] * A_processorStack[S_processorStackPointer])
    
    S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Divide():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    GroupExpression()
    
    B_stackpointer = A_processorStack[S_processorStackPointer]
    
    if B_stackpointer == 0:

        ErrorMessage(ERROR_CODE_DIVISION_BY_ZERO, ERROR_MESSAGE_DIVISION_BY_ZERO)

        S_processorStackPointer = S_processorStackPointer - 1

        return
    
    else:

        B_stackpointer = S_processorStackPointer - 1

        A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] / A_processorStack[S_processorStackPointer])

        S_processorStackPointer = S_processorStackPointer - 1


def TinyBasic_Modulus():

    global C_characterPointer, S_processorStackPointer

    C_characterPointer = C_characterPointer + 1
    
    GroupExpression()
    
    B_stackpointer = A_processorStack[S_processorStackPointer]
    
    if B_stackpointer == 0:

        ErrorMessage(ERROR_CODE_DIVISION_BY_ZERO, ERROR_MESSAGE_DIVISION_BY_ZERO)

        S_processorStackPointer = S_processorStackPointer - 1

        return
    
    else:

        B_stackpointer = S_processorStackPointer - 1

        A_processorStack.insert(B_stackpointer, A_processorStack[B_stackpointer] % A_processorStack[S_processorStackPointer])

        S_processorStackPointer = S_processorStackPointer - 1


def ConvertToUppercase(textstringToConvert):

    global asciiCode

    stringPointer = 0

    convertedString = ""

    while stringPointer < len(textstringToConvert):

        # get character to work with into
        # temporary variable, saves code
        character = textstringToConvert[stringPointer]

        # test character to see if lowercase
        if (character >= "a") and (character <= "z"):

            # it is, so convert it
            # get code for character - offset 'A'
            asciiCode = ord(character) - ASC_LOWERCASE_A

            # add value to offset for 'A'
            convertedString = convertedString + chr(ASC_UPPERCASE_A + asciiCode)

        else:

            convertedString = convertedString + character

        stringPointer = stringPointer + 1

    return convertedString


def ErrorMessage(code, message):

    global errorCode, Es_errorMessage

    if Es_errorMessage == EMPTY_STRING:

        errorCode = code

        Es_errorMessage = message


def ErrorHandler():

    global errorCode, Es_errorMessage

    if Es_errorMessage != EMPTY_STRING:

        if E_errorLineNumber > 0 and errorCode == ERROR_CODE_STOP:

            Es_errorMessage = Es_errorMessage + " AT LINE " + str(E_errorLineNumber)

            DisplayErrorMessage(Es_errorMessage)

            return

        if E_errorLineNumber > 0:

            Es_errorMessage = "ERROR IN LINE " + str(E_errorLineNumber) + ": " + Es_errorMessage

        else:

            Es_errorMessage = "ERROR: " + Es_errorMessage

    DisplayErrorMessage(Es_errorMessage)


def DisplayErrorMessage(errorMessage):

    global Es_errorMessage

    print(errorMessage)

    Es_errorMessage = EMPTY_STRING


Start()
