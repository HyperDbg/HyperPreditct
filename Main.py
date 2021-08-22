from Scanner import *
from SyscallAnalyzer import *
import json 

def printPatternDict(patternRate):
    for p in patternRate.keys():
        print("\tsyscall =", p.getString(), ": rate =", patternRate[p])

def printAllPatternDict(allPattternRates):
    for targetSyscall in allPattternRates.keys():
        for patternRange in allPattternRates[targetSyscall].keys():
            print(("%0.4X" % targetSyscall), " ", patternRange, ":")
            printPatternDict(allPattternRates[targetSyscall][patternRange])

def jsonize(allPattternRatesDict, fileName):
    newDict = dict()
    for targetSyscall in allPattternRatesDict.keys():
        newDict[("%0.4X" % targetSyscall)] = dict()
        for patternRange in allPattternRatesDict[targetSyscall].keys():
            newDict[("%0.4X" % targetSyscall)][patternRange] = dict()
            for pattern in  allPattternRatesDict[targetSyscall][patternRange].keys():
                newDict[("%0.4X" % targetSyscall)][patternRange][pattern.getString()] = allPattternRatesDict[targetSyscall][patternRange][pattern]

    
    # print(newDict)
    print(json.dumps(newDict, sort_keys=True, indent=4))

    with open(fileName,"w") as f:
        json.dump(newDict, f, sort_keys=True, indent=4)


def main():
    syscallList = merge_logs(LogPath=".\\logs", MainLogPath=".\\outputs\\main-log.txt")
    syscallAnalyzer = SyscallAnalyzer(syscallList)
    allPattternRates = syscallAnalyzer.analyzeAll(5, searchNext = True)
    jsonize(allPattternRates, ".\\outputs\\output.json")
    # printPatternDict(patternRate)
    # print(allPattternRates)
    # json_object = json.dumps(allPattternRates, indent = 4) 
    # printAllPatternDict(allPattternRates)




if __name__ == "__main__":
    main()