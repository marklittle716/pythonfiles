# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#create
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apple', "Oranges", 'Grapes'))

# A Set is a collection which is unordered and unindexed. No duplicate members.
print(fruits2[2])

# create set
fruit_set = {'apples', 'Oranges', 'Mango'}


#Check if in set
print('Grapes' in fruit_set)

#Add to set
fruit_set.add('Grape')

#Clear set
fruit_set.clear()
