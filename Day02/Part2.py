def check_safe(lst):
    for i in range(len(lst)):
        modified_lst = lst[:i] + lst[i+1:]
        diff_lst = []
        for j in range(1,len(modified_lst)):
            diff = modified_lst[j] - modified_lst[j-1]
            diff_lst.append(diff)
        decrease = list(map(lambda x : -3 <= x <= -1, diff_lst))
        increase = list(map(lambda x : 1 <= x <= 3, diff_lst))
        if False not in decrease and modified_lst == sorted(modified_lst, reverse = True):
            return True
        elif False not in increase and modified_lst == sorted(modified_lst):
            return True
    return False

input_data = open('/home/advent-of-code-2024/Day02/advent_of_code_2.txt','r')
input_data_lst = [[int(y) for y in x.split(' ')] for x in input_data]
print(sum(map(check_safe,input_data_lst)))
input_data.close()