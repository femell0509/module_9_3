first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_second = list(zip(first, second))
print(first_second)

first_result = (len(x)-len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
second_result_2 = (len(x)==len(y) for x, y in zip(first, second))
print(list(second_result_2))