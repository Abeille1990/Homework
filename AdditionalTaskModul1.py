grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

if len(grades) == len(students) :
  print(list(students))
else:
  print("number of students does't match grades lists")

students_list = list(students)
print(sorted(students_list))

grades_m= []
a=0
while a < len(students_list):
  s = sum(grades[a])/len(grades[a])
  a +=1
  grades_m.append(s)

print(grades_m)

print(dict(zip(sorted(students_list), grades_m)))

