# Two-Pass-Assembler
# Overview
This is a two-pass assembler written using PYTHON. It takes assembly language as input in a file named Input.txt and generates corresponding machine code in a file named outputMCode.txt. Symbol table and Opcode table are generated and displayed in the terminal. Errors in assembly code, if any, will be reported in the terminal. Until all errors are resolved, the program will not generate machine code or symbol/opcode table.
# Opcode Used:
![image](https://user-images.githubusercontent.com/94596235/200106875-1fd2b438-1e0d-4ae5-9711-6d0faaf340e3.png)
# Types of Instructions:
Type 0: Instructions containing no argument.
Type 1: Instruction containing one argument.
# Syntax Used and Assumptions:
Syntax for the comment is, # for single line comments.
There should be no space between label and “:”.
For opCode with no operands like CLA, 8 “0”s will be added after opCode
# Sample Input/Output:
Sample Input-
	CLA
	LAC	A
	SUB	B
	BRN	L1
	DSP	A
	CLA
	BRZ	L2
L1: DSP
	CLA
	BRZ	L2
L2: STP
	ADD	X
L	ADD	Y
	BRN	L
	STP
