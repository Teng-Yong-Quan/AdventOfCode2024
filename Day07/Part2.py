def solve(lst,value):
    bfs = []
    power = 0
    prev_lst = [lst[power]]
    while power < len(lst)-1:
        temp_lst = []
        for i in range(len(prev_lst)):
            num_1 = prev_lst[i] + lst[power+1]
            num_2 = prev_lst[i] * lst[power+1]
            num_3 = int(str(prev_lst[i]) + str(lst[power+1]))
            bfs.append(prev_lst[i])
            temp_lst.append(num_1)
            temp_lst.append(num_2)
            temp_lst.append(num_3)
        prev_lst = temp_lst
        power+=1
    if value in prev_lst:
        return True
    return False

input_data = open('/home/advent-of-code-2024/Day07/advent_of_code_7.txt','r')
input_data_lst = [x.replace('\n','').split(':') for x in input_data]  
final_num = [int(x[0]) for x in input_data_lst] 
nums = [list(map(int,y.split())) for y in [x[1] for x in input_data_lst]]

valid_final_num = []
valid_nums = []
for i in range(len(final_num)):
    if solve(nums[i],final_num[i]):
        valid_final_num.append(final_num[i])
        valid_nums.append(nums[i])
        
final_num = [x for x in final_num if x]
nums = [y for y in nums if y]    
ans = sum(valid_final_num)
print(ans)
input_data.close()