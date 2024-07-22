calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):

    count_calls()
    return(len(string), string.upper(), string.lower())

print(string_info("Capybara"))
print(string_info("Armagedon"))

def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower() # преобразование в переменной string
    lower_list = [item.lower() for item in list_to_search]
    return lower_string in lower_list

print(is_contains('Urban', ['ban', 'BaNaN', 'UrBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
