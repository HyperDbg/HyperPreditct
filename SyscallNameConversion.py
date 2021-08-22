import csv

with open('.\\windows-syscalls\\x64\\csv\\nt.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0] + " : " + row[30])
