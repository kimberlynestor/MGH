
"""
name: compute_thick_datasheet
Author: Kimberly Nestor
Use:
This script/function takes volumes and their associated way points and computes the laplace equation through freeview using the terminal and saves the output files. It uses separate text files named volume_names and label_names as inputs due to a large volume of data and messy directories.

Inputs:
case - case name
area - brain area i.e. "crown" or "fundus"

Outputs:
csv files with thickness and intensity data
"""


import os
import glob
import pathlib
import sys

#This script will open freeview and the way points associated with the volume, then open the lineprofile tool and compute the laplace equation and save the output file.

def compute_thick_file(case, area):
    if area == "crown":
        path_data = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/' + case + '/edited/'

        path_sheet = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/'

    elif area == "fundus":
        path_data = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/' + case + '/'

        path_sheet = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/'

    label_names = open(path_sheet+"label_names_long.csv", "r")
    label_names2 = label_names.readlines()

    volume_names = open(path_sheet+"volume_names.csv", "r")
    volume_names2 = volume_names.readlines()

    volume_list = []
    label_list = []
    [volume_list.append(volume) for volume in volume_names2 if case in volume]
    [label_list.append(label) for label in label_names2 if case in label]
    #print(volume_list)
    #print(label_list)

    for volume in volume_list:
        if "I25_block4" in volume:
            continue
        else:
            name_root = volume[:-5]
            #print(name_root)
            ind_volume_slice_labels = []
            for label in label_list:
                if name_root in label:
                    ind_volume_slice_labels.append(label)
            #print(ind_volume_slice_labels)
            ind_case_slice_BA_label = []
            badlabel = False
            for label in ind_volume_slice_labels:
                try:
                    if name_root in label and "LI_long.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "LII.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "LIII.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "LIV.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "LV.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "LVI.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    elif name_root in label and "GWB_long.label" in label:
                        ind_case_slice_BA_label.append(label)
                        if label == None:
                            badlabel = True
                            continue
                    #print(ind_case_slice_BA_label)
                    #print(ind_case_slice_BA_label[0])
                    #print(name_root)


                    shell_compute_command = "freeview -v " + path_data + volume + " -w " + path_data + ind_case_slice_BA_label[3] + " " + path_data + ind_case_slice_BA_label[2] + " " + path_data + ind_case_slice_BA_label[1] + " " + path_data + ind_case_slice_BA_label[4] + " " + path_data + ind_case_slice_BA_label[6] + " " + path_data + ind_case_slice_BA_label[5] + " " + path_data + ind_case_slice_BA_label[0] + " -lineprofile " + path_data +name_root + "_profile_all_long.csv:resolution=5:spacing=5:offset=50:radius=0.005 -quit"

                    shell_compute_command = shell_compute_command.replace('\n', '')
                    print(shell_compute_command)

                    os.system(shell_compute_command)

                except IndexError:
                    continue

    label_names.close()
    volume_names.close()



case_list_crown = ["I25", "I27", "I30", "I31", "I32", "I33", "I34", "I40", "I42", "I44", "I47", "I49"]

case_list_fundus = ["I25", "I32", "I33", "I34", "I40", "I42", "I44", "I47", "I49"]


#for case in case_list_crown:
#    compute_thick_file(case, "crown")

# for case in case_list_fundus:
#     compute_thick_file(case, "fundus")


#compute_thick_file("I25", "crown")


case_list_crown_long = ["I25", "I32"]

case_list_fundus_long = ["I25", "I42",]


for case in case_list_crown:
   compute_thick_file(case, "crown")

for case in case_list_fundus:
    compute_thick_file(case, "fundus")
