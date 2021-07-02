"""
Name: Kimberly Nestor
Date: 06/2021
Description: This program loads a volume and waypoints slice by slice, 
            enter key is used to signal the next iteration of the loop. This 
            allows the user to edit waypoints one slice at a time and prevent 
            the points from connecting over several slices.
"""

import os

#volume waypoint input info
vpath = '/autofs/cluster/oribivault/data/EXC022_lh_phoenixcoil_062320/label/'
wpath = '/autofs/cluster/oribivault/data/EXC022_lh_phoenixcoil_062320/label/\
way_points'
vol = 'flash20.mgz'
start, end = 560, 660 #label slice info

#loop to load each slice in BA 44/45
for i in list(range(start, end)):
    str_i = '*' + str(i) + '*'
    load_cmd = 'freeview ' + os.path.join(vpath, vol) + ' -viewport y -slice ' \
    + str(i) + ' 700 320 -w ' + os.path.join(wpath, str_i)
    input("Press ENTER:")
    print(load_cmd, "\n")
    os.system(load_cmd)