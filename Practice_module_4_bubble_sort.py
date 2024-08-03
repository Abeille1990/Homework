nums = [4, 6, 3, 8, 3, 9, 1, 2, 5, 7]


def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


bubble_sort(nums)

print(nums)
