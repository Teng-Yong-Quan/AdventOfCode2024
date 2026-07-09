def sum_count(length):
    count = 0
    for i in range(length):
        count+=i
    return count

input_data = open('/home/advent-of-code-2024/Day05/advent_of_code_5.txt','r')
input_lst = [x for x in input_data]
rule_lst = [list(map(int,x.replace('\n','').replace('|', ' ').split())) for x in input_lst if '|' in x]
update_lst = [list(map(int,x.replace('\n','').replace(',', ' ').split())) for x in input_lst if ',' in x]
correct_update_lst = []
for update in update_lst:
    update_index, moving_index,count = 0,0,0
    while update_index < len(update)-1:
        while True:
            moving_index +=1
            for rule_index in range(len(rule_lst)):
                if rule_lst[rule_index][0] == update[update_index] and rule_lst[rule_index][1] == update[moving_index]:
                    count += 1
                    break
            if moving_index == len(update) - 1:
                break
        update_index += 1
        moving_index = update_index
    if count == sum_count(len(update)):
        correct_update_lst.append(update)
ans = sum(list(map(lambda x : x[(len(x)-1)//2],correct_update_lst))) 
print(ans)
input_data.close()