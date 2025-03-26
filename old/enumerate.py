'''
The enumerate method add a counter to an iterable and returns it as object

Syntax: enumerate(iterable, start=0)
'''

language =['py','jv','c']
enumerate_me = enumerate(language)

print(list(enumerate_me))
#print(type(enumerate_me))

#output : [(0, 'py'), (1, 'jv'), (2, 'c')]
#output: <class 'enumerate'>

###################

#Looping over enumerate

for each in enumerate(language) :
	print(each)

for i,each in enumerate(language) :
	print(i,each)


for each in enumerate_me :
	print(each)
	# would generate blank 
	'''
	>>> e = enumerate(range(4))
>>> list(e)
[(0, 0), (1, 1), (2, 2), (3, 3)]
>>> list(e)
[]

It is an iterator once end i s reached it does not shows the beginning item 
e.next() StopIteration

'''