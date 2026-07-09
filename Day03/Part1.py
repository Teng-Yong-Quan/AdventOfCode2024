input_data = open('/home/advent-of-code-2024/Day03/advent_of_code_3.txt','r')
input_data_lst = ''.join(sum([x.split() for x in input_data],[]))
valid_mul_list = []
mul_index_lst = [i for i in range(len(input_data_lst)) if input_data_lst.startswith("mul(", i)]
index,finalised_index = 0,0
while index < len(input_data_lst):
    if mul_index_lst:
        if index == mul_index_lst[finalised_index]:
            string = 'mul('
            index += 4
            num = 0
            while num < 8:
                if index + num >= len(input_data_lst):
                    break
                if num < 3 and input_data_lst[index + num].isdigit():
                    string += input_data_lst[index + num]
                    num += 1
                    continue
                elif 0 < num <= 3 and input_data_lst[index + num] == ',':
                    string += input_data_lst[index + num]
                    num += 1
                    continue
                elif 1 < num < 7 and input_data_lst[index + num].isdigit() and ',' in string:
                    string += input_data_lst[index + num]
                    num += 1
                    continue
                elif 2 < num <= 7 and input_data_lst[index + num] == ')' and ',' in string:
                    string += input_data_lst[index + num]
                    valid_mul_list.append(string)
                    break
                else:
                    break
            finalised_index += 1
            if finalised_index >= len(mul_index_lst):
                break
            else:
                index = mul_index_lst[finalised_index]
        else:
            index += 1
    else:
        break
       
         
valid_mul_list = list(map(lambda x : x.split(','),list(map(lambda x : x[4:-1],valid_mul_list))))
ans = sum(list(map(lambda x : int(x[0])*int(x[1]),valid_mul_list)))
print(ans)
input_data.close()