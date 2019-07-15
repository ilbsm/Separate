import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-R", help='Recursive search')
parser.add_argument("-M", help='Error margin', default=0.4)
parser.add_argument("-A", help='Acceptable number of errors', default=10)
parser.add_argument("-O", help='Detailed output', action='store_true')

args = parser.parse_args()


def iterate(filename, margin, acceptable):
    num_lines = sum(1 for line in open(f'%s' % filename))
    with open('%s' % filename) as file_line:
        lista_wartosci = []
        for i in range(num_lines):
            linia_pliku = file_line.readline().rstrip()
            if '>' not in linia_pliku:
                for i1 in range(len(linia_pliku)):
                    try:
                        if linia_pliku[i1] == '-':
                            lista_wartosci[i1].append(0)
                        else:
                            lista_wartosci[i1].append(1)
                    except IndexError:
                        if linia_pliku[i1] == '-':
                            lista_wartosci.append([0])
                        else:
                            lista_wartosci.append([1])

    for i in range(len(lista_wartosci)):
        lista_wartosci[i] = sum(lista_wartosci[i]) / len(lista_wartosci[i])

    with open('%s' % filename) as file_line:
        zapis = open('%s_advfil.txt' % filename.split('.')[0], 'w')
        if args.O:
            print('Filename: %s' % filename)
            print('%4s %5s %30s %s' % ('err', 'line', 'name', 'seq'))
        for i in range(num_lines):
            linia_pliku = file_line.readline().rstrip()
            if '>' not in linia_pliku:
                mistake_count = 0
                for i1 in range(len(linia_pliku)):
                    if linia_pliku[i1] == '-':
                        if lista_wartosci[i1] >= 1 - margin:
                            mistake_count += 1
                    else:
                        if lista_wartosci[i1] <= margin:
                            mistake_count += 1
                if mistake_count > acceptable:
                    if args.O:
                        print('%4s %5s %30s %s' % (mistake_count, i, name, linia_pliku))
                else:
                    zapis.write('%s\n' % name)
                    zapis.write('%s\n' % linia_pliku)
            else:
                name = linia_pliku


if args.F:
    iterate(args.F, float(args.M), int(args.A))
elif args.R:
    raw_list = os.listdir(args.R)
    new_list = []
    for files in raw_list:
        if '_f.txt' not in files:
            if '_filter.txt' not in files:
                if '_advfil.txt' not in files:
                    new_list.append(files)
    for files in new_list:
        iterate("%s/%s" % (args.R, files), float(args.M), int(args.A))
else:
    print('No file/folder!')
