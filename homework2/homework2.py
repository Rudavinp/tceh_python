#task1
questions = {
'Which python is better 2 or 3? ': ['3', '3.6'],
'What is the latest version of the python now? ': ['3.6', '3.6.4'],
'What will be printed: print(int(True))? ': ['1', 'one'],
}

answer = None
for key in questions:
	while answer not in questions[key]:
		answer = input(key)
		

#task2
string = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque \
 laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto \
 beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut \
 dit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. \
 Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit,\
 sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat \
 voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit \
 laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit \
 qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum \
 fugiat quo voluptas nulla pariatur?"

# пусто словарь для хранения пар {слово: кол-во повторений в тексте}
dict_words = {}
# цикл for убирает все знаки препинания заменяя их пустой строкой							
for i in ['.', ',', '?']:					
	string = string.replace(i, '')
# разбить текст на слова по пробелам, удаляя пустые символы
# добавить слова в dict_words
strings = string.split(' ')
for item in strings:
	if item == '':
		strings.remove(item)
	else:
		dict_words[item] = strings.count(item)
# пустые списки для хранения 10-ти слов которые надо вывести
# и список для хранения кол-ва повторяющихся слов
list_words = []
list_values = []
# заполняем список с кол-вом повторяющихся слов, сортируем его и разворачиваем
# что бы наибольшие значения стояли в начале списка
for value in dict_words.values():
	if value not in list_values:
		list_values.append(value)
list_values.sort()
list_values.reverse()
# итерируемся по списку list_value и по дикту dict_words
# добовляем в конечный список слов все слова значения которых встречаются в списке list_value
# начиная с наибольшего, пока в списке list_words не будет десять слов
for i in list_values:
	for key, value in dict_words.items():
		if len(list_words) == 10:
				break
		if i == value:
			list_words.append(str(key) + ' ' + str(value))
 
# выводим топ-10 слов
for i in list_words:
	print(i)

        





	

