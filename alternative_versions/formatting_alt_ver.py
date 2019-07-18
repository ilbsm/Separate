import argparse
import os


'''
Delete all gaps and convert names.
'''


parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-S", help='Substitute character')
parser.add_argument("-R", help='Recursive formatting - all files in folder will be formatted, use instead of -F flag')

args = parser.parse_args()


def Iteration(filename, new_character):
    num_lines = sum(1 for line in open('%s.txt' % filename))
    nowy = open(f'%s/format/%s_f.txt' % (filename.split("/")[0], filename.split("/")[-1]), 'w')
    with open('%s.txt' % filename) as filename:
        for i in range(num_lines):
            linia_pliku = filename.readline()
            temp = ''
            if '>' in linia_pliku:
                for i1 in linia_pliku:
                    if i1 == '/' or i1 == '-':
                        temp += new_character
                    else:
                        temp += i1
            else:
                for i1 in linia_pliku:
                    if i1 != '-':
                        temp += i1
            nowy.write(temp)
    nowy.close()


new_character = '_'
if args.S:
    new_character = str(args.S)
if args.R:
    listaplikow = os.listdir(args.R)
    for i in listaplikow:
        if '_f.txt' not in i:
            if i != 'format':
                Iteration('%s/%s' % (args.R, i.split(".")[0]), new_character)
elif args.F:
    filename = args.F
    if '.' in filename:
        filename = filename.split(".")[0]
    Iteration(filename, new_character)
else:
    print('No file or folder')
    exit()
