def find_sys_number(sys_number):
    flag=0
    for j in range(len(syscals_name_number_nt)):
        if syscals_name_number_nt[j]==sys_number:
            flag=1
            return syscals_name_nt[j]
    if flag==0:
        for j in range(len(syscals_name_number_win)):
            if sys_number == syscals_name_number_win[j]:
                flag=1
                return syscals_name_win[j]
    if flag==0:
        return "Nn"
    

def find_sys_number_indexs(sys_number):
    indexs=[]
    for i in range(len(syscals_number)):
        if syscals_number[i]==sys_number:
            indexs.append(i)
    return indexs


def find_10(index,n,stock):
    list_re=[]
    while(stock > 0 and (index+n < len(syscals_number) and index+n > -1) ):
        index=index+n
        list_re.append(syscals_number[index])
        stock=stock-1
    return list_re


def find_fan_sys(Tr, list_rt ):
    temp_list=[]
    for i in range(len(list_rt)):
        if list_rt[i] > Tr:
            temp_list.append(set_sys_cal[i])
    return temp_list

def translate_num_to_name(list_tem):
    tra=[]
    for i in list_tem:
        tra.append(dic_syscals[i])
    return tra  