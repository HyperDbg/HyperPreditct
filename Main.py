from Scanner import *
from SyscallAnalyzer import *
from SyscallNameConversion import *
import json 
import operator

def printPatternDict(patternRate):
    for p in patternRate.keys():
        print("\tsyscall =", p.getString(), ": rate =", patternRate[p])

def printAllPatternDict(allPattternRates):
    for targetSyscall in allPattternRates.keys():
        for patternRange in allPattternRates[targetSyscall].keys():
            print(("%0.4X" % targetSyscall), " ", patternRange, ":")
            printPatternDict(allPattternRates[targetSyscall][patternRange])

def jsonizeAll(allPattternRatesDict, fileName):
    newDict = dict()
    for targetSyscall in allPattternRatesDict.keys():
        newDict[convertSyscallNumberToFunctionName(targetSyscall)] = dict()
        for patternRange in allPattternRatesDict[targetSyscall].keys():
            newDict[convertSyscallNumberToFunctionName(targetSyscall)][patternRange] = dict()
            for pattern in  allPattternRatesDict[targetSyscall][patternRange].keys():
                newDict[convertSyscallNumberToFunctionName(targetSyscall)][patternRange][pattern.getString()] = allPattternRatesDict[targetSyscall][patternRange][pattern]
                
def jsonize(allPattternRatesDict, folderName, maximumResults):
    newDict = dict()
    for targetSyscall in allPattternRatesDict.keys():
        newDict = dict()
        newDict[convertSyscallNumberToFunctionName(targetSyscall)] = dict()
        for patternRange in allPattternRatesDict[targetSyscall].keys():
            newDict[convertSyscallNumberToFunctionName(targetSyscall)][patternRange] = dict()
            
            controlMaximum = 0
            tempStorage = dict()
            tempStorage2 = dict()
            
            for pattern in  allPattternRatesDict[targetSyscall][patternRange].keys():
                tempStorage[pattern] = allPattternRatesDict[targetSyscall][patternRange][pattern]
                # print(pattern.getString() + " : " + str(allPattternRatesDict[targetSyscall][patternRange][pattern]))

            # sort dictionary by value
            sortedTempStorage = dict(sorted(tempStorage.items(), key=operator.itemgetter(1),reverse=True))

            # apply sort and limit
            for pattern in  sortedTempStorage.keys():
                controlMaximum += 1
                if controlMaximum > maximumResults :
                    break
                    
                tempStorage2[pattern] = allPattternRatesDict[targetSyscall][patternRange][pattern]
            
            # save the results
            for pattern in  tempStorage2.keys():
                newDict[convertSyscallNumberToFunctionName(targetSyscall)][patternRange][pattern.getString()] = allPattternRatesDict[targetSyscall][patternRange][pattern]
        
        with open(folderName + '\\' + convertSyscallNumberToFunctionName(targetSyscall) + '.json', "w") as f:
            json.dump(newDict, f, sort_keys=True, indent=4)
        print(json.dumps(newDict, sort_keys=True, indent=4))
    

def main():

    syscallList = merge_logs(LogPath=".\\logs", MainLogPath=".\\outputs\\main-log.txt")
    syscallAnalyzer = SyscallAnalyzer(syscallList)
    allPattternRates = syscallAnalyzer.analyzeAll(5)
    jsonize(allPattternRates, ".\\outputs", 5)
    
    #jsonizeAll(allPattternRates, ".\\outputs\\output.json")
    # printPatternDict(patternRate)
    # print(allPattternRates)
    # json_object = json.dumps(allPattternRates, indent = 4) 
    # printAllPatternDict(allPattternRates)

if __name__ == "__main__":
    main()