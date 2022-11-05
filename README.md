# Two-Pass-Assembler
# Overview
This is a two-pass assembler written using PYTHON. It takes assembly language as input in a file named Input.txt and generates corresponding machine code in a file named outputMCode.txt. Symbol table and Opcode table are generated and displayed in the terminal. Errors in assembly code, if any, will be reported in the terminal. Until all errors are resolved, the program will not generate machine code or symbol/opcode table.
# Opcode Used:
![OpcodeGuide](https://user-images.githubusercontent.com/94596235/200107102-b524bae5-7a47-4ddb-ad16-aeceee51831e.png)
# Types of Instructions:
Type 0: Instructions containing no argument.
Type 1: Instruction containing one argument.
# Syntax Used and Assumptions:
Syntax for the comment is, # for single line comments.
There should be no space between label and “:”.
For opCode with no operands like CLA, 8 “0”s will be added after opCode
# Sample Input/Output:
# Sample Input-
[input.txt](https://github.com/Abhilasha-222/Two-Pass-Assembler/files/9943243/input.txt)
Sample Output-
[outputMCode.txt](https://github.com/Abhilasha-222/Two-Pass-Assembler/files/9943250/outputMCode.txt)
# Execution Process:
Put assembly language code in a file named inputACode.txt in the same directory as the python file.
Run from terminal using :
$ python opa.py
