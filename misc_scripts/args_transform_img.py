#!/usr/bin/env python3
"""
Updated by Jackson Nolan

Usage:  ./args_transform_img.py <path/to/volumes/to/orient> -c -op <path/to/output/images/to> [OPTIONAL: -v target_vol_for_images.mgz]
        ./args_transform_img.py <path/to/volumes/to/orient> -o <orientation number>

    This script is used for orienting reconed volumes into the correcet anatomical orientation (RAS).
    1. Run the script first with the -c/--check flag to create a .png image of the volume in all possible orientations,
    you must also specify a directory to outut the images with the -op/--outpath flag. By default, the script will 
    search for a file 'flash20.mgz' in the path passed as the first argument, pass the -v/--vol flag followed by a 
    string to change the file used as the target for the orientation images.
    2. Once the orientation images are produced, evaluate them for the correct orientation. Note the number postfixed
    to the file name (_[0-20].png), and pass that int to the -o/--orient flag. This will orient all volumes in the
    path passed to the script. By default, the script orients the standard 'parameter_maps' volumes. To change the 
    volumes the script will orient, edit the value of the variable 'vol_list' under 'GLOBAL VARS'
"""
import os
import sys
from nilearn import plotting
import nibabel as nib
import argparse

"""
GLOBAL VARS
"""
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

"""
FUNCTIONS
"""
def arg_parser():
    #HELP/DESCRIPTIONS 
    descript = 'This script is used to manipulate reconed volumes into the correct anatomical orientation (RAS).\
        \n\nThe first time you run this script, pass the --check flag to create images of each possible orientation.\
        \n\nThe second time pass the --orient flag with the correct orientation number to transform all volumes'
    h_path = 'REQUIRED: Absolute path to directory containing volumes'
    h_outpath = 'Path to where output dir will be created, directory must exist prior to running script'
    h_check = 'Create transform_test directory and populate with images of all possible orientations'
    h_orient = 'Changes orientation of original volumes to anatomicaly correct orientation, must pass orientation number'
    h_vol = 'Volume used to create orientation images, DEFAULT: flash20.mgz'

    #DEF PARSER
    parser = argparse.ArgumentParser(description=descript)

    #POSITIONAL ARG
    parser.add_argument('path', help=h_path, type=str)

    #FLAGS
    parser.add_argument('-c', '--check', help=h_check, required=False, action='store_true',default=False)
    parser.add_argument('-o', '--orient', help=h_orient, required=False, action='store', default=None, type=int)
    parser.add_argument('-v', '--vol', help=h_vol, required=False, action='store', nargs=1, default='flash20.mgz', type=str)
    parser.add_argument('-op','--outpath', help=h_outpath, required=False, action='store', nargs=1, default=None, type=str)

    return parser.parse_args()


########### HANDLE ARGS
def parse(args):
    
    args_bad = False
    """
    Check that required files exist
    """
    if not(args.path):
        print("IOError: Path to volume dir must be passed\nEXITING")
        args_bad = True
    if not(os.path.isdir(args.path)):
        print(f'IOError: {args.path} is not a directory\nEXITING')
        args_bad = True
    if (not(os.path.isfile(args.path+'/'+args.vol)) and (args.vol)):
        print(f'IOError: Volume: {args.path}/{args.vol} does not exits\nEXITING')
        args_bad = True
    if args.outpath:
        if(args.outpath == None):
            print('--outpath was passed with no location specified\nEXITING')
            args_bad = True
        if not(os.path.isdir(arsg.outpath)):
            print(f'IOError: {args.outpath} does not exist\nEXITING')
            args_bad = True
    """
    Ensure optional flags do not conflict and have required args
    """
    if not args.orient and not args.check:
        print('Neither --check nor --orient flag was passed\nPass --check to create images of possible orientations\n\
            Pass --orient # to transform all volumes to that orientation\n\nEXITING')
        args_bad = True
    if args.orient and args.check:
        print('Both --check and --orient flags were passed, you can only select one\nEXITING')
        args_bad = True
    if ((args.orient and (args.orient == None)) or args.orient>20):
        print('Must specify orientation number between [0-20] with --orient flag\nEXITING')
        args_bad = True
    """
    Tell user if args are bad, return args_bad
    """
    if args_bad:
        print('EXITING')
    return args_bad

############ STEP 1
def create_orientation_images(args):
    #Set path to volumes dir and volume to produce images
    path = args.path + '/'
    volume = args.vol
    outpath = ''
    #create the test dir
    if(args.outpath):
        outpath = args.outpath
    else:
        outpath = path + 'transform_test/'
        create_test_dir = "mkdir " + outpath
        os.system(create_test_dir)

    # create nifti file
    create_nii = "mri_convert " + path + volume + " " + outpath + volume[:-4] + "_org.nii"
    os.system(create_nii)

    # volume and path info for org and new nifti volumes
    nii_vol_org = outpath + volume[:-4] + "_org.nii"
    nii_vol_new = outpath + volume[:-4] + "_new.nii"

    # loop will go through and apply all possible combinations of ras coordinates
    # for png image y = coronal, x = sagittal, z = axial
    # check output in transform_test dir
    count = 0
    for a, b, c in zip(ras_coor_dict['sag_ras_x'], ras_coor_dict['coronal_ras_y'], \
    ras_coor_dict['axial_ras_z']):
        try:
            # do transforms and for each iteration save over nii_vol_new, turn off after first
            transform_vol_cmd = "mri_convert -iid " + a + " -ijd " + b + " -ikd "\
            + c + " " + nii_vol_org + " " + nii_vol_new
            os.system(transform_vol_cmd)

            # names for png files
            nii_png_planes = outpath + volume[:-4] + "_rot" + str(count) + ".png"

            # make object of volume
            nii_obj = nib.load(nii_vol_new)

            # create png images
            plotting.plot_anat(anat_img=nii_obj, output_file=nii_png_planes, \
            display_mode='ortho', title='Rotation'+str(count))
            # plotting.show()

            count+=1
        except(ValueError, NameError, TypeError):
            continue

############### STEP 2
def orient_volumes(args):
    path = args.path +'/'
    orientation = args.orient

    # RAS coordinates for freesurfer
    # change the index number after you figure out what RAS you need
    SAG_RAS_X = ras_coor_dict['sag_ras_x'][orientation]
    CORONAL_RAS_Y = ras_coor_dict['coronal_ras_y'][orientation]
    AXIAL_RAS_Z = ras_coor_dict['axial_ras_z'][orientation]

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

def main():
    args = arg_parser()
    if parse(args):
        sys.exit()
    if(args.check):
        create_orientation_images(args)
    elif (args.orient != None):
        orient_volumes(args)
    return 0

if __name__ == '__main__':
    main()
