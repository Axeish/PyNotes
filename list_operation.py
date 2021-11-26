# Defining list 
object= None
list_1 = []
list_2=list()
'''
diff list() vs []

- [] is faster 
- list() needs to look at function name , global lookup and function call
-list() on string creates list object while [] conversts to list
'''

slist = ["apple"]
blist = list("apple")
print(blist, slist)