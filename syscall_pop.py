import numpy as np
import json 
from utils import *

systemcalls_txt_file_path="./inputs/mnz.txt"
NT10_txt_path="./inputs/25915_NT10.txt"
WIN32_txt_path="./inputs/25915_WIN32.txt"
output_path="./outputs/sample.json"

tresh=15
stock=20


f = open(systemcalls_txt_file_path, "r")
syscals_number=[]
for x in f:
  syscals_number.append(int(x.split(',')[0], 16))

set_sys_cal=[]
for i in set(syscals_number):
    set_sys_cal.append(i)

f = open(NT10_txt_path, "r")
syscals_name_nt=[]
syscals_name_number_nt=[]
for x in f:
    syscals_name_nt.append(x.split("\t")[0])
    syscals_name_number_nt.append(int(x.split("\t")[1].split('\n')[0]))

f = open(WIN32_txt_path, "r")
syscals_name_win=[]
syscals_name_number_win=[]
for x in f:
    syscals_name_win.append(x.split("\t")[0])
    syscals_name_number_win.append(int(x.split("\t")[1].split('\n')[0]))

syscals_number_name_sin=[]
for i in range(len(syscals_number)):
     syscals_number_name_sin.append("")

for i in range(len(syscals_number)):
    for j in range(len(syscals_name_number_nt)):
        if syscals_number[i]==syscals_name_number_nt[j]:
            syscals_number_name_sin[i]=syscals_name_nt[j]

for i in range(len(syscals_number)):
    for j in range(len(syscals_name_number_win)):
        if syscals_number[i]==syscals_name_number_win[j]:
            syscals_number_name_sin[i]=syscals_name_win[j]

count=0
for i in syscals_number_name_sin :
    if i == "":
        count +=1

dic_syscals={}
for i in set_sys_cal:
    dic_syscals[i]=find_sys_number(i)

trend_sys_call=[]
for i in range(len(set_sys_cal)):
     trend_sys_call.append([])


for i in range(len(set_sys_cal)):
    indexs=find_sys_number_indexs(set_sys_cal[i])
    back=[]
    front=[]
    for j in indexs:
        list_temp_front=find_10(j,1,stock)
        list_temp_back=find_10(j,-1,stock)
        for k in list_temp_front:
            front.append(k)
        for k in list_temp_back:
            back.append(k)
    trend_sys_call[i].append(front)
    trend_sys_call[i].append(back)

totall_sys_calls_front=np.zeros([len(set_sys_cal),len(set_sys_cal)])
totall_sys_calls_back=np.zeros([len(set_sys_cal),len(set_sys_cal)])

for i in range(len(set_sys_cal)):
    for j in (trend_sys_call[i][0]):
        totall_sys_calls_front[i,set_sys_cal.index(j)] +=1

for i in range(len(set_sys_cal)):
    for j in (trend_sys_call[i][1]):
        totall_sys_calls_back[i,set_sys_cal.index(j)] +=1

trend_sys_call_2=[]
for i in range(len(set_sys_cal)):
     trend_sys_call_2.append([])


for i in range(len(set_sys_cal)):
    temp_list_front=find_fan_sys(tresh, totall_sys_calls_front[i] )
    temp_list_back=find_fan_sys(tresh, totall_sys_calls_back[i] )
#     print(temp_list_front)
    trend_sys_call_2[i].append(temp_list_front)
    trend_sys_call_2[i].append(temp_list_back)   

final_dic={}
for i in range(len(set_sys_cal)):
    if len(trend_sys_call_2[i])>0:
        if len(trend_sys_call_2[i][0])>0:
            front_temp=translate_num_to_name(trend_sys_call_2[i][0])
        else:
            front_temp=["NO!!!!!!!!!!"]
        if len(trend_sys_call_2[i][1])>0:
            back_temp=translate_num_to_name(trend_sys_call_2[i][1])
        else:
            back_temp=["NO!!!!!!!!!!"]
        final_dic[dic_syscals[set_sys_cal[i]]]=[{'front':front_temp,'back':back_temp}]
    else:
        final_dic[dic_syscals[set_sys_cal[i]]]=[{'front':["NO!!!!!!!!!!"],'back':["NO!!!!!!!!!!"]}]

with open(output_path, "w") as outfile:
    json.dump(final_dic, outfile, sort_keys=True, indent=4)