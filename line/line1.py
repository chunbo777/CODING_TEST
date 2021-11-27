
def solution(record):
    def solution_1(record):
        record_list =  [i.split(" ") for i in record]
        sales = 0
        for i in record_list:
            if i[0] == "S":
                sales += int(i[2])
        purc = []
        for k, price, num in record_list:
            if k == "P":
                for i in range(int(num)):
                    purc.append(int(price))
            if len(purc) >= sales:
                purc =  purc[:sales]
                break
        return sum(purc)
    def solution2(record):
        record_list =  [i.split(" ") for i in record]
        final = []
        idx = 0
        while True:
            sales = 0
            purc = []
            purc_num = 0
            while record_list[-1][0] != "P":  
                k = record_list.pop()
                sales+=int(k[2])
            while record_list[-1][0] != "S": 
                k = record_list.pop()
                for i in range(int(k[2])):
                    purc.append(int(k[1]))
                purc_num += int(k[2])
                if purc_num >= sales:
                    final.extend(purc[:sales])
                    break
                else:
                    final.extend(purc[:purc_num])
                    record_list.append(["S", k[1], sales-purc_num])

            if record_list==[]:
                break
        return sum(final)
    return [solution_1(record), solution2(record)]

        


# record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
# solution1(record)
solution(record)