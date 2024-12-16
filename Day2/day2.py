safe_reports_count = 0
with open('Day2/input_day2.txt') as file:
  for line in file:
    line = line.split()
    test_list = [int(elem) for elem in line]
    if sorted(test_list) == test_list or test_list == sorted(test_list, reverse=True):
      temp_list = []
      for i in range(len(test_list)-1):
        if abs(test_list[i] - test_list[i+1]) <= 3 and abs(test_list[i] - test_list[i+1]) >= 1:
          temp_list.append(test_list[i])
        if len(temp_list) > len(test_list)-2:
          safe_reports_count += 1
print(safe_reports_count)


