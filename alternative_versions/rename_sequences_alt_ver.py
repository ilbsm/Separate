import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-R", help='Recursive search')

args = parser.parse_args()

# ---------------------------------------------------------------------------------------------


def renaming_process(filename):
    prefix = filename
    if '.txt' in filename:
        prefix = filename.split('.')[-2]
    prefix2 = prefix
    if '/' in prefix2:
        prefix2 = prefix2.split('/')[-1]
    zapis = open('.%s_renamed.txt' % prefix, 'w')
    num_lines = sum(1 for line in open(filename))
    with open(filename) as file:
        for i in range(num_lines):
            line = file.readline()
            if '>' in line:
                newline = re.sub('>', '>%s_' % prefix2, line)
                zapis.write(newline)
            else:
                zapis.write(line)
    zapis.close()


# ---------------------------------------------------------------------------------------------

if args.F:
    renaming_process(args.F)
elif args.R:
    list_of_files = os.listdir(args.R)
    for i in list_of_files:
        if 'renamed' not in i:
            renaming_process('%s/%s' % (args.R, i))

