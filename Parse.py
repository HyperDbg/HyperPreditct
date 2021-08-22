import glob
import string

DataDictionary = {}
StatisticsList = {}
LogPath = ".\\logs"

def is_hex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)


def merge_logs():
    syscall_set = set()
    ### Merging and filtering logs ###
    with open("main-log.txt", "w") as MainLog:

        for item in glob.glob(".\\logs\\*") :
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
                    syscall_set.add(Tmp[2])
    
            LogFile.close()
            print(len(list(syscall_set)))

'''
### Reading main log, line by line and make dictionary ###

FinalLog = open("main-log.txt", 'r') 
print("Loading data from main log...")
while True:
    # Get next line from file
    Line = FinalLog.readline()

    # if line is empty
    # end of file is reached
    if not Line:
        break

    Tmp = Line.strip().split('-')
    
    # mask the syscall to remove extra bytes
    ExtraBytes = int(Tmp[2],16)
    ExtraBytes = ExtraBytes & 0xffff 
    Tmp[2] = str(hex(ExtraBytes))
    
    if Tmp[1] in DataDictionary:
        # append the new number to the existing array at this slot
        DataDictionary[Tmp[1]].append(int(Tmp[2],16))
    else:
        # create a new array in this slot
        DataDictionary[Tmp[1]] = [int(Tmp[2],16)]

    if str(Tmp[2]) in StatisticsList:
        # append the new number to the existing array at this slot
        TmpForStat = StatisticsList.get(Tmp[2])
        TmpForStat = TmpForStat + 1
        StatisticsList[str(Tmp[2])] = TmpForStat
    else:
        # create a new array in this slot
        StatisticsList[str(Tmp[2])] = 1


print("Length of unique processes : " + str(len(DataDictionary)))



# Print header
print("---------------------- List of top used syscalls ----------------------")

# Sort dictionary
SortedStatisticsList = {k: v for k, v in sorted(StatisticsList.items(), key=lambda item: item[1])}

# Show list of top n, mosts used functions in all logs
for key, value in SortedStatisticsList.items():
    print("Syscall : " + key + ", executed " + str(value) + " times")

print("-----------------------------------------------------------------------\n")
  
### Iterate syscall list's dictionary
print("--------------- Syscalls counts list based on processes ---------------")

for key, value in DataDictionary.items():
    print('key : ' + key)
    # print('List :')
    # print(value)
    print("Length of syscalls : " + str(len(value)))

print("-----------------------------------------------------------------------\n")
'''