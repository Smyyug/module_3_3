def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [4, 'cnhjrf', False]
values_dict = { 'a' : 3, 'b' : " предложение ", 'c' : False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [15, 'слово']
print_params(*values_list_2, 44)