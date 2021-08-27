import csv

readData = False
listOfSyscalls = []

def readDataFromFile():

    global listOfSyscalls
    global readData
    
    tempStorage1 = []
    tempStorage2 = []

    if readData == False:
        file =  open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '')
        tempStorage1 = csv.reader(file)
        file2 =  open('.\\windows-syscalls\\x64\\csv\\win32k.csv', newline= '')
        tempStorage2 = csv.reader(file2)
        readData = True
    
    firstColumn = True
    
    # save into global variables (nt) 
    for row in tempStorage1 :
    
        if firstColumn :
            firstColumn = False
            continue
            
        if row[30] == '' :
            continue
            
        listOfSyscalls.append(row)
    
    firstColumn = True

    # save into global variables (win32k)    
    for row in tempStorage2 :
    
        if firstColumn :
            firstColumn = False
            continue
            
        if row[30] == '' :
            continue
            
        listOfSyscalls.append(row)

def readAllFunctions():
    
    global listOfSyscalls
    
    readDataFromFile()
    
    for row in listOfSyscalls:
        print(row[0] + " : " + row[30])

def convertSyscallNumberToFunctionName(SyscallNum):
    
    global listOfSyscalls
    
    
    # read the data
    readDataFromFile()

    for row in listOfSyscalls:
        if int(row[30], 16) == SyscallNum :
                return row[0]
    return 'FunctionNotFound'   

def testFunctionConversion():
    # Test
    with open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '') as f:
        reader2 = csv.reader(f)
        firstColumn = True
        
        for row in reader2:
            if firstColumn :
                firstColumn = False
                continue
                
            if row[30] == '' :
                continue
            print(convertSyscallNumberToFunctionName(int(row[30], 16)))
            #print(str(row[30]))
