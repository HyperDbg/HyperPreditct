import glob
import string

### Util function 
def is_hex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)

### Merging and filtering logs ###
def merge_logs(LogPath, MainLogPath):
    syscall_list = list()
    with open(MainLogPath, "w") as MainLog:

        for item in glob.glob(LogPath+ "\*") :
            LogFile = open(item, 'r')
            print("Merging logs from: " + item)
            while True:
                # Get next line from file
                Line = LogFile.readline()

                # if line is empty
                # end of file is reached
                if not Line:
                    break
                # check if line is valid
                if Line.count('-') == 2:
                    Tmp = Line.strip().split('-')
                    if is_hex(Tmp[0]) and is_hex(Tmp[2]):
                        # it's probably valid
                        Tmp = []
                    else :
                        continue

                else :
                    continue
                    
                if (not "HyperDbg" in Line) and (not "%llx" in Line)  : 
                    # print(Line.strip())
                    Tmp = Line.strip().split('-')
                    MainLog.writelines(Tmp[2] + '\n')
                    syscall_list.append(int(Tmp[2], 16))
    
            LogFile.close()
            return syscall_list

