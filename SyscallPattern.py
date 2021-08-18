
from os import path


class SyscallPattern():
    def __init__(self, pattern):
        self.pattern = pattern
    
    def __eq__(self, other):
        return self.isEqual(other)

    def __hash__(self):
        return hash(tuple(self.pattern))

    def __str__(self) :
        return self.getString()


    def getString(self):        
        str = ""
        i = 0 
        for syscall in self.pattern:
            str += "%0.4X" % syscall
            if i != len(self.pattern)-1:
                str += " "
            i +=1

        return str

    def isEqual(self, syscallPattern):
        i = 0 
        for i in range(len(syscallPattern.pattern)):
            if i >= len(self.pattern):
                return False 
            if syscallPattern.pattern[i] != self.pattern[i]:
                return False 

        return True