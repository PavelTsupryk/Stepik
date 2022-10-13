line = input()
cost_line = 60
number = len(line)
rubl = (number * cost_line) // 100
penn = (number * cost_line) % 100
print(rubl, 'р.', penn, 'коп.')
