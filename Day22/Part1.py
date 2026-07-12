def mix(secret_num, result):
	return secret_num ^ result

def prune(secret_num):
	return secret_num % 16777216

def first_step(secret_num):
	result = 64 * secret_num
	return prune(mix(secret_num, result))

def second_step(secret_num):
	result = secret_num // 32
	return prune(mix(secret_num, result))

def third_step(secret_num):
	result = secret_num * 2048
	return prune(mix(secret_num, result))
	
input_data = open('/home/advent-of-code-2024/Day22/advent_of_code_22.txt','r')
input_data_lst = [int(x.replace('\n','')) for x in input_data]
for i in range(2000):
	for j in range(len(input_data_lst)):
		secret_num = input_data_lst[j]
		input_data_lst[j] = third_step(second_step(first_step(input_data_lst[j])))
ans = sum(input_data_lst)
print(ans)
input_data.close()