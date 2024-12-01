
string_addition = 'a' + 'a'


maximum = max([1, 2, 3 ,4 ])

#print(maximum)


measurements = [20, 56, 34, 46, 120, 2]

# Remove the smallest and largest values.
measurements.remove(max(measurements))
measurements.remove(min(measurements))

measurements.sort()
#print(measurements == [20, 34, 46, 56])


#using tuples

some_numbers = (1, 2, 3, 4)

#some_numbers[1] = 5
#print(some_numbers[1])


# using dicts
treasure_locations = {
          (2, 3): "gold",
            (3, 5): "silver",
              (1, 4): "bronze"
              }

coordinates = (3, 5)

# What's at this location?
print(treasure_locations[coordinates])



#Tuples of lists - unpacking


shopping_list = [
        (3 ,"banana")
        (2, "milk"),
        (1, "bread"), ]
