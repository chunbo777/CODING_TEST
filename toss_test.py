#test1

def solution(data):
    data_list=list(data.lower())
    new_list=[]
    toss_list=[]
    dict1={}
    key_list=[]
    for x in data_list: 
        dict1[x]=data_list.count(x)

    for key, value in dict1.items():
        if dict1[key]==max(dict1.values()):
            key_list.append(key)
    #key_list에 높은 빈도를 반환
    key_list=list(set(key_list))
    key_list.sort()
    for data in key_list:
        if data in  ["T", "O", "S", "t", "o", "s"]:
            toss_list.append(data)
        if data not in  ["T", "O", "S", "t", "o", "s"]:
            new_list.append(data)
    


    list2= list(set(toss_list))
    key_t=[]
    key_o=[]
    key_s=[]
    for x in list2:
        if x in[ "T" , "t"]:
            key_t.append(x)
        elif x in ["O", "o"]:
            key_o.append(x)
        elif x in ["S" , "s"]:
            key_s.append(x)
    key_tos=key_t+key_o+key_s
    
    return (str(''.join(key_tos)).upper()).replace("S","SS")+str("".join(new_list)).lower()


#test 2
def solution(price):
    stock_day=[]
    for day, pr in enumerate(price):
        stock_num=100000000//price[day]
        remains=100000000%price[day]
        # print(stock_num, remains)
        otherday_stock_num=0
        for otherday in range(0,len(price)):    
            if ((price[day]/2) >= price[otherday]) and otherday>=day :
                # print(price[day],price[otherday])
                otherday_stock_num=(50000000+remains)//price[otherday]
                otherday_stock_rem=(50000000+remains)%price[otherday]
                print(otherday)
                stock_num+=otherday_stock_num
                remains-=50000000
                remains+=otherday_stock_rem
                break
        stock_day.append([stock_num, remains, otherday])
    print(stock_day)
    
    stock_dict={}
    for i, [stock_num, remains,otherday] in enumerate(stock_day):
         for day, pr in enumerate(price):
            # print((price[day]*stock_num)+remains)
            if ((price[day]*stock_num)+remains)>=1000000000 and i<day:
                stock_dict[i]=day-i
                # print(stock_dict)
                break
                
            else: 
                stock_dict[i]=-1
    return list(stock_dict.values())