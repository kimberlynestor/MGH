
"""
name: rename_file_text
Author: Kimberly Nestor
Use:
This script takes names of point set labels from a file and changes the end of
the name for layer1 and GWB.
"""

import sys

#path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/'
path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/'



label_name_long_file = open(path+"label_names_long.csv", 'r')
#label_name_long_file2 = open("label_names_long.csv", 'w')

label_name_long_file_list = [i for i in label_name_long_file]
#print(label_name_long_file_list)

label_name_long_file = open(path+"label_names_long.csv", 'w')
label_name_long_file = open(path+"label_names_long.csv", 'a')
# sys.exit()

for i in label_name_long_file_list:

    if "LI.label" in i:
        label_long_name = i[:-7] + "_long.label\n"
        label_name_long_file.write(label_long_name)
        #print(label_long_name)
        #print(i[:-7])
        #print(i)
    elif "GWB.label" in i:
        label_long_name = i[:-7] + "_long.label\n"
        label_name_long_file.write(label_long_name)
        #print(label_long_name)
        #print(i)
    else:
        label_name_long_file.write(i)


label_name_long_file.close()

# sys.exit()
