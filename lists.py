#lists


mylist = ['string',1,2,3,True,[1,2,3]]

#print(len(mylist))

#print(mylist[1:])

#mylist[0] = 'New Item'

#print(mylist[:2])

mylist.append('New Item')

#print(mylist)

listwo = ['x','y','z']

mylist.extend(listwo)

#print(mylist)

mylist.reverse()

#print(mylist)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]

print(first_col)
