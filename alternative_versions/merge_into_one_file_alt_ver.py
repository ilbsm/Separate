import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-R", help='Folder directory')
parser.add_argument("-O", help='Output file name', default='merged')

args = parser.parse_args()

# -------------------------------------------------------------------------------

zapis = open('%s.txt' % args.O, 'w')

list_of_files = os.listdir(args.R)
for filename in list_of_files:
    num_lines = sum(1 for line in open('%s/%s' % (args.R, filename)))
    with open('%s/%s' % (args.R, filename)) as file:
        for i in range(num_lines):
            zapis.write(file.readline())
zapis.close()
