import csv

readData = False
listOfSyscalls = []

def readDataFromFile():

    global listOfSyscalls
    global readData
    
    tempStorage = []

    if readData == False:
        file =  open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '')
        tempStorage = csv.reader(file)
        readData = True

    # save into global variables    
    for row in tempStorage :
        listOfSyscalls.append(row)

def readAllFunctions():
    
    global listOfSyscalls
    
    readDataFromFile()
    
    for row in listOfSyscalls:
        print(row[0] + " : " + row[30])

def convertSyscallNumberToFunctionName(SyscallNum):
    
    global listOfSyscalls
    
    firstColumn = True
    
    # read the data
    readDataFromFile()

    for row in listOfSyscalls:
        if firstColumn :
            firstColumn = False
            continue
            
        if row[30] == '' :
            continue
            
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
