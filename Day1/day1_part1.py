
list1 = []
list2 = []
total_distance = 0

# 1. Read file
f = open("input_day1.txt", "r")
lines = f.readlines()

# 2. Split string into two lists
for line in lines:
  x, y = line.split()
  list1.append(x.rstrip())
  list2.append(y.rstrip())

# 3. Sort list
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# 4. Loop through list
for list1, list2 in zip(sorted_list1, sorted_list2):   
# 5. Calculate distace
    distance = abs(int(list1)-int(list2))
# 6. Add difference 
    total_distance += distance

print(total_distance)
