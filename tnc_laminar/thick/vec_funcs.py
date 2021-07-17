"""
Name: Kimberly Nestor
Date: 07/2021
Description: This module is to support plot.str_vec.py and 
compute_strvec_thickcsv.py, where the goal is to plot straight line vectors. 
Energy minimization is used to determine the optimal place for the vectors on 
the pial and gwb surface. The function vec_coords is based on Bruce and Marty's 
algorithm, found in the paper below. Edge detection is used to obtain all 
coordinates along the labelled lamianr boundaries.

(Fischl and Sereno, 2018)
https://www.sciencedirect.com/science/article/pii/S1053811918300363 

"""


import os
import sys
import csv

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2 #opencv-python
from sklearn.cluster import KMeans
import sklearn.metrics as sk
from sklearn.preprocessing import StandardScaler, LabelEncoder

import matplotlib.transforms as transforms
import matplotlib.image as mpimg
from PIL import Image

import warnings

# pd.set_option("display.max_rows", None, "display.max_columns", None)
warnings.filterwarnings("ignore")



def layer_coords(label_lst): #full path
    """This function takes as input a list of paths to the manual layer labels.
        Uses edge detection to determine all coordinates along the line. kMeans
        to cluster our unwanted points. Returns dict of coords for each layer."""
    
    #if a fundus then do this block
    gyrus_check = all(i.__contains__("fundus") for i in label_lst)
    if gyrus_check:
        for layer in label_lst:
            #read data
            df_layer  = pd.read_csv(layer)
            df_layer = df_layer.iloc[1:,0]
            df_layer = pd.DataFrame( [list(map(float, i)) for i in [list(i.split()) for i in \
            df_layer.values]], columns=['idk1', 'X', 'Y', 'Z', 'idk2'])[['X', 'Y', 'Z']]

            #compute slope
            yvals = [(y2 - y1) for y1, y2 in zip(df_layer['Y'], df_layer['Y'][1:])]
            xvals = [(x2 - x1) for x1, x2 in zip(df_layer['X'], df_layer['X'][1:])]
            layer_slope = [round(i,2) for i in np.divide(yvals, xvals)]

            #split lam label into three
            split = math.floor(len(df_layer['X'].values)/3)
            df_layer_right = df_layer[0:split]
            df_layer_left = df_layer[-split:]
            df_layer_middle = df_layer[split:-split]

            plt.plot(df_layer['X'], df_layer['Y'], lw=3) #color='#000000'
            # plt.plot(df_layer['X'], df_layer['Y'], linewidth=1, marker='o', markersize=5)
            plt.axis('off')
            plt.savefig('layer_contour.png')
        # plt.show()
        plt.close()

        #read, convert to grayscale, find edges
        layer_img = cv2.imread('layer_contour.png')
        layer_img_grey = cv2.cvtColor(layer_img, cv2.COLOR_BGR2GRAY)
        layer_edges = cv2.Canny(layer_img_grey, 30, 200)

        #find contours
        contours, hierachy = cv2.findContours(layer_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv2.imshow('contour', layer_edges)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
            
        #order contours
        contours = [np.squeeze(i) for i in contours]
        df_contours = pd.DataFrame(contours)
        contours_ord = df_contours.loc[6].values, df_contours.loc[4].values, \
                    df_contours.loc[3].values, df_contours.loc[2].values, \
                    df_contours.loc[1].values, df_contours.loc[0].values, \
                    df_contours.loc[5].values
        contours_ord = np.squeeze(contours_ord)
        

        #plot all layers and add coordinate data to dict   
        lay_coords_dict = {}
        for laycon, i in zip(contours_ord, list(range(len(contours)))):            
            #split coordinates into top and bottom edge
            if i == 0: #0 == pial
                c_idx = int(np.floor(len(laycon)/2))
                coords_top = np.array(list(reversed(laycon[:c_idx])))
                lay_coords_dict[i] = coords_top[10:]
                # print(coords_top)

            else:
                c_idx = int(np.floor(len(laycon)/2))
                coords_top = np.array(list(reversed(laycon[c_idx:])))
                lay_coords_dict[i] = coords_top[5:-7]

        
        #plot coords
        # for key, val in lay_coords_dict.items():
        #     plt.plot([i[0] for i in val], [i[1] for i in val], lw=1.75)
        # plt.gca().invert_yaxis()
        # plt.show()
        # plt.close()
        # sys.exit()

        #delete edge detect image and return dict
        rm_img_cmd = "rm layer_contour.png"
        os.system(rm_img_cmd)
        return(lay_coords_dict)
    

    #for crown data do this block
    else:
        for layer in label_lst:
            #read data
            df_layer  = pd.read_csv(layer)
            df_layer = df_layer.iloc[1:,0]
            df_layer = pd.DataFrame( [list(map(float, i)) for i in [list(i.split()) for i in \
            df_layer.values]], columns=['idk1', 'X', 'Y', 'Z', 'idk2'])[['X', 'Y', 'Z']]

            #compute slope
            yvals = [(y2 - y1) for y1, y2 in zip(df_layer['Y'], df_layer['Y'][1:])]
            xvals = [(x2 - x1) for x1, x2 in zip(df_layer['X'], df_layer['X'][1:])]
            layer_slope = [round(i,2) for i in np.divide(yvals, xvals)]

            #split lam label into three
            split = math.floor(len(df_layer['X'].values)/3)
            df_layer_right = df_layer[0:split]
            df_layer_left = df_layer[-split:]
            df_layer_middle = df_layer[split:-split]

            plt.plot(df_layer['X'], df_layer['Y'], lw=3) #color='#000000', lw=5
            # plt.plot(df_layer['X'], df_layer['Y'], linewidth=1, marker='o', markersize=5)
            plt.axis('off')
            plt.savefig('layer_contour.png')
        # plt.show()
        plt.close()

        #read, convert to grayscale, find edges
        layer_img = cv2.imread('layer_contour.png')
        layer_img_grey = cv2.cvtColor(layer_img, cv2.COLOR_BGR2GRAY)
        layer_edges = cv2.Canny(layer_img_grey, 30, 200)

        #find contours
        contours, hierachy = cv2.findContours(layer_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv2.imshow('contour', layer_edges)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
            

        #plot all layers and add coordinate data to dict
        lay_coords_dict = {}
        for laycon, i in zip(contours, list(range( len(contours) ) )[::-1] ):#7
            #split coordinates into top and bottom edge
            # print(laycon)
            coords_lst = [list(ii) for i in laycon for ii in i] # 0 == GWB
            # print(coords_lst)

            c_split = math.floor(len(coords_lst)/4)
            coords_top = coords_lst[:c_split][::-1] + coords_lst[-c_split:][::-1]
            lay_coords_dict[i] = coords_top
            df_coords = pd.DataFrame(coords_top, columns=['X', 'Y'])
            # print(df_coords)

            #plot using all coordinates
            plt.plot(df_coords['X'].values, df_coords['Y'].values, lw=3)
        plt.gca().invert_yaxis()
        # plt.show()
        plt.close()


        # use k means to get rid of extra coords on short lines
        for i in list(range(1,6)):
            # kMEANS clustering, separate short line bottom half
            df_short = pd.DataFrame(lay_coords_dict[i], columns=['X', 'Y']) #1=L1,
            # plt.scatter( df_short['X'].values, df_short['Y'].values, s=5 )
            # plt.gca().invert_yaxis()
            # plt.show()

            #scale data
            scaler = StandardScaler()
            scaler.fit( df_short[['X', 'Y']].values )
            short_scale = scaler.transform( df_short[['X', 'Y']].values )

            init = np.array([[0.514, -0.629], [-1.101, 1.344]])

            #predict
            # kmeans_classifier = KMeans(n_clusters=2, init=init) #fixed centroids
            kmeans_classifier = KMeans(n_clusters=2) 

            y_kmeans = kmeans_classifier.fit_predict(short_scale)
            centroids = kmeans_classifier.cluster_centers_
            inertia = kmeans_classifier.inertia_


            #update df
            df_short.insert(2, column='kClass', value=y_kmeans)

            #df scaled
            df_short_scale = pd.DataFrame(short_scale, columns=['X', 'Y'])
            df_short_scale.insert(2, column='kClass', value=y_kmeans)
            

            """
            #plot data points for k means, clusters
            colmap = {0: '#029386', 1: '#D2691E', 2: '#A52A2A'}
            for i in range(2):
                new_df = df_short_scale[df_short_scale['kClass']==i]
                plt.scatter(new_df['X'].values, new_df['Y'].values, s=20, \
                            label='cluster' + str(i+1), color=colmap[i])

            #plot centroids
            for i in range (2):
                plt.scatter(centroids[i][0], centroids[i][1], marker='x', s=500, \
                        label='centroid' + str(i+1), color=colmap[i])
            
            plt.legend()
            plt.gca().invert_yaxis()
            plt.show()
            """


            #new df for clean data, take centroid with more data points
            num_class0 = len(df_short[df_short['kClass']==0])
            num_class1 = len(df_short[df_short['kClass']==1])

            if num_class0 > num_class1:
                
                df_short_clean = df_short[df_short['kClass']==0]
                lay_coords_dict[i] = [[i,j] for i,j in zip(df_short_clean['X'].values,\
                df_short_clean['Y'].values)]
            else:
                df_short_clean = df_short[df_short['kClass']==1]
                lay_coords_dict[i] = [[i,j] for i,j in zip(df_short_clean['X'].values,\
                df_short_clean['Y'].values)]

            #plot clean short line
            # plt.scatter(df_short_clean['X'].values, df_short_clean['Y'].values, s=20)
            # plt.gca().invert_yaxis()
            # plt.show()

        #delete edge detect image and return dict
        rm_img_cmd = "rm layer_contour.png"
        os.system(rm_img_cmd)
        return(lay_coords_dict)



def vec_coords(label_coords, LAMBDA=1, spacing=1):
    """ This function takes as input a dictionary of coordinates for each layer \
    (output from label_coords). The function uses the pial and gwb coordinates \
    to plot straight vectors using energy minimization to determine the opimal \
    point on the gwb to plot a vector from point x on the pial surface. This is \
    a 2D version of the algorithm Bruce and Marty published. 
    
    LAMBDA: determines how clumped together the vectors are
    spacing: determines how far apart vectors are """

    #LAMBDA = 1
    #SPACING = 8
    SPACING = spacing
    
    coords_pial = np.array(label_coords[0])
    coords_gwb = np.array(label_coords[6]) #[::SPACING]


    ##### Normal Vector Pial
    #derivatives and velocity
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
    x_der = np.gradient(coords_gwb[:,0])
    y_der = np.gradient(coords_gwb[:,1]) 
    velo = np.array([[x_der[i], y_der[i]] for i in range(x_der.size)])

    #displacement, tangent
    displ = np.sqrt( x_der * x_der + y_der * y_der ) 
    tang = np.array([1/displ] *2 ).transpose() * velo

    #outward point surface normal, owv
    gwb_normal = [ [y*-1, x] for x, y in zip(tang[:,0], tang[:,1]) ]



    plot_coords_lst = []
    used_energy_lst = []
    ##### FIND ENERGY
    # for each coord on the pial surface, x
    for x in range(len(coords_pial)):
        pial = coords_pial[x]
        
        #find vector pial to gwb, unit length, tv
        if x == 0:
            min_energy = []
            normal_term_lst = []
            vec_dist_lst = []
            parallel_term_lst = []
            vec_dist_lst = []
            for v in range(len(coords_gwb)):
                #find vector distance from pial to gwb
                gwb = coords_gwb[v]
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
                # if x == 0:
                
                #find dot product, using self distance
                dot_prod3 = np.dot(vec_dist_lst[v], vec_dist_lst[v])
                parallel_term_v = (1 - np.abs(dot_prod3))
                parallel_term_lst.append(parallel_term_v)
                
            #energy, no summation
            ind_energy = list(enumerate(np.array([((1-LAMBDA)*n) + (LAMBDA*p) for n, p in \
                                zip(normal_term_lst, parallel_term_lst)]).T))
                    
            #find local minima energy
            for i in range(len(ind_energy)):
                curr = ind_energy[i]
                fut = ind_energy[i+1]
                if fut[1] > curr[1]:
                    min_energy.append(curr)
                    used_energy_lst.append(curr)
                    break

            # append coordinates to plot straight vector from pial to gwb, min energy
            gwb_idx = min_energy.pop()[0]
            # gwb_idx = min_energy[-1][0]
            plot_coords_lst.append([pial, list(coords_gwb[gwb_idx])])

        elif x > 0:
            min_energy = []
            normal_term_lst = []
            vec_dist_lst = []
            parallel_term_lst = []
            vec_dist_lst = []
            
            
            # used_start = int(used_energy_lst[-1][0])+20
            used_start = used_energy_lst[-1][0]

            for v in list( range(used_start, len(coords_gwb)-1) ):
                #find vector distance from pial to gwb
                gwb = coords_gwb[v]
                vec_pial_gwb = np.array(gwb) - np.array(pial)
                vec_mag = np.array(vec_pial_gwb[0]**2 + vec_pial_gwb[1]**2)
                unit_vec_dist = vec_pial_gwb/vec_mag
                vec_dist_lst.append(unit_vec_dist)

                #find dot product for tv and owhite, tv and opial
                dot_prod1 = np.dot(vec_dist_lst[-1], gwb_normal[v])
                dot_prod2 = np.dot(vec_dist_lst[-1], pial_normal[x])

                #normal term for each v
                normal_term_v = (1 - np.abs(dot_prod1)) + (1 - np.abs(dot_prod2))
                normal_term_lst.append(normal_term_v)

                #parallel term for each v                    
                #find dot product, using neighbour vector distance
                knear_vec_dist = np.array(plot_coords_lst[-1][1]) - np.array(plot_coords_lst[-1][0])
                dot_prod3 = np.dot(vec_dist_lst[-1], knear_vec_dist)
                parallel_term_v = (1 - np.abs(dot_prod3))
                parallel_term_lst.append(parallel_term_v)   

            #energy, no summation
            ind_energy = list( enumerate(np.array([ ((1-LAMBDA)*n) + (LAMBDA*p) for n, p in \
                        zip(normal_term_lst, parallel_term_lst)]).T, used_energy_lst[-1][0])) #v

            #find local minima energy, and associated coordinate
            for i in range(len(ind_energy)):
                try:
                    curr = ind_energy[i]
                    fut = ind_energy[i+1]
                except(IndexError):
                    continue
                    
                if fut[1] > curr[1]:
                    min_energy.append(curr)
                    used_energy_lst.append(curr)
                    # print("curr energy = ", curr)
                    break

            try:
                gwb_idx = min_energy.pop()[0] #+ 20 #atleast deltaX apart
                plot_coords_lst.append([pial, list(coords_gwb[gwb_idx])])
                # print("energy coordinates = ", list( map(list, [pial, coords_gwb[gwb_idx]])) )
            except(IndexError):
                continue


    """
    #encourage atleast one space between each end point coordinate
    energy_idx = [i[0] for i in used_energy_lst]
    new_energy_idx = []
    energy_idx_cp = energy_idx.copy()

    count = 0
    same_count = 0
    # loop to remove repeat indices, makes list two short
    while count < len(energy_idx):
        energy_concat = []
        i = count
        curr = energy_idx_cp[i]
        if energy_idx_cp[i] not in new_energy_idx:
            new_energy_idx.append(curr)
            same_count = 0
        else:        
            energy_idx_cp = energy_idx_cp[:i] + list((np.array(energy_idx_cp[i:]) \
                                                            + same_count))

            same_count+=1
        
        count+=1
    """


    #encourage even space between each end point coordinate
    energy_idx = [i[0] for i in used_energy_lst]
    new_energy_idx = list(map(math.floor , np.linspace(energy_idx[0] , \
                    len(coords_gwb[energy_idx[0]: len(coords_gwb)]), num=len(energy_idx)))) 

    # new_plot_coords_lst = [[list(i[0]), list(coords_gwb[j])] for i, j in \
    #                         zip(plot_coords_lst, new_energy_idx)]

    new_plot_coords_lst = []
    for i, j in zip(plot_coords_lst, new_energy_idx):
        try:
            pial_gwb_plot = [list(i[0]), list(coords_gwb[j])]
            new_plot_coords_lst.append(pial_gwb_plot)        
        except(IndexError):
            continue

    #space vectors according to SPACING var
    new_plot_coords_lst = new_plot_coords_lst[::SPACING] 

    return(new_plot_coords_lst)



def vec_thick(layer_coords, vector_coords, tissue_img):
    """ This function takes as input coordinates for the straight vectors 
    and a path to the original tissue image from the microscope the layers 
    boundaries are based on. This image is used to determine the distance of 
    the vectors and returns a list of distances in mm corresponding to the 
    original input vector coordinates."""

    # print('vector_coords = ', vector_coords)
    vec_euc_lst = []
    #plot layers 
    for layer in layer_coords:
        plt.plot([i[0] for i in layer_coords[layer]], [i[1] for i in layer_coords[layer]], \
            lw=2.5, c='#964000') #7F50CD
    #plot ind straight vectors
    for coords in vector_coords:
        try:
            fig = plt.plot([i[0] for i in coords], [i[1] for i in coords], c="#767676", \
            alpha=1, lw=1.2)#767676    
        except(IndexError):
            continue


        euc = np.linalg.norm(np.array(coords[0]) - np.array(coords[1]))
        vec_euc_lst.append(euc)

    # print('vec_euc_lst = ', vec_euc_lst)

    #find bbox euc distance
    vec_xlims = plt.gca().get_xlim()
    vecx_euc_dist = np.linalg.norm( np.array(vec_xlims)[0] - np.array(vec_xlims)[1] )

    plt.gca().invert_yaxis()
    # plt.show()
    plt.close()


    #plot tissue img
    tiss_img = plt.imshow(mpimg.imread(tissue_img))
    plt.gca().invert_yaxis()
    # plt.show()
    plt.close()

    #get tiss_img dimensions, find distance in mm, 4x microscope 1px = 1.85um
    img_px_dim = Image.open(tissue_img).size
    img_mm_dim = (img_px_dim[0] * 1.85) / 1000

    """
    #size of axes in pixels *dpi, 4.96 3.696
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()) 
    print("bbox in inches = ", bbox.width, bbox.height)

    #grayscale
    img = Image.open(tissue_img).convert("L")
    arr = np.asarray(img)
    plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
    plt.gca().invert_yaxis()
    plt.show()
    """

    #euc to mm conversion 
    euc_mm_unit = img_mm_dim / vecx_euc_dist
    vec_mm_dist_lst = [euc * euc_mm_unit for euc in vec_euc_lst]

    return(vec_mm_dist_lst)



def roi_vecs_v1(vec_coords, vec_thick, region):
    """This function takes as input the coordinates for straight vectors 
    and the associated thickmess values from the pial surface to the gwb. 
    The function then returns the coordinates of the vectors only in our 
    small ROI, where the crown and fundus are closest to a slope of 0."""
    
    if region =='fundus':
        #find gradients for thickness vectors
        vec_thick_gradients = list(np.gradient(vec_thick))
        min_val, min_idx = min(vec_thick_gradients), vec_thick_gradients.\
                                                    index(min(vec_thick_gradients))
        vec_thick_grad_enum = list(enumerate(np.gradient(vec_thick)))

        """
        #plot gradient descent curve
        for i in vec_thick_grad_enum:
            print(i)
        plt.plot(vec_thick_gradients, marker='o', ms=2.5)
        plt.show()
        """
            
        #use gradient descent to find start and stop vectors
        for i in reversed(vec_thick_grad_enum[:min_idx]):
            if i[1] < min_val + 0.01:
                vec_start = i
            elif i[1] > min_val + 0.01:
                break
        for i in vec_thick_grad_enum[min_idx:]:
            if i[1] < min_val + 0.08:
                vec_stop = i
            elif i[1] > min_val + 0.08:
                break

        #vector coordinates and thickness values in roi
        roi_vec_coords = vec_coords[vec_start[0]:vec_stop[0]+1]
        roi_vec_thick = vec_thick[vec_start[0]:vec_stop[0]+1]

        return roi_vec_coords, roi_vec_thick
    
    elif region =='crown':
        #find gradients for thickness vectors
        vec_thick_gradients = list(np.gradient(vec_thick))
        min_val, min_idx = min(vec_thick_gradients), vec_thick_gradients.\
                                                    index(min(vec_thick_gradients))
        vec_thick_grad_enum = list(enumerate(np.gradient(vec_thick)))

        """
        #plot gradient descent curve
        for i in vec_thick_grad_enum:
            print(i)
        plt.plot(vec_thick_gradients, marker='o', ms=2.5)
        plt.show()
        """
        

        #threshold out lines outside of roi
        roi_grad_lst = np.unique([round(i,2) for i in np.linspace(0.05, 0.3, 60)])
        roi_thres_lst = []
        for i in vec_thick_grad_enum:
            if round(i[1], 2) in roi_grad_lst:
                roi_thres_lst.append(i)


        #vector coordinates and thickness values in roi
        vec_start = roi_thres_lst[0]
        vec_stop = roi_thres_lst[-1]
        
        roi_vec_coords = vec_coords[vec_start[0]:vec_stop[0]+1]
        roi_vec_thick = vec_thick[vec_start[0]:vec_stop[0]+1]

        return roi_vec_coords, roi_vec_thick



def roi_vecs(layer_coords, vec_coords, region):
    """This function takes as input the coordinates for layer boundaries and 
    straight vectors from the pial surface to gwb. The function then returns 
    the coordinates of the vectors only in our small ROI."""
    
    if region == 'crown':
        #find threshold for vectors inside roi
        start_x_lst = []
        stop_x_lst = []
        for i in range(1,5):
            start_x_lst.append(layer_coords[i][0][0])
            stop_x_lst.append(layer_coords[i][-1][0])

        start_x = max(start_x_lst)
        stop_x = min(stop_x_lst)
        
        roi_vec_coords = [i for i in vec_coords if i[0][0] in list(range(start_x, stop_x+5))]
        
        return roi_vec_coords
    
    elif region == 'fundus':
        #find threshold for vectors inside roi
        start_x_lst = []
        stop_x_lst = []
        for i in range(1,5):
            start_x_lst.append(layer_coords[i][0][0])
            stop_x_lst.append(layer_coords[i][-1][0])

        start_x = max(start_x_lst)
        stop_x = min(stop_x_lst)

        # roi_vec_coords = [i for i in vec_coords if i[1][0] in list(range(start_x-10, stop_x+3))]
        roi_vec_coords = [i for i in vec_coords if i[0][0] in list(range(stop_x, start_x))]
        
        # print(roi_vec_coords)
        return roi_vec_coords



def ind_thick(layer_coords, roi_vec_coords, tissue_image):
    """This function takes as input a list of coordinates for each individual 
    layer(roi_vec_coords) and returns a list of individual thickness values 
    for each layer."""
    #find thickness for each ind layer
    
    vecall_lall_lst = []
    for vec in roi_vec_coords:
        #coordinates for intersection of vector and layer
        x_in_pts = list(map(math.floor, np.linspace(vec[0][0], vec[1][0], 70)))[1:-1] #or70
        # print(x_in_pts)
        l1_vec = vec[0], list(np.squeeze([i for i in layer_coords[1] if i[0] == x_in_pts[0]]))
        l2_vec = l1_vec[1], list(np.squeeze([i for i in layer_coords[2] if i[0] == x_in_pts[1]]))
        l3_vec = l2_vec[1], list(np.squeeze([i for i in layer_coords[3] if i[0] == x_in_pts[2]]))
        l4_vec = l3_vec[1], list(np.squeeze([i for i in layer_coords[4] if i[0] == x_in_pts[3]]))
        l5_vec = l4_vec[1], list(np.squeeze([i for i in layer_coords[5] if i[0] == x_in_pts[4]]))
        l6_vec = l5_vec[1], vec[1]
        

        #thickness values for each layer
        lall_vec = l1_vec, l2_vec, l3_vec, l4_vec, l5_vec, l6_vec
        lall_thick = vec_thick(layer_coords, lall_vec, tissue_image)
        
        # print(l5_vec, "\n", l6_vec)
        print(lall_thick)    

        vecall_lall_lst.append(lall_thick)
    
    return vecall_lall_lst



def save_thick_csv(path, label_lst, org_tiss_img, save_name):
    """This function takes as input the names of the laminar boundary labels and 
    saves an output csv file with thickness values."""
    #get label full path info
    org_tiss_img = path + org_tiss_img

    org_label_lst = [i for i in label_lst if 'LI_long' in i], \
    [i for i in label_lst if 'LII.' in i], [i for i in label_lst if 'LIII.' in i], \
    [i for i in label_lst if 'LIV.' in i], [i for i in label_lst if 'LV.' in i], \
    [i for i in label_lst if 'LVI.' in i], [i for i in label_lst if 'GWB_long' in i]

    org_label_lst = [ii for i in org_label_lst for ii in i]
    full_path_lst = [path+i for i in org_label_lst]
    

    #get coordinates and vectors for laminar boundaries
    lay_coords = layer_coords(full_path_lst)
    vector_coords = np.array(vec_coords(lay_coords))
    
    
    fun_check = [True for i in label_lst if 'fundus' in i]

    # samp_vec_lst = []
    if all(fun_check):
        samp_vecs = np.array(roi_vecs(lay_coords, vector_coords, 'fundus'))
        # samp_vec_lst = samp_vecs
        # print(samp_vecs)
    else:
        samp_vecs = np.array(roi_vecs(lay_coords, vector_coords, 'crown'))

    #get ind layer thickness
    header = ['Layer1', 'Layer2', 'Layer3', 'Layer4', 'Layer5', 'Layer6', 'Tot_thick']
    layer_thickness = ind_thick(lay_coords, samp_vecs, org_tiss_img)
    full_line = layer_thickness
    # print(layer_thickness)
    # layer_thickness.append(str(sum(layer_thickness)))
    
    #create file and save thickness data
    with open(os.path.join(path, save_name+'.csv'), mode='w') as thick_csv:
        thick_csv_writer = csv.writer(thick_csv)
        thick_csv_writer.writerow(header)
        for thickness in layer_thickness:
            tot_thick = sum(thickness)
            full_line = thickness + [tot_thick]
            thick_csv_writer.writerow(full_line)
            