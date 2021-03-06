import numpy as np
from matplotlib import pyplot as plt
import random
import argparse

# -------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-P", help='Plot', action='store_true')
parser.add_argument("-M", help='Multi (more than 2)', action='store_true')

args = parser.parse_args()

# -------------------------------------------------------------------
if args.F:
    filename = args.F
    if '.' in filename:
        filename = filename.split(".")[0]
    file = open(f'{filename}.txt').readlines()
    file = [i.rstrip() for i in file]
else:
    print('No input file.')
    exit()

# -------------------------------------------------------------------
maxi = 0
temp_seq = ''
sequences = []
names = []
values_start = []
values_end = []
for i in range(len(file)):
    if '>' in file[i]:
        if temp_seq:
            sequences.append(temp_seq)
            temp_seq = ''
        temp = file[i].lstrip('>')
        names.append(temp.split('/')[0])
        values_start.append(int(temp.split('/')[1].split('-')[0]))
        values_end.append(int(temp.split('/')[1].split('-')[1]))
        if int(int(temp.split('/')[1].split('-')[1])) > maxi:
            maxi = int(int(temp.split('/')[1].split('-')[1]))
    else:
        temp_seq += file[i]
sequences.append(temp_seq)

if not args.P:
    summary = {}
    # # # {name: [[start, end, id, seq], [start, end, id, seq]]} - sort by start position
    for i in range(len(names)):
        if names[i] not in summary:
            temp_list = [[values_start[i], values_end[i], i, sequences[i]]]
            for i1 in range(i + 1, len(names)):
                if names[i] == names[i1]:
                    temp_list.append([values_start[i1], values_end[i1], i1, sequences[i1]])
            temp_list.sort(key=lambda i: i[0])
            summary[names[i]] = temp_list

# # # maxcount = 8 (Tyle maksymalnie powtórzeń o tej samej nazwie)

# -----------------------------------------------------------------------
if args.P:
    x_ticks = np.arange(1, maxi, 400)
    starts_y_axis = [random.random() for i in range(len(values_start))]
    ends_y_axis = [random.random() + 2 for i in range(len(values_end))]
    plt.figure(figsize=(12, 3))
    plt.scatter(values_start, starts_y_axis, s=0.2)
    plt.scatter(values_end, ends_y_axis, s=0.2)
    plt.yticks([0.5, 2.5], ['start', 'end'])
    plt.xticks(x_ticks)
    plt.show()

# -----------------------------------------------------------------------
if not args.P:
    if args.M:
        max_counts = len(summary[max(summary, key=lambda i: len(summary[i]))])
        for i in range(max_counts+1):
            if i != 0:
                list_of_files = [f'{filename}_{i}_{chr(65 + i1)}.txt' for i1 in range(i)]
                # for i1 in list_of_files:
                opened_files = [open(i2, 'w') for i2 in list_of_files]
                for i2 in summary:
                    if len(summary[i2]) == i:
                        for i3 in range(i):
                            opened_files[i3].write(f'>{i2}/{summary[i2][i3][0]}-{summary[i2][i3][1]}\n')
                            opened_files[i3].write(f'{summary[i2][i3][3]}\n')
                for i4 in opened_files:
                    i4.close()
    else:
        A_part = open(f'{filename}_2_A.txt', 'w')
        B_part = open(f'{filename}_2_B.txt', 'w')
        for i in summary:
            if len(summary[i]) == 2:
                A_part.write(f'>{i}/{summary[i][0][0]}-{summary[i][0][1]}\n')
                A_part.write(f'{summary[i][0][3]}\n')
                B_part.write(f'>{i}/{summary[i][1][0]}-{summary[i][1][1]}\n')
                B_part.write(f'{summary[i][1][3]}\n')

