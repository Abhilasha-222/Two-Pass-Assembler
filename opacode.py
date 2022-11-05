with open('input.txt', 'r') as f1:
    inp=f1.readlines()               #reading the input file
with open('instructions.txt','r') as f2:
    opc=f2.readlines()               #reading opcode file
symtab={}
optab=[]
errtab=[]
oplist=[]
print(inp)

for i in range(len(opc)):
    oplist.append(opc[i][5:8])

opadd=[]
for i in range(len(opc)):
    opadd.append(opc[i][:4])

def printSymbolTable():
  print("*** SYMBOL TABLE ***")
  print("\tSymbol\t Location")
  for symbol,location in symtab.items():
    print("  \t",symbol," \t",format(location, "08b"))


def printOpCodeTable():
  print("*** OPCODE TABLE ***")
  print("\t Location\tOpCode")
  for o in optab:
    print("\t",format(o[0], "08b"),"\t",format(int(o[1]), "04b"))
  print("")


def check_valid_variable(symbol,ln):   #checking if the symbol is a variable
    if type(symbol[0])==type(1):
        errtab.append([ln,"ERROR: Symbol's starting cannot be a number in " + symbol])
        return False
    validchars = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    flag = 0
    for character in symbol:
        if character not in validchars:
            flag = 1
            errtab.append([ln,"ERROR: Invalid character " + character + " in symbol " + symbol])
    if flag == 1:
        return False     #if not a variable
    return True          #if a variable

def onepass(lc):

    ln=0                                #line number
    while ln!=len(inp):                 #till input file is fully read
        line=inp[ln]                    #each line in the input.txt

        if '#' in line:                 #if line has a comment
            line=line.split('#')[0]
            line=line.strip()
            if len(line)==0:
                ln+=1
                continue
        if ':' in line:                 #if it has a symbol
            symtab[line.split(':')[0]]=lc#add the symbol in sym. table
            line=line.split(':')[1]     #now check the rest of the line
    
        line = line.split()
        op = line[0]
        if(ln==len(inp)-1):                 #end of file
            if(op!='STP'):                  #stp missing 
                errtab.append([ln,": End statement missing"])
        
        if op in oplist:                    #making opcode table
            z=oplist.index(op)
            optab.append((lc,opadd[z]))
        else:
            errtab.append([ln,": Opcode not recognised"])
        
        line = line[1:]                     #handle variable or symbol
        for var in line:
            if var not in symtab:
                if(check_valid_variable(var,ln)==False):
                    continue
                if ('BR' in op):            #if branching or jump
                    symtab[var] = (-1,ln)
                else:
                    symtab[var] = (-2,ln)
            else:
                if ('BR' in op and symtab[var][0] == -2):
                    errtab.append([ln,"ERROR: Invalid jump location " + var + " Since it's already used as a variable."])
                if('BR' not in op and symtab[var][0] == -1):
                    errtab.append([ln,"ERROR: Invalid use of " + var + ", it has already been used as a jump location."])

        ln+=1
        lc+=1
    return lc


def passTWO(outFile):
  
  ln = 0
  while ln != len(inp):         #read every line
    line = inp[ln]
    if '#' in line:
        line = line.split('#')[0]
        line = line.strip()
        if(len(line) == 0):
            ln += 1
            continue
    if ':' in line:
        line = line.split(':')[1]
    
    line = line.split()

    op = line[0]
    if op in oplist:
        outFile.write(format(opadd[oplist.index(op)]))      #if opcode write the add. of opcode
    line = line[1:]
    if(len(line) == 0):                                     #if no symbol or var. ahead then add 8 0's
        outFile.write(format(0,"08b"))
    else:
      for var in line:                                      #if there is, write symbol location
        if var in symtab.keys():
            outFile.write(format(symtab[var],"08b"))
    
    outFile.write("\n")
    ln += 1

def handle_var(lc):
  for symbol in symtab:
    if type(symtab[symbol]) == type((1,1)):
      if symtab[symbol][0] == -2:
        symtab[symbol] = lc
        lc += 1
      elif symtab[symbol][0] == -1:
        errtab.append([symtab[symbol][1],"ERROR: Label " + symbol  + " used but not defined."])
  return lc


location=onepass(0)
handle_var(location)
if len(errtab)==0:
    with open("outputMCode.txt","w+") as outFile:
        passTWO(outFile)
    # print(optab)
    print(symtab)
    printSymbolTable()
    printOpCodeTable()
else:
    print("error table")
    print(errtab)






