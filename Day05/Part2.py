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

incorrect_update_lst = [x for x in update_lst if x not in correct_update_lst]
corrected_update_lst = []
for incorrect_update in incorrect_update_lst:
    chosen_rule_lst, corrected_update = [],[0]*len(incorrect_update)
    for rule in rule_lst:
        if rule[0] in incorrect_update and rule[1] in incorrect_update:
            chosen_rule_lst.append(rule)
    while incorrect_update:
        front,back = 0,0
        if chosen_rule_lst:
            front_rule = set([x[0] for x in chosen_rule_lst])
            back_rule = set([x[1] for x in chosen_rule_lst])
        for num in range(len(incorrect_update)):
            if not chosen_rule_lst:
                for x in range(len(corrected_update)):
                    if corrected_update[x] == 0:
                        corrected_update[x] = incorrect_update[num]
                incorrect_update[num] = 0
            elif incorrect_update[num] in front_rule and incorrect_update[num] not in back_rule:
                front = incorrect_update[num]
                incorrect_update[num] = 0
            elif incorrect_update[num] not in front_rule and incorrect_update[num] in back_rule:
                back = incorrect_update[num]
                incorrect_update[num] = 0
        incorrect_update = [x for x in incorrect_update if x != 0]
        if 0 in corrected_update:
            for i in range((len(corrected_update)-1)//2):
                if corrected_update[i] == 0 and corrected_update[len(corrected_update)-1-i] == 0:
                    corrected_update[i],corrected_update[len(corrected_update)-1-i] = front,back
                    break
        if chosen_rule_lst:
            for chosen_rule_index in range(len(chosen_rule_lst)):
                if chosen_rule_lst[chosen_rule_index][0] == front or chosen_rule_lst[chosen_rule_index][1] == back:
                    chosen_rule_lst[chosen_rule_index] = 0
            chosen_rule_lst = [x for x in chosen_rule_lst if x != 0]
    corrected_update_lst.append(corrected_update)
ans = sum(list(map(lambda x : x[(len(x)-1)//2],corrected_update_lst)))
print(ans)
input_data.close()