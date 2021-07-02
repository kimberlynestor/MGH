"""
Name: Kimberly Nestor
Date: 06/2021
Description: This program makes a gif out of input volumes and labels. 
             Uses parallel processing, half total number of cores to account 
             for computer freezing while using Freeview.
"""

import os
import sys
import multiprocessing as mp
import imageio


# init parallel processing
pool = mp.Pool( int(mp.cpu_count()/2) )

# volume and label info
indir = '/autofs/cluster/exvivo3/I56_rh_32chexvivo_010320/mri/label/'
outdir = '/autofs/cluster/exvivo3/I56_rh_32chexvivo_010320/mri/label/gif_imgs_dir/'

volume = 'flash20_rotated.mgz'
label = 'I56layer_labels_rotated_SmartInterp_edit.mgz'

"""
# 'view_plane' : [[vol_start, vol_stop], cursor, coord] , cursor for first vol
# indicate direction with reversed(), can change to centroid on label

#dict of volume slice and cursor info, change
plane_slice_dict = {'x': [730, 760, list(range(70, 565))], \
                    'y': [list(range(70, 1400)), 780, 300], \
                    'z': [800, list(range(325, 1160)), 300] }


#loop to generate screenshots and then make gif
for key, val in plane_slice_dict.items():
    #sagittal plane
    if key == 'x':
        axis = key
        take_img_cmd_lst = []
        make_gif_cmd_lst = []

        take_img_cmd_ol_lst = []
        make_gif_cmd_ol_lst = []


        #generate screenshots
        for i in list(range(1, len(val[2]))):
            slice = val[2][i]

            #full label
            take_img_cmd = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:opacity=0.25 -ss ' + os.path.join(outdir, axis + \
                '_img' + str(i).zfill( len(str(len(val[2]))) )) + ' 5 -viewport \'' \
                + axis + '\' -slice ' + str(val[0]) + ' ' + str(val[1]) + ' ' \
                + str(slice) + ' -zoom 1.65' 
            
            # take_img_cmd_lst.append(take_img_cmd)
            print(take_img_cmd, "\n")
            # os.system(take_img_cmd)

            #label outline, label_outline for surfaces
            take_img_cmd_ol = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:outline=1:opacity=1 -ss ' + os.path.join(outdir, \
                axis + '_img_ol' + str(i).zfill( len(str(len(val[2]))) )) \
                + ' 5 -viewport \'' + axis + '\' -slice ' + str(val[0]) + ' ' + \
                str(val[1]) + ' ' + str(slice) + ' -zoom 1.65' 
            
            #using bash imagemagick
            take_img_cmd_ol_lst.append(take_img_cmd_ol) 
            print(take_img_cmd_ol, "\n")
            # os.system(take_img_cmd_ol)

        # parallel processing
        pool.map_async(os.system, take_img_cmd_lst)
        pool.map_async(os.system, take_img_cmd_ol_lst)
        
        # if process:
        #     os.wait()
      

        #make gif command
        make_gif_cmd = 'convert -reverse ' + axis + '_img*.png axis_' + axis + '.gif'
        make_gif_cmd_ol = 'convert -reverse ' + axis + '_img_ol*.png axis_' + axis + 'ol.gif'

        make_gif_cmd_lst.append(make_gif_cmd) 
        make_gif_cmd_ol_lst.append(make_gif_cmd_ol) 


    #coronal plane
    if key == 'y':
        axis = key
        take_img_cmd_lst = []
        take_img_cmd_ol_lst = []

        #generate screenshots
        for i in list(range(1, len(val[0]))):
            slice = val[0][i]

            #full label
            take_img_cmd = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:opacity=0.25 -ss ' + os.path.join(outdir, axis + \
                '_img' + str(i).zfill( len(str(len(val[0]))) )) + ' 5 -viewport \'' \
                + axis + '\' -slice ' + str(slice) + ' ' + str(val[1]) + ' ' \
                + str(val[2]) + ' ' + ' -zoom 1.65' 
            
            take_img_cmd_lst.append(take_img_cmd)
            print(take_img_cmd, "\n")
            # os.system(take_img_cmd)

            #label outline
            take_img_cmd_ol = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:outline=1:opacity=1 -ss ' + os.path.join(outdir, \
                axis + '_img_ol' + str(i).zfill( len(str(len(val[0]))) )) \
                + ' 5 -viewport \'' + axis + '\' -slice ' + str(slice) + ' ' + \
                str(val[1]) + ' ' + str(val[2]) + ' ' + ' -zoom 1.65' 
            
            take_img_cmd_ol_lst.append(take_img_cmd_ol)
            print(take_img_cmd_ol, "\n")
            # os.system(take_img_cmd_ol)
            
        # parallel processing
        pool.map_async(os.system, take_img_cmd_lst)
        pool.map_async(os.system, take_img_cmd_ol_lst)
        # if process:
        #     os.wait()
       

        #make gif command
        make_gif_cmd = 'convert ' + axis + '_img*.png axis_' + axis + '.gif'
        make_gif_cmd_ol = 'convert ' + axis + '_img_ol*.png axis_' + axis + 'ol.gif'

        make_gif_cmd_lst.append(make_gif_cmd) 
        make_gif_cmd_ol_lst.append(make_gif_cmd_ol) 


    #axial plane
    if key == 'z':
        axis = key
        take_img_cmd_lst = []
        take_img_cmd_ol_lst = []

        #generate screenshots
        for i in list(range(1, len(val[1]))):
            slice = val[1][i]

            #full label
            take_img_cmd = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:opacity=0.25 -ss ' + \
                os.path.join(outdir, axis + '_img' + str(i).zfill( len(str(len(val[1]))) )) \
                + ' 5 -viewport \'' + axis + '\' -slice ' + str(val[0]) + ' ' + \
                str(slice) + ' ' + str(val[2]) + ' ' + ' -zoom 1' 
            
            take_img_cmd_lst.append(take_img_cmd)
            print(take_img_cmd, "\n")
            # os.system(take_img_cmd)

            #label outline
            take_img_cmd_ol = 'freeview -v ' + os.path.join(indir, volume) + \
                ':grayscale=17.65,39.26 ' + os.path.join(indir, label) + \
                ':colormap=LUT:outline=1:opacity=1 -ss ' + os.path.join(outdir, \
                axis + '_img_ol' + str(i).zfill( len(str(len(val[1]))) )) \
                + ' 5 -viewport \'' + axis + '\' -slice ' + str(val[0]) + ' ' \
                + str(slice) + ' ' + str(val[2]) + ' ' + ' -zoom 1' 
            
            take_img_cmd_ol_lst.append(take_img_cmd_ol)
            print(take_img_cmd_ol, "\n")
            # os.system(take_img_cmd_ol)

        # parallel processing
        pool.map_async(os.system, take_img_cmd_lst)
        pool.map_async(os.system, take_img_cmd_ol_lst)
        pool.close()
        pool.join()

        #make gif command
        make_gif_cmd = 'convert ' + axis + '_img*.png axis_' + axis + '.gif'
        make_gif_cmd_ol = 'convert ' + axis + '_img_ol*.png axis_' + axis + 'ol.gif'

        make_gif_cmd_lst.append(make_gif_cmd) 
        make_gif_cmd_ol_lst.append(make_gif_cmd_ol) 


"""


