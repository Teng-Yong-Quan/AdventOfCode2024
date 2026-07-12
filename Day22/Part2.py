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
buyers_lst = []
for i in range(len(input_data_lst)):
	buyer_lst = [input_data_lst[i] % 10]
	secret_num = input_data_lst[i]
	for j in range(2000):
		secret_num = third_step(second_step(first_step(secret_num)))
		buyer_lst.append(secret_num % 10)
	buyers_lst.append(buyer_lst)
price_intervals_lst = []
for i in range(len(buyers_lst)):
	price_intervals = []
	for j in range(len(buyers_lst[i]) - 1):
		price_intervals.append(buyers_lst[i][j+1] - buyers_lst[i][j])
	price_intervals_lst.append(price_intervals)
overall = {}
for i in range(len(buyers_lst)):
	curr_price_interval = price_intervals_lst[i]
	current_buyer = buyers_lst[i]
	occurrences_dict = {}
	for j in range(len(curr_price_interval) - 3):
		k = tuple(curr_price_interval[j:j+4])
		if k not in occurrences_dict:
			occurrences_dict[k] = current_buyer[j+4]
			if k not in overall:
				overall[k] = 0
			overall[k] += current_buyer[j+4]
print(max(overall.values()))
input_data.close()