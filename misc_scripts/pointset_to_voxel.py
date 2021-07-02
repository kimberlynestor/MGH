"""
Name: Jocelyn Mora, Kimberly Nestor
Description: This script will convert pointsets to a voxel labeled volume and assign the appropriate label values \
to its respective label boundary.
Usage: python pointset_to_voxel.py
"""

import os

## Set paths and variables for input to pointset2label command 
# Input path to label directory, way point directory, and naming convention for input and output volumes below.
# If you want output to be in a label file you're currently working on then in_vol and out_vol should be the same.

l_path = "/autofs/cluster/oribivault/data/EXC022_lh_phoenixcoil_062320/label/"
w_path = "/autofs/cluster/oribivault/data/EXC022_lh_phoenixcoil_062320/label/way_point_test/"
in_vol = os.path.join(l_path, "flash20.mgz")
out_vol = os.path.join(l_path, "point2vox_label_test.mgz")

## Search through list of way points and convert way points to voxel labels

w_list=os.listdir(w_path)
# print(w_list)

for label in w_list:
    if "pial" in label:
        point2vox_cmd = "pointset2label " + os.path.join(w_path, label) + " " + in_vol + " 3 " + out_vol + " -clear"
        print(point2vox_cmd, "\n")
        os.system(point2vox_cmd)
    elif "supra_infra" in label:
        point2vox_cmd = "pointset2label " + os.path.join(w_path, label) + " " + in_vol + " 2 " + out_vol
        print(point2vox_cmd, "\n")
        os.system(point2vox_cmd)
    elif "gwb" in label:
        point2vox_cmd = "pointset2label " + os.path.join(w_path, label) + " " + in_vol + " 1 " + out_vol
        print(point2vox_cmd, "\n")
        os.system(point2vox_cmd)