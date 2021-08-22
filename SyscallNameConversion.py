import csv


def readAllFunctions():
    with open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0] + " : " + row[30])

def convertSyscallNumberToFunctionName(SyscallNum):

    with open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '') as f:
        listOfSyscalls = csv.reader(f)
        for row in listOfSyscalls:
            if row[30] == SyscallNum :
                    return row[0]

# Test
with open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline= '') as f:
    reader2 = csv.reader(f)
    for row in reader2:
        print(convertSyscallNumberToFunctionName(str(row[30])))
        #print(str(row[30]))