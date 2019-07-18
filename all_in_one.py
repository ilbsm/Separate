import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-C", help='Directory to CLANS')
parser.add_argument("-P", help='File from Pfam directory')
parser.add_argument("-F", help='File name with full sequences')

args = parser.parse_args()


print('Separating counts...')
os.system('python3 separate_Pfam_to_counts.py -F %s' % args.P)
print('Done!')

print('Formatting...')
for i in os.listdir('files_from_separate_Pfam_to_counts'):
    if i != 'format':
        name = i
        os.system(f'python3 formatting.py -F files_from_separate_Pfam_to_counts/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Extracting 2-repeats from full sequences...')
os.system(f'python3 full_seq_extract_n_counts.py -F {args.F} -S files_from_separate_Pfam_to_counts/{name}')
print('Done!')

print('Formatting...')
for i in os.listdir('files_from_full_seq_extract_n_counts'):
    if i != 'format':
        name = i
        os.system(f'python3 formatting.py -F files_from_full_seq_extract_n_counts/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Running CLANS...')
print('#-----------------------------!!!-----------------------------#')
print('#---------------------------WARNING---------------------------#')
print('#------REMEMBER TO SAVE FINISHED RUN AND CREATE GROUPS!!!-----#')
print('#-----------------------------!!!-----------------------------#')
input('Press any key to continue...')
os.system(f'java -Xmx16384m -jar {args.C} -infile {args.F} -blastpath "blastp -num_descriptions 300" -cpu 3 -verbose 0')
print('Done!')

input("Have you created groups in CLANS and put them into 'groups_from_CLANS' folder? If not open saved run to do so. Press any key if you are ready to continue...")
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Separating groups to counts...')
os.system('python3 separate_groups_to_counts.py')
print('Done!')

print('Formatting...')
for i in os.listdir('files_from_separate_groups_to_counts'):
    if i != 'format':
        name = i
        os.system(f'python3 formatting.py -F files_from_separate_groups_to_counts/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Filtering...')
for i in os.listdir('files_from_separate_groups_to_counts'):
    if i != 'format':
        name = i
        os.system(f'python3 advanced_filter_by_value.py -F files_from_separate_groups_to_counts/{i}')
print('Done!')

print('Formatting...')
for i in os.listdir('files_from_advanced_filter_by_value'):
    if i != 'format':
        name = i
        os.system(f'python3 formatting.py -F files_from_advanced_filter_by_value/{i}')
print('Done!')

print('Finished!')
