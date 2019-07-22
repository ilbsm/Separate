# Separate

If original scripts (in master folder) will not work, try to copy paste scripts from alternative_version folder to master and use them instead. 


## Dependencies
Program tested on Linux Ubuntu 18.04.2. Should be also working on Windows however it's not recommended.

Those scripts need [Python3](https://www.python.org/) and are using those libraries (they should be built-in):
* argparse
* os
* numpy (not necessary - used in flag -P in separate_Pfam_to_counts.py ($ sudo pip3 install numpy))
* matplotlib (not necessary - used in flag -P in separate_Pfam_to_counts.py ($ sudo pip3 install matplotlib))

However for full functionality you will need to install [CLANS](https://www.eb.tuebingen.mpg.de/protein-evolution/software/clans/)


## Important note!!!
If you want to use CLANS program for example during all_in_one.py script **remember to save result** after finished clustering then **create groups** and put them into **"groups_from_CLANS"** folder!


## all_in_one.py

Automatically process your data using default parameters (see below under respective scripts).

Flag | Description                           | Default
---- | ------------------------------------- | ----
-C   | Directory to CLANS                    | 
-P   | File from Pfam directory              |
-F   | Directory to file with full sequences | 

Example usage:  
`python3 all_in_one.py -P other_files/PF01699_full.txt -F other_files/PF01699_raw.fasta -C here-put-directory-to/clans.jar`


## separate_Pfam_to_counts.py

Input: File with repeats downloaded from Pfam database. 
* **IMPORTANT:**
   * Format: **FASTA**
   * Gaps: **Gaps as "-" (dashes)**

Flag | Description                                           | Default
---- | ----------------------------------------------------- | ----
-F   | Directory to the file                                 | 
-P   | Show the plot with all start/end positions            | False
-M   | Separate all structures, also with more than 2 counts | False

Example usage:  
`python3 separate_Pfam_to_counts.py -F PF00000_full.txt`  
or to see a plot:  
`python3 separate_Pfam_to_counts.py -F PF00000_full.txt -P`


## formatting.py

Delete all gaps and convert names.

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 
-S   | Substitute character                              | _

Example usage:  
`python3 formatting.py -F files_from_separate_Pfam_to_counts/put-file-name-here`  
or for recursive search in folder:  
`python3 formatting.py -R files_from_separate_Pfam_to_counts`  


## full_seq_extract_n_counts.py

While file downloaded from Pfam may contain sequences with other number than n repeats (for example 2), this program
will filter only interesting ones.

Flag | Description                                    | Default
---- | ---------------------------------------------- | ----
-F   | Directory to file with full sequences          | 
-S   | Directory to file from separate_Pfam_to_counts | 
-N   | Number of repeats                              | 2

Example usage:  
`python3 full_seq_extract_n_counts.py -F PF00000_raw.fasta -S files_from_separate_Pfam_to_counts/put-here-name-of-the-file`  

## separate_groups_to_counts.py

Seperate CLANS groups files to counts.

Flag | Description                      | Default
---- | -------------------------------- | ----
-G   | Folder name with groups files    | groups_from_CLANS
-S   | Folder name with separated files | files_from_separate_Pfam_to_counts
-N   | Number of counts                 | 2

Example usage:  
`python3 separate_groups_to_counts.py`  


## simple_filter_by_length.py

Filters sequences by their length (number of letters). It helps to filter longer or shorter seq than average but will
not filter if seq is missing some part but is longer in other while length stays similar to others. 

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 
-A   | More or less value than average                   |

Example usage:  
`python3 simple_filter_by_length.py -F files_from_separate_groups_to_counts/put-here-file-name -A 15`  
or for recursive search:  
`python3 simple_filter_by_length.py -R files_from_separate_groups_to_counts -A 10`  


## advanced_filter_by_value.py

Example can be found below

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 
-M   | Error margin                                      | 0.4
-A   | Acceptable number of errors                       | 10
-O   | Detailed output                                   | False

Example usage:  
`python3 advanced_filter_by_value.py -F files_from_separate_groups_to_counts/put-here-file-name'`  
for recursive search:  
`python3 advanced_filter_by_value.py -R files_from_separate_groups_to_counts'`  
to change parameters:  
`python3 advanced_filter_by_value.py -R files_from_separate_groups_to_counts -M 0.5 -A 20'` 


## About advanced_filter_by_value.py

Example for:  
margin = 0.4  
error = 1

Sequence    | col 1 | col 2 | col 3 | col 4 | col 5 | Comment
------------|-------|-------|-------|-------|-------|-----------------------------
S1          |   -   |   -   |   -   |   -   |   A   |
S2          |   -   |   -   |   -   |   A   |   A   |
S3          |   -   |   -   |   A   |   A   |   A   |
S4          |   -   |   A   |   A   |   A   |   A   |
S5          |   A   |   A   |   A   |   A   |   A   |
Value       |  0.2  |  0.4  |  0.6  |  0.8  |   1   |
Compare S1  |  OK   |  OK   |   X   |   X   |  OK   | Error: 2 - Sequence deleted
Compare S2  |  OK   |  OK   |   X   |  OK   |  OK   | Error: 1 - Sequence is OK
Compare S3  |  OK   |  OK   |  OK   |  OK   |  OK   | Error: 0 - Sequence is OK
Compare S4  |  OK   |   X   |  OK   |  OK   |  OK   | Error: 1 - Sequence is OK
Compare S5  |   X   |   X   |  OK   |  OK   |  OK   | Error: 2 - Sequence deleted

So too long and too short sequence are deleted. Notice, that even if columns are in different order result will be the same.
