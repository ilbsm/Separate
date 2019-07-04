import numpy as np
from matplotlib import pyplot as plt
import random
import time
file = open('PF01699_full.txt').readlines()
file = [i.rstrip() for i in file]


starts = []
ends = []
maxi = 0
temp = ''
sequences = []
for i in range(len(file)):
    if '>' in file[i]:
        if temp:
            sequences.append([name_temp, temp])
            temp = ''
        name_temp = file[i]
        start, end = file[i].split('/')[1].split('-')
        starts.append(int(start))
        ends.append(int(end))
        # print(start, end)
        if int(end) > maxi:
            maxi = int(end)
    else:
        temp += file[i]
sequences.append([name_temp, temp])


# x_ticks = np.arange(1, maxi, 400)
# starts_y_axis = [random.random() for i in range(len(starts))]
# ends_y_axis = [random.random() + 2 for i in range(len(ends))]
# plt.figure(figsize=(12, 3))
# plt.scatter(starts, starts_y_axis, s=0.2)
# plt.scatter(ends, ends_y_axis, s=0.2)
# plt.yticks([0.5, 2.5], ['start', 'end'])
# plt.xticks(x_ticks)
# plt.show()

names = []
values_start = []
values_end = []
for i in range(len(file)):
    if '>' in file[i]:
        temp = file[i].lstrip('>')
        names.append(temp.split('/')[0])
        values_start.append(int(temp.split('/')[1].split('-')[0]))
        values_end.append(int(temp.split('/')[1].split('-')[1]))

czas = time.time()
summary = {}
# # # {name: [[start, end, id], [start, end, id]]} - sort by start position
for i in range(len(names)):
    if names[i] not in summary:
        temp_list = [[values_start[i], values_end[i], i]]
        count = 1
        # print(i)
        for i1 in range(i + 1, len(names)):
            if names[i] == names[i1]:
                count+=1
                temp_list.append([values_start[i1], values_end[i1], i1])
        temp_list.sort(key=lambda i: i[0])
        summary[names[i]] = temp_list
        # print(i, summary)

# # # maxcount = 8 (Tyle powtórzeń o tej samej nazwie)
print(time.time()-czas)


A_part = open('PF01699_2_A.txt', 'w')
B_part = open('PF01699_2_B.txt', 'w')
for i in summary:
    if len(summary[i]) == 2:
        A_part.write(f'{sequences[summary[i][0][2]][0]}\n')
        A_part.write(f'{sequences[summary[i][0][2]][1]}\n')
        B_part.write(f'{sequences[summary[i][1][2]][0]}\n')
        B_part.write(f'{sequences[summary[i][1][2]][1]}\n')


