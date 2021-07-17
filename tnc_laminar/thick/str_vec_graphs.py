"""
Name: Kimberly Nestor
Date: 06/2021
Description: This program program outputs the sample graphs for the 
            plot_str_vec.py program which plots straight vectors on the gyral 
            crown and fundus."""

import os
import sys

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

fullpath_lst = [dpath + i for i in LAB_LST]
coords = vf.label_coords(fullpath_lst)
plot_vec_coords = vf.str_vec_coords(coords, spacing=8)


#plot layers and straight vectors
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], \
        lw=2.5, c='#964000') #7F50CD
for coords in np.array(plot_vec_coords):
    plt.plot([i[0] for i in coords], [i[1] for i in coords], c="#767676", \
    alpha=1, lw=1.2)#767676

plt.gca().invert_yaxis()
plt.tight_layout()
plt.xticks([])
plt.yticks([])
plt.savefig('BA_crown_str_vec_dpi300.png', dpi=300)
plt.show()
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


fullpath_lst = [dpath + i for i in LAB_LST]
coords = vf.label_coords(fullpath_lst)
plot_vec_coords = vf.str_vec_coords(coords, spacing=6)


#plot layers and straight vectors
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], \
        lw=2.5, c='#964000') #7F50CD
for coords in np.array(plot_vec_coords):
    plt.plot([i[0] for i in coords], [i[1] for i in coords], c="#767676", \
    alpha=1, lw=1.2)#767676

plt.gca().invert_yaxis()
plt.tight_layout()
plt.xticks([])
plt.yticks([])
plt.savefig('BA_fundus_str_vec_dpi300.png', dpi=300)
plt.show()
plt.close()

