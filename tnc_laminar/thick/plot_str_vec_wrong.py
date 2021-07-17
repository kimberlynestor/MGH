"""
Name: Kimberly Nestor
Description: This program takes manually labelled points for a boundary and uses \
edge detection to determine coordinates. Coordinates are then used to plot \
straight line vectors. This version plots lines that are incorrect but shows the \
challenges of measuring thickness in the brain. 
"""

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

dpath = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/\
laminar_thickness/crown/I42/edited/'

LAB_LST = ['I42_block1_slice120_BA20B_LI_long.label', 'I42_block1_slice120_BA20B_LII.label', \
'I42_block1_slice120_BA20B_LIII.label', 'I42_block1_slice120_BA20B_LIV.label', \
'I42_block1_slice120_BA20B_LV.label', 'I42_block1_slice120_BA20B_LVI.label', \
'I42_block1_slice120_BA20B_GWB_long.label']

LAB_LST_LONG = ['I42_block1_slice120_BA20B_LI_long.label', \
                'I42_block1_slice120_BA20B_GWB_long.label']

LAB_LST_SHORT = ['I42_block1_slice120_BA20B_LII.label', \
'I42_block1_slice120_BA20B_LIII.label', 'I42_block1_slice120_BA20B_LIV.label', \
'I42_block1_slice120_BA20B_LV.label', 'I42_block1_slice120_BA20B_LVI.label']


fullpath_lst = [dpath + i for i in LAB_LST]
coords = vf.label_coords(fullpath_lst)


# PLOT MIN EUC DIST - very clumpy, bumps on gyral surface
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], lw=2)
for iso_pial in coords[0]:
    iso_dist_lst = []
    for iso_gwb in coords[6]:
        iso_dist = np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb))        
        iso_dist_lst.append(iso_dist)
    min_iso_dist = min(iso_dist_lst)
    min_iso_idx = iso_dist_lst.index(min_iso_dist)
    min_iso_coord = coords[6][min_iso_idx]
    plt.plot([iso_pial[0], min_iso_coord[0]], [iso_pial[1], min_iso_coord[1]],\
     lw=1.5, c='#000000')

plt.gca().invert_yaxis()
plt.axes().set_aspect('equal')
plt.show()
plt.close()


# PLOT USING SKIP - very crooked
# plot first line only using min euc dist
iso_pial_start = coords[0][0]
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], lw=2)
iso_dist_lst = []
for iso_gwb in coords[6]:
    iso_dist = np.linalg.norm(np.array(iso_pial_start) - np.array(iso_gwb))
    iso_dist_lst.append(iso_dist)
min_iso_dist = min(iso_dist_lst)
min_iso_idx = iso_dist_lst.index(min_iso_dist)
iso_gwb_start = coords[6][min_iso_idx]
plt.plot([iso_pial_start[0], iso_gwb_start[0]], [iso_pial_start[1], iso_gwb_start[1]],\
 lw=1.5, c='#000000')

# skip certain distance and then plot
for coord_pial, coord_gwb in zip(coords[0][1::4], \
 coords[6][min_iso_idx:len(coords[0]):2]):
    plt.plot([coord_pial[0], coord_gwb[0]], [coord_pial[1], coord_gwb[1]],\
     lw=1.5, c='#000000')
plt.gca().invert_yaxis()
plt.show()


# MIN DIST WITHIN WINDOW - mostly ok, still a little crooked
#plot layers
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], \
    lw=2.5, c='#964000')#850101
#plot first line using min dist
iso_dist_lst = []
for iso_gwb in coords[6]:
    iso_dist = np.linalg.norm(np.array(iso_pial_start) - np.array(iso_gwb))
    iso_dist_lst.append(iso_dist)
min_iso_dist = min(iso_dist_lst)
min_iso_idx = iso_dist_lst.index(min_iso_dist)
iso_gwb_start = coords[6][min_iso_idx]
plt.plot([iso_pial_start[0], iso_gwb_start[0]], [iso_pial_start[1], iso_gwb_start[1]],\
 lw=1.5, c='#000000')

#plot lines, min dist within window
gskip = 3
pskip = 7
iparam = list(range(min_iso_idx+4, len(coords[6]), gskip))
jparam = list(range(min_iso_idx+6, len(coords[6]), gskip))
pial_param = coords[0][4::pskip]

for i, j, iso_pial in zip( iparam, jparam, pial_param):
    iso_gwb_wind = list(enumerate(coords[6][i:j]))

    iso_dist_wind = [np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb[1])) \
      for iso_gwb in iso_gwb_wind]

    min_dist_coords = iso_gwb_wind[iso_dist_wind.index(min(iso_dist_wind))]

    plt.plot([iso_pial[0], min_dist_coords[1][0]], [iso_pial[1], \
      min_dist_coords[1][1]], lw=1.5, c='#000000')#0047AB , #0F52BA
