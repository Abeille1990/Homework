#Dictionaries
print("TASK Dictionaries:")
my_dic = {'Ann':1990,'Peter':1984,"Paul":1991}
print("Dict: ",my_dic)
print("Exsisting value:",my_dic.get("Ann"))
print("Not existing value: ",my_dic.get("Helen"))
my_dic.update({"Mary":1985,"Bob":1987})
a = my_dic.pop("Ann")
print("Deleted value: ",a)
print("Modifyed dictionary: ",my_dic)
print("_______________________")
#Sets
print("TASK Sets:")
my_set = {1,2,3,4,True,"Ann","Paul","Ann",3,4} #почему элемент True не выводится на экран? Видела в примере в лекции такой вприант, там тоже не выводилось, этот тип данных вообще не нужно использовать во множествах? не понимаю какую смысловую нагрузку он несет
print("Set: ",my_set)
my_set.add("Marysya")
my_set.add((1,2,3))
my_set.remove("Ann") # почему нельзя удалить через индекс ".remove [1]"? выдает ошибку про неизменяемый элемент
print("Modyfied set: ", my_set)

