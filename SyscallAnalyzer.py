from SyscallPattern import * 

class SyscallAnalyzer:
    def __init__(self, syscallsList):
        self.syscallsList = syscallsList
        self.syscallsSet = set(syscallsList)

    # This function gets a syscall number and patternLength and returns a dictionary 
    # containing all possible patterns after the syscall and their rates of occurrence
    # in the self.syscallsList.
    def analyzeNext(self, targetSyscall, patternLength):
        patternsRateDict = dict()
        i = 0 
        for syscall in self.syscallsList:
            if targetSyscall == syscall:
                pattern = self.nextPattern(i, patternLength)
                if not pattern is None:
                  
                    if not self.isAvailabe(pattern, patternsRateDict):
                        patternsRateDict[pattern] = 1
                    else:
                        patternsRateDict[pattern] = patternsRateDict[pattern] + 1
            i += 1
        return dict(sorted(patternsRateDict.items(), key=lambda item: item[1]))


    # This function gets a syscall number and patternLength and returns a dictionary 
    # containing all possible patterns before the syscall and their rates of occurrence
    # in the self.syscallsList.
    def analyzePrevious(self, targetSyscall, patternLength):
        patternsRateDict = dict()
        i = 0 
        for syscall in self.syscallsList:
            if targetSyscall == syscall:
                pattern = self.previousPattern(i, patternLength)
                if not pattern is None:
                  
                    if not self.isAvailabe(pattern, patternsRateDict):
                        patternsRateDict[pattern] = 1
                    else:
                        patternsRateDict[pattern] = patternsRateDict[pattern] + 1
            i += 1
        return dict(sorted(patternsRateDict.items(), key=lambda item: item[1]))

    def isAvailabe(self, pattern, patternDict):
        for p in patternDict.keys():
            if pattern.isEqual(p):
                return True
        return False 

    def nextPattern(self, index, patternLength):
        syscallsList = []
        for i in range(patternLength):
            if (i + index + 1) >= len(self.syscallsList):
                return None
            syscallsList.append(self.syscallsList[i + index + 1])
            
        return SyscallPattern(syscallsList)


    def previousPattern(self, index, patternLength):
        syscallsList = []
        for i in range(patternLength):
            if (index - 1 - i) < 0:
                return None
            syscallsList.append(self.syscallsList[index - i - 1])
            
        return SyscallPattern(syscallsList)

    # Calls analyze for all syscalls.
    def analyzeAll(self, patternLength, searchNext):
        allPattternRates = dict()
        if searchNext:
            for targetSyscall in self.syscallsSet:
                allPattternRates[targetSyscall] = dict()
                for i in range(1, patternLength + 1):
                    allPattternRates[targetSyscall][i] = self.analyzeNext(targetSyscall, i)
        else:
            for targetSyscall in self.syscallsSet:
                allPattternRates[targetSyscall] = dict()
                for i in range(1, patternLength + 1):
                    allPattternRates[targetSyscall][i] = self.analyzePrevious(targetSyscall, i)


        return allPattternRates
