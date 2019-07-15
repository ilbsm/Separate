import argparse
import os


'''
Filters sequences by their length (number of letters). It helps to filter longer or shorter seq than average but will
not filter if seq is missing some part but is longer in other while length stays similar to others. 
'''


parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-A", help='More or less than average')
parser.add_argument("-R", help='Recursive search')

args = parser.parse_args()

def Iterate(filename):
    values = []
    counter = 0
    num_lines = sum(1 for line in open(f'%s' % filename))
    with open('%s' % filename) as file_line:
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

    zapis = open("%s_filter.txt" % (filename.split('.')[0]), 'w')
    with open('%s' % filename) as file_line:
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
        Iterate("%s/%s" %(args.R, i))
else:
    print('No file/folder!')