plt.scatter([i[0] for i in coords[6][::25]], [i[1] for i in coords[6][::25]], s=20, c='#964000')#850101
plt.gca().invert_yaxis()
plt.show()


# CURVATURE GWB
#derivatives and velocity
cskip = 25
coords_gwb = np.array(coords[6][::cskip])
x_der = np.gradient(coords_gwb[:,0])
y_der = np.gradient(coords_gwb[:,1]) #col slicing, R, np.array, [:,0]
velo = np.array([[x_der[i], y_der[i]] for i in range(x_der.size)])

#displacement, tangent
displ = np.sqrt( x_der * x_der + y_der * y_der ) #speed, time
tang = np.array([1/displ] *2 ).transpose() * velo


x_tang = tang[:,0]
y_tang = tang[:,1]

x_tang_der = np.gradient(x_tang)
y_tang_der = np.gradient(y_tang)

#differential, rate of change
differ = np.array([[x_tang_der[i], y_tang_der[i]] for i in range(x_tang_der.size)])
len_differ = np.sqrt(x_tang_der * x_tang_der + y_tang_der * y_tang_der)

norm_vec = np.array([1/len_differ] * 2).transpose() * differ #direc of curve turn


#determine left curve, right curve start and stop
lcurve_lst = []
for i in list(enumerate(norm_vec)):
    if i[1][0] >0 and i[1][1] >0:
        lcurve_lst.append(i)
    elif i[1][0] <0:
        break

rcurve_lst = []
for i in list(enumerate(norm_vec)):
    if i[1][0] <0:
        rcurve_lst.append(i)
    
lcurve_start, lcurve_stop = lcurve_lst[0][0]*cskip, (lcurve_lst[-1][0]*cskip)-cskip
rcurve_start, rcurve_stop = (rcurve_lst[0][0]*cskip)+cskip, rcurve_lst[-1][0]*cskip
center_start, center_stop = (lcurve_lst[-1][0]*cskip)-cskip, (rcurve_lst[0][0]*cskip)+cskip


# PLOT USING CURVATURE 
#plot layers
for layer in coords:
    plt.plot([i[0] for i in coords[layer]], [i[1] for i in coords[layer]], lw=2.5, c='#964000')#850101
#plot first line using min dist
# iso_dist_lst = []
# for iso_gwb in coords[6]:
#     iso_dist = np.linalg.norm(np.array(iso_pial_start) - np.array(iso_gwb))
#     iso_dist_lst.append(iso_dist)
# min_iso_dist = min(iso_dist_lst)
# min_iso_idx = iso_dist_lst.index(min_iso_dist)
# iso_gwb_start = coords[6][min_iso_idx]
# plt.plot([iso_pial_start[0], iso_gwb_start[0]], [iso_pial_start[1], iso_gwb_start[1]],\
#  lw=1.5, c='#000000')

#plot lines, min dist within window
gskip = 3
pskip = 7
# iparam = list(range(min_iso_idx+4, lcurve_start, gskip)) #+ list(range(rcurve_stop+4, len(coords[6]), gskip))
# jparam = list(range(min_iso_idx+6, lcurve_start, gskip)) #+ list(range(rcurve_stop+6, len(coords[6]), gskip))
iparam = list(range(min_iso_idx+9, len(coords[6]), gskip))
jparam = list(range(min_iso_idx+10, len(coords[6]), gskip))
pial_param = coords[0][4::pskip]
for i, j, iso_pial in zip( iparam, jparam, pial_param):
    if i in list(range(lcurve_start, lcurve_stop)):
        iso_gwb_wind = list(enumerate(coords[6][i+5:j+5]))

        iso_dist_wind = [np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb[1])) \
        for iso_gwb in iso_gwb_wind]

        min_dist_coords = iso_gwb_wind[iso_dist_wind.index(min(iso_dist_wind))]
        plt.plot([iso_pial[0], min_dist_coords[1][0]], [iso_pial[1], \
        min_dist_coords[1][1]], lw=1.5, c='#000000')
        continue
    elif i in list(range(rcurve_start, rcurve_stop)):
        iso_gwb_wind = list(enumerate(coords[6][i+2:j+2]))

        iso_dist_wind = [np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb[1])) \
        for iso_gwb in iso_gwb_wind]

        min_dist_coords = iso_gwb_wind[iso_dist_wind.index(min(iso_dist_wind))]
        plt.plot([iso_pial[0], min_dist_coords[1][0]], [iso_pial[1], \
        min_dist_coords[1][1]], lw=1.5, c='#000000')
        continue
    elif i in list(range(center_start, center_stop)):
        iso_gwb_wind = list(enumerate(coords[6][i+6:j+6]))

        iso_dist_wind = [np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb[1])) \
        for iso_gwb in iso_gwb_wind]

        min_dist_coords = iso_gwb_wind[iso_dist_wind.index(min(iso_dist_wind))]
        plt.plot([iso_pial[0], min_dist_coords[1][0]], [iso_pial[1], \
        min_dist_coords[1][1]], lw=1.5, c='#000000')
        continue
    else:
        iso_gwb_wind = list(enumerate(coords[6][i:j]))

        iso_dist_wind = [np.linalg.norm(np.array(iso_pial) - np.array(iso_gwb[1])) \
        for iso_gwb in iso_gwb_wind]

        min_dist_coords = iso_gwb_wind[iso_dist_wind.index(min(iso_dist_wind))]
        plt.plot([iso_pial[0], min_dist_coords[1][0]], [iso_pial[1], \
        min_dist_coords[1][1]], lw=1.5, c='#000000')#0047AB , #0F52BA
