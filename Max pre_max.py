s = input()
numbers = s.split(',')
maximum, pre_maximum = None, None
for c in numbers:
    if c == '' or c == ' ' or c == '\n':
        continue
    n = float(c)
    if maximum == None:
        maximum = n
    elif n >= maximum:
        pre_maximum = maximum
        maximum = n
    elif pre_maximum == None:
        pre_maximum = n
    elif n > pre_maximum:
        pre_maximum = n
print(f'First maximum: {maximum}')
print(f'Second maximum: {pre_maximum}')
