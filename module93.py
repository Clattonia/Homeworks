first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


result1 = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

result_list = list(result1)
print(result_list)
    
result2 = (len(f) == len(s) for f, s in zip(first, second))

result_list = list(result2)
print(result_list)