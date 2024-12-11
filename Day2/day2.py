helper_dict = {}
safe_reports_count = 0
with open('Day2/test_input.txt') as file:
  for line in file:
    line = line.split()
    test_list = [int(elem) for elem in line]
    if sorted(test_list) == test_list or test_list == sorted(test_list, reverse=True):
      for i in range(len(test_list)-1):
        if abs(test_list[i] - test_list[i+1]) <= 3 and abs(test_list[i] - test_list[i+1]) >= 1:
          safe_reports_count += 1
print(safe_reports_count)


