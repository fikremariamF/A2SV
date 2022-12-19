# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
a = int(input())
mylist = []
counter = 0
while counter < a:
    inp = input()
    mylist.append(inp)
    counter += 1
    
mydict = OrderedDict()
for value in mylist:
    mydict[value] = mydict.get(value,0) + 1
print(len(mydict))
for value in mydict:
    print(mydict[value], end= " ")
