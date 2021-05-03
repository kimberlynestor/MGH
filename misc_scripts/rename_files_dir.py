"""
Name: Kimberly Nestor
Description: This program will rename files in a directory. You can use a string to rename or python pattern matching.
https://docs.python.org/3/howto/regrex.html
"""

import os
import fileinput
import sys


def rename(case):
    #path = os.path.join("/autofs/space/vault_006/exvivo/exvivo_data_collection/wet_lab_data/tnc_project/photomacro_nissl_4x/", case, "edited/")
    path = os.path.join("/autofs/space/asterion_001/users/kn751/wet_lab_data_asterion/tnc_project_asterion/laminar_thickness/fundus/", case)
    for filename in os.listdir(path):
        if "_4x_final" in filename:
            #print(filename)
            old_name = os.path.join(path, filename)
            new_name = os.path.join(path, filename.replace("_4x_final_", "_"))
            os.rename(old_name, new_name)


#rename("I25")

case_list_crown = ["I25", "I27", "I30", "I31", "I32", "I33", "I34", "I40", "I42", "I44", "I47", "I49"]

case_list_fundus = ["I25", "I32", "I33", "I34", "I40", "I42", "I44", "I47", "I49"]


for item in case_list_fundus:
    rename(item)
