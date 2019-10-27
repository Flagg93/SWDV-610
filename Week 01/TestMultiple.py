def is_multiple(n,m):
    #true is n = mi where i is an integer
    return n%m==0
    
def getInput(label):
    out = None
    validInput = False
    strInput = input(label)
    if(strInput.upper() != "EXIT"):
        while(not validInput):                    
            if strInput.isnumeric():
                out = int(strInput)
                validInput = True
    return out

#def getInputs(inputLabel1, inputLabel2):
#    out1 = getInput(inputLabel1)
#    out2 = getInput(inputLabel2)
#    return out1, out2
    
                    
def main():
    loop = True
    while(loop):
        print("This program will determine if n is a multiple of m(Enter 'Exit' to close the program")
        n = getInput("n: ")
        if n != None:
            m = getInput("m: ")
            if m != None:
                notString = ""
                if not is_multiple(n,m):
                    notString = "not "
                print("{0}(n) is {1}a multiple of {2}(m)".format(n, notString, m))
            else:
                loop = False
                    
        else:
            loop = False
main()