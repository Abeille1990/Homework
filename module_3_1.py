calls = 0
def count_calls():
    global calls
    calls += 1

for string in range(0, 2):
    def string_info(string):

        length = len(string)
        upper = string.upper()
        lower = string.lower()

        return length, upper, lower

    string = str(input())
    length, lower, upper = string_info(string)
    count_calls()
    print(calls)
    print((string_info(string)))

string = (input())
list_to_search = [(input()), (input()), (input())]
print(list_to_search)

for string in range(0,2):
    def it_contains(string, list_to_search):

        if string in list_to_search:
            print("True")
        else:
            print("False")

    count_calls()
    print(calls)

    it_contains(string,list_to_search)
