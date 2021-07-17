"""
Name: Kimberly Nestor
Date: 07/2021
Description: This program takes manually labelled points for laminar boundaries 
in the cortex and computes straight vectors between the pial and gwb surfaces. 
The vectors are then used to determine thickness for each individual layer and 
total cortical thickness. Values are saved in a csv file. Used in tandem with 
homemade module vec_funcs. This is a test version with crown and fundus of one 
case."""


import os
import sys
import re
import csv

import numpy as np
import matplotlib.pyplot as plt

import multiprocessing as mp
import vec_funcs as vf
# from vec_funcs import *


case_dict = {'crown' : ['I25', 'I27', 'I30', 'I31', 'I32', 'I33', 'I34', 'I40', \
                        'I42', 'I44', 'I47', 'I49'], 
            'fundus' : ['I25', 'I32', 'I33', 'I34', 'I40', 'I42', 'I44', 'I47', 'I49']}


"""
for key, val in case_dict.items():
    if key == 'crown':
        for case in val:
            path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/' + case + '/edited/'
            
            all_labels = [i for i in os.listdir(path) if i.endswith('.label') \
                and not i.endswith('LI.label') and not i.endswith('GWB.label')]

            #use pattern matching, for label info
            lab_info = []
            for label in sorted(all_labels):
                split = re.split('(slice\d+_BA\d+|)', label)
                lab_info.append(split[1])
            lab_info = np.unique(lab_info)    

            #get label names and save thickness
            for lab in lab_info:
                labels = [i for i in all_labels if lab in i]
                tissue_image = [i for i in os.listdir(path) if lab in i \
                                and i.endswith('tif')]

                if len(labels) <7:
                    continue
                else:
                    #separate out BA20A and BA20B 
                    if any([True for i in labels if 'BA20' in i]):
                        labels_ba20a = [i for i in labels if 'BA20A' in i] 
                        labels_ba20b = [i for i in labels if 'BA20B' in i]
                        
                        save_name_a = case + '_' + lab + 'A' + '_strvec'
                        save_name_b = case + '_' + lab + 'B' + '_strvec'

                        tissue_a = [i for i in tissue_image if 'BA20A' in i]
                        tissue_b = [i for i in tissue_image if 'BA20B' in i]

                        try:
                            vf.save_thick_csv(path, labels_ba20a, tissue_a[0], save_name_a)
                            print("Currently saving:\n", path + save_name_a + '.csv\n')

                        except:
                            print("There was an error in:\n", path + save_name_a + '.csv\n')
                            continue
                            
                        try:
                            vf.save_thick_csv(path, labels_ba20b, tissue_b[0], save_name_b)
                            print("Currently saving:\n", path + save_name_b + '.csv\n')

                        # except(ValueError, TypeError, KeyError):
                        except:
                            print("There was an error in:\n", path + save_name_b + '.csv\n')
                            continue

                    #save thickness data for straight vectors
                    else:
                        save_name = case + '_' + lab + '_strvec'
                        
                        try:
                            vf.save_thick_csv(path, labels, tissue_image[0], save_name)
                            print("Currently saving:\n", path + save_name + '.csv\n')

                        except:
                            print("There was an error in:\n", path + save_name + '.csv\n')
                            continue

    if key == 'fundus':
        for case in val:
            path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/' + case + '/'
            
            all_labels = [i for i in os.listdir(path) if i.endswith('.label') \
                and not i.endswith('LI.label') and not i.endswith('GWB.label')]

            #use pattern matching, for label info
            lab_info_full = []
            for label in sorted(all_labels):
                split = re.split('(slice\d+_fundus_BA\w+|)', label)
                try:
                    lab_info_full.append(split[1])
                except:
                    continue

            #separate out extra info so that only slice_fundus_BA is left
            lab_info = []
            for lab in lab_info_full:
                if 'long' in lab:
                    lab_split = lab.split('_')
                    lab_root = lab_split[:-2]
                    lab_root = "_".join(lab_root)
                    lab_info.append(lab_root)
                else:
                    lab_split = lab.split('_')
                    lab_root = lab_split[:-1]
                    lab_root = "_".join(lab_root)
                    lab_info.append(lab_root)
            lab_info = np.unique(lab_info)
            
            #get label names and save thickness
            for lab in lab_info:
                labels = [i for i in all_labels if lab in i]
                tissue_image = [i for i in os.listdir(path) if lab in i \
                                and i.endswith('tif')]

                if len(labels) <7:
                    continue
                else:
                    save_name = case + '_' + lab + '_strvec'
                    try:
                        vf.save_thick_csv(path, labels, tissue_image[0], save_name)
                        print("Currently saving:\n", path + save_name + '.csv\n')

                    except:
                        print("There was an error in:\n", path + save_name + '.csv\n')
                        continue

"""





"""
####TESTING
##CROWN
path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/\
laminar_thickness/crown/I42/edited/'

LAB_LST = ['I42_block1_slice125_BA20B_LI_long.label', 'I42_block1_slice125_BA20B_LII.label', \
'I42_block1_slice125_BA20B_LIII.label', 'I42_block1_slice125_BA20B_LIV.label', \
'I42_block1_slice125_BA20B_LV.label', 'I42_block1_slice125_BA20B_LVI.label', \
'I42_block1_slice125_BA20B_GWB_long.label']

tissue_image = 'I42_block1_slice125_BA20B.tif'

vf.save_thick_csv(path, LAB_LST, tissue_image, 'I42_slice125_BA20B_strvec')
"""


"""
##FUNDUS
path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/\
laminar_thickness/fundus/I42/'

LAB_LST = ['I42_block1_slice120_fundus_BA20B_21_LI_long.label', \
'I42_block1_slice120_fundus_BA20B_21_LII.label', \
'I42_block1_slice120_fundus_BA20B_21_LIII.label', \
'I42_block1_slice120_fundus_BA20B_21_LIV.label', \
'I42_block1_slice120_fundus_BA20B_21_LV.label', \
'I42_block1_slice120_fundus_BA20B_21_LVI.label', \
'I42_block1_slice120_fundus_BA20B_21_GWB_long.label'] 

tissue_image = 'I42_block1_slice120_fundus_BA20B_21.tif'

vf.save_thick_csv(path, LAB_LST, tissue_image, 'slice120_fundus_BA20B_21_strvec')
"""


path = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/I40/'
#slice 30, 35, 30
LAB_LST = ['I40_block2_slice40_fundus_BA20A_20A_GWB_long.label', \
'I40_block2_slice40_fundus_BA20A_20A_LIII.label', \
'I40_block2_slice40_fundus_BA20A_20A_LII.label', \
'I40_block2_slice40_fundus_BA20A_20A_LI_long.label', \
'I40_block2_slice40_fundus_BA20A_20A_LIV.label', \
'I40_block2_slice40_fundus_BA20A_20A_LVI.label', \
'I40_block2_slice40_fundus_BA20A_20A_LV.label'] 

tissue_image = 'I40_block2_slice40_fundus_BA20A_20A.tif'

vf.save_thick_csv(path, LAB_LST, tissue_image, 'I40_slice40_fundus_BA20A_20A_strvec')



# full_list = [path+i for i in LAB_LST]
# vec_coords = vf.vec_coords(vf.layer_coords(full_list), spacing=6)

#plot ind str vectors, only in roi
# for coords in np.array(vec_coords):
#     plt.plot([i[0] for i in coords], [i[1] for i in coords], \
#         c="#767676", alpha=1, lw=1.2)
# plt.gca().invert_yaxis()
# plt.show()
# # plt.close()
