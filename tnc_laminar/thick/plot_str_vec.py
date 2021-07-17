"""
Name: Kimberly Nestor
Date: 07/2021
Description: This program takes manually labelled points for laminar boundaries 
in the cortex computes straight vectors between the pial and gwb surfaces. 
The vectors are then used to determine thickness for each individual layer. 
Used in tandem with homemade module vec_funcs. This is a test version with 
crown and fundus of one case."""

import os
import sys

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.transforms as transforms
import matplotlib.image as mpimg
from PIL import Image

import warnings
import multiprocessing as mp
import vec_funcs as vf


# pd.set_option("display.max_rows", None, "display.max_columns", None)
warnings.filterwarnings("ignore")


#### CROWN
dpath = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/\
laminar_thickness/crown/I42/edited/'

LAB_LST = ['I42_block1_slice120_BA20B_LI_long.label', 'I42_block1_slice120_BA20B_LII.label', \
'I42_block1_slice120_BA20B_LIII.label', 'I42_block1_slice120_BA20B_LIV.label', \
'I42_block1_slice120_BA20B_LV.label', 'I42_block1_slice120_BA20B_LVI.label', \
'I42_block1_slice120_BA20B_GWB_long.label'] #I42_slice120_fundus_BA20B_21_long

img_path = os.path.join(dpath, 'I42_block1_slice120_BA20B.tif')

#coordinates for layer boundary and vectors
fullpath_lst = [dpath + i for i in LAB_LST]
layer_coords = vf.layer_coords(fullpath_lst)
vec_coords = vf.vec_coords(layer_coords, spacing=8)

#thickness values for full vectors and each individual layer
vec_thick = vf.vec_thick(layer_coords, vec_coords, img_path)
roi_vec_coords = vf.roi_vecs(layer_coords, vec_coords, 'crown')
lall_ind_thick = vf.ind_thick(layer_coords, roi_vec_coords, img_path)
print("crown lall_ind_thick = \n", np.array(lall_ind_thick) ,"\n")


#plot layers and straight vectors
for layer in layer_coords:
    plt.plot([i[0] for i in layer_coords[layer]], [i[1] for i in layer_coords[layer]], \
        lw=2.5, c='#964000') #7F50CD
#plot ind str vectors
# for coords in np.array(vec_coords):
#     plt.plot([i[0] for i in coords], [i[1] for i in coords], c="#767676", \
#     alpha=1, lw=1.2)#767676

#plot ind str vectors, only in roi
for coords in np.array(roi_vec_coords):
    plt.plot([i[0] for i in coords], [i[1] for i in coords], \
        c="#767676", alpha=1, lw=1.2)
plt.gca().invert_yaxis()
# plt.show()
plt.close()



#### FUNDUS
dpath = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/\
laminar_thickness/fundus/I42/'

LAB_LST = ['I42_block1_slice120_fundus_BA20B_21_LI_long.label', \
'I42_block1_slice120_fundus_BA20B_21_LII.label', \
'I42_block1_slice120_fundus_BA20B_21_LIII.label', \
'I42_block1_slice120_fundus_BA20B_21_LIV.label', \
'I42_block1_slice120_fundus_BA20B_21_LV.label', \
'I42_block1_slice120_fundus_BA20B_21_LVI.label', \
'I42_block1_slice120_fundus_BA20B_21_GWB_long.label'] 

img_path = os.path.join(dpath, 'I42_block1_slice120_fundus_BA20B_21.tif')

#coordinates for layer boundary and vectors
fullpath_lst = [dpath + i for i in LAB_LST]
layer_coords = vf.layer_coords(fullpath_lst)
vec_coords = vf.vec_coords(layer_coords, spacing=6)

#thickness values for full vectors and each individual layer
vec_thick = vf.vec_thick(layer_coords, vec_coords, img_path)
roi_vec_coords = vf.roi_vecs(layer_coords, vec_coords, 'fundus')
lall_ind_thick = vf.ind_thick(layer_coords, roi_vec_coords, img_path)
print("fundus lall_ind_thick = \n", np.array(lall_ind_thick) ,"\n")
# print(vf.vec_thick(layer_coords, roi_vec_coords, img_path), "\n")
# print('tot_thick = ', sum(lalllall_ind_thick_thick), "\n")


#plot layers 
for layer in layer_coords:
    plt.plot([i[0] for i in layer_coords[layer]], [i[1] for i in layer_coords[layer]], \
        lw=2.5, c='#964000') #7F50CD
#plot ind str vectors
# for coords in np.array(roi_vecs[0]):
#     plt.plot([i[0] for i in coords], [i[1] for i in coords], c="#767676", \
#     alpha=1, lw=1.2)#767676

#plot ind str vectors, only in roi
for coords in np.array(roi_vec_coords):
    ax = plt.subplot()
    vec = ax.plot([i[0] for i in coords], [i[1] for i in coords], \
        c="#767676", alpha=1, lw=1.2)
plt.gca().invert_yaxis()
# plt.show()
plt.close()




#todo
#compute csv thickness for all data, parallel process
#analyse csv data