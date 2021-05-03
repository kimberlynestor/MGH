
import sys
import os
#sys.exit()

dicompath = '/autofs/cluster/oribivault/raw/I53_lh_32chexvivo_20190316/dicom/'

outputloc = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/mri/I53_lh_32chexvivo_20190316_b1corr/b1transmit_scans/'

astpath = '/autofs/space/asterion_001/users/kn751/div_discorr/I53_lh_32chexvivo_20190316/correction_scripts/'

scanlog = open(astpath + "scan.log", 'r')
scanlog2 = scanlog.readlines()

#all the voltage scans that were done, phase is listed first then the magnitude
voltage_scansall = []
for i in scanlog2:
    if "gre_1echo_2mm_PA" in i:
        voltage_scansall.append(i)

#only magnitude not the phase
voltage_scansmag = voltage_scansall[1::2]
#print(voltage_scansmag)

#list of dicom names for only the magnitude scans
dicom_list = []
for i in voltage_scansmag:
    dicom_index = i.index("MR")
    dicom_range = i[dicom_index:]
    dicom_list.append(dicom_range)

scan_names = []
for i in voltage_scansmag:
    scan_index1 = i.index("gre")
    scan_index2 = i.index(" ok")
    scan_range = i[scan_index1:scan_index2]
    scan_range = scan_range[:-1]
    scan_names.append(scan_range)

zip_dicom_ScanName = list(zip(dicom_list, scan_names))
# print(zip_dicom_ScanName)


for dicom, scan in zip(dicom_list, scan_names):
    try:
        shell_convert_command = "mri_convert " + dicompath + dicom + " " + outputloc + scan + "_mag.mgz"
        shell_convert_command = shell_convert_command.replace('\n', '')
        #print(shell_convert_command)
        os.system(shell_convert_command)

    except IndexError:
        continue


scanlog.close()
