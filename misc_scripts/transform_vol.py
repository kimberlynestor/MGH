"""
Name: Kimberly Nestor
Date: 10/15/2020
Description: This program will take an exvivo volume and transform the RAS \
coordinates to the actual anatomical position.
"""

import os
import sys
from subprocess import run
import subprocess

# freesurfer unix commands to find xyz ras coordinates
# mri_info --cdc flash10.mgz
# mri_info --rdc flash10.mgz
# mri_info --sdc flash10.mgz
# mri_info --cras flash10.mgz

# hard path to data
path = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_\
20190316/mri/parameter_maps_B0_B1Tx/'
# inpath = ''
# outpath = ''


# list of volumes that need to be rotated
volume = 'flash10.mgz'

vol_lst = ['2bias_flash10_polyfit2_masked.mgz', 'bias_flash20_polyfit2_masked.mgz',\
 'bias_flash40_polyfit2_masked.mgz', 'faf.mgz', 'flash10.mgz', 'flash10_polyfit2_masked.mgz',\
 'flash20.mgz', 'flash20_polyfit2_masked.mgz', 'flash40.mgz', 'flash40_polyfit2_masked.mgz',\
 'mask_flash10_polyfit2_masked.mgz', 'mask_flash20_polyfit2_masked.mgz',\
 'mask_flash40_polyfit2_masked.mgz', 'PD.mgz', 'sse.mgz', 'T1.mgz', 'T2star.mgz']

# all posible combinations of ras coordinates
ras_coor_dict = {
'sag_ras_x': ["1 0 0", "0 1 0", "0 0 1", "-1 0 0", "1 0 0", "1 0 0", "0 -1 0", \
"0 1 0", "0 1 0", "0 0 -1", "0 0 1", "0 0 1", "-1 0 0", "1 0 0", "-1 0 0", \
"0 -1 0", "0 1 0", "0 -1 0", "-1 0 0", "0 -1 0", "0 0 -1"],

'coronal_ras_y': ["0 1 0", "0 0 1", "1 0 0", "0 1 0", "0 -1 0", "0 1 0", "0 0 1",\
 "0 0 -1", "0 0 1", "1 0 0", "-1 0 0", "1 0 0", "0 -1 0", "0 -1 0", "0 1 0", \
 "0 0 -1", "0 0 -1", "0 0 1", "0 -1 0", "0 0 -1", "-1 0 0"],

'axial_ras_z': ["0 0 1", "1 0 0", "0 1 0", "0 0 1", "0 0 1", "0 0 -1", "1 0 0", \
"1 0 0", "-1 0 0", "0 1 0", "0 1 0", "0 -1 0", "0 0 1", "0 0 -1", "0 0 -1", \
"1 0 0", "-1 0 0", "-1 0 0", "0 0 -1", "-1 0 0",  "0 -1 0"]
}


# RAS coordinates for freesurfer
# change the index number after you figure out what RAS you need
SAG_RAS_X = ras_coor_dict['sag_ras_x'][8]
CORONAL_RAS_Y = ras_coor_dict['coronal_ras_y'][8]
AXIAL_RAS_Z = ras_coor_dict['axial_ras_z'][8]
# CENTER_RAS = 0.324455, -0.629539, 23.6538


# this for loop will go through and apply all possible combinations of ras
#coordinates to a volume to determine which should be used
# turn off os.system() when
count = 1
for a, b, c in zip(ras_coor_dict['sag_ras_x'], ras_coor_dict['coronal_ras_y'], \
ras_coor_dict['axial_ras_z']):
    try:
        transform_vol_command = "mri_convert -iid " + a + " -ijd " + b + " -ikd "\
         + c + " " + path + volume + " " + path + volume[:-4] + "_rotated" + str(count) + ".mgz"
        count+=1
        # print(transform_vol_command)
        os.system(transform_vol_command)
    except(ValueError, NameError, TypeError):
        continue

# print(SAG_RAS_X)
# print(CORONAL_RAS_Y)
# print(AXIAL_RAS_Z)

# after you figure out which ras coordinate you need to use run again and \
# turn on os.system()
for volume in vol_lst:
    try:
        transform_vol_command = "mri_convert -iid " + SAG_RAS_X + " -ijd " + \
        CORONAL_RAS_Y + " -ikd " + AXIAL_RAS_Z + " " + path + volume + " " + path + volume[:-4] \
        + "_rotated.mgz"
        # print(transform_vol_command)
        # os.system(transform_vol_command)
    except(ValueError, NameError, TypeError):
        print("Something went wrong in ", volume, ". You should check it.")
        continue
    # print(transform_vol_command)


# sys.exit()
