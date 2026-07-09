input_data = open('/home/advent-of-code-2024/Day09/advent_of_code_9.txt','r')
input_data_str = [x for x in input_data][0]
lst = []

id = 0
for i in range(len(input_data_str)):
    multiplier = int(input_data_str[i])
    if i%2:
        if multiplier:
            for j in range(multiplier):
                lst.append('.')
    else:
        if multiplier:
            for k in range(multiplier):
                lst.append(id)
        id +=1 
org_lst = lst.copy()       
end = len(lst)-1
while end:
    if lst[end] == '.':
        end -= 1
    else:
        break
id_end = lst[end]
while id_end >= 0:
    print(id_end)
    id_counter = lst.count(id_end)
    id_index = [x for x in range(len(lst)) if lst[x] == id_end]
    space_counter = 0
    space_index = []
    start = 0
    while space_counter < id_counter:
        if lst[start] == '.':
            space_counter +=1
            space_index.append(start)
        start+=1
    if max(space_index) < min(id_index):
        for i in range(id_counter):
            lst[id_index[i]], lst[space_index[i]] = lst[space_index[i]], lst[id_index[i]]
    id_end -= 1
ans = 0
for i in range(len(lst)):
    if lst[i] != '.':
        ans += i*lst[i]
print(ans)
input_data.close()