task1
question_1 = None
while question_1 != '3':
	question_1 = input('Which python is better 2 or 3? ')

question_2 = None
while question_2 != '3.6':
	question_2 = input('What is the latest version of the python now? ')

question_3 = None
while question_3 != '1':
	question_3 = input('What will be printed: print(int(True))? ')
	
while True:
	a = input('enter the number ')
	if a.isdigit():
		a = int(a)
		break
b = None
c = None
while True:	
	b = input('enter the operation ')
	if b == '':
		break
	c = input('enter next number ')
	if c == '':
		break
	c = int(c)
	if b == '+':
		a = a + c
	elif b == '-':
		a = a - c 
	elif b == '*':
		a = a * c 
	elif b == '/':
		a = a / c 
	print(a) 
