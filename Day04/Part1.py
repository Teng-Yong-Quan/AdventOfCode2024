def check_horizontal(string,word):
    count = 0
    for i in range(len(string)):
        for j in range(len(string[0])-3):
            sub = string[i][j] + string[i][j+1] + string[i][j+2] + string[i][j+3]
            if sub == word:
                count += 1
        for j in range(3,len(string[0])):
            sub = string[i][j] + string[i][j-1] + string[i][j-2] + string[i][j-3]
            if sub == word:
                count += 1
    return count
def check_vertical(string,word):
    count = 0
    for j in range(len(string[0])):
        for i in range(len(string)-3):
            sub = string[i][j] + string[i+1][j] + string[i+2][j] + string[i+3][j]
            if sub == word:
                count += 1
        for i in range(3,len(string)):
            sub = string[i][j] + string[i-1][j] + string[i-2][j] + string[i-3][j]
            if sub == word:
                count += 1
    return count
def check_right_diagonal(string,word):
    count = 0
    for i in range(len(string)-3):
        for j in range(len(string[0])-3):
            sub = string[i][j] + string[i+1][j+1] + string[i+2][j+2] + string[i+3][j+3]
            if sub == word or sub[::-1] == word:
                count += 1
    return count
def check_left_diagonal(string,word):
    count = 0
    for i in range(3,len(string)):
        for j in range(3,len(string[0])):
            sub = string[i][j-3] + string[i-1][j-2] + string[i-2][j-1] + string[i-3][j]
            if sub == word or sub[::-1] == word:
                count += 1
    return count     
input_data = open('/home/advent-of-code-2024/Day04/advent_of_code_4.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
ans = check_horizontal(input_data_lst, 'XMAS') + check_vertical(input_data_lst, 'XMAS') + check_right_diagonal(input_data_lst, 'XMAS') + check_left_diagonal(input_data_lst, 'XMAS')
print(ans)
input_data.close()
