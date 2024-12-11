similarity_score = 0
list1 = []
list2 = []

with open("Day1/input_day1.txt", "r") as file:
  for line in file:
    x, y = line.split()
    list1.append(int(x.rstrip()))
    list2.append(int(y.rstrip()))

# 1. Loop through the first  list
for elem in list1:
  if elem in list2:
    occurancy = list2.count(elem)
    similarity_score += occurancy * elem
print(similarity_score)









