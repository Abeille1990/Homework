nums = [4, 6, 3, 8, 3, 9, 1, 2, 5, 7]


def selection_sort(ls):

    for i in range(len(ls)):
        lowest = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


selection_sort(nums)

print(nums)