#get all gif img names
all_gif_img = sorted([i for i in os.listdir(outdir) if i.endswith('.png')])

x_img = sorted([i for i in all_gif_img if i.startswith('x_img') \
        and 'ol' not in i], reverse = True)
y_img = sorted([i for i in all_gif_img if i.startswith('y_img') \
        and 'ol' not in i])
z_img = sorted([i for i in all_gif_img if i.startswith('z_img') \
        and 'ol' not in i])

x_img_ol = sorted([i for i in all_gif_img if i.startswith('x_img_ol')], \
            reverse = True)
y_img_ol = sorted([i for i in all_gif_img if i.startswith('y_img_ol')])
z_img_ol = sorted([i for i in all_gif_img if i.startswith('z_img_ol')])

#make dict
group_dict = {'x': x_img, 
              'y': y_img, 
              'z': z_img,
              'xol': x_img_ol,
              'yol': y_img_ol,
              'zol': z_img_ol}


#execute make gif commands, using python imageio
img_lst = []
for key, val in group_dict.items():
    
    #make gif for key val group
    print(f'Currently appending key {key} ...')
    for img in val:
        img_lst.append( imageio.imread( os.path.join(outdir, img) ) )
    
    save_name = 'axis_' + key + '.gif'
    print(f'Currently saving {save_name} ...', "\n")
    imageio.mimsave( os.path.join(outdir, save_name) , img_lst)
    



"""
#execute make gif commands, using bash imagemagick
for make_gif_cmd, make_gif_cmd_ol in zip(make_gif_cmd_lst, make_gif_cmd_ol_lst):
    print(make_gif_cmd)
    print(make_gif_cmd_ol)
    os.chdir(outdir)
    os.system(make_gif_cmd)
    os.system(make_gif_cmd_ol)
"""

"""
# rename files in 001, 002, 003 format instead of 1, 2, 3
axis = 'x'
ones_lst = []
tens_lst = []
for image in sorted(os.listdir(outdir)):
    if image.startswith(axis) and image.endswith('.png'):
        # print(image[-6:-4])
        
        if len(image) == 10:
            ones_lst.append(image)
        elif len(image) == 11:
            tens_lst.append(image)

ones_lst = sorted(ones_lst)
tens_lst = sorted(tens_lst)

for image, i in zip(ones_lst, range(1, 10)):
    old_name = os.path.join(outdir, image)
    new_name = os.path.join(outdir, image.replace(image[-5:-4], \
                '{0:0>3}'.format(i)))
    os.rename(old_name, new_name)
    # print(new_name)

for image, i in zip(tens_lst, range(10, 100)):
    old_name = os.path.join(outdir, image)
    new_name = os.path.join(outdir, image.replace(image[-6:-4], \
                '{0:0>3}'.format(i)))
    os.rename(old_name, new_name)
    # print(new_name)
"""
