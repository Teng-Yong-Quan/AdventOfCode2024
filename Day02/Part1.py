def check_safe(lst):
    diff_lst = []
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        diff_lst.append(diff)
    decrease = list(map(lambda x : -3 <= x <= -1, diff_lst))
    increase = list(map(lambda x : 1 <= x <= 3, diff_lst))
    if False not in decrease and lst == sorted(lst, reverse = True):
        return True
    elif False not in increase and lst == sorted(lst):
        return True
    return False

input_data = open('/home/advent-of-code-2024/Day02/advent_of_code_2.txt','r')
input_data_lst = [[int(y) for y in x.split(' ')] for x in input_data]
print(sum(map(check_safe,input_data_lst)))
input_data.close()