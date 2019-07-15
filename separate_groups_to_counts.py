import argparse
import os


'''
Seperate CLANS groups files to counts.
'''


parser = argparse.ArgumentParser()

parser.add_argument("-G", help='Folder name with groups files', default='groups')
parser.add_argument("-S", help='Folder name with separated files', default='Pliki_z_separate')
parser.add_argument("-N", help='Number of counts', default='2')

args = parser.parse_args()

separate_list_of_files = os.listdir(args.S)
correct_list_with_separate = []
for i in separate_list_of_files:
    if f'_{int(args.N)}_' in i:
        if f'_f.' not in i:
            correct_list_with_separate.append(i)

for i0 in range(len(correct_list_with_separate)):
    temp_seq = ''
    filename = correct_list_with_separate[i0]
    num_lines = sum(1 for line in open(f'{args.S}/{filename}'))
    with open(f'{args.S}/{filename}') as file_line:
        temp_seq = ''
        sequences = []
        names = []
        values_start = []
        values_end = []
        for i in range(num_lines):
            dana_linia = file_line.readline()
            dana_linia = dana_linia.rstrip()
            if '>' in dana_linia:
                if temp_seq:
                    sequences.append(temp_seq)
                    temp_seq = ''
                temp = dana_linia.lstrip('>')
                names.append(temp.split('/')[0])
                values_start.append(int(temp.split('/')[1].split('-')[0]))
                values_end.append(int(temp.split('/')[1].split('-')[1]))
            else:
                temp_seq += dana_linia
        sequences.append(temp_seq)

    summary = {}
    for i in range(len(names)):
        if names[i] not in summary:
            temp_list = [[values_start[i], values_end[i], i, sequences[i]]]
            for i1 in range(i + 1, len(names)):
                if names[i] == names[i1]:
                    temp_list.append([values_start[i1], values_end[i1], i1, sequences[i1]])
            summary[names[i]] = temp_list

    lista_plikow = os.listdir(args.G)
    for i in range(len(lista_plikow)):
        num_lines = sum(1 for line in open(f'{args.G}/{lista_plikow[i]}'))
        with open(f"{args.G}/{lista_plikow[i]}") as nazwa_pliku:
            zapis = open(f'{args.G}_separated/{lista_plikow[i].split(".")[0]}_{args.N}_{chr(65 + i0)}.txt', 'w')
            for i1 in range(num_lines):
                linia_pliku = nazwa_pliku.readline().rstrip()
                if '>' in linia_pliku:
                    try:
                        zapis.write(f"{linia_pliku}/{summary[linia_pliku.lstrip('>')][0][0]}-{summary[linia_pliku.lstrip('>')][0][1]}\n")
                        zapis.write(f"{summary[linia_pliku.lstrip('>')][0][3]}\n")
                    except KeyError:
                        print(f'Warning: {linia_pliku} not found!')
                        continue
            zapis.close()
