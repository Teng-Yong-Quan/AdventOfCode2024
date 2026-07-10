input_data = open('/home/advent-of-code-2024/Day11/advent_of_code_11.txt','r')
input_data_lst = [x.split() for x in input_data][0]
lst = input_data_lst.copy()
dic = {}
for index in range(len(lst)):
    if lst[index] not in dic:
        dic[lst[index]] = 1
    elif lst[index] in dic:
        dic[lst[index]] += 1
        
for i in range(75):
    new_dic = {}
    for k,v in dic.items(): 
        if k == '0':
            if '1' not in new_dic:
                new_dic['1'] = v
            else:
                new_dic['1'] += v
        elif not len(k)%2:
            half = len(k)//2
            left = str(int(k[:half]))
            if left not in new_dic:
                new_dic[left] = v
            else:
                new_dic[left] += v
            right = str(int(k[half:]))
            if right not in new_dic:
                new_dic[right] = v
            else:
                new_dic[right] += v
        else:
            num_int = int(k)
            middle = str(num_int*2024)
            if middle not in new_dic:
                new_dic[middle] = v
            else:
                new_dic[middle] += v
    dic = new_dic
ans = sum(dic.values())
print(ans)
input_data.close()