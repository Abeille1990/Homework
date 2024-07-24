def single_root_words (root_word, *other_words):
    same_words = []
    root_word_upper = root_word.upper()

    for i in other_words: # перебираем кажое слово в множестве Other_words и как бы определяем каждую единицу переменной i
        i.upper() # переводим все слова в верхний регистр для игнорирования регистра
        if root_word_upper in i.upper() or i.upper() in root_word_upper: # выполняем поиск слов, которые или содержат
            # коренное слово содержит в себе слово из списка
            same_words.append(i)

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


