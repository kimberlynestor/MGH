import glob, os
import sys

volpath = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/mri/**'
output_dir = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/mri/parameter_maps_B0_B1Tx/'
scrpath = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/correction_scripts/'

volume_list = []
for volname in glob.glob(volpath, recursive=True):
    #print(volname)
    if os.path.isfile(volname):
        if "echo" in volname and "whitened_rms_b0Corr_ep05_lp5_FA" in volname:
            if "echo0" in volname and "FA20" in volname:
                continue
            # elif "echo0" in volname and "FA10_R0neg"  in volname:
            #     continue
            volume_list.append(volname)

volume_list.sort()
#print(volume_list)

# fa10 = [volname for volname in volume_list if "FA10_b0corr" in volname]
# fa10_r0neg = [volname for volname in volume_list if "FA10_R0neg_b0corr" in volname]
# print(fa10_r0neg)
# fa20_r0neg = [volname for volname in volume_list if "FA20_R0neg_b0corr" in volname]
# fa40 = [volname for volname in volume_list if "FA40_b0corr" in volname]

b1transmap = [volname for volname in glob.glob(volpath, recursive=True) if volname.endswith("B1Txmap_resamp_epol.nii.gz")]
# print(b1transmap)

tr = 34
te_list = [5.65, 11.95, 18.25, 24.55]

prlist = []
for volname in volume_list:
    if "FA10" in volname:
        fa = 10
        if "echo0" in volname:
            te = te_list[0]
        elif "echo1" in volname:
            te = te_list[1]
        elif "echo2" in volname:
            te = te_list[2]
        elif "echo3" in volname:
            te = te_list[3]
    elif "FA20" in volname:
        fa = 20
        if "echo0" in volname:
            te = te_list[0]
        elif "echo1" in volname:
            te = te_list[1]
        elif "echo2" in volname:
            te = te_list[2]
        elif "echo3" in volname:
            te = te_list[3]
    elif "FA40" in volname:
        fa = 40
        if "echo0" in volname:
            te = te_list[0]
        elif "echo1" in volname:
            te = te_list[1]
        elif "echo2" in volname:
            te = te_list[2]
        elif "echo3" in volname:
            te = te_list[3]
    prvar = volname + " -te " + str(te) + " -tr " + str(tr) + " -fa " + str(fa)
    prlist.append(prvar)
#print(prlist)


shell_command = "mri_ms_fitparms -fam " + str(b1transmap) + " 1 -n 0 -te 24.55 -tr 34 -fa 20 " + str(prlist) + " " + output_dir + " > " + scrpath + "fitparm.log"
shell_command = shell_command.replace('[', '')
shell_command = shell_command.replace(']', '')
shell_command = shell_command.replace(',', '')
shell_command = shell_command.replace("'", "")



os.system(shell_command)
# print(shell_command)
#sys.exit()



#