plt.scatter([i[0] for i in coords[6][::25]], [i[1] for i in coords[6][::25]], s=20, c='#964000')#850101
plt.gca().invert_yaxis()
plt.show()


lam = 1

##### Normal Vector Pial
#derivatives and velocity
coords_pial = np.array(coords[0])
x_der = np.gradient(coords_pial[:,0])
y_der = np.gradient(coords_pial[:,1]) #col slicing, R, np.array, [:,0]
velo = np.array([[x_der[i], y_der[i]] for i in range(x_der.size)])

#displacement, tangent
displ = np.sqrt( x_der * x_der + y_der * y_der ) #speed, time
tang = np.array([1/displ] *2 ).transpose() * velo

#outward point surface normal, from tang flip, make first neg, opv
pial_normal = [ [y*-1, x] for x, y in zip(tang[:,0], tang[:,1]) ]


##### Normal Vector GWB
#derivatives and velocity
coords_gwb = np.array(coords[6])
x_der = np.gradient(coords_gwb[:,0])
y_der = np.gradient(coords_gwb[:,1]) 
velo = np.array([[x_der[i], y_der[i]] for i in range(x_der.size)])

#displacement, tangent
displ = np.sqrt( x_der * x_der + y_der * y_der ) 
tang = np.array([1/displ] *2 ).transpose() * velo

#outward point surface normal, owv
gwb_normal = [ [y*-1, x] for x, y in zip(tang[:,0], tang[:,1]) ]


#### TERM Jn(X)
# for each coord on the pial surface, x
for x in range(len(coords[0])):
    pial = coords[0][x]
    
    #find vector pial to gwb, unit length, tv
    vec_dist_lst = []

    start = 0
    energy_lst = []
    while start < len(coords[6]):
        normal_term_lst = []
        parallel_term_lst = []
        for v in range(start, len(coords[6])):
            #find vector distance from pial to gwb
            gwb = coords[6][v]
            vec_pial_gwb = np.array(gwb) - np.array(pial)
            vec_mag = np.array(vec_pial_gwb[0]**2 + vec_pial_gwb[1]**2)
            unit_vec_dist = vec_pial_gwb/vec_mag
            vec_dist_lst.append(unit_vec_dist)

            #find dot product for tv and owhite, tv and opial
            dot_prod1 = np.dot(vec_dist_lst[v], gwb_normal[v])
            dot_prod2 = np.dot(vec_dist_lst[v], pial_normal[x])

            #normal term for each v
            normal_term_v = (1 - np.abs(dot_prod1)) + (1 - np.abs(dot_prod2))
            normal_term_lst.append(normal_term_v)

            #parallel term for each v
            if x == 0:
                ####plot first line using min dist
                iso_pial_start = coords[0][0]
                iso_dist_lst = []
                for iso_gwb in coords[6][:40]:
                    iso_dist = np.linalg.norm(np.array(iso_pial_start) - np.array(iso_gwb))
                    iso_dist_lst.append(iso_dist)
                min_iso_dist = min(iso_dist_lst)
                min_iso_idx = iso_dist_lst.index(min_iso_dist)
                iso_gwb_start = coords[6][min_iso_idx]
                #find vector dist
                start_vec_dist = np.array(iso_gwb_start) - np.array(iso_pial_start)

                vec_mag_start = np.array(start_vec_dist[0]**2 + start_vec_dist[1]**2)
                unit_vec_dist_start = start_vec_dist/vec_mag_start


                #find dot product
                dot_prod3 = np.dot(vec_dist_lst[v], unit_vec_dist_start)
                parallel_term_v = (1 - np.abs(dot_prod3))
                parallel_term_lst.append(parallel_term_v)

        
        # print(normal_term_lst)
        # sys.exit()
        #calculate term1 in equation
        sumof_term_norm = np.sum(normal_term_lst)
        term1 = (1 - lam) * sumof_term_norm        

        #calculate term2 in equation
        sumof_term_paral = np.sum(parallel_term_lst)
        term2 = lam * sumof_term_paral

        #energy
        energy = term1 + term2
        energy_lst.append(energy)

        ind_energy = np.array([((1-lam)*n) + (lam*p) for n, p in zip(normal_term_lst, parallel_term_lst)])
        print(ind_energy.T)
        sys.exit()

        start+=1

    print(np.array(energy_lst))
    sys.exit()


