input_data = open('/home/advent-of-code-2024/Day01/advent_of_code_1.txt','r')
input_data_lst = [[int(y) for y in x.split()] for x in input_data]
lst_1 = sorted([x[0] for x in input_data_lst])
lst_2 = sorted([x[1] for x in input_data_lst])
sum_diff = sum(map(lambda x,y: abs(x-y),lst_1,lst_2))
print(sum_diff)
input_data.close()