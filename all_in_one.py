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
        print(name)
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
        print(name)
        os.system(f'python3 formatting.py -F files_from_full_seq_extract_n_counts/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Running CLANS...')
print('###########################################################')
print('###########-----------------!!!-----------------###########')
print('#########-------------------!!!-------------------#########')
print('#######---------------------!!!---------------------#######')
print('#####                                                 #####')
print('###                                                     ###')
print('#-------------------------WARNING-------------------------#')
print('#----REMEMBER TO SAVE FINISHED RUN AND CREATE GROUPS!!!---#')
print('###                                                     ###')
print('#####                                                 #####')
print('#######---------------------!!!---------------------#######')
print('#########-------------------!!!-------------------#########')
print('###########-----------------!!!-----------------###########')
print('###########################################################')
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
        print(name)
        os.system(f'python3 formatting.py -F files_from_separate_groups_to_counts/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Filtering...')
for i in os.listdir('files_from_separate_groups_to_counts'):
    if i != 'format':
        name = i
        print(name)
        os.system(f'python3 advanced_filter_by_value.py -F files_from_separate_groups_to_counts/{i}')
print('Done!')

print('Formatting...')
for i in os.listdir('files_from_advanced_filter_by_value'):
    if i != 'format':
        name = i
        print(name)
        os.system(f'python3 formatting.py -F files_from_advanced_filter_by_value/{i}')
print('Done!')

# --------------------------------------------------------------------------------------------------------


print('Creating hhm files...')
for i in os.listdir('files_from_advanced_filter_by_value'):
    if i != 'format':
        name = i
        print(name)
        os.system(f'hhmake -i files_from_advanced_filter_by_value/{i} -o ./advfil_hhm/{i.split(".")[0]}.hhm -M 50')
print('Done!')

print('Creating all.hhms file...')
os.system('cd advfil_hhm')
os.system('cat advfil_hhm/*hhm > advfil_hhm/all.hhms')
print('Done!')

# --------------------------------------------------------------------------------------------------------


print('Creating hhr files...')
for i in os.listdir('advfil_hhm'):
    if i != 'all.hhms':
        name = i
        print(name)
        os.system(f'hhsearch -i ./advfil_hhm/{name} -d ./advfil_hhm/all.hhms -o ./advfil_hhr/{name.split(".")[0]}.hhr')
print('Done!')

# --------------------------------------------------------------------------------------------------------


print('Preparing 2nd part of clans...')
os.system("python3 to_CLANS_part_2.py ./advfil_hhr/ > repeats_profiles_compare")

print('Done!')

print('Opening CLANS...')
os.system(f'java -Xmx16384m -jar {args.C} repeats_profiles_compare')
print('Done!')

# --------------------------------------------------------------------------------------------------------

print('Finished!')
