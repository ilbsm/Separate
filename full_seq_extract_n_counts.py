import argparse


'''
While file downloaded from Pfam may contain sequences with other number than n repeats (for example 2), this program
will filter only interesting ones.
'''


parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name with full sequences')
parser.add_argument('-S', help='Separated file')
parser.add_argument("-N", help='Number of repeats', default='2')

args = parser.parse_args()

if args.F:
    filename_f = args.F
else:
    print('No full seq file')
    exit()

if args.S:
    filename_s = args.S
else:
    print('No separated file')
    exit()

num_lines = sum(1 for line in open(f'{args.F}'))

with open(f'{args.F}') as file_line:
    temp_seq = ''
    sequences = []
    names = []
    for i in range(num_lines):
        dana_linia = file_line.readline()
        dana_linia = dana_linia.rstrip()
        if '>' in dana_linia:
            if temp_seq:
                sequences.append(temp_seq)
                temp_seq = ''
            temp = dana_linia.lstrip('>')
            names.append(temp)
        else:
            temp_seq += dana_linia
    sequences.append(temp_seq)

summary = {}
# # # {name: [[start, end, id, seq], [start, end, id, seq]]} - sort by start position
for i in range(len(names)):
    if names[i] not in summary:
        temp_list = sequences[i]
        for i1 in range(i + 1, len(names)):
            if names[i] == names[i1]:
                temp_list.append(sequences[i1])
        summary[names[i]] = temp_list

if '.' in filename_f:
    new_name = filename_f.split('.')[0]
else:
    new_name = filename_f
if '/' in new_name:
    new_name = new_name.split('/')[-1]
zapis = open(f'files_from_full_seq_extract_n_counts/{new_name}_{str(args.N)}.txt', 'w')
with open(f'{args.S}') as nazwa_pliku:
    for i in range(num_lines):
        linia_pliku = nazwa_pliku.readline()
        if '>' in linia_pliku:
            if '/' in linia_pliku:
                seq_name = linia_pliku.split('/')[0].lstrip('>').rstrip()
                if seq_name in summary:
                    zapis.write(f'>{seq_name}\n')
                    zapis.write(f'{summary[seq_name]}\n')
zapis.close()
