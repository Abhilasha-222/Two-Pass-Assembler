# Two-Pass-Assembler
# Overview
This is a two-pass assembler written using PYTHON. It takes assembly language as input in a file named Input.txt and generates corresponding machine code in a file named outputMCode.txt. Symbol table and Opcode table are generated and displayed in the terminal. Errors in assembly code, if any, will be reported in the terminal. Until all errors are resolved, the program will not generate machine code or symbol/opcode table.
# Opcode Used:
![OpcodeGuide](https://user-images.githubusercontent.com/94596235/200107102-b524bae5-7a47-4ddb-ad16-aeceee51831e.png)
# Types of Instructions:
Type 0: Instructions containing no argument.

Type 1: Instruction containing one argument.
# Syntax Used and Assumptions:
1. Syntax for the comment is, # for single line comments.
2. There should be no space between label and “:”.
3. For opCode with no operands like CLA, 8 “0”s will be added after opCode

# Sample Input/Output:

# Sample Input-
![Input](https://user-images.githubusercontent.com/94596235/200107287-5f60ab93-6386-4088-be10-e0ebedd02dcc.png)
# Sample Output-
![Output](https://user-images.githubusercontent.com/94596235/200107295-6ca81929-f6c0-4dfa-8e34-b9cd402c7d41.png)
# Execution Process:
1. Put assembly language code in a file named inputACode.txt in the same directory as the python file. 
2. Run from terminal using :
![file-name](https://user-images.githubusercontent.com/94596235/200107358-315adc4e-9435-4dd1-a1af-5ee4cdb3b302.png)
3. Output machine code is stored in OutputMCode.txt
# Errors Reported:
1. If the starting of the symbol is a number.
2. If Invalid characters detected in a symbol
3. End statement missing
4. Opcode not recognised
5. If an Invalid jump location is given
6. If Invalid use of a variable is made
7. If the Symbol is used but not defined

# Code Flow:
# PASS 1
1. The symbol table and opCode table are initialized as symtab and optab
respectively.
2. The Assembly program is processed line by line.
3. The program reads instructions and extracts labels, opcodes, operands, 
and comments.
4. opCodes and labels are stored with their location.
# PASS 2
1. variables are assigned addresses
2. Instruction tables constructed in pass one are used to create the final 
machine code as a .txt file
