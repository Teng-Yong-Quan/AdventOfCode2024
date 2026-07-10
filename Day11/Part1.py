def dfs(num,string):
    if not string:
        return 0
    else:
        count = 0
        left,right,middle = '','',''
        if string == '0':
            middle = '1'
            count+=1
        elif not len(string)%2:
            half = len(string)//2
            left = str(int(string[:half]))
            right = str(int(string[half:]))
            count += 2
        else:
            num_int = int(string)
            middle = str(num_int*2024)
            count += 1
        if num == 1:
            return count
        elif num > 1:
            total = dfs(num-1,left) + dfs(num-1,right) + dfs(num-1,middle)
            return total

input_data = open('/home/advent-of-code-2024/Day11/advent_of_code_11.txt','r')
input_data_lst = [x.split() for x in input_data][0]
lst = input_data_lst.copy()
count = 0       
for j in range(len(lst)):
    count+= dfs(25,lst[j])    
print(count)
input_data.close()