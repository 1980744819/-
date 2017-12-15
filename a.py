import csv

file = open('1745264_seg_1.csv', 'r', encoding='UTF-8')
reader = csv.reader(file)
data = list(reader)
# print(data)
i = 0
numlist = set()
for item in data[1:]:
    print(i, ':', end=' ')
    print(item[7] + ',', end='\n')
    i += 1
    numlist.add(item[7])
i = 0
j = 0;
print(j)
for item in numlist:
    # print(i, ':', end=' ')
    print(item + '、', end='')
    i += 1
    if i == 50:
        j += 1
        # print('\n', j)
        i = 0
