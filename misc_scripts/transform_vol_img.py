"""
Name: Kimberly Nestor
Date: 01/19/2021
Description: This program will take an exvivo volume and generate several
            orientations using RAS coordinates. Output is in png format. User then
            selects which orientation is the correct anatomical position. Then
            program is run again to transform all desired volumes to the actual
            anatomical position.
Documentation:
https://nilearn.github.io/plotting/index.html
FreeSurfer commands: mri_convert, mri_info, tkregister2, mri_vol2vol
"""

import os
import sys
from nilearn import plotting
import nibabel as nib

# hard path to data
path = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/mri/parameter_maps_B0_B1Tx/'

create_test_dir = "mkdir " + path + "transform_test/"
os.system(create_test_dir)

# different orientations output dir
outpath = path + 'transform_test/'


#initial volume to use as a test for orientation
volume = 'flash20.mgz'
# list of volumes that need to be rotated
vol_lst = ['bias_flash10_polyfit2_masked.mgz', 'bias_flash20_polyfit2_masked.mgz',\
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

# create nifti file as an input for first loop to check orientations
# you should turn this os.system off after first loop
create_nii = "mri_convert " + path + volume + " " + outpath + volume[:-4] + "_org.nii"
# os.system(create_nii)
# sys.exit()

# volume and path info for org and new nifti volumes
nii_vol_org = outpath + volume[:-4] + "_org.nii"
nii_vol_new = outpath + volume[:-4] + "_new.nii"

# loop will go through and apply all possible combinations of ras coordinates
# for png image y = coronal, x = sagittal, z = axial
# turn off os.system when done with this loop
# check output in transform_test dir
count = 1
for a, b, c in zip(ras_coor_dict['sag_ras_x'], ras_coor_dict['coronal_ras_y'], \
ras_coor_dict['axial_ras_z']):
    try:
        # do transforms and for each iteration save over nii_vol_new, turn off after first
        transform_vol_cmd = "mri_convert -iid " + a + " -ijd " + b + " -ikd "\
         + c + " " + nii_vol_org + " " + nii_vol_new
        # os.system(transform_vol_cmd)

        # names for png files
        nii_png_planes = outpath + volume[:-4] + "_rot" + str(count) + ".png"

        # make object of volume
        nii_obj = nib.load(nii_vol_new)

        # create png images, turn off on second round
        # plotting.plot_anat(anat_img=nii_obj, output_file=nii_png_planes, \
        # display_mode='ortho', title='Rotation'+str(count))
        # plotting.show()

        count+=1
    except(ValueError, NameError, TypeError):
        continue

# print(SAG_RAS_X)
# print(CORONAL_RAS_Y)
# print(AXIAL_RAS_Z)

# after you figure out which ras coordinate run again, turn two os.system
for volume in vol_lst:
    try:
        # set variables
        vol_rot = volume[:-4] + "_rotated.mgz"
        vol_lta = vol_rot[:-4] + ".lta"

        # command line mri_convert, turn the os.system on 2nd run of script
        transform_vol_cmd = "mri_convert -iid " + SAG_RAS_X + " -ijd " + \
        CORONAL_RAS_Y + " -ikd " + AXIAL_RAS_Z + " " + path + volume + " " + path + vol_rot
        os.system(transform_vol_cmd)

        #command line make lta file, headless, turn on os.system
        create_lta_cmd = "tkregister2 --mov " + volume + " --targ " + vol_rot \
        + " --regheader --reg deleteme.dat --ltaout " + vol_lta + " --noedit"
        os.system(create_lta_cmd)

    except(ValueError, NameError, TypeError):
        print("Something went wrong in ", volume, ". You should check it.")
        continue

# you can use this anywhere in the script to hard end the program before completion
# sys.exit()

# when you're done delete the transform_test directory, you don't need it

#transform using lta file in commandline, alternative to mri_convert
# mri_vol2vol --mov T1.mgz --targ T1_rotated.mgz --o T1_rot_test.mgz --lta T1_rot_test.lta --no-resample
