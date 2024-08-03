# first_field = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# n = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

result = []

n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if n % (i+j) == 0 and j > i:
            result.append(i)
            result.append(j)

result1 = ""
for p in result:
    result1 += str(p)
print('Шифр: ', result1)
