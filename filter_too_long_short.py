import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-A", help='More or less than average')
parser.add_argument("-R", help='Recursive search')

args = parser.parse_args()

def Iterate(filename):
    values = []
    counter = 0
    num_lines = sum(1 for line in open(f'{filename}'))
    with open(f'{filename}') as file_line:
        for i in range(num_lines):
            linia_pliku = file_line.readline()
            if '>' not in linia_pliku:
                for i1 in linia_pliku:
                    if i1 != '-':
                        counter += 1
            else:
                if counter:
                    values.append(counter)
                    counter = 0
        values.append(counter)

    average = sum(values) / len(values)
    average = int(average)

    more_less = int(args.A)

    zapis = open(f"{filename.split('.')[0]}_filter.txt", 'w')
    with open(f'{filename}') as file_line:
        for i in range(num_lines):
            linia_pliku = file_line.readline()
            if '>' in linia_pliku:
                name = linia_pliku
            else:
                counter = 0
                for i1 in linia_pliku.rstrip():
                    if i1 != '-':
                        counter += 1
                if average - more_less < counter < average + more_less:
                    zapis.write(name)
                    zapis.write(linia_pliku)


if args.F:
    Iterate(args.F)
elif args.R:
    raw_list = os.listdir(args.R)
    new_list = []
    for i in raw_list:
        if '_filter.txt' not in i:
            new_list.append(i)
    for i in new_list:
        Iterate(f"{args.R}/{i}")
else:
    print('No file/folder!')
