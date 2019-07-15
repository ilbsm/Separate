# Separate

## separate_Pfam_to_counts_new.py

Input: File with repeats downloaded from Pfam database. 
* **IMPORTANT:**
   * Format: **FASTA**
   * Gaps: **Gaps as "-" (dashes)**

Flag | Description | Default
---- | ---- | ----
-F | Directory to the file | 
-P | Show the plot with all start/end positions | False
-M | Separate all structures, also with more than 2 counts | False



## formatting.py

Delete all gaps and convert names.

Flag | Description | Default
---- | ---- | ----
-F | Directory to the file | 
-R | Recursive search - Directory to folder with files | 
-S | Substitute character | _



## full_seq_extract_n_counts.py

While file downloaded from Pfam may contain sequences with other number than n repeats (for example 2), this program
will filter only interesting ones.

Flag | Description | Default
---- | ---- | ----
-F | Directory to file with full sequences | 
-S | Directory to file from separate_Pfam_to_counts| 
-N | Number of repeats | 2


## separate_groups_to_counts.py

Seperate CLANS groups files to counts.

Flag | Description | Default
---- | ---- | ----
-G | Folder name with groups files | groups
-S | Folder name with separated files | Files_from_separate
-N | Number of counts | 2


## simple_filter_by_length.py

Filters sequences by their length (number of letters). It helps to filter longer or shorter seq than average but will
not filter if seq is missing some part but is longer in other while length stays similar to others. 

Flag | Description | Default
---- | ---- | ----
-F | Directory to the file | 
-R | Recursive search - Directory to folder with files | 
-A | More or less value than average |


## advanced_filter_by_value.py

Description can be found in other file (not done yet)

Flag | Description | Default
---- | ---- | ----
-F | Directory to the file | 
-R | Recursive search - Directory to folder with files | 
-M | Error margin | 0.4
-A | Acceptable number of errors | 10
-O | Detailed output | False
