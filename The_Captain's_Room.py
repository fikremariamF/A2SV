# Enter your code here. Read input from STDIN. Print output to STDOUT
families = int(input())

hotel = input()
hotel = hotel.split()

mydict = dict()
for value in hotel:
    mydict[value] = mydict.get(value, 0) + 1
    
for value in mydict:
    if mydict[value] == 1:
        print(value)
    
