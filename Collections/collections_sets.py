
cars_set = {"Nissan", "BMW", "Honda"}
print(cars_set)

#How to insert new item in a set?

cars_set.add('Eric')
print(cars_set)

#How to remove item from a set?

cars_set.remove('Eric')
print(cars_set)

#How to insert multiple item in a set?

cars_set.update({'Suzuki', 'Toyota'})
print(cars_set)

#We can't print an item using indexes in Sets

#print(cars_set[0]) # will throw an error


#Check for a item in a set…
if "one" in cars_set:
    print("Found")
else:
    print("Not found")

print(len(cars_set)) # print length of a set


#Join two set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


cars_set.clear()  # will clear/remove all items in the set
print(cars_set)

del cars_set # will delete set
print(cars_set) # will give error
