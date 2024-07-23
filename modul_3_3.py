def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, 'куку', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, True, 'Hello']
values_dict = { 'a': 1, 'b': True, 'c': 'Hello'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [55.34,'String']
print_params(*values_list_2, 42)