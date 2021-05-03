
"""
name: script_thick_crown_fundus
Author: Kimberly Nestor
Use:
This script is part of the TNC laminar thickness project and uses the output thickness data from the laplace equation to do statistical analyses and data visualization. It also saves and compiles the data in an excel sheet named lam_thick_data_sheet.
"""

# thick_funcs is the homemade module thick_funcs.py with functions for this project
from thick_funcs import *
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import random as random
import array
import seaborn as sns
import statsmodels.stats.multitest as ssm
import glob, os
import sys
import plotly.offline as py
import plotly.figure_factory as ff
#import plotly.graph_objects as go
import plotly.io as pio
import plotly
from IPython.display import SVG, display
import thick_funcs
from pingouin import ancova
import plotly.graph_objects as go
#you'll need to include this in your script if orca is downloaded but plotly can't find it. If you want to make this permanend then source python from the terminal, import plotly, set the path and then save the config

#plotly.io.orca.config.executable = '/autofs/cluster/freesurfer/python/3.6/centos7/bin/orca'
#plotly.io.orca.config.save()


#CROWN

lam_thick_descrip_stats_crown = open("lam_thick_descrip_stats_crown.csv", "w")   #overwrite any info in file

lam_thick_descrip_stats_crown_sex = open("lam_thick_descrip_stats_crown_sex.csv", "w")

#sulcus_test = open("sulcus_test.csv", "w")


#Data description
print("Descriptive Statistics - Crown Thickness")
lam_thick_descrip_stats_crown.write("Descriptive Statistics - Crown Thickness\n")

lam_thick_descrip_stats_crown_sex.write("Descriptive Statistics - Crown Sex Thickness\n")


lam_thick_descrip_stats_crown = open("lam_thick_descrip_stats_crown.csv", "a")   #append everything else to the file

lam_thick_descrip_stats_crown_sex = open("lam_thick_descrip_stats_crown_sex.csv", "a")

# sulcus_test = open("sulcus_test.csv", "a")



#I25
I25_BA20A_avg_Lall_crown = import_clean_data_avg("I25", "BA20A", "crown")
I25_BA20B_avg_Lall_crown = import_clean_data_avg("I25", "BA20B", "crown")
I25_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I25", "BA20A", "BA20B")
I25_BA21_avg_Lall_crown = import_clean_data_avg("I25", "BA21", "crown")
I25_BA22_avg_Lall_crown = import_clean_data_avg("I25", "BA22", "crown")
I25_BA36_avg_Lall_crown = import_clean_data_avg("I25", "BA36", "crown")
# print("I25_BA21_avg_Lall_crown = ", I25_BA21_avg_Lall_crown)
# print("I25_BA20_all_avg_Lall_crown = ", I25_BA20_all_avg_Lall_crown)
#sulcus_test.write("I25_BA21_avg_Lall_crown = {}\n".format(I25_BA21_avg_Lall_crown))
# sys.exit()

# I25_BA21_avg_Lall_sulcus_inf = import_clean_data_avg("I25", "BA21", "sulcus")
#print("I25_BA21_avg_Lall_sulcus_inf = ", I25_BA21_avg_Lall_sulcus_inf)
#sulcus_test.write("I25_BA21_avg_Lall_sulcus_inf = {}\n".format(I25_BA21_avg_Lall_sulcus_inf))
# sys.exit()


#I27
I27_BA20A_avg_Lall_crown = import_clean_data_avg("I27", "BA20A", "crown")
I27_BA20B_avg_Lall_crown = import_clean_data_avg("I27", "BA20B", "crown")
I27_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I27", "BA20A", "BA20B")
I27_BA21_avg_Lall_crown = import_clean_data_avg("I27", "BA21", "crown")
#print("I27_BA20A_avg_Lall_crown = ", I27_BA20A_avg_Lall_crown)

#I30
I30_BA21_avg_Lall_crown = import_clean_data_avg("I30", "BA21", "crown")
I30_BA22_avg_Lall_crown = import_clean_data_avg("I30", "BA22", "crown")

#I31
I31_BA21_avg_Lall_crown = import_clean_data_avg("I31", "BA21", "crown")

#I32
I32_BA20A_avg_Lall_crown = import_clean_data_avg("I32", "BA20A", "crown")
I32_BA20B_avg_Lall_crown = import_clean_data_avg("I32", "BA20B", "crown")
I32_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I32", "BA20A", "BA20B")
I32_BA21_avg_Lall_crown = import_clean_data_avg("I32", "BA21", "crown")
I32_BA22_avg_Lall_crown = import_clean_data_avg("I32", "BA22", "crown")
I32_BA36_avg_Lall_crown = import_clean_data_avg("I32", "BA36", "crown")
#print("I32_BA20A_avg_Lall_crown = ", I32_BA20A_avg_Lall_crown)

#I33
I33_BA20A_avg_Lall_crown = import_clean_data_avg("I33", "BA20A", "crown")
I33_BA20B_avg_Lall_crown = import_clean_data_avg("I33", "BA20B", "crown")
I33_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I33", "BA20A", "BA20B")
I33_BA21_avg_Lall_crown = import_clean_data_avg("I33", "BA21", "crown")
I33_BA22_avg_Lall_crown = import_clean_data_avg("I33", "BA22", "crown")
#print("I33_BA20A_avg_Lall_crown = ", I33_BA20A_avg_Lall_crown)
#print("I33_BA20B_avg_Lall_crown = ", I33_BA20B_avg_Lall_crown)

#I34
I34_BA20A_avg_Lall_crown = import_clean_data_avg("I34", "BA20A", "crown")
I34_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I34", "BA20A", None)
I34_BA22_avg_Lall_crown = import_clean_data_avg("I34", "BA22", "crown")
I34_BA36_avg_Lall_crown = import_clean_data_avg("I34", "BA36", "crown")
#print("I34_BA20A_avg_Lall_crown = ", I34_BA20A_avg_Lall_crown)

#I40
I40_BA20A_avg_Lall_crown = import_clean_data_avg("I40", "BA20A", "crown")
I40_BA20B_avg_Lall_crown = import_clean_data_avg("I40", "BA20B", "crown")
I40_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I40", "BA20A", "BA20B")
I40_BA21_avg_Lall_crown = import_clean_data_avg("I40", "BA21", "crown")
I40_BA22_avg_Lall_crown = import_clean_data_avg("I40", "BA22", "crown")
#print("I40_BA20A_avg_Lall_crown = ", I40_BA20A_avg_Lall_crown)

#I42
I42_BA20A_avg_Lall_crown = import_clean_data_avg("I42", "BA20A", "crown")
I42_BA20B_avg_Lall_crown = import_clean_data_avg("I42", "BA20B", "crown")
I42_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I42", "BA20A", "BA20B")
I42_BA21_avg_Lall_crown = import_clean_data_avg("I42", "BA21", "crown")
I42_BA22_avg_Lall_crown = import_clean_data_avg("I42", "BA22", "crown")
I42_BA36_avg_Lall_crown = import_clean_data_avg("I42", "BA36", "crown")
#print("I42_BA20A_avg_Lall_crown = ", I42_BA20A_avg_Lall_crown)

#I44
I44_BA20A_avg_Lall_crown = import_clean_data_avg("I44", "BA20A", "crown")
I44_BA20B_avg_Lall_crown = import_clean_data_avg("I44", "BA20B", "crown")
I44_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I44", "BA20A", "BA20B")
I44_BA21_avg_Lall_crown = import_clean_data_avg("I44", "BA21", "crown")
I44_BA36_avg_Lall_crown = import_clean_data_avg("I44", "BA36", "crown")
#print("I44_BA20A_avg_Lall_crown = ", I44_BA20A_avg_Lall_crown)

#I47
I47_BA20A_avg_Lall_crown = import_clean_data_avg("I47", "BA20A", "crown")
I47_BA20B_avg_Lall_crown = import_clean_data_avg("I47", "BA20B", "crown")
I47_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I47", "BA20A", "BA20B")
I47_BA21_avg_Lall_crown = import_clean_data_avg("I47", "BA21", "crown")
#print("I47_BA20A_avg_Lall_crown = ", I47_BA20A_avg_Lall_crown)

#I49
I49_BA20A_avg_Lall_crown = import_clean_data_avg("I49", "BA20A", "crown")
I49_BA20_all_avg_Lall_crown = BA20_all_clean_data_avg("I49", "BA20A", None)
I49_BA21_avg_Lall_crown = import_clean_data_avg("I49", "BA21", "crown")
I49_BA22_avg_Lall_crown = import_clean_data_avg("I49", "BA22", "crown")
I49_BA36_avg_Lall_crown = import_clean_data_avg("I49", "BA36", "crown")
#print("I49_BA20A_avg_Lall_crown = ", I49_BA20A_avg_Lall_crown)


#I25
I25_BA20A_rel_Lall_crown = make_relative(I25_BA20A_avg_Lall_crown)
I25_BA20B_rel_Lall_crown = make_relative(I25_BA20B_avg_Lall_crown)
I25_BA20_all_rel_Lall_crown = make_relative(I25_BA20_all_avg_Lall_crown)
I25_BA21_rel_Lall_crown = make_relative(I25_BA21_avg_Lall_crown)
I25_BA22_rel_Lall_crown = make_relative(I25_BA22_avg_Lall_crown)
I25_BA36_rel_Lall_crown = make_relative(I25_BA36_avg_Lall_crown)
# print("I25_BA20A_rel_Lall_crown = ", I25_BA20A_rel_Lall_crown)
# sys.exit()
#sulcus_test.write("I25_BA21_rel_Lall_crown = {}\n".format(I25_BA21_rel_Lall_crown))


# I25_BA21_rel_Lall_sulcus_inf = make_relative(I25_BA21_avg_Lall_sulcus_inf)
#sulcus_test.write("I25_BA21_rel_Lall_sulcus_inf = {}\n".format(I25_BA21_rel_Lall_sulcus_inf))


#I27
I27_BA20A_rel_Lall_crown = make_relative(I27_BA20A_avg_Lall_crown)
I27_BA20B_rel_Lall_crown = make_relative(I27_BA20B_avg_Lall_crown)
I27_BA20_all_rel_Lall_crown = make_relative(I27_BA20_all_avg_Lall_crown)
I27_BA21_rel_Lall_crown = make_relative(I27_BA21_avg_Lall_crown)
#print("I27_BA20A_rel_Lall_crown = ", I27_BA20A_rel_Lall_crown)

#I30
I30_BA21_rel_Lall_crown = make_relative(I30_BA21_avg_Lall_crown)
I30_BA22_rel_Lall_crown = make_relative(I30_BA22_avg_Lall_crown)

#I31
I31_BA21_rel_Lall_crown = make_relative(I31_BA21_avg_Lall_crown)

#I32
I32_BA20A_rel_Lall_crown = make_relative(I32_BA20A_avg_Lall_crown)
I32_BA20B_rel_Lall_crown = make_relative(I32_BA20B_avg_Lall_crown)
I32_BA20_all_rel_Lall_crown = make_relative(I32_BA20_all_avg_Lall_crown)
I32_BA21_rel_Lall_crown = make_relative(I32_BA21_avg_Lall_crown)
I32_BA22_rel_Lall_crown = make_relative(I32_BA22_avg_Lall_crown)
I32_BA36_rel_Lall_crown = make_relative(I32_BA36_avg_Lall_crown)
#print("I32_BA20A_rel_Lall_crown = ", I32_BA20A_rel_Lall_crown)

#I33
I33_BA20A_rel_Lall_crown = make_relative(I33_BA20A_avg_Lall_crown)
I33_BA20B_rel_Lall_crown = make_relative(I33_BA20B_avg_Lall_crown)
I33_BA20_all_rel_Lall_crown = make_relative(I33_BA20_all_avg_Lall_crown)
I33_BA21_rel_Lall_crown = make_relative(I33_BA21_avg_Lall_crown)
I33_BA22_rel_Lall_crown = make_relative(I33_BA22_avg_Lall_crown)
#print("I33_BA20A_rel_Lall_crown = ", I33_BA20A_rel_Lall_crown)
#print("I33_BA20B_rel_Lall_crown = ", I33_BA20B_rel_Lall_crown)

#I34
I34_BA20A_rel_Lall_crown = make_relative(I34_BA20A_avg_Lall_crown)
I34_BA20_all_rel_Lall_crown = make_relative(I34_BA20_all_avg_Lall_crown)
I34_BA22_rel_Lall_crown = make_relative(I34_BA22_avg_Lall_crown)
I34_BA36_rel_Lall_crown = make_relative(I34_BA36_avg_Lall_crown)
#print("I34_BA20A_rel_Lall_crown = ", I34_BA20A_rel_Lall_crown)

#I40
I40_BA20A_rel_Lall_crown = make_relative(I40_BA20A_avg_Lall_crown)
I40_BA20B_rel_Lall_crown = make_relative(I40_BA20B_avg_Lall_crown)
I40_BA20_all_rel_Lall_crown = make_relative(I40_BA20_all_avg_Lall_crown)
I40_BA21_rel_Lall_crown = make_relative(I40_BA21_avg_Lall_crown)
I40_BA22_rel_Lall_crown = make_relative(I40_BA22_avg_Lall_crown)
#print("I40_BA20A_rel_Lall_crown = ", I40_BA20A_rel_Lall_crown)

#I42
I42_BA20A_rel_Lall_crown = make_relative(I42_BA20A_avg_Lall_crown)
I42_BA20B_rel_Lall_crown = make_relative(I42_BA20B_avg_Lall_crown)
I42_BA20_all_rel_Lall_crown = make_relative(I42_BA20_all_avg_Lall_crown)
I42_BA21_rel_Lall_crown = make_relative(I42_BA21_avg_Lall_crown)
I42_BA22_rel_Lall_crown = make_relative(I42_BA22_avg_Lall_crown)
I42_BA36_rel_Lall_crown = make_relative(I42_BA36_avg_Lall_crown)
#print("I42_BA20A_rel_Lall_crown = ", I42_BA20A_rel_Lall_crown)

#I44
I44_BA20A_rel_Lall_crown = make_relative(I44_BA20A_avg_Lall_crown)
I44_BA20B_rel_Lall_crown = make_relative(I44_BA20B_avg_Lall_crown)
I44_BA20_all_rel_Lall_crown = make_relative(I44_BA20_all_avg_Lall_crown)
I44_BA21_rel_Lall_crown = make_relative(I44_BA21_avg_Lall_crown)
I44_BA36_rel_Lall_crown = make_relative(I44_BA36_avg_Lall_crown)
#print("I44_BA20A_rel_Lall_crown = ", I44_BA20A_rel_Lall_crown)

#I47
I47_BA20A_rel_Lall_crown = make_relative(I47_BA20A_avg_Lall_crown)
I47_BA20B_rel_Lall_crown = make_relative(I47_BA20B_avg_Lall_crown)
I47_BA20_all_rel_Lall_crown = make_relative(I47_BA20_all_avg_Lall_crown)
I47_BA21_rel_Lall_crown = make_relative(I47_BA21_avg_Lall_crown)
#print("I47_BA20A_rel_Lall_crown = ", I47_BA20A_rel_Lall_crown)

#I49
I49_BA20A_rel_Lall_crown = make_relative(I49_BA20A_avg_Lall_crown)
I49_BA20_all_rel_Lall_crown = make_relative(I49_BA20_all_avg_Lall_crown)
I49_BA21_rel_Lall_crown = make_relative(I49_BA21_avg_Lall_crown)
I49_BA22_rel_Lall_crown = make_relative(I49_BA22_avg_Lall_crown)
I49_BA36_rel_Lall_crown = make_relative(I49_BA36_avg_Lall_crown)
#print("I49_BA20A_rel_Lall_crown = ", I49_BA20A_rel_Lall_crown)


#this section adds the relative and absolute values to a spreadsheet, values are associated with case and BA, crown and fundus are on separate sheets

df_list_crown_absolute = [I25_BA20A_avg_Lall_crown, I25_BA20B_avg_Lall_crown, I25_BA20_all_avg_Lall_crown, I25_BA21_avg_Lall_crown, I25_BA22_avg_Lall_crown, I25_BA36_avg_Lall_crown, I27_BA20A_avg_Lall_crown, I27_BA20B_avg_Lall_crown, I27_BA20_all_avg_Lall_crown, I27_BA21_avg_Lall_crown, I30_BA21_avg_Lall_crown, I30_BA22_avg_Lall_crown, I31_BA21_avg_Lall_crown, I32_BA20A_avg_Lall_crown, I32_BA20B_avg_Lall_crown, I32_BA20_all_avg_Lall_crown, I32_BA21_avg_Lall_crown, I32_BA22_avg_Lall_crown, I32_BA36_avg_Lall_crown, I33_BA20A_avg_Lall_crown, I33_BA20B_avg_Lall_crown, I33_BA20_all_avg_Lall_crown, I33_BA21_avg_Lall_crown, I33_BA22_avg_Lall_crown, I34_BA20A_avg_Lall_crown, I34_BA20_all_avg_Lall_crown, I34_BA22_avg_Lall_crown, I34_BA36_avg_Lall_crown, I40_BA20A_avg_Lall_crown, I40_BA20B_avg_Lall_crown, I40_BA20_all_avg_Lall_crown, I40_BA21_avg_Lall_crown, I40_BA22_avg_Lall_crown, I42_BA20A_avg_Lall_crown, I42_BA20B_avg_Lall_crown, I42_BA20_all_avg_Lall_crown, I42_BA21_avg_Lall_crown, I42_BA22_avg_Lall_crown, I42_BA36_avg_Lall_crown, I44_BA20A_avg_Lall_crown, I44_BA20B_avg_Lall_crown, I44_BA20_all_avg_Lall_crown, I44_BA21_avg_Lall_crown, I44_BA36_avg_Lall_crown, I47_BA20A_avg_Lall_crown, I47_BA20B_avg_Lall_crown, I47_BA20_all_avg_Lall_crown, I47_BA21_avg_Lall_crown, I49_BA20A_avg_Lall_crown, I49_BA20_all_avg_Lall_crown, I49_BA21_avg_Lall_crown, I49_BA22_avg_Lall_crown, I49_BA36_avg_Lall_crown]
#print("df_list_crown_absolute = ", df_list_crown_absolute)

BA_all_avg_absolute_crown = np.mean(df_list_crown_absolute, axis=0)
#print("BA_all_avg_absolute_crown", BA_all_avg_absolute_crown)

BA_all_avg_relative_crown = make_relative(BA_all_avg_absolute_crown)
#print("BA_all_avg_relative_crown = ", BA_all_avg_relative_crown)

df_list_crown = [I25_BA20A_rel_Lall_crown, I25_BA20B_rel_Lall_crown, I25_BA20_all_rel_Lall_crown, I25_BA21_rel_Lall_crown, I25_BA22_rel_Lall_crown, I25_BA36_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I30_BA22_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I32_BA21_rel_Lall_crown, I32_BA22_rel_Lall_crown, I32_BA36_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I33_BA21_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I34_BA22_rel_Lall_crown, I34_BA36_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I40_BA21_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I42_BA21_rel_Lall_crown, I42_BA22_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I44_BA21_rel_Lall_crown, I44_BA36_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I47_BA20B_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA20A_rel_Lall_crown, I49_BA20_all_rel_Lall_crown, I49_BA21_rel_Lall_crown, I49_BA22_rel_Lall_crown, I49_BA36_rel_Lall_crown]

case_info_crown = ["I25_BA20A", "I25_BA20B", "I25_BA20_all", "I25_BA21", "I25_BA22", "I25_BA36", "I27_BA20A", "I27_BA20B", "I27_BA20_all", "I27_BA21", "I30_BA21", "I30_BA22", "I31_BA21", "I32_BA20A", "I32_BA20B", "I32_BA20_all", "I32_BA21", "I32_BA22", "I32_BA36", "I33_BA20A", "I33_BA20B", "I33_BA20_all", "I33_BA21", "I33_BA22", "I34_BA20A", "I34_BA20_all", "I34_BA22", "I34_BA36", "I40_BA20A", "I40_BA20B", "I40_BA20_all", "I40_BA21", "I40_BA22", "I42_BA20A", "I42_BA20B", "I42_BA20_all", "I42_BA21", "I42_BA22", "I42_BA36", "I44_BA20A", "I44_BA20B", "I44_BA20_all", "I44_BA21", "I44_BA36", "I47_BA20A", "I47_BA20B", "I47_BA20_all", "I47_BA21", "I49_BA20A", "I49_BA20_all", "I49_BA21", "I49_BA22", "I49_BA36"]


df_crown = pd.DataFrame(np.array([variable for variable in df_list_crown]), columns=['layer1', 'layer2', 'layer3', 'layer4', 'layer5', 'layer6'])

df_crown_absolute = pd.DataFrame(np.array([variable for variable in df_list_crown_absolute]), columns=['layer1', 'layer2', 'layer3', 'layer4', 'layer5', 'layer6'])


writer = pd.ExcelWriter('lam_thick_data_sheet.xls')

df_case_info_crown = df_crown.insert(0, "Case_info_relative", [case for case in case_info_crown])

df_case_info_crown_absolute = df_crown_absolute.insert(0, "Case_info_absolute", [case for case in case_info_crown])


df_crown.to_excel(writer, index=False, sheet_name='crown_rel_allcase')

df_crown_absolute.to_excel(writer, index=False, sheet_name='crown_abs_allcase')


#print(df_crown)


#BA20A individual layers
BA20A_L1_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L1")
BA20A_L2_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L2")
BA20A_L3_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L3")
BA20A_L4_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L4")
BA20A_L5_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L5")
BA20A_L6_crown = get_ind_layer([I25_BA20A_rel_Lall_crown, I27_BA20A_rel_Lall_crown, I32_BA20A_rel_Lall_crown, I33_BA20A_rel_Lall_crown, I34_BA20A_rel_Lall_crown, I40_BA20A_rel_Lall_crown, I42_BA20A_rel_Lall_crown, I44_BA20A_rel_Lall_crown, I47_BA20A_rel_Lall_crown, I49_BA20A_rel_Lall_crown], "L6")
#print("BA20A_LI = ", BA20A_L1_crown)

BA20A_L1_crown_female = [BA20A_L1_crown[1], BA20A_L1_crown[2], BA20A_L1_crown[3]]
BA20A_L2_crown_female = [BA20A_L2_crown[1], BA20A_L2_crown[2], BA20A_L2_crown[3]]
BA20A_L3_crown_female = [BA20A_L3_crown[1], BA20A_L3_crown[2], BA20A_L3_crown[3]]
BA20A_L4_crown_female = [BA20A_L4_crown[1], BA20A_L4_crown[2], BA20A_L4_crown[3]]
BA20A_L5_crown_female = [BA20A_L5_crown[1], BA20A_L5_crown[2], BA20A_L5_crown[3]]
BA20A_L6_crown_female = [BA20A_L6_crown[1], BA20A_L6_crown[2], BA20A_L6_crown[3]]

BA20A_L1_crown_male = [BA20A_L1_crown[0], BA20A_L1_crown[4], BA20A_L1_crown[5], BA20A_L1_crown[6], BA20A_L1_crown[7], BA20A_L1_crown[8], BA20A_L1_crown[9]]
BA20A_L2_crown_male = [BA20A_L2_crown[0], BA20A_L2_crown[4], BA20A_L2_crown[5], BA20A_L2_crown[6], BA20A_L2_crown[7], BA20A_L2_crown[8], BA20A_L2_crown[9]]
BA20A_L3_crown_male = [BA20A_L3_crown[0], BA20A_L3_crown[4], BA20A_L3_crown[5], BA20A_L3_crown[6], BA20A_L3_crown[7], BA20A_L3_crown[8], BA20A_L3_crown[9]]
BA20A_L4_crown_male = [BA20A_L4_crown[0], BA20A_L4_crown[4], BA20A_L4_crown[5], BA20A_L4_crown[6], BA20A_L4_crown[7], BA20A_L4_crown[8], BA20A_L4_crown[9]]
BA20A_L5_crown_male = [BA20A_L5_crown[0], BA20A_L5_crown[4], BA20A_L5_crown[5], BA20A_L5_crown[6], BA20A_L5_crown[7], BA20A_L5_crown[8], BA20A_L5_crown[9]]
BA20A_L6_crown_male = [BA20A_L6_crown[0], BA20A_L6_crown[4], BA20A_L6_crown[5], BA20A_L6_crown[6], BA20A_L6_crown[7], BA20A_L6_crown[8], BA20A_L6_crown[9]]


#BA20B
BA20B_L1_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L1")
BA20B_L2_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L2")
BA20B_L3_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L3")
BA20B_L4_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L4")
BA20B_L5_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L5")
BA20B_L6_crown = get_ind_layer([I25_BA20B_rel_Lall_crown, I27_BA20B_rel_Lall_crown, I32_BA20B_rel_Lall_crown, I33_BA20B_rel_Lall_crown, I40_BA20B_rel_Lall_crown, I42_BA20B_rel_Lall_crown, I44_BA20B_rel_Lall_crown, I47_BA20B_rel_Lall_crown], "L6")
#print("BA20B_LI = ", BA20B_L1_crown)

BA20B_L1_crown_female = [BA20B_L1_crown[1], BA20B_L1_crown[2], BA20B_L1_crown[3]]
BA20B_L2_crown_female = [BA20B_L2_crown[1], BA20B_L2_crown[2], BA20B_L2_crown[3]]
BA20B_L3_crown_female = [BA20B_L3_crown[1], BA20B_L3_crown[2], BA20B_L3_crown[3]]
BA20B_L4_crown_female = [BA20B_L4_crown[1], BA20B_L4_crown[2], BA20B_L4_crown[3]]
BA20B_L5_crown_female = [BA20B_L5_crown[1], BA20B_L5_crown[2], BA20B_L5_crown[3]]
BA20B_L6_crown_female = [BA20B_L6_crown[1], BA20B_L6_crown[2], BA20B_L6_crown[3]]

BA20B_L1_crown_male = [BA20B_L1_crown[0], BA20B_L1_crown[4], BA20B_L1_crown[5], BA20B_L1_crown[6], BA20B_L1_crown[7]]
BA20B_L2_crown_male = [BA20B_L2_crown[0], BA20B_L2_crown[4], BA20B_L2_crown[5], BA20B_L2_crown[6], BA20B_L2_crown[7]]
BA20B_L3_crown_male = [BA20B_L3_crown[0], BA20B_L3_crown[4], BA20B_L3_crown[5], BA20B_L3_crown[6], BA20B_L3_crown[7]]
BA20B_L4_crown_male = [BA20B_L4_crown[0], BA20B_L4_crown[4], BA20B_L4_crown[5], BA20B_L4_crown[6], BA20B_L4_crown[7]]
BA20B_L5_crown_male = [BA20B_L5_crown[0], BA20B_L5_crown[4], BA20B_L5_crown[5], BA20B_L5_crown[6], BA20B_L5_crown[7]]
BA20B_L6_crown_male = [BA20B_L6_crown[0], BA20B_L6_crown[4], BA20B_L6_crown[5], BA20B_L6_crown[6], BA20B_L6_crown[7]]


#BA20_all
BA20_all_L1_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L1")
BA20_all_L2_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L2")
BA20_all_L3_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L3")
BA20_all_L4_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L4")
BA20_all_L5_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L5")

BA20_all_L6_crown = get_ind_layer([I25_BA20_all_rel_Lall_crown, I27_BA20_all_rel_Lall_crown, I32_BA20_all_rel_Lall_crown, I33_BA20_all_rel_Lall_crown, I34_BA20_all_rel_Lall_crown, I40_BA20_all_rel_Lall_crown, I42_BA20_all_rel_Lall_crown, I44_BA20_all_rel_Lall_crown, I47_BA20_all_rel_Lall_crown, I49_BA20_all_rel_Lall_crown], "L6")
#print("BA20_all_clean_data_avg_LI = ", BA20_all_clean_data_avg_L1_crown)

BA20_all_L1_crown_female = [BA20_all_L1_crown[1], BA20_all_L1_crown[2], BA20_all_L1_crown[3]]
BA20_all_L2_crown_female = [BA20_all_L2_crown[1], BA20_all_L2_crown[2], BA20_all_L2_crown[3]]
BA20_all_L3_crown_female = [BA20_all_L3_crown[1], BA20_all_L3_crown[2], BA20_all_L3_crown[3]]
BA20_all_L4_crown_female = [BA20_all_L4_crown[1], BA20_all_L4_crown[2], BA20_all_L4_crown[3]]
BA20_all_L5_crown_female = [BA20_all_L5_crown[1], BA20_all_L5_crown[2], BA20_all_L5_crown[3]]
BA20_all_L6_crown_female = [BA20_all_L6_crown[1], BA20_all_L6_crown[2], BA20_all_L6_crown[3]]

BA20_all_L1_crown_male = [BA20_all_L1_crown[0], BA20_all_L1_crown[4], BA20_all_L1_crown[5], BA20_all_L1_crown[6], BA20_all_L1_crown[7], BA20_all_L1_crown[8], BA20_all_L1_crown[9]]
BA20_all_L2_crown_male = [BA20_all_L2_crown[0], BA20_all_L2_crown[4], BA20_all_L2_crown[5], BA20_all_L2_crown[6], BA20_all_L2_crown[7], BA20_all_L2_crown[8], BA20_all_L2_crown[9]]
BA20_all_L3_crown_male = [BA20_all_L3_crown[0], BA20_all_L3_crown[4], BA20_all_L3_crown[5], BA20_all_L3_crown[6], BA20_all_L3_crown[7], BA20_all_L3_crown[8], BA20_all_L3_crown[9]]
BA20_all_L4_crown_male = [BA20_all_L4_crown[0], BA20_all_L4_crown[4], BA20_all_L4_crown[5], BA20_all_L4_crown[6], BA20_all_L4_crown[7], BA20_all_L4_crown[8], BA20_all_L4_crown[9]]
BA20_all_L5_crown_male = [BA20_all_L5_crown[0], BA20_all_L5_crown[4], BA20_all_L5_crown[5], BA20_all_L5_crown[6], BA20_all_L5_crown[7], BA20_all_L5_crown[8], BA20_all_L5_crown[9]]
BA20_all_L6_crown_male = [BA20_all_L6_crown[0], BA20_all_L6_crown[4], BA20_all_L6_crown[5], BA20_all_L6_crown[6], BA20_all_L6_crown[7], BA20_all_L6_crown[8], BA20_all_L6_crown[9]]


#BA21
BA21_L1_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L1")
BA21_L2_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L2")
BA21_L3_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L3")
BA21_L4_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L4")
BA21_L5_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L5")
BA21_L6_crown = get_ind_layer([I25_BA21_rel_Lall_crown, I27_BA21_rel_Lall_crown, I30_BA21_rel_Lall_crown, I31_BA21_rel_Lall_crown, I32_BA21_rel_Lall_crown, I33_BA21_rel_Lall_crown, I40_BA21_rel_Lall_crown, I42_BA21_rel_Lall_crown, I44_BA21_rel_Lall_crown, I47_BA21_rel_Lall_crown, I49_BA21_rel_Lall_crown], "L6")

BA21_L1_crown_female = [BA21_L1_crown[1], BA21_L1_crown[2], BA21_L1_crown[4], BA21_L1_crown[5]]
BA21_L2_crown_female = [BA21_L2_crown[1], BA21_L2_crown[2], BA21_L2_crown[4], BA21_L2_crown[5]]
BA21_L3_crown_female = [BA21_L3_crown[1], BA21_L3_crown[2], BA21_L3_crown[4], BA21_L3_crown[5]]
BA21_L4_crown_female = [BA21_L4_crown[1], BA21_L4_crown[2], BA21_L4_crown[4], BA21_L4_crown[5]]
BA21_L5_crown_female = [BA21_L5_crown[1], BA21_L5_crown[2], BA21_L5_crown[4], BA21_L5_crown[5]]
BA21_L6_crown_female = [BA21_L6_crown[1], BA21_L6_crown[2], BA21_L6_crown[4], BA21_L6_crown[5]]

BA21_L1_crown_male = [BA21_L1_crown[0], BA21_L1_crown[3], BA21_L1_crown[6], BA21_L1_crown[7], BA21_L1_crown[8], BA21_L1_crown[9], BA21_L1_crown[10]]
BA21_L2_crown_male = [BA21_L2_crown[0], BA21_L2_crown[3], BA21_L2_crown[6], BA21_L2_crown[7], BA21_L2_crown[8], BA21_L2_crown[9], BA21_L2_crown[10]]
BA21_L3_crown_male = [BA21_L3_crown[0], BA21_L3_crown[3], BA21_L3_crown[6], BA21_L3_crown[7], BA21_L3_crown[8], BA21_L3_crown[9], BA21_L3_crown[10]]
BA21_L4_crown_male = [BA21_L4_crown[0], BA21_L4_crown[3], BA21_L4_crown[6], BA21_L4_crown[7], BA21_L4_crown[8], BA21_L4_crown[9], BA21_L4_crown[10]]
BA21_L5_crown_male = [BA21_L5_crown[0], BA21_L5_crown[3], BA21_L5_crown[6], BA21_L5_crown[7], BA21_L5_crown[8], BA21_L5_crown[9], BA21_L5_crown[10]]
BA21_L6_crown_male = [BA21_L6_crown[0], BA21_L6_crown[3], BA21_L6_crown[6], BA21_L6_crown[7], BA21_L6_crown[8], BA21_L6_crown[9], BA21_L6_crown[10]]


#BA22
BA22_L1_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L1")
BA22_L2_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L2")
BA22_L3_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L3")
BA22_L4_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L4")
BA22_L5_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L5")
BA22_L6_crown = get_ind_layer([I25_BA22_rel_Lall_crown, I30_BA22_rel_Lall_crown, I32_BA22_rel_Lall_crown, I33_BA22_rel_Lall_crown, I34_BA22_rel_Lall_crown, I40_BA22_rel_Lall_crown, I42_BA22_rel_Lall_crown, I49_BA22_rel_Lall_crown], "L6")

BA22_L1_crown_female = [BA22_L1_crown[1], BA22_L1_crown[2], BA22_L1_crown[3]]
BA22_L2_crown_female = [BA22_L2_crown[1], BA22_L2_crown[2], BA22_L2_crown[3]]
BA22_L3_crown_female = [BA22_L3_crown[1], BA22_L3_crown[2], BA22_L3_crown[3]]
BA22_L4_crown_female = [BA22_L4_crown[1], BA22_L4_crown[2], BA22_L4_crown[3]]
BA22_L5_crown_female = [BA22_L5_crown[1], BA22_L5_crown[2], BA22_L5_crown[3]]
BA22_L6_crown_female = [BA22_L6_crown[1], BA22_L6_crown[2], BA22_L6_crown[3]]

BA22_L1_crown_male = [BA22_L1_crown[0], BA22_L1_crown[4], BA22_L1_crown[5], BA22_L1_crown[6], BA22_L1_crown[7]]
BA22_L2_crown_male = [BA22_L2_crown[0], BA22_L2_crown[4], BA22_L2_crown[5], BA22_L2_crown[6], BA22_L2_crown[7]]
BA22_L3_crown_male = [BA22_L3_crown[0], BA22_L3_crown[4], BA22_L3_crown[5], BA22_L3_crown[6], BA22_L3_crown[7]]
BA22_L4_crown_male = [BA22_L4_crown[0], BA22_L4_crown[4], BA22_L4_crown[5], BA22_L4_crown[6], BA22_L4_crown[7]]
BA22_L5_crown_male = [BA22_L5_crown[0], BA22_L5_crown[4], BA22_L5_crown[5], BA22_L5_crown[6], BA22_L5_crown[7]]
BA22_L6_crown_male = [BA22_L6_crown[0], BA22_L6_crown[4], BA22_L6_crown[5], BA22_L6_crown[6], BA22_L6_crown[7]]


#BA36
BA36_L1_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L1")
BA36_L2_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L2")
BA36_L3_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L3")
BA36_L4_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L4")
BA36_L5_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L5")
BA36_L6_crown = get_ind_layer([I25_BA36_rel_Lall_crown, I32_BA36_rel_Lall_crown, I34_BA36_rel_Lall_crown, I42_BA36_rel_Lall_crown, I44_BA36_rel_Lall_crown, I49_BA36_rel_Lall_crown], "L6")

BA36_L1_crown_female = [BA36_L1_crown[1]]
BA36_L2_crown_female = [BA36_L2_crown[1]]
BA36_L3_crown_female = [BA36_L3_crown[1]]
BA36_L4_crown_female = [BA36_L4_crown[1]]
BA36_L5_crown_female = [BA36_L5_crown[1]]
BA36_L6_crown_female = [BA36_L6_crown[1]]

BA36_L1_crown_male = [BA36_L1_crown[0], BA36_L1_crown[2], BA36_L1_crown[3], BA36_L1_crown[4], BA36_L1_crown[5]]
BA36_L2_crown_male = [BA36_L2_crown[0], BA36_L2_crown[2], BA36_L2_crown[3], BA36_L2_crown[4], BA36_L2_crown[5]]
BA36_L3_crown_male = [BA36_L3_crown[0], BA36_L3_crown[2], BA36_L3_crown[3], BA36_L3_crown[4], BA36_L3_crown[5]]
BA36_L4_crown_male = [BA36_L4_crown[0], BA36_L4_crown[2], BA36_L4_crown[3], BA36_L4_crown[4], BA36_L4_crown[5]]
BA36_L5_crown_male = [BA36_L5_crown[0], BA36_L5_crown[2], BA36_L5_crown[3], BA36_L5_crown[4], BA36_L5_crown[5]]
BA36_L6_crown_male = [BA36_L6_crown[0], BA36_L6_crown[2], BA36_L6_crown[3], BA36_L6_crown[4], BA36_L6_crown[5]]



#COUNT
#all data
BA20A_crown_count = len(BA20A_L1_crown)
BA20B_crown_count = len(BA20B_L1_crown)
BA20_all_crown_count = len(BA20_all_L1_crown)
BA21_crown_count = len(BA21_L1_crown)
BA22_crown_count = len(BA22_L1_crown)
BA36_crown_count = len(BA36_L1_crown)
print("BA20A_crown_count = ", BA20A_crown_count)
print("BA20B_crown_count = ", BA20B_crown_count)
print("BA20_all_crown_count = ", BA20_all_crown_count)
print("BA21_crown_count = ", BA21_crown_count)
print("BA22_crown_count = ", BA22_crown_count)
print("BA36_crown_count = ", BA36_crown_count)
lam_thick_descrip_stats_crown.write("BA20A_crown_count = {}\n".format(BA20A_crown_count))
lam_thick_descrip_stats_crown.write("BA20B_crown_count = {}\n".format(BA20B_crown_count))
lam_thick_descrip_stats_crown.write("BA20_all_crown_count = {}\n".format(BA20_all_crown_count))
lam_thick_descrip_stats_crown.write("BA21_crown_count = {}\n".format(BA21_crown_count))
lam_thick_descrip_stats_crown.write("BA22_crown_count = {}\n".format(BA22_crown_count))
lam_thick_descrip_stats_crown.write("BA36_crown_count = {}\n".format(BA36_crown_count))

#female data
BA20A_crown_count_female = len(BA20A_L1_crown_female)
BA20B_crown_count_female = len(BA20B_L1_crown_female)
BA20_all_crown_count_female = len(BA20_all_L1_crown_female)
BA21_crown_count_female = len(BA21_L1_crown_female)
BA22_crown_count_female = len(BA22_L1_crown_female)
BA36_crown_count_female = len(BA36_L1_crown_female)
print("BA20A_crown_count_female = ", BA20A_crown_count_female)
print("BA20B_crown_count_female = ", BA20B_crown_count_female)
print("BA20_all_crown_count_female = ", BA20_all_crown_count_female)
print("BA21_crown_count_female = ", BA21_crown_count_female)
print("BA22_crown_count_female = ", BA22_crown_count_female)
print("BA36_crown_count_female = ", BA36_crown_count_female)
lam_thick_descrip_stats_crown_sex.write("BA20A_crown_count_female = {}\n".format(BA20A_crown_count_female))
lam_thick_descrip_stats_crown_sex.write("BA20B_crown_count_female = {}\n".format(BA20B_crown_count_female))
lam_thick_descrip_stats_crown_sex.write("BA20_all_crown_count_female = {}\n".format(BA20_all_crown_count_female))
lam_thick_descrip_stats_crown_sex.write("BA21_crown_count_female = {}\n".format(BA21_crown_count_female))
lam_thick_descrip_stats_crown_sex.write("BA22_crown_count_female = {}\n".format(BA22_crown_count_female))
lam_thick_descrip_stats_crown_sex.write("BA36_crown_count_female = {}\n".format(BA36_crown_count_female))


#male data
BA20A_crown_count_male = len(BA20A_L1_crown_male)
BA20B_crown_count_male = len(BA20B_L1_crown_male)
BA20_all_crown_count_male = len(BA20_all_L1_crown_male)
BA21_crown_count_male = len(BA21_L1_crown_male)
BA22_crown_count_male = len(BA22_L1_crown_male)
BA36_crown_count_male = len(BA36_L1_crown_male)
print("BA20A_crown_count_male = ", BA20A_crown_count_male)
print("BA20B_crown_count_male = ", BA20B_crown_count_male)
print("BA20_all_crown_count_male = ", BA20_all_crown_count_male)
print("BA21_crown_count_male = ", BA21_crown_count_male)
print("BA22_crown_count_male = ", BA22_crown_count_male)
print("BA36_crown_count_male = ", BA36_crown_count_male)
lam_thick_descrip_stats_crown_sex.write("BA20A_crown_count_male = {}\n".format(BA20A_crown_count_male))
lam_thick_descrip_stats_crown_sex.write("BA20B_crown_count_male = {}\n".format(BA20B_crown_count_male))
lam_thick_descrip_stats_crown_sex.write("BA20_all_crown_count_male = {}\n".format(BA20_all_crown_count_male))
lam_thick_descrip_stats_crown_sex.write("BA21_crown_count_male = {}\n".format(BA21_crown_count_male))
lam_thick_descrip_stats_crown_sex.write("BA22_crown_count_male = {}\n".format(BA22_crown_count_male))
lam_thick_descrip_stats_crown_sex.write("BA36_crown_count_male = {}\n".format(BA36_crown_count_male))

lam_thick_descrip_stats_crown.write("list = [layer1, layer2, layer3, layer4, layer5, layer6]\n")
lam_thick_descrip_stats_crown_sex.write("list = [layer1, layer2, layer3, layer4, layer5, layer6]\n")


#all data
BA20A_crown = [BA20A_L1_crown, BA20A_L2_crown, BA20A_L3_crown, BA20A_L4_crown, BA20A_L5_crown, BA20A_L6_crown] #list of lists
BA20B_crown = [BA20B_L1_crown, BA20B_L2_crown, BA20B_L3_crown, BA20B_L4_crown, BA20B_L5_crown, BA20B_L6_crown]

BA20_all_crown = [BA20_all_L1_crown, BA20_all_L2_crown, BA20_all_L3_crown, BA20_all_L4_crown, BA20_all_L5_crown, BA20_all_L6_crown]

BA21_crown = [BA21_L1_crown, BA21_L2_crown, BA21_L3_crown, BA21_L4_crown, BA21_L5_crown, BA21_L6_crown]
BA22_crown = [BA22_L1_crown, BA22_L2_crown, BA22_L3_crown, BA22_L4_crown, BA22_L5_crown, BA22_L6_crown]
BA36_crown = [BA36_L1_crown, BA36_L2_crown, BA36_L3_crown, BA36_L4_crown, BA36_L5_crown, BA36_L6_crown]

#female
BA20A_crown_female = [BA20A_L1_crown_female, BA20A_L2_crown_female, BA20A_L3_crown_female, BA20A_L4_crown_female, BA20A_L5_crown_female, BA20A_L6_crown_female] #list of lists

BA20B_crown_female = [BA20B_L1_crown_female, BA20B_L2_crown_female, BA20B_L3_crown_female, BA20B_L4_crown_female, BA20B_L5_crown_female, BA20B_L6_crown_female]

BA20_all_crown_female = [BA20_all_L1_crown_female, BA20_all_L2_crown_female, BA20_all_L3_crown_female, BA20_all_L4_crown_female, BA20_all_L5_crown_female, BA20_all_L6_crown_female]

BA21_crown_female = [BA21_L1_crown_female, BA21_L2_crown_female, BA21_L3_crown_female, BA21_L4_crown_female, BA21_L5_crown_female, BA21_L6_crown_female]

BA22_crown_female = [BA22_L1_crown_female, BA22_L2_crown_female, BA22_L3_crown_female, BA22_L4_crown_female, BA22_L5_crown_female, BA22_L6_crown_female]

BA36_crown_female = [BA36_L1_crown_female, BA36_L2_crown_female, BA36_L3_crown_female, BA36_L4_crown_female, BA36_L5_crown_female, BA36_L6_crown_female]

#male
BA20A_crown_male = [BA20A_L1_crown_male, BA20A_L2_crown_male, BA20A_L3_crown_male, BA20A_L4_crown_male, BA20A_L5_crown_male, BA20A_L6_crown_male] #list of lists

BA20B_crown_male = [BA20B_L1_crown_male, BA20B_L2_crown_male, BA20B_L3_crown_male, BA20B_L4_crown_male, BA20B_L5_crown_male, BA20B_L6_crown_male]

BA20_all_crown_male = [BA20_all_L1_crown_male, BA20_all_L2_crown_male, BA20_all_L3_crown_male, BA20_all_L4_crown_male, BA20_all_L5_crown_male, BA20_all_L6_crown_male]


BA21_crown_male = [BA21_L1_crown_male, BA21_L2_crown_male, BA21_L3_crown_male, BA21_L4_crown_male, BA21_L5_crown_male, BA21_L6_crown_male]

BA22_crown_male = [BA22_L1_crown_male, BA22_L2_crown_male, BA22_L3_crown_male, BA22_L4_crown_male, BA22_L5_crown_male, BA22_L6_crown_male]

BA36_crown_male = [BA36_L1_crown_male, BA36_L2_crown_male, BA36_L3_crown_male, BA36_L4_crown_male, BA36_L5_crown_male, BA36_L6_crown_male]


#MEAN
#all data
BA20A_Lall_crown_mean = [np.mean(list) for list in BA20A_crown]
BA20B_Lall_crown_mean = [np.mean(list) for list in BA20B_crown]
BA20_all_Lall_crown_mean = [np.mean(list) for list in BA20_all_crown]
BA21_Lall_crown_mean = [np.mean(list) for list in BA21_crown]
BA22_Lall_crown_mean = [np.mean(list) for list in BA22_crown]
BA36_Lall_crown_mean = [np.mean(list) for list in BA36_crown]
print("BA20A_Lall_crown_mean = ", BA20A_Lall_crown_mean)
print("BA20B_Lall_crown_mean = ", BA20B_Lall_crown_mean)
print("BA20_all_Lall_crown_mean = ", BA20_all_Lall_crown_mean)
print("BA21_Lall_crown_mean = ", BA21_Lall_crown_mean)
print("BA22_Lall_crown_mean = ", BA22_Lall_crown_mean)
print("BA36_Lall_crown_mean = ", BA36_Lall_crown_mean)
lam_thick_descrip_stats_crown.write("BA20A_Lall_crown_mean = {}\n".format(BA20A_Lall_crown_mean))
lam_thick_descrip_stats_crown.write("BA20B_Lall_crown_mean = {}\n".format(BA20B_Lall_crown_mean))
lam_thick_descrip_stats_crown.write("BA20_all_Lall_crown_mean = {}\n".format(BA20_all_Lall_crown_mean))
lam_thick_descrip_stats_crown.write("BA21_Lall_crown_mean = {}\n".format(BA21_Lall_crown_mean))
lam_thick_descrip_stats_crown.write("BA22_Lall_crown_mean = {}\n".format(BA22_Lall_crown_mean))
lam_thick_descrip_stats_crown.write("BA36_Lall_crown_mean = {}\n".format(BA36_Lall_crown_mean))

#female
BA20A_Lall_crown_mean_female = [np.mean(list) for list in BA20A_crown_female]
BA20B_Lall_crown_mean_female = [np.mean(list) for list in BA20B_crown_female]
BA20_all_Lall_crown_mean_female = [np.mean(list) for list in BA20_all_crown_female]
BA21_Lall_crown_mean_female = [np.mean(list) for list in BA21_crown_female]
BA22_Lall_crown_mean_female = [np.mean(list) for list in BA22_crown_female]
BA36_Lall_crown_mean_female = [np.mean(list) for list in BA36_crown_female]
print("BA20A_Lall_crown_mean_female = ", BA20A_Lall_crown_mean_female)
print("BA20B_Lall_crown_mean_female = ", BA20B_Lall_crown_mean_female)
print("BA20_all_Lall_crown_mean_female = ", BA20_all_Lall_crown_mean_female)
print("BA21_Lall_crown_mean_female = ", BA21_Lall_crown_mean_female)
print("BA22_Lall_crown_mean_female = ", BA22_Lall_crown_mean_female)
print("BA36_Lall_crown_mean_female = ", BA36_Lall_crown_mean_female)
lam_thick_descrip_stats_crown_sex.write("BA20A_Lall_crown_mean_female = {}\n".format(BA20A_Lall_crown_mean_female))
lam_thick_descrip_stats_crown_sex.write("BA20B_Lall_crown_mean_female = {}\n".format(BA20B_Lall_crown_mean_female))
lam_thick_descrip_stats_crown_sex.write("BA20_all_Lall_crown_mean_female = {}\n".format(BA20_all_Lall_crown_mean_female))
lam_thick_descrip_stats_crown_sex.write("BA21_Lall_crown_mean_female = {}\n".format(BA21_Lall_crown_mean_female))
lam_thick_descrip_stats_crown_sex.write("BA22_Lall_crown_mean_female = {}\n".format(BA22_Lall_crown_mean_female))
lam_thick_descrip_stats_crown_sex.write("BA36_Lall_crown_mean_female = {}\n".format(BA36_Lall_crown_mean_female))


#male
BA20A_Lall_crown_mean_male = [np.mean(list) for list in BA20A_crown_male]
BA20B_Lall_crown_mean_male = [np.mean(list) for list in BA20B_crown_male]
BA20_all_Lall_crown_mean_male = [np.mean(list) for list in BA20_all_crown_male]
BA21_Lall_crown_mean_male = [np.mean(list) for list in BA21_crown_male]
BA22_Lall_crown_mean_male = [np.mean(list) for list in BA22_crown_male]
BA36_Lall_crown_mean_male = [np.mean(list) for list in BA36_crown_male]
print("BA20A_Lall_crown_mean_male = ", BA20A_Lall_crown_mean_male)
print("BA20B_Lall_crown_mean_male = ", BA20B_Lall_crown_mean_male)
print("BA20_all_Lall_crown_mean_male = ", BA20_all_Lall_crown_mean_male)
print("BA21_Lall_crown_mean_male = ", BA21_Lall_crown_mean_male)
print("BA22_Lall_crown_mean_male = ", BA22_Lall_crown_mean_male)
print("BA36_Lall_crown_mean_male = ", BA36_Lall_crown_mean_male)
lam_thick_descrip_stats_crown_sex.write("BA20A_Lall_crown_mean_male = {}\n".format(BA20A_Lall_crown_mean_male))
lam_thick_descrip_stats_crown_sex.write("BA20B_Lall_crown_mean_male = {}\n".format(BA20B_Lall_crown_mean_male))
lam_thick_descrip_stats_crown_sex.write("BA20_all_Lall_crown_mean_male = {}\n".format(BA20_all_Lall_crown_mean_male))
lam_thick_descrip_stats_crown_sex.write("BA21_Lall_crown_mean_male = {}\n".format(BA21_Lall_crown_mean_male))
lam_thick_descrip_stats_crown_sex.write("BA22_Lall_crown_mean_male = {}\n".format(BA22_Lall_crown_mean_male))
lam_thick_descrip_stats_crown_sex.write("BA36_Lall_crown_mean_male = {}\n".format(BA36_Lall_crown_mean_male))


#STD
BA20A_Lall_crown_std = [np.std(list) for list in BA20A_crown]
BA20B_Lall_crown_std = [np.std(list) for list in BA20B_crown]
BA20_all_Lall_crown_std = [np.std(list) for list in BA20_all_crown]
BA21_Lall_crown_std = [np.std(list) for list in BA21_crown]
BA22_Lall_crown_std = [np.std(list) for list in BA22_crown]
BA36_Lall_crown_std = [np.std(list) for list in BA36_crown]
print("BA20A_Lall_crown_std = ", BA20A_Lall_crown_std)
print("BA20B_Lall_crown_std = ", BA20B_Lall_crown_std)
print("BA20_all_Lall_crown_std = ", BA20_all_Lall_crown_std)
print("BA21_Lall_crown_std = ", BA21_Lall_crown_std)
print("BA22_Lall_crown_std = ", BA22_Lall_crown_std)
print("BA36_Lall_crown_std = ", BA36_Lall_crown_std)
lam_thick_descrip_stats_crown.write("BA20A_Lall_crown_std = {}\n".format(BA20A_Lall_crown_std))
lam_thick_descrip_stats_crown.write("BA20B_Lall_crown_std = {}\n".format(BA20B_Lall_crown_std))
lam_thick_descrip_stats_crown.write("BA20_all_Lall_crown_std = {}\n".format(BA20_all_Lall_crown_std))
lam_thick_descrip_stats_crown.write("BA21_Lall_crown_std = {}\n".format(BA21_Lall_crown_std))
lam_thick_descrip_stats_crown.write("BA22_Lall_crown_std = {}\n".format(BA22_Lall_crown_std))
lam_thick_descrip_stats_crown.write("BA36_Lall_crown_std = {}\n".format(BA36_Lall_crown_std))


#Paired t-test
#BA20A x BA20B
BA20A_20B_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_crown, BA20B_crown)]
print("BA20A_20B_crown_paired_ttest = ", BA20A_20B_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20A_20B_crown_paired_ttest = {}\n".format(BA20A_20B_crown_paired_ttest))

#BA20A x BA21
BA20A_21_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_crown, BA21_crown)]
print("BA20A_21_crown_paired_ttest = ", BA20A_21_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20A_21_crown_paired_ttest = {}\n".format(BA20A_21_crown_paired_ttest))

#BA20A x BA22
BA20A_22_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_crown, BA22_crown)]
print("BA20A_22_crown_paired_ttest = ", BA20A_22_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20A_22_crown_paired_ttest = {}\n".format(BA20A_22_crown_paired_ttest))

#BA20A x BA36
BA20A_36_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_crown, BA36_crown)]
print("BA20A_36_crown_paired_ttest = ", BA20A_36_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20A_36_crown_paired_ttest = {}\n".format(BA20A_36_crown_paired_ttest))

#BA20B x BA21
BA20B_21_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20B_crown, BA21_crown)]
print("BA20B_21_crown_paired_ttest = ", BA20B_21_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20B_21_crown_paired_ttest = {}\n".format(BA20B_21_crown_paired_ttest))

#BA20B x BA22
BA20B_22_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20B_crown, BA22_crown)]
print("BA20B_22_crown_paired_ttest = ", BA20B_22_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20B_22_crown_paired_ttest = {}\n".format(BA20B_22_crown_paired_ttest))

#BA20B x BA36
BA20B_36_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20B_crown, BA36_crown)]
print("BA20B_36_crown_paired_ttest = ", BA20B_36_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20B_36_crown_paired_ttest = {}\n".format(BA20B_36_crown_paired_ttest))

#BA20_all x BA21
BA20_all_21_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20_all_crown, BA21_crown)]
print("BA20_all_21_crown_paired_ttest = ", BA20_all_21_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20_all_21_crown_paired_ttest = {}\n".format(BA20_all_21_crown_paired_ttest))

#BA20_all x BA22
BA20_all_22_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20_all_crown, BA22_crown)]
print("BA20_all_22_crown_paired_ttest = ", BA20_all_22_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20_all_22_crown_paired_ttest = {}\n".format(BA20_all_22_crown_paired_ttest))

#BA20_all_clean_data_avg x BA36
BA20_all_36_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20_all_crown, BA36_crown)]
print("BA20_all_36_crown_paired_ttest = ", BA20_all_36_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA20_all_36_crown_paired_ttest = {}\n".format(BA20_all_36_crown_paired_ttest))

#BA21 x BA22
BA21_22_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA21_crown, BA22_crown)]
print("BA21_22_crown_paired_ttest = ", BA21_22_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA21_22_crown_paired_ttest = {}\n".format(BA21_22_crown_paired_ttest))

#BA21 x BA36
BA21_36_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA21_crown, BA36_crown)]
print("BA21_36_crown_paired_ttest = ", BA21_36_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA21_36_crown_paired_ttest = {}\n".format(BA21_36_crown_paired_ttest))

#BA22 x BA36
BA22_36_crown_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA22_crown, BA36_crown)]
print("BA22_36_crown_paired_ttest = ", BA22_36_crown_paired_ttest)
lam_thick_descrip_stats_crown.write("BA22_36_crown_paired_ttest = {}\n".format(BA22_36_crown_paired_ttest))



pairedt_list_crown = [BA20A_20B_crown_paired_ttest, BA20A_21_crown_paired_ttest, BA20A_22_crown_paired_ttest, BA20A_36_crown_paired_ttest, BA20B_21_crown_paired_ttest, BA20B_22_crown_paired_ttest, BA20B_36_crown_paired_ttest, BA20_all_21_crown_paired_ttest, BA20_all_22_crown_paired_ttest, BA20_all_36_crown_paired_ttest, BA21_22_crown_paired_ttest, BA21_36_crown_paired_ttest, BA22_36_crown_paired_ttest]

crown_pval_list = []
for list in pairedt_list_crown:
    for i in list:
        crown_pval_list.append(i[1])
#print(len(crown_pval_list))
print("crown_pval_list = ", crown_pval_list)

crown_sig_pvals = []
for i in crown_pval_list:
    if i < 0.05:
        crown_sig_pvals.append(i)

print("crown_sig_pvals = ", crown_sig_pvals)
lam_thick_descrip_stats_crown.write("crown_sig_pvals = {}\n".format(crown_sig_pvals))

crown_sig_pvals_fdr = ssm.fdrcorrection(crown_sig_pvals, alpha=0.05, method='indep', is_sorted=False)
print("crown_sig_pvals_fdr = ", crown_sig_pvals_fdr)
lam_thick_descrip_stats_crown.write("crown_sig_pvals_fdr = {}\n".format(crown_sig_pvals_fdr))


#closes data description file
lam_thick_descrip_stats_crown.close()
lam_thick_descrip_stats_crown_sex.close()


#FUNDUS

lam_thick_descrip_stats_fundus = open("lam_thick_descrip_stats_fundus.csv", "w")   #overwrite any info in file

#Data description
print("Descriptive Statistics - Fundus Thickness")
lam_thick_descrip_stats_fundus.write("Descriptive Statistics - Fundus Thickness\n")

lam_thick_descrip_stats_fundus = open("lam_thick_descrip_stats_fundus.csv", "a")   #append everything else to the file

#IDEAL CASES

#BA20A_20B
I44_BA20A_20B_avg_Lall_fundus = import_clean_data_avg("I44", "BA20A_20B", "fundus")

#BA20B_21
I25_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I25", "BA20B_21", "fundus")
I42_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I42", "BA20B_21", "fundus")
I49_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I49", "BA20B_21", "fundus")

#print("I25_BA20B_21_avg_Lall_fundus = ", I25_BA20B_21_avg_Lall_fundus)
#sulcus_test.write("I25_BA20B_21_avg_Lall_fundus = {}\n".format(I25_BA20B_21_avg_Lall_fundus))


#BA20A_20B
I44_BA20A_20B_rel_Lall_fundus = make_relative(I44_BA20A_20B_avg_Lall_fundus)


#BA20B_21
I25_BA20B_21_rel_Lall_fundus = make_relative(I25_BA20B_21_avg_Lall_fundus)

I42_BA20B_21_rel_Lall_fundus = make_relative(I42_BA20B_21_avg_Lall_fundus)
#print("I42_BA20B_21_rel_Lall_fundus = ", I42_BA20B_21_rel_Lall_fundus)

I49_BA20B_21_rel_Lall_fundus = make_relative(I49_BA20B_21_avg_Lall_fundus)

#sulcus_test.write("I25_BA20B_21_rel_Lall_fundus = {}\n".format(I25_BA20B_21_rel_Lall_fundus))



#NOT IDEAL SULCI
#BA20A_20A
I40_BA20A_20A_avg_Lall_fundus = import_clean_data_avg("I40", "BA20A_20A", "fundus")
#print("I40_BA20A_20A_rel_Lall_fundus = ", I40_BA20A_20A_rel_Lall_fundus)

I40_BA20A_20A_rel_Lall_fundus = make_relative(I40_BA20A_20A_avg_Lall_fundus)

#BA20A_20B
I34_BA20A_20B_avg_Lall_fundus = import_clean_data_avg("I34", "BA20A_20B", "fundus")

I34_BA20A_20B_rel_Lall_fundus = make_relative(I34_BA20A_20B_avg_Lall_fundus)

#BA20B_21
I32_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I32", "BA20B_21", "fundus")
I33_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I33", "BA20B_21", "fundus")
# print("I33_BA20B_21_avg_Lall_fundus = ", I33_BA20B_21_avg_Lall_fundus)
# sys.exit()

I47_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I47", "BA20B_21", "fundus")


I32_BA20B_21_rel_Lall_fundus = make_relative(I32_BA20B_21_avg_Lall_fundus)
I33_BA20B_21_rel_Lall_fundus = make_relative(I33_BA20B_21_avg_Lall_fundus)
I47_BA20B_21_rel_Lall_fundus = make_relative(I47_BA20B_21_avg_Lall_fundus)


#BA21_22
I32_BA21_22_avg_Lall_fundus = import_clean_data_avg("I32", "BA21_22", "fundus")
I33_BA21_22_avg_Lall_fundus = import_clean_data_avg("I33", "BA21_22", "fundus")

I34_BA21_22_avg_Lall_fundus = import_clean_data_avg("I34", "BA21_22", "fundus")

I32_BA21_22_rel_Lall_fundus = make_relative(I32_BA21_22_avg_Lall_fundus)
I33_BA21_22_rel_Lall_fundus = make_relative(I33_BA21_22_avg_Lall_fundus)
I34_BA21_22_rel_Lall_fundus = make_relative(I34_BA21_22_avg_Lall_fundus)

df_list_fundus = [I44_BA20A_20B_rel_Lall_fundus, I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I40_BA20A_20A_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus, I32_BA21_22_rel_Lall_fundus, I33_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus]

df_list_fundus_absolute = [I44_BA20A_20B_avg_Lall_fundus, I25_BA20B_21_avg_Lall_fundus, I42_BA20B_21_avg_Lall_fundus, I49_BA20B_21_avg_Lall_fundus, I40_BA20A_20A_avg_Lall_fundus, I34_BA20A_20B_avg_Lall_fundus, I32_BA20B_21_avg_Lall_fundus, I33_BA20B_21_avg_Lall_fundus, I47_BA20B_21_avg_Lall_fundus, I32_BA21_22_avg_Lall_fundus, I33_BA21_22_avg_Lall_fundus, I34_BA21_22_avg_Lall_fundus]

BA_all_avg_absolute_fundus = np.mean(df_list_fundus_absolute, axis=0)
#print("BA_all_avg_absolute_fundus", BA_all_avg_absolute_fundus)

BA_all_avg_relative_fundus = make_relative(BA_all_avg_absolute_fundus)
#print("BA_all_avg_relative_fundus = ", BA_all_avg_relative_fundus)



case_info_fundus = ["I44_BA20A_20B", "I25_BA20B_21", "I42_BA20B_21", "I49_BA20B_21", "I40_BA20A_20A", "I34_BA20A_20B", "I32_BA20B_21", "I33_BA20B_21", "I47_BA20B_21", "I32_BA21_22", "I33_BA21_22", "I34_BA21_22"]

df_fundus = pd.DataFrame(np.array([variable for variable in df_list_fundus]), columns=['layer1', 'layer2', 'layer3', 'layer4', 'layer5', 'layer6'])

df_fundus_absolute = pd.DataFrame(np.array([variable for variable in df_list_fundus_absolute]), columns=['layer1', 'layer2', 'layer3', 'layer4', 'layer5', 'layer6'])

df_case_info_fundus = df_fundus.insert(0, "Case_info_relative", [case for case in case_info_fundus])

df_case_info_fundus_absolute = df_fundus_absolute.insert(0, "Case_info_absolute", [case for case in case_info_fundus])

df_fundus.to_excel(writer, index=False, sheet_name='fundus_rel_allcase')
df_fundus_absolute.to_excel(writer, index=False, sheet_name='fundus_abs_allcase')

writer.save()


#INDIVIDUAL LAYERS
#BA20A_20A
BA20A_20A_L1_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L1")
BA20A_20A_L2_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L2")
BA20A_20A_L3_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L3")
BA20A_20A_L4_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L4")
BA20A_20A_L5_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L5")
BA20A_20A_L6_fundus = get_ind_layer([I40_BA20A_20A_rel_Lall_fundus], "L6")
# print("BA20A_20A_L1_fundus = ", BA20A_20A_L1_fundus)

#BA20A_20B
BA20A_20B_L1_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L1")
BA20A_20B_L2_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L2")
BA20A_20B_L3_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L3")
BA20A_20B_L4_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L4")
BA20A_20B_L5_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L5")
BA20A_20B_L6_fundus = get_ind_layer([I44_BA20A_20B_rel_Lall_fundus, I34_BA20A_20B_rel_Lall_fundus], "L6")

#BA20B_21
BA20B_21_L1_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L1")
BA20B_21_L2_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L2")
BA20B_21_L3_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L3")
BA20B_21_L4_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L4")
BA20B_21_L5_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L5")
BA20B_21_L6_fundus = get_ind_layer([I25_BA20B_21_rel_Lall_fundus, I42_BA20B_21_rel_Lall_fundus, I49_BA20B_21_rel_Lall_fundus, I32_BA20B_21_rel_Lall_fundus, I33_BA20B_21_rel_Lall_fundus, I47_BA20B_21_rel_Lall_fundus], "L6")

#BA21_22
BA21_22_L1_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus, I33_BA21_22_rel_Lall_fundus], "L1")
BA21_22_L2_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus], "L2")
BA21_22_L3_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus], "L3")
BA21_22_L4_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus], "L4")
BA21_22_L5_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus], "L5")
BA21_22_L6_fundus = get_ind_layer([I32_BA21_22_rel_Lall_fundus, I34_BA21_22_rel_Lall_fundus], "L6")


#COUNT
BA20A_20A_count_fundus = len(BA20A_20A_L1_fundus)
BA20A_20B_count_fundus = len(BA20A_20B_L1_fundus)
BA20B_21_count_fundus = len(BA20B_21_L1_fundus)
BA21_22_count_fundus = len(BA21_22_L1_fundus)
print("BA20A_20A_count_fundus = ", BA20A_20A_count_fundus)
print("BA20A_20B_count_fundus = ", BA20A_20B_count_fundus)
print("BA20B_21_count_fundus = ", BA20B_21_count_fundus)
print("BA21_22_count_fundus = ", BA21_22_count_fundus)
lam_thick_descrip_stats_fundus.write("BA20A_20A_count_fundus = {}\n".format(BA20A_20A_count_fundus))
lam_thick_descrip_stats_fundus.write("BA20A_20B_count_fundus = {}\n".format(BA20A_20B_count_fundus))
lam_thick_descrip_stats_fundus.write("BA20B_21_count_fundus = {}\n".format(BA20B_21_count_fundus))
lam_thick_descrip_stats_fundus.write("BA21_22_count_fundus = {}\n".format(BA21_22_count_fundus))

lam_thick_descrip_stats_fundus.write("list = [layer1, layer2, layer3, layer4, layer5, layer6]\n")

#list_of_lists
BA20A_20A_fundus_notflat = [BA20A_20A_L1_fundus, BA20A_20A_L2_fundus, BA20A_20A_L3_fundus, BA20A_20A_L4_fundus, BA20A_20A_L5_fundus, BA20A_20A_L6_fundus]
BA20A_20A_fundus = []
for list in BA20A_20A_fundus_notflat:
    for i in list:
        BA20A_20A_fundus.append(i)

BA20A_20B_fundus = [BA20A_20B_L1_fundus, BA20A_20B_L2_fundus, BA20A_20B_L3_fundus, BA20A_20B_L4_fundus, BA20A_20B_L5_fundus, BA20A_20B_L6_fundus]
BA20B_21_fundus = [BA20B_21_L1_fundus, BA20B_21_L2_fundus, BA20B_21_L3_fundus, BA20B_21_L4_fundus, BA20B_21_L5_fundus, BA20B_21_L6_fundus]
BA21_22_fundus = [BA21_22_L1_fundus, BA21_22_L2_fundus, BA21_22_L3_fundus, BA21_22_L4_fundus, BA21_22_L5_fundus, BA21_22_L6_fundus]
#print("BA20A_20A_fundus = ", BA20A_20A_fundus)


#MEAN
BA20A_20A_fundus_mean = BA20A_20A_fundus #only one case
BA20A_20B_fundus_mean = [np.mean(list) for list in BA20A_20B_fundus]
BA20B_21_fundus_mean = [np.mean(list) for list in BA20B_21_fundus]
BA21_22_fundus_mean = [np.mean(list) for list in BA21_22_fundus]
print("BA20A_20A_fundus_mean = ", BA20A_20A_fundus_mean)
print("BA20A_20B_fundus_mean = ", BA20A_20B_fundus_mean)
print("BA20B_21_fundus_mean = ", BA20B_21_fundus_mean)
print("BA21_22_fundus_mean = ", BA21_22_fundus_mean)
lam_thick_descrip_stats_fundus.write("BA20A_20A_fundus_mean = {}\n - only one case".format(BA20A_20A_fundus_mean))

lam_thick_descrip_stats_fundus.write("BA20A_20B_fundus_mean = {}\n".format(BA20A_20B_fundus_mean))
lam_thick_descrip_stats_fundus.write("BA20B_21_fundus_mean = {}\n".format(BA20B_21_fundus_mean))
lam_thick_descrip_stats_fundus.write("BA21_22_fundus_mean = {}\n".format(BA21_22_fundus_mean))

#STD
BA20A_20A_fundus_std = None
BA20A_20B_fundus_std = [np.std(list) for list in BA20A_20B_fundus]
BA20B_21_fundus_std = [np.std(list) for list in BA20B_21_fundus]
BA21_22_fundus_std = [np.std(list) for list in BA21_22_fundus]
print("BA20A_20A_fundus_std = None - only one case")
print("BA20A_20B_fundus_std = ", BA20A_20B_fundus_std)
print("BA20B_21_fundus_std = ", BA20B_21_fundus_std)
print("BA21_22_fundus_std = ", BA21_22_fundus_std)
lam_thick_descrip_stats_fundus.write("BA20A_20A_fundus_std = None - only one case \n")
lam_thick_descrip_stats_fundus.write("BA20A_20B_fundus_std = {}\n".format(BA20A_20B_fundus_std))
lam_thick_descrip_stats_fundus.write("BA20B_21_fundus_std = {}\n".format(BA20B_21_fundus_std))
lam_thick_descrip_stats_fundus.write("BA21_22_fundus_std = {}\n".format(BA21_22_fundus_std))


#Paired t-test

#BA20A_BA20B x BA20B_BA21
BA20A_20B_x_BA20B_BA21_fundus_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_20B_fundus, BA20B_21_fundus)]
print("BA20A_20B_x_BA20B_BA21_fundus_paired_ttest = ", BA20A_20B_x_BA20B_BA21_fundus_paired_ttest)
lam_thick_descrip_stats_fundus.write("BA20A_20B_x_BA20B_BA21_fundus_paired_ttest = {}\n".format(BA20A_20B_x_BA20B_BA21_fundus_paired_ttest))

#BA20A_BA20B x BA21_BA22
BA20A_20B_x_BA21_22_fundus_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20A_20B_fundus, BA21_22_fundus)]
print("BA20A_20B_x_BA21_22_fundus_paired_ttest = ", BA20A_20B_x_BA21_22_fundus_paired_ttest)
lam_thick_descrip_stats_fundus.write("BA20A_20B_x_BA21_22_fundus_paired_ttest = {}\n".format(BA20A_20B_x_BA21_22_fundus_paired_ttest))

#BA20B_BA21 x BA21_BA22
BA20B_21_x_BA21_22_fundus_paired_ttest = [stats.ttest_ind(list1, list2, equal_var=False) for list1, list2 in zip(BA20B_21_fundus, BA21_22_fundus)]
print("BA20B_21_x_BA21_22_fundus_paired_ttest = ", BA20B_21_x_BA21_22_fundus_paired_ttest)
lam_thick_descrip_stats_fundus.write("BA20B_21_x_BA21_22_fundus_paired_ttest = {}\n".format(BA20B_21_x_BA21_22_fundus_paired_ttest))

pairedt_list_fundus = [BA20A_20B_x_BA20B_BA21_fundus_paired_ttest, BA20A_20B_x_BA21_22_fundus_paired_ttest, BA20B_21_x_BA21_22_fundus_paired_ttest]

fundus_pval_list = []
for list in pairedt_list_fundus:
    for i in list:
        fundus_pval_list.append(i[1])
#print(len(fundus_pval_list))
print("fundus_pval_list = ", fundus_pval_list)

fundus_sig_pvals = []
for i in fundus_pval_list:
    if i < 0.05:
        fundus_sig_pvals.append(i)

sig_index_fundus_list = []
for i in fundus_sig_pvals:
    sig_index_fundus = fundus_pval_list.index(i)
    sig_index_fundus_list.append(sig_index_fundus)
print("fundus_sig_pvals = ", fundus_sig_pvals)
lam_thick_descrip_stats_fundus.write("fundus_sig_pvals = {}\n".format(fundus_sig_pvals))
print("Index for sig p vals (fundus) in pairedt_list_fundus = ", sig_index_fundus_list)


fundus_sig_pvals_fdr = ssm.fdrcorrection(fundus_sig_pvals, alpha=0.05, method='indep', is_sorted=False)
print("fundus_sig_pvals_fdr = ", fundus_sig_pvals_fdr)
lam_thick_descrip_stats_fundus.write("fundus_sig_pvals_fdr = {}\n".format(fundus_sig_pvals_fdr))


#correction - 3 vars - BA2s0A_BA20B - BA20B_BA21 - BA21_BA22
#BA20A_20B_x_BA21_22_fundus_L4_bon_corr = BA20A_20B_x_BA21_22_fundus_paired_ttest[3][1] * 3
#print("BA20A_20B_x_BA21_22_fundus_L4_bon_corr = ", BA20A_20B_x_BA21_22_fundus_L4_bon_corr)
#lam_thick_descrip_stats_fundus.write("BA20A_20B_x_BA21_22_fundus_L4_bon_corr = {}\n".format(BA20A_20B_x_BA21_22_fundus_L4_bon_corr))

BA20B_21_x_BA21_22_fundus_paired_ttest


lam_thick_descrip_stats_fundus.close()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)



#TABLES - relative data
df_list_relative = [[round(item, 2) for item in BA22_Lall_crown_mean], [round(item, 2) for item in BA21_22_fundus_mean], [round(item, 2) for item in BA21_Lall_crown_mean], [round(item, 2) for item in BA20B_21_fundus_mean], [round(item, 2) for item in BA20_all_Lall_crown_mean], [round(item, 2) for item in BA20A_20B_fundus_mean], [round(item, 2) for item in BA36_Lall_crown_mean]]

df_relative = pd.DataFrame(df_list_relative, columns=['Layer I', 'Layer II', 'Layer III', 'Layer IV', 'Layer V', 'Layer VI'])

info_relative = ["BA22 crown", "BA22_21 fundus", "BA21 crown", "BA21_20 fundus", "BA20 crown", "BA20_20 fundus", "BA36 crown"]

df_info_relative = df_relative.insert(0, "Gyrus Info", [item for item in info_relative])

df_relative.to_excel(writer, index=False, sheet_name='crown_fundus_relative')

df_relative_crown = df_relative[::2]
df_relative_crown.to_excel(writer, index=False, sheet_name='crown_relative')

df_relative_fundus = df_relative[1::2]
df_relative_fundus.to_excel(writer, index=False, sheet_name='fundus_relative')
writer.save()

#print(df_relative[::2])
#print(df_relative[1::2])


#table with average data for the crown and fundus and all the BA

df_list_crown_absolute_BA22 = np.mean([I25_BA22_avg_Lall_crown, I30_BA22_avg_Lall_crown, I32_BA22_avg_Lall_crown, I33_BA22_avg_Lall_crown, I34_BA22_avg_Lall_crown, I40_BA22_avg_Lall_crown, I42_BA22_avg_Lall_crown, I49_BA22_avg_Lall_crown], axis=0)
print("df_list_crown_absolute_BA22 = ", df_list_crown_absolute_BA22)

df_list_fundus_absolute_BA21_22 = np.mean([I32_BA21_22_avg_Lall_fundus, I33_BA21_22_avg_Lall_fundus, I34_BA21_22_avg_Lall_fundus], axis=0)
print("df_list_fundus_absolute_BA21_22 = ", df_list_fundus_absolute_BA21_22)

df_list_crown_absolute_BA21 = np.mean([I25_BA21_avg_Lall_crown, I27_BA21_avg_Lall_crown, I30_BA21_avg_Lall_crown, I31_BA21_avg_Lall_crown, I32_BA21_avg_Lall_crown, I33_BA21_avg_Lall_crown, I40_BA21_avg_Lall_crown, I42_BA21_avg_Lall_crown, I44_BA21_avg_Lall_crown, I47_BA21_avg_Lall_crown, I49_BA21_avg_Lall_crown], axis=0)
print("df_list_crown_absolute_BA21 = ", df_list_crown_absolute_BA21)

df_list_fundus_absolute_BA20B_21 = np.mean([I25_BA20B_21_avg_Lall_fundus, I42_BA20B_21_avg_Lall_fundus, I49_BA20B_21_avg_Lall_fundus, I32_BA20B_21_avg_Lall_fundus, I33_BA20B_21_avg_Lall_fundus, I47_BA20B_21_avg_Lall_fundus], axis=0)
print("df_list_fundus_absolute_BA20B_21 = ", df_list_fundus_absolute_BA20B_21)

#df_list_crown_absolute_BA20B = np.mean([I25_BA20B_avg_Lall_crown, I27_BA20B_avg_Lall_crown, I32_BA20B_avg_Lall_crown, I33_BA20B_avg_Lall_crown, I40_BA20B_avg_Lall_crown, I42_BA20B_avg_Lall_crown, I44_BA20B_avg_Lall_crown, I47_BA20B_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA20_all = np.mean([I25_BA20_all_avg_Lall_crown, I27_BA20_all_avg_Lall_crown, I32_BA20_all_avg_Lall_crown, I33_BA20_all_avg_Lall_crown, I34_BA20_all_avg_Lall_crown, I40_BA20_all_avg_Lall_crown, I42_BA20_all_avg_Lall_crown, I44_BA20_all_avg_Lall_crown, I47_BA20_all_avg_Lall_crown, I49_BA20_all_avg_Lall_crown], axis=0)
print("df_list_crown_absolute_BA20_all = ", df_list_crown_absolute_BA20_all)

df_list_fundus_absolute_BA20A_20B = np.mean([I44_BA20A_20B_avg_Lall_fundus, I34_BA20A_20B_avg_Lall_fundus], axis=0)
print("df_list_fundus_absolute_BA20A_20B = ", df_list_fundus_absolute_BA20A_20B)

df_list_crown_absolute_BA36 = np.mean([I25_BA36_avg_Lall_crown, I32_BA36_avg_Lall_crown, I34_BA36_avg_Lall_crown, I42_BA36_avg_Lall_crown, I44_BA36_avg_Lall_crown, I49_BA36_avg_Lall_crown], axis=0)
print("df_list_crown_absolute_BA36 = ", df_list_crown_absolute_BA36)

#df_list_crown_absolute_BA20A = np.mean([I25_BA20A_avg_Lall_crown, I27_BA20A_avg_Lall_crown, I32_BA20A_avg_Lall_crown, I33_BA20A_avg_Lall_crown, I34_BA20A_avg_Lall_crown, I40_BA20A_avg_Lall_crown, I42_BA20A_avg_Lall_crown, I44_BA20A_avg_Lall_crown, I47_BA20A_avg_Lall_crown, I49_BA20A_avg_Lall_crown], axis=0)


df_list_mean = [[round(item, 2) for item in df_list_crown_absolute_BA22], [round(item, 2) for item in df_list_fundus_absolute_BA21_22], [round(item, 2) for item in df_list_crown_absolute_BA21], [round(item, 2) for item in df_list_fundus_absolute_BA20B_21], [round(item, 2) for item in df_list_crown_absolute_BA20_all], [round(item, 2) for item in df_list_fundus_absolute_BA20A_20B], [round(item, 2) for item in df_list_crown_absolute_BA36]]
#print("df_list_mean = ", df_list_mean)

#make the list in to a dataframe table
df_mean = pd.DataFrame(df_list_mean, columns=['Layer I', 'Layer II', 'Layer III', 'Layer IV', 'Layer V', 'Layer VI'])

info_mean = ["BA22 crown", "BA22_21 fundus", "BA21 crown", "BA21_20 fundus", "BA20 crown", "BA20_20 fundus", "BA36 crown"]

df_mean_micron = df_mean * 1000

df_absolute = pd.DataFrame(df_list_mean, columns=['Layer I mm (%)', 'Layer II mm (%)', 'Layer III mm (%)', 'Layer IV mm (%)', 'Layer V mm (%)', 'Layer VI mm (%)'])

lista = np.ones(42)

#df_absolute_relative = [item[" ({}\n)".format([i for i in lista]) for item in df_absolute]
#print(df_absolute_relative)

df_info_mean = df_mean.insert(0, "Gyrus Info", [item for item in info_mean])
df_info_mean_micron = df_mean_micron.insert(0, "Gyrus Info", [item for item in info_mean])
#df_info_absolute_relative = df_absolute_relative.insert(0, "Gyrus Info", [item for item in info_mean])

tot_cortical_thick = df_mean.insert(7, "Cortical Thickness (mm)", [round(sum(item), 2) for item in df_list_mean])

tot_cortical_thick_micron = df_mean_micron.insert(7, "Cortical Thickness (um)", [round(sum(item*1000), 2) for item in df_list_mean])


#write the dataframe to an excel file
df_mean.to_excel(writer, index=False, sheet_name='crown_fundus_absolute')

df_mean_crown = df_mean[::2]
df_mean_crown.to_excel(writer, index=False, sheet_name='crown_absolute')

df_mean_fundus = df_mean[1::2]
df_mean_fundus.to_excel(writer, index=False, sheet_name='fundus_absolute')

df_mean_micron.to_excel(writer, index=False, sheet_name='crown_fundus_absolute_micron')

df_mean_micron_crown = df_mean_micron[::2]
df_mean_micron_crown.to_excel(writer, index=False, sheet_name='crown_absolute_micron')

df_mean_micron_fundus = df_mean_micron[1::2]
df_mean_micron_crown.to_excel(writer, index=False, sheet_name='fundus_absolute_micron')


writer.save()
#print(df_mean)

#print(df_mean_micron)

#this section will turn the basic dataframe table into a pretty table, that can be plotted offline with firefox. can also save a static image and change quality of image

#table colours
colorscale = [[0, '#660033'], [0.5, '#E0E0E0'], [1, '#ffffff']]

#create the table
df_table = ff.create_table(df_mean, colorscale=colorscale)

# Make table text size larger
for i in range(len(df_table.layout.annotations)):
    df_table.layout.annotations[i].font.size = 13.50

#save table as a static image
#df_table.write_image("BA_all_crown_fundus_average_table.png", width=1400, height=350, scale=6)


#AVERAGE SEX
df_list_crown_absolute_BA22_female = np.mean([I30_BA22_avg_Lall_crown, I32_BA22_avg_Lall_crown, I33_BA22_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA22_male = np.mean([I25_BA22_avg_Lall_crown, I34_BA22_avg_Lall_crown, I40_BA22_avg_Lall_crown, I42_BA22_avg_Lall_crown, I49_BA22_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA21_female = np.mean([I27_BA21_avg_Lall_crown, I30_BA21_avg_Lall_crown, I32_BA21_avg_Lall_crown, I33_BA21_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA21_male = np.mean([I25_BA21_avg_Lall_crown, I31_BA21_avg_Lall_crown, I40_BA21_avg_Lall_crown, I42_BA21_avg_Lall_crown, I44_BA21_avg_Lall_crown, I47_BA21_avg_Lall_crown, I49_BA21_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA20_all_female = np.mean([I27_BA20_all_avg_Lall_crown, I32_BA20_all_avg_Lall_crown, I33_BA20_all_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA20_all_male = np.mean([I25_BA20_all_avg_Lall_crown, I34_BA20_all_avg_Lall_crown, I40_BA20_all_avg_Lall_crown, I42_BA20_all_avg_Lall_crown, I44_BA20_all_avg_Lall_crown, I47_BA20_all_avg_Lall_crown, I49_BA20_all_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA36_female = np.mean([I32_BA36_avg_Lall_crown], axis=0)

df_list_crown_absolute_BA36_male = np.mean([I25_BA36_avg_Lall_crown, I34_BA36_avg_Lall_crown, I42_BA36_avg_Lall_crown, I44_BA36_avg_Lall_crown, I49_BA36_avg_Lall_crown], axis=0)

#df_list_crown_absolute_BA20B_female = np.mean([I27_BA20B_avg_Lall_crown, I32_BA20B_avg_Lall_crown, I33_BA20B_avg_Lall_crown], axis=0)

#df_list_crown_absolute_BA20B_male = np.mean([I25_BA20B_avg_Lall_crown, I40_BA20B_avg_Lall_crown, I42_BA20B_avg_Lall_crown, I44_BA20B_avg_Lall_crown, I47_BA20B_avg_Lall_crown], axis=0)

#df_list_crown_absolute_BA20A_female = np.mean([I27_BA20A_avg_Lall_crown, I32_BA20A_avg_Lall_crown, I33_BA20A_avg_Lall_crown], axis=0)

#df_list_crown_absolute_BA20A_male = np.mean([I25_BA20A_avg_Lall_crown, I34_BA20A_avg_Lall_crown, I40_BA20A_avg_Lall_crown, I42_BA20A_avg_Lall_crown, I44_BA20A_avg_Lall_crown, I47_BA20A_avg_Lall_crown, I49_BA20A_avg_Lall_crown], axis=0)


df_list_mean_sex = [[round(item, 2) for item in df_list_crown_absolute_BA22_female], [round(item, 2) for item in df_list_crown_absolute_BA22_male], [round(item, 2) for item in df_list_crown_absolute_BA21_female], [round(item, 2) for item in df_list_crown_absolute_BA21_male], [round(item, 2) for item in df_list_crown_absolute_BA20_all_female], [round(item, 2) for item in df_list_crown_absolute_BA20_all_male], [round(item, 2) for item in df_list_crown_absolute_BA36_female], [round(item, 2) for item in df_list_crown_absolute_BA36_male]]

df_mean_sex = pd.DataFrame(df_list_mean_sex, columns=['Layer I', 'Layer II', 'Layer III', 'Layer IV', 'Layer V', 'Layer VI'])

info_mean_sex = ["BA22 crown female", "BA22 crown male", "BA21 crown female", "BA21 crown male", "BA20 crown female", "BA20 crown male", "BA36 crown female", "BA36 crown male"]

df_info_mean_sex = df_mean_sex.insert(0, "Gyrus Info", [item for item in info_mean_sex])

tot_cortical_thick_sex = df_mean_sex.insert(7, "Cortical Thickness (mm)", [round(sum(item), 2) for item in df_list_mean_sex])
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
#print(df_mean_sex)

df_mean_sex.to_excel(writer, index=False, sheet_name='crown_absolute_sex')
writer.save()

df_table_sex = ff.create_table(df_mean_sex, colorscale=colorscale)

# Make table text size larger
for i in range(len(df_table_sex.layout.annotations)):
    df_table_sex.layout.annotations[i].font.size = 13.50

#save table as a static image
#df_table_sex.write_image("BA_all_crown_average_table_sex.png", width=1400, height=350, scale=6)


#this line will open the nice table in firefox for viewing, this is a plot and not static
#py.iplot(df_table, filename='BA_all_crown_fundus_average_table2.png', image='svg')

#alternative ways to do things
#df_table.layout.width = 1200
#pio.to_image(df_table, format="svg")
#display(SVG(img_bytes))


#percentage change between crown
BA22crown_BA21crown_per_change = [((b-a)/a)*100 for a, b in zip(BA22_Lall_crown_mean, BA21_Lall_crown_mean)]

BA22crown_BA20crown_per_change = [((b-a)/a)*100 for a, b in zip(BA22_Lall_crown_mean, BA20_all_Lall_crown_mean)]

BA22crown_BA36crown_per_change = [((b-a)/a)*100 for a, b in zip(BA22_Lall_crown_mean, BA36_Lall_crown_mean)]

BA21crown_BA20crown_per_change = [((b-a)/a)*100 for a, b in zip(BA21_Lall_crown_mean, BA20_all_Lall_crown_mean)]

BA21crown_BA36crown_per_change = [((b-a)/a)*100 for a, b in zip(BA21_Lall_crown_mean, BA36_Lall_crown_mean)]

BA20crown_BA36crown_per_change = [((b-a)/a)*100 for a, b in zip(BA20_all_Lall_crown_mean, BA36_Lall_crown_mean)]

per_change_list_crown = [BA22crown_BA21crown_per_change, BA22crown_BA20crown_per_change, BA22crown_BA36crown_per_change, BA21crown_BA20crown_per_change, BA21crown_BA36crown_per_change, BA20crown_BA36crown_per_change]

df_per_change_crown = pd.DataFrame(per_change_list_crown, columns=['Layer I', 'Layer II', 'Layer III', 'Layer IV', 'Layer V', 'Layer VI'])

info_per_change_crown = ["BA22_crown BA21_crown", "BA22_crown BA20_crown", "BA22_crown BA36_crown", "BA21_crown BA20_crown", "BA21_crown BA36_crown", "BA20_crown BA36_crown"]

df_info_per_change_crown = df_per_change_crown.insert(0, "Gyrus Info", [item for item in info_per_change_crown])

df_per_change_crown.to_excel(writer, index=False, sheet_name='crown_per_change')
writer.save()


#percentage change between crown and fundus
BA22crown_BA21_22fundus_per_change = [((b-a)/a)*100 for a, b in zip(BA22_Lall_crown_mean, BA21_22_fundus_mean)]

BA21crown_BA21_22fundus_per_change = [((b-a)/a)*100 for a, b in zip(BA21_Lall_crown_mean, BA21_22_fundus_mean)]

BA21crown_BA20B_21fundus_per_change = [((b-a)/a)*100 for a, b in zip(BA21_Lall_crown_mean, BA20B_21_fundus_mean)]

# sulcus_test.write("BA21crown_BA20B_21fundus_per_change = {}\n".format(BA21crown_BA20B_21fundus_per_change))

BA20_all_crown_BA20B_21fundus_per_change = [((b-a)/a)*100 for a, b in zip(BA20_all_Lall_crown_mean, BA20B_21_fundus_mean)]

BA20_all_crown_BA20A_20Bfundus_per_change = [((b-a)/a)*100 for a, b in zip(BA20_all_Lall_crown_mean, BA20A_20B_fundus_mean)]

BA36crown_BA20A_20Bfundus_per_change = [((b-a)/a)*100 for a, b in zip(BA36_Lall_crown_mean, BA20A_20B_fundus_mean)]

#all BA averaged together
BA_all_avg_together_crown_fundus_per_change = [((b-a)/a)*100 for a, b in zip(BA22_Lall_crown_mean, BA21_22_fundus_mean)]
print("BA_all_avg_together_crown_fundus_per_change = ", BA_all_avg_together_crown_fundus_per_change)

print("BA_all_avg_together_crown_fundus_per_change[0] = ", round(BA_all_avg_together_crown_fundus_per_change[0], 2))

#sulcus test
# BA21crown_BA21sulcus_inf_per_change = [((b-a)/a)*100 for a, b in zip(BA_all_avg_absolute_crown, BA_all_avg_absolute_fundus)]

# sulcus_test.write("BA21crown_BA21sulcus_inf_per_change = {}\n".format(BA21crown_BA21sulcus_inf_per_change))


# BA21sulcus_inf_BA20B_21_fundus_per_change = [((b-a)/a)*100 for a, b in zip(I25_BA21_rel_Lall_sulcus_inf, BA20B_21_fundus_mean)]

# sulcus_test.write("BA21sulcus_inf_BA20B_21_fundus_per_change = {}\n".format(BA21sulcus_inf_BA20B_21_fundus_per_change))


per_change_list = [BA22crown_BA21_22fundus_per_change, BA21crown_BA21_22fundus_per_change, BA21crown_BA20B_21fundus_per_change, BA20_all_crown_BA20B_21fundus_per_change, BA20_all_crown_BA20A_20Bfundus_per_change, BA36crown_BA20A_20Bfundus_per_change]


df_per_change = pd.DataFrame(per_change_list, columns=['Layer I', 'Layer II', 'Layer III', 'Layer IV', 'Layer V', 'Layer VI'])

info_per_change = ["BA22_crown BA22_21_fundus", "BA21_crown BA22_21_fundus", "BA21_crown BA21_20_fundus", "BA20_crown BA21_20_fundus", "BA20_crown BA20_20_fundus", "BA36_crown BA20_20_fundus"]

df_info_per_change = df_per_change.insert(0, "Gyrus Info", [item for item in info_per_change])

df_per_change.to_excel(writer, index=False, sheet_name='crown_fundus_per_change')
writer.save()

# sulcus_test.close()

#Von Economo style table

df_list_mean_flat = ["{}".format(i) for list in df_list_mean for i in list]
#print(df_list_mean_flat)

df_list_relative_flat = [" ({})".format(i) for list in df_list_relative for i in list]
#print(df_list_relative_flat)

list_absolute_relative_flat = [a + b for a, b in zip(df_list_mean_flat, df_list_relative_flat)]

list_absolute_relative = [list_absolute_relative_flat[0:6], list_absolute_relative_flat[6:12], list_absolute_relative_flat[12:18], list_absolute_relative_flat[18:24], list_absolute_relative_flat[24:30], list_absolute_relative_flat[30:36], list_absolute_relative_flat[36:42]]
print("list_absolute_relative = ",list_absolute_relative )

#dict_absolute_relative = dict(zip(df_list_mean_flat, df_list_relative_flat))
#print("dict_absolute_relative = ", dict_absolute_relative)

df_absolute_relative = pd.DataFrame(list_absolute_relative, columns=['Layer I \nmm (%)', 'Layer II \nmm (%)', 'Layer III \nmm (%)', 'Layer IV \nmm (%)', 'Layer V \nmm (%)', 'Layer VI \nmm (%)'])

df_absolute_relative_info = df_absolute_relative.insert(0, "Gyrus \nInformation", [item for item in info_mean])

tot_cortical_thick = [round(sum(item), 2) for item in df_list_mean]

tot_cortical_thick_VE = ["{} (1)".format(i) for i in tot_cortical_thick]

df_absolute_relative.insert(7, "Cortical \nThickness mm (%)", tot_cortical_thick_VE)
#print(df_absolute_relative)

df_absolute_relative.to_excel(writer, index=False, sheet_name='crown_fundus_absolute_relative')
writer.save()


#VON ECONOMO DATA
#absolute TABLE I
VE_M1_FA_absolute_6a_only = np.array([0.18, 0.00, 1.47, 0.00, 0.80, 1.00])
VE_A1_TC_absolute_6a_only = np.array([0.26, 0.28, 0.74, 0.45, 0.53, 0.39])
VE_A1_TB_absolute_6a_only = np.array([0.24, 0.20, 0.88, 0.37, 0.40, 0.53])
VE_V1_OB_absolute_6a_only = np.array([0.16, 0.18, 0.46, 0.18, 0.26, 0.32])
VE_S1_PC_absolute_6a_only = np.array([0.23, 0.23, 0.86, 0.36, 0.38, 0.60])
VE_association_cortex_TA_absolute_6a_only = np.array([0.25, 0.16, 0.69, 0.19, 0.33, 0.31])
VE_association_cortex_TE_absolute_6a_only = np.array([0.24, 0.20, 0.95, 0.22, 0.50, 0.53])
# print("VE_M1_FA_absolute_6a_only = ", VE_M1_FA_absolute_6a_only)


VE_V1_OB_absolute_6a_plus_6b_T1 = np.array([0.16, 0.18, 0.46, 0.18, 0.26, 0.32+0.26])
VE_A1_TC_absolute_6a_plus_6b_T1 = np.array([0.26, 0.28, 0.74, 0.45, 0.53, 0.39+0.25])
VE_S1_PC_absolute_6a_plus_6b_T1 = np.array([0.23, 0.23, 0.86, 0.36, 0.38, 0.60+0.50])
VE_association_cortex_TE_absolute_6a_plus_6b_T1 = np.array([0.24, 0.17, 0.86, 0.24, 0.69, 0.76+0.59])
# print("VE_M1_FA_absolute_6a_plus_6b_T1 = ", VE_M1_FA_absolute_6a_plus_6b_T1)


#FIGURES

#red colour scheme
#D07979 - alpha=1
#EC5959 - alpha=0.95
#A43E3E - alpha=1
#C10303 - alpha=0.95
#800000 - alpha=1
#400404 - alpha=1

#blue-green colour scheme
#5F9EA0 - alpha=0.90
#1BA7AC - alpha=0.90
#207979 - alpha=1
#06697D - alpha=0.90
#09414A - alpha=0.90
#001414 - alpha=0.90

#beautiful deep green, blue, teal - #006666

#pink colour scheme
#C783B3 - alpha=0.90
#DB7093 - alpha=0.90
#993366 - alpha=0.90
#900C3F - alpha=0.90
#660033 - alpha=0.90
#330019 - alpha=0.90

#purple colour scheme
#7F57A8 - alpha=0.86
#8A2BE2 - alpha=1
#5C3386 - alpha=1
#510251 - alpha=1
#2B0352 - alpha=1
#1B0235 - alpha=1


#PERCENTAGE CHANGE GRAPH - crown and fundus

bars1 = BA22crown_BA21_22fundus_per_change
bars2 = BA21crown_BA20B_21fundus_per_change
bars3 = BA20_all_crown_BA20A_20Bfundus_per_change
bars4 = BA36crown_BA20A_20Bfundus_per_change

#all pairs
#bars1 = BA22crown_BA21_22fundus_per_change
#bars2 = BA21crown_BA21_22fundus_per_change
#bars3 = BA21crown_BA20B_21fundus_per_change
#bars4 = BA20_all_crown_BA20B_21fundus_per_change
#bars5 = BA20_all_crown_BA20A_20Bfundus_per_change
#bars6 = BA36crown_BA20A_20Bfundus_per_change


#bar position on graph
barWidth = 0.24
#barWidth = 0.15


r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]

plt.bar(r1, bars1, color='#F39A9A', edgecolor='white', width=barWidth, label='BA22_crown and BA22_21_fundus',  alpha=1,)
#plt.text(-0.1, 257, int(round(BA22crown_BA21_22fundus_per_change[0])), fontsize=6) #layer 1

plt.bar(r2, bars2, color='#CD5C5C', edgecolor='white', width=barWidth, label='BA21_crown and BA21_20_fundus',  alpha=1,)
#plt.text(0.07, 241.8, int(round(BA21crown_BA20B_21fundus_per_change[0])), fontsize=6) #layer 1

#plt.bar(r2, bars2, color='#CD5C5C', edgecolor='white', width=barWidth, label='BA21_crown and BA22_21_fundus',  alpha=1,)

plt.bar(r3, bars3, color='#B22222', edgecolor='white', width=barWidth, label='BA20_crown and BA20_20_fundus',  alpha=1,)

#plt.bar(r3, bars3, color='#B22222', edgecolor='white', width=barWidth, label='BA21_crown and BA21_20_fundus',  alpha=1,)

plt.bar(r4, bars4, color='#8B0000', edgecolor='white', width=barWidth, label='BA36_crown and BA20_20_fundus',  alpha=1)

#plt.bar(r4, bars4, color='#8B0000', edgecolor='white', width=barWidth, label='BA20_crown and BA21_20_fundus',  alpha=1,)

#plt.bar(r5, bars5, color='#8B0000', edgecolor='white', width=barWidth, label='BA20_crown and BA20_20_fundus',  alpha=1,)

#plt.bar(r6, bars6, color='#8B0000', edgecolor='white', width=barWidth, label='BA36_crown and BA20_20_fundus',  alpha=1,)


plt.ylabel('Percentage change (crown to fundus)', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks([r + 0.37 for r in range(len(bars1))] , ['LI','LII', 'LIII', 'LIV', 'LV', 'LVI'], fontsize=11, fontname="serif")
plt.yticks(np.arange(-75, 280, 50)) #yaxis points
plt.legend(loc='upper right', prop={'size': 6})

#plt.savefig('BA_all_crown_fundus_per_change_grouped_bar_chart_values.png', dpi=1000)
#plt.savefig('BA_all_crown_fundus_per_change_grouped_bar_chart_novalues.png', dpi=1000)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_per_change_grouped_bar_chart_novalues_allpairs.png', dpi=1000)

plt.show()


#PERCENTAGE CHANGE GRAPH - crown and fundus - ALL BA average together

#error bar info
bar_LI_std = [BA22_Lall_crown_std[0],  BA21_22_fundus_std[0], BA21_Lall_crown_std[0], BA20B_21_fundus_std[0], BA20_all_Lall_crown_std[0], BA20A_20B_fundus_std[0], BA36_Lall_crown_std[0]]
bar_LII_std = [BA22_Lall_crown_std[1],  BA21_22_fundus_std[1], BA21_Lall_crown_std[1], BA20B_21_fundus_std[1], BA20_all_Lall_crown_std[1], BA20A_20B_fundus_std[1], BA36_Lall_crown_std[1]]
bar_LIII_std = [BA22_Lall_crown_std[2],  BA21_22_fundus_std[2], BA21_Lall_crown_std[2], BA20B_21_fundus_std[2], BA20_all_Lall_crown_std[2], BA20A_20B_fundus_std[2], BA36_Lall_crown_std[2]]
bar_LIV_std = [BA22_Lall_crown_std[3],  BA21_22_fundus_std[3], BA21_Lall_crown_std[3], BA20B_21_fundus_std[3], BA20_all_Lall_crown_std[3], BA20A_20B_fundus_std[3], BA36_Lall_crown_std[3]]

bar_LV_std = [BA22_Lall_crown_std[4],  BA21_22_fundus_std[4], BA21_Lall_crown_std[4], BA20B_21_fundus_std[4], BA20_all_Lall_crown_std[4], BA20A_20B_fundus_std[4], BA36_Lall_crown_std[4]]

bar_LVI_std = [BA22_Lall_crown_std[5],  BA21_22_fundus_std[5], BA21_Lall_crown_std[5], BA20B_21_fundus_std[5], BA20_all_Lall_crown_std[5], BA20A_20B_fundus_std[5], BA36_Lall_crown_std[5]]


mean_lst_std = [np.mean(bar_LI_std)*100, np.mean(bar_LII_std)*100, np.mean(bar_LIII_std)*100,\
np.mean(bar_LIV_std)*100, np.mean(bar_LV_std)*100, np.mean(bar_LVI_std)*100]

mean_lst_std_noscale = [round(i, 2) for i in [np.mean(bar_LI_std), np.mean(bar_LII_std), \
np.mean(bar_LIII_std),np.mean(bar_LIV_std), np.mean(bar_LV_std), np.mean(bar_LVI_std)]]

lst_std = [bar_LI_std, bar_LII_std, bar_LIII_std, bar_LIV_std, bar_LV_std, bar_LVI_std]

print("lst_std = ", lst_std)
print("mean_lst_std = ", mean_lst_std)
print("mean_lst_std_noscale = ", mean_lst_std_noscale)



bars = BA_all_avg_together_crown_fundus_per_change

#bar position on graph
barWidth = 0.6

r1 = np.arange(len(bars))
#r1 = 6

#plt.bar(r1, bars, color='#8B0000', edgecolor='white', width=barWidth, alpha=1)
plt.bar(r1, bars, color='#6B2A24', edgecolor='white', width=barWidth, alpha=1,\
yerr=mean_lst_std)


plt.text(-0.28, BA_all_avg_together_crown_fundus_per_change[0]+7, round(BA_all_avg_together_crown_fundus_per_change[0], 2), fontsize=10, fontweight='bold') #layer 1
plt.text(0.76, BA_all_avg_together_crown_fundus_per_change[1]+7, round(BA_all_avg_together_crown_fundus_per_change[1], 2), fontsize=10, fontweight='bold') #layer 2
plt.text(1.72, BA_all_avg_together_crown_fundus_per_change[2]-17, round(BA_all_avg_together_crown_fundus_per_change[2], 2), fontsize=10, fontweight='bold') #layer 3
plt.text(2.80, BA_all_avg_together_crown_fundus_per_change[3]+7, round(BA_all_avg_together_crown_fundus_per_change[3], 2), fontsize=10, fontweight='bold') #layer 4
plt.text(3.72, BA_all_avg_together_crown_fundus_per_change[4]-15, round(BA_all_avg_together_crown_fundus_per_change[4], 2), fontsize=10, fontweight='bold') #layer 5
plt.text(4.72, BA_all_avg_together_crown_fundus_per_change[5]-16, round(BA_all_avg_together_crown_fundus_per_change[5], 2), fontsize=10, fontweight='bold') #layer 6


#plt.axhline(y=0, color='#EAECEE', linestyle='solid', linewidth=0.8)
#plt.axhline(y=0, color='#FDEDEC', linestyle='solid', linewidth=0.8)
#plt.axhline(y=0, color='#FCEDEC', linestyle='solid', linewidth=1.5)
#plt.axhline(y=0, color='#F9F9F9', linestyle='solid', linewidth=1.5)
#plt.axhline(y=0, color='#303030', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#3D3D3D', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#535353', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#464449', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#4D4C50', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#5E5E60', linestyle='solid', linewidth=1)
plt.axhline(y=0, color='#6F6F70', linestyle='solid', linewidth=1)
#plt.axhline(y=0, color='#808080', linestyle='solid', linewidth=1)


plt.xticks([r + 0 for r in range(len(bars))] , ['LI','LII', 'LIII', 'LIV', 'LV', 'LVI'], fontsize=13, fontname="serif")
#plt.xticks([r + 0 for r in range(len(bars))], fontsize=11, fontname="serif")
plt.yticks(np.arange(-75, 280, 50)) #yaxis points
plt.ylabel('Percentage change thickness', fontname="serif", fontsize=12, fontweight='bold')
plt.tight_layout()
# plt.savefig('BA_all_avg_together_crown_fundus_per_change_bar_chart_values_long.png', dpi=1000)
plt.savefig('BA_all_avg_together_crown_fundus_per_change_bar_chart_values_longyerr_dpi1000.png', dpi=1000)
plt.savefig('BA_all_avg_together_crown_fundus_per_change_bar_chart_values_longyerr_dpi300.png', dpi=300)
plt.savefig('BA_all_avg_together_crown_fundus_per_change_bar_chart_values_longyerr_dpi100.png')

plt.show()


#PERCENTAGE CHANGE GRAPH - crown, sulcus and fundus
#
# bars1 = BA21crown_BA20B_21fundus_per_change
# bars2 = BA21crown_BA21sulcus_inf_per_change
# bars3 = BA21sulcus_inf_BA20B_21_fundus_per_change
#
# #bar position on graph
# barWidth = 0.24
# #barWidth = 0.15
#
#
# r1 = np.arange(len(bars1))
# r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]
#
# plt.bar(r1, bars1, color='#F39A9A', edgecolor='white', width=barWidth, label='BA21_crown and BA20B_21_fundus',  alpha=1,)
#
# plt.bar(r2, bars2, color='#CD5C5C', edgecolor='white', width=barWidth, label='BA21_crown and BA21_sulcus_inf',  alpha=1,)
#
# plt.bar(r3, bars3, color='#B22222', edgecolor='white', width=barWidth, label='BA21_sulcus_inf and BA20B_21_fundus',  alpha=1,)
#
#
# plt.ylabel('Percentage change (crown, sulcus and fundus)', fontname="serif", fontsize=8, fontweight='bold')
# plt.xticks([r + 0.37 for r in range(len(bars1))] , ['LI','LII', 'LIII', 'LIV', 'LV', 'LVI'], fontsize=11, fontname="serif")
# plt.yticks(np.arange(-75, 280, 50)) #yaxis points
# plt.legend(loc='upper right', prop={'size': 6})
# plt.tight_layout()
# plt.show()



#PERCENTAGE CHANGE GRAPH - crown
bars1 = BA22crown_BA21crown_per_change
bars2 = BA22crown_BA20crown_per_change
bars3 = BA22crown_BA36crown_per_change
bars4 = BA21crown_BA20crown_per_change
bars5 = BA21crown_BA36crown_per_change
bars6 = BA20crown_BA36crown_per_change

#bar position on graph
barWidth = 0.15

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]

plt.bar(r1, bars1, color='#F39A9A', edgecolor='white', width=barWidth, label='BA22_crown and BA21_crown',  alpha=1,)
plt.bar(r2, bars2, color='#CD5C5C', edgecolor='white', width=barWidth, label='BA22_crown and BA20_crown',  alpha=1,)
plt.bar(r3, bars3, color='#B22222', edgecolor='white', width=barWidth, label='BA22_crown and BA36_crown',  alpha=1,)
plt.bar(r4, bars4, color='#8B0000', edgecolor='white', width=barWidth, label='BA21_crown and BA20_crown',  alpha=1,)
plt.bar(r5, bars5, color='#8B0000', edgecolor='white', width=barWidth, label='BA21_crown and BA36_crown',  alpha=1,)
plt.bar(r6, bars6, color='#8B0000', edgecolor='white', width=barWidth, label='BA20_crown and BA36_crown',  alpha=1,)


plt.ylabel('Percentage change', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks([r + 0.37 for r in range(len(bars1))] , ['LI','LII', 'LIII', 'LIV', 'LV', 'LVI'], fontsize=11, fontname="serif")
plt.yticks(np.arange(-15, 20, 5)) #yaxis points
plt.legend(loc='upper right', prop={'size': 7})
plt.tight_layout()
#plt.savefig('BA_all_crown_per_change_grouped_bar_chart_novalues.png', dpi=1000)
plt.show()


#CROWN ONLY
#segmented bar graph

bar_LI = [BA22_Lall_crown_mean[0], BA21_Lall_crown_mean[0], BA20_all_Lall_crown_mean[0], BA36_Lall_crown_mean[0]]

bar_LII = [BA22_Lall_crown_mean[1], BA21_Lall_crown_mean[1], BA20_all_Lall_crown_mean[1], BA36_Lall_crown_mean[1]]

bar_LIII = [BA22_Lall_crown_mean[2], BA21_Lall_crown_mean[2], BA20_all_Lall_crown_mean[2], BA36_Lall_crown_mean[2]]

bar_LIV = [BA22_Lall_crown_mean[3], BA21_Lall_crown_mean[3], BA20_all_Lall_crown_mean[3], BA36_Lall_crown_mean[3]]

bar_LV = [BA22_Lall_crown_mean[4], BA21_Lall_crown_mean[4], BA20_all_Lall_crown_mean[4], BA36_Lall_crown_mean[4]]

bar_LVI = [BA22_Lall_crown_mean[5], BA21_Lall_crown_mean[5], BA20_all_Lall_crown_mean[5], BA36_Lall_crown_mean[5]]
#print(bar_LV)


barWidth = 0.5
ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)

plt.bar(ind, bar_LI, color='#C783B3', edgecolor='white', width=barWidth, label='Layer I', alpha=0.90, bottom=r5)
plt.bar(ind, bar_LII, color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=r4)
plt.bar(ind, bar_LIII, color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=0.90, bottom=r3)
plt.bar(ind, bar_LIV, color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2)
plt.bar(ind, bar_LV, color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=r1)
plt.bar(ind, bar_LVI, color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)


plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks(ind, ['BA22\ncrown', 'BA21\ncrown', 'BA20\ncrown', 'BA36\ncrown'], fontsize=7, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.yticks(np.arange(0, 1.24, 0.2)) #yaxis points
plt.title('Segmented bar graph showing the laminar layers of the crown in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 4.6})
plt.tight_layout()
#plt.savefig('BA_all_crown_seg_chart.png', dpi=1000)
plt.show()


#FUNDUS ONLY
#segmented bar graph

bar_LI = [BA21_22_fundus_mean[0], BA20B_21_fundus_mean[0], BA20A_20B_fundus_mean[0]]

bar_LII = [BA21_22_fundus_mean[1], BA20B_21_fundus_mean[1], BA20A_20B_fundus_mean[1]]

bar_LIII = [BA21_22_fundus_mean[2], BA20B_21_fundus_mean[2], BA20A_20B_fundus_mean[2]]

bar_LIV = [BA21_22_fundus_mean[3], BA20B_21_fundus_mean[3], BA20A_20B_fundus_mean[3]]

bar_LV = [BA21_22_fundus_mean[4], BA20B_21_fundus_mean[4], BA20A_20B_fundus_mean[4]]

bar_LVI = [BA21_22_fundus_mean[5], BA20B_21_fundus_mean[5], BA20A_20B_fundus_mean[5]]
#print(bar_LV)


barWidth = 0.4
ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)


plt.bar(ind, bar_LI, color='#C783B3', edgecolor='white', width=barWidth, label='Layer I', alpha=0.8, bottom=r5) #CD5C5C
plt.bar(ind, bar_LII, color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=1, bottom=r4) #F74242 #F73636
plt.bar(ind, bar_LIII, color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=r3)
plt.bar(ind, bar_LIV, color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2)
plt.bar(ind, bar_LV, color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.95, bottom=r1)
plt.bar(ind, bar_LVI, color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90) #330000


plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks(ind, ['BA22_21\nfundus', 'BA21_20\nfundus', 'BA20_20\nfundus'], fontsize=7, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.yticks(np.arange(0, 1.24, 0.2)) #yaxis points
plt.title('Segmented bar graph showing the laminar layers of the fundus in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 4.6})
plt.tight_layout()
#plt.savefig('BA_all_fundus_seg_chart.png', dpi=1000)
plt.show()


#CROWN AND FUNDUS - mixed groups with the same colour - RELATIVE
#segmented bar graph

bar_LI = [BA22_Lall_crown_mean[0], BA21_22_fundus_mean[0], BA21_Lall_crown_mean[0], BA20B_21_fundus_mean[0], BA20_all_Lall_crown_mean[0], BA20A_20B_fundus_mean[0], BA36_Lall_crown_mean[0]]
#print("bar_LI = ", bar_LI)

bar_LII = [BA22_Lall_crown_mean[1], BA21_22_fundus_mean[1], BA21_Lall_crown_mean[1], BA20B_21_fundus_mean[1], BA20_all_Lall_crown_mean[1], BA20A_20B_fundus_mean[1], BA36_Lall_crown_mean[1]]

bar_LIII = [BA22_Lall_crown_mean[2], BA21_22_fundus_mean[2], BA21_Lall_crown_mean[2], BA20B_21_fundus_mean[2], BA20_all_Lall_crown_mean[2], BA20A_20B_fundus_mean[2], BA36_Lall_crown_mean[2]]

bar_LIV = [BA22_Lall_crown_mean[3], BA21_22_fundus_mean[3], BA21_Lall_crown_mean[3], BA20B_21_fundus_mean[3], BA20_all_Lall_crown_mean[3], BA20A_20B_fundus_mean[3], BA36_Lall_crown_mean[3]]

bar_LV = [BA22_Lall_crown_mean[4], BA21_22_fundus_mean[4], BA21_Lall_crown_mean[4], BA20B_21_fundus_mean[4], BA20_all_Lall_crown_mean[4], BA20A_20B_fundus_mean[4], BA36_Lall_crown_mean[4]]

bar_LVI = [BA22_Lall_crown_mean[5], BA21_22_fundus_mean[5], BA21_Lall_crown_mean[5], BA20B_21_fundus_mean[5], BA20_all_Lall_crown_mean[5], BA20A_20B_fundus_mean[5], BA36_Lall_crown_mean[5]]



barWidth = 0.65

ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)

plt.bar(ind, bar_LI, color='#C783B3', edgecolor='white', width=barWidth, label='Layer I', alpha=0.90, bottom=r5) #, yerr=bar_LI_std)
plt.bar(ind, bar_LII, color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=r4) #, yerr=bar_LII_std)
plt.bar(ind, bar_LIII, color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=0.90, bottom=r3) #, yerr=bar_LIII_std)
plt.bar(ind, bar_LIV, color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2) #, yerr=bar_LIV_std)
plt.bar(ind, bar_LV, color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=r1) #, yerr=bar_LV_std)
plt.bar(ind, bar_LVI, color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90) #, yerr=bar_LVI_std)

plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.xticks(ind, ['BA22\ncrown', 'BA22_21\nfundus', 'BA21\ncrown', 'BA21_20\nfundus', 'BA20\ncrown', 'BA20_20\nfundus', 'BA36\ncrown'], fontsize=11, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=15, fontweight='bold')
plt.yticks(np.arange(0, 1.6, 0.2)) #yaxis points
#plt.title('Segmented bar graph showing the laminar layers of the crown and fundus in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 7.5})
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_relative_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_relative_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_relative_long_dpi100.png')

#plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_notitle.png', dpi=1000)

#plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_notitle_yerr.png', dpi=1000)

plt.show()


#CROWN AND FUNDUS - mixed groups with the same colour - ABSOLUTE
#segmented bar graph

bar_LI = [df_list_crown_absolute_BA22[0], df_list_fundus_absolute_BA21_22[0], df_list_crown_absolute_BA21[0], df_list_fundus_absolute_BA20B_21[0], df_list_crown_absolute_BA20_all[0], df_list_fundus_absolute_BA20A_20B[0], df_list_crown_absolute_BA36[0]]
#print("bar_LI = ", bar_LI)

bar_LII = [df_list_crown_absolute_BA22[1], df_list_fundus_absolute_BA21_22[1], df_list_crown_absolute_BA21[1], df_list_fundus_absolute_BA20B_21[1], df_list_crown_absolute_BA20_all[1], df_list_fundus_absolute_BA20A_20B[1], df_list_crown_absolute_BA36[1]]

bar_LIII = [df_list_crown_absolute_BA22[2], df_list_fundus_absolute_BA21_22[2], df_list_crown_absolute_BA21[2], df_list_fundus_absolute_BA20B_21[2], df_list_crown_absolute_BA20_all[2], df_list_fundus_absolute_BA20A_20B[2], df_list_crown_absolute_BA36[2]]

bar_LIV = [df_list_crown_absolute_BA22[3], df_list_fundus_absolute_BA21_22[3], df_list_crown_absolute_BA21[3], df_list_fundus_absolute_BA20B_21[3], df_list_crown_absolute_BA20_all[3], df_list_fundus_absolute_BA20A_20B[3], df_list_crown_absolute_BA36[3]]

bar_LV = [df_list_crown_absolute_BA22[4], df_list_fundus_absolute_BA21_22[4], df_list_crown_absolute_BA21[4], df_list_fundus_absolute_BA20B_21[4], df_list_crown_absolute_BA20_all[4], df_list_fundus_absolute_BA20A_20B[4], df_list_crown_absolute_BA36[4]]

bar_LVI = [df_list_crown_absolute_BA22[5], df_list_fundus_absolute_BA21_22[5], df_list_crown_absolute_BA21[5], df_list_fundus_absolute_BA20B_21[5], df_list_crown_absolute_BA20_all[5], df_list_fundus_absolute_BA20A_20B[5], df_list_crown_absolute_BA36[5]]

barWidth = 0.65

ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)

plt.bar(ind, bar_LI, color='#C783B3', edgecolor='white', width=barWidth, label='Layer I', alpha=0.90, bottom=r5) #, yerr=bar_LI_std)
plt.bar(ind, bar_LII, color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=r4) #, yerr=bar_LII_std)
plt.bar(ind, bar_LIII, color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=0.90, bottom=r3) #, yerr=bar_LIII_std)
plt.bar(ind, bar_LIV, color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2) #, yerr=bar_LIV_std)
plt.bar(ind, bar_LV, color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=r1) #, yerr=bar_LV_std)
plt.bar(ind, bar_LVI, color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)

plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.xticks(ind, ['BA22\ncrown', 'BA22_21\nfundus', 'BA21\ncrown', 'BA21_20\nfundus', 'BA20\ncrown', 'BA20_20\nfundus', 'BA36\ncrown'], fontsize=11, fontname="serif")
plt.ylabel("Absolute layer thickness (mm)", fontname="serif", fontsize=15, fontweight='bold')
plt.yticks(np.arange(0, 4.7, 0.5)) #yaxis points
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 7.5})
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_absolute_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_absolute_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_absolute_long_dpi100.png')

plt.show()


#VON ECONOMO DATA GRAPH - ABSOLUTE
#segmented bar graph

bar_LI = [VE_V1_OB_absolute_6a_plus_6b_T1[0], VE_A1_TC_absolute_6a_plus_6b_T1[0], VE_S1_PC_absolute_6a_plus_6b_T1[0], VE_association_cortex_TE_absolute_6a_plus_6b_T1[0]]
#print("bar_LI = ", bar_LI)

bar_LII = [VE_V1_OB_absolute_6a_plus_6b_T1[1], VE_A1_TC_absolute_6a_plus_6b_T1[1], VE_S1_PC_absolute_6a_plus_6b_T1[1], VE_association_cortex_TE_absolute_6a_plus_6b_T1[1]]

bar_LIII = [VE_V1_OB_absolute_6a_plus_6b_T1[2], VE_A1_TC_absolute_6a_plus_6b_T1[2], VE_S1_PC_absolute_6a_plus_6b_T1[2], VE_association_cortex_TE_absolute_6a_plus_6b_T1[2]]

bar_LIV = [VE_V1_OB_absolute_6a_plus_6b_T1[3], VE_A1_TC_absolute_6a_plus_6b_T1[3], VE_S1_PC_absolute_6a_plus_6b_T1[3], VE_association_cortex_TE_absolute_6a_plus_6b_T1[3]]

bar_LV = [VE_V1_OB_absolute_6a_plus_6b_T1[4], VE_A1_TC_absolute_6a_plus_6b_T1[4], VE_S1_PC_absolute_6a_plus_6b_T1[4], VE_association_cortex_TE_absolute_6a_plus_6b_T1[4]]

bar_LVI = [VE_V1_OB_absolute_6a_plus_6b_T1[5], VE_A1_TC_absolute_6a_plus_6b_T1[5], VE_S1_PC_absolute_6a_plus_6b_T1[5], VE_association_cortex_TE_absolute_6a_plus_6b_T1[5]]

barWidth = 0.42

ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)

plt.bar(ind, bar_LI, color='#fe7171', edgecolor='black', width=barWidth, label='Layer I', alpha=0.80, bottom=r5) #, yerr=bar_LI_std)
plt.bar(ind, bar_LII, color='#ffb871', edgecolor='black', width=barWidth, label='Layer II', alpha=0.80, bottom=r4) #, yerr=bar_LII_std)
plt.bar(ind, bar_LIII, color='#f3f46c', edgecolor='black', width=barWidth, label='Layer III', alpha=0.75, bottom=r3) #, yerr=bar_LIII_std)
plt.bar(ind, bar_LIV, color='#71fe71', edgecolor='black', width=barWidth, label='Layer IV', alpha=0.75, bottom=r2) #, yerr=bar_LIV_std)
plt.bar(ind, bar_LV, color='#6ffefe', edgecolor='black', width=barWidth, label='Layer V', alpha=0.75, bottom=r1) #, yerr=bar_LV_std)
plt.bar(ind, bar_LVI, color='#6f6ffe', edgecolor='black', width=barWidth, label='Layer VI', alpha=0.75)

plt.xlabel('Region', fontname="serif", fontsize=14, fontweight='bold')
plt.xticks(ind, ['Primary\nvisual cortex\n(OB)', 'Primary\nauditory cortex\n(TC)', 'Primary\nsomatosensory\ncortex\n(PC)', 'Temporal\nneocortex\n(TE)'], fontsize=11, fontname="serif")

plt.ylabel("Absolute layer thickness (mm)", fontname="serif", fontsize=14, fontweight='bold')
plt.yticks(np.arange(0, 5.2, 0.5)) #yaxis points
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 7})
plt.tight_layout()
plt.savefig('VE_data_seg_chart_mixed_group_samecolour_absolute_dpi1000.png', dpi=1000)
plt.savefig('VE_data_seg_chart_mixed_group_samecolour_absolute_dpi300.png', dpi=300)
plt.savefig('VE_data_seg_chart_mixed_group_samecolour_absolute_dpi100.png')


plt.show()


#VIOLIN PLOT - Layer 1

BA22_crown_allcase_rel = []
BA21_22_fundus_allcase_rel = []
BA21_crown_allcase_rel = []
BA20B_21_fundus_allcase_rel = []
BA20_all_crown_allcase_rel = []
BA20A_20B_fundus_allcase_rel = []
BA36_crown_allcase_rel = []

BA22_crown_allcase_rel_info = []
BA21_22_fundus_allcase_rel_info = []
BA21_crown_allcase_rel_info = []
BA20B_21_fundus_allcase_rel_info = []
BA20_all_crown_allcase_rel_info = []
BA20A_20B_fundus_allcase_rel_info = []
BA36_crown_allcase_rel_info = []

for info in case_info_crown:
    if "BA22" in info:
        BA22_crown_allcase_rel_info.append(info)
        i = case_info_crown.index(info)
        BA22_data = BA22_crown_allcase_rel.append(df_list_crown[i])
    elif "BA21" in info:
        BA21_crown_allcase_rel_info.append(info)
        i = case_info_crown.index(info)
        BA21_data = BA21_crown_allcase_rel.append(df_list_crown[i])
    elif "BA20_all" in info:
        BA20_all_crown_allcase_rel_info.append(info)
        i = case_info_crown.index(info)
        BA20_all_data = BA20_all_crown_allcase_rel.append(df_list_crown[i])
    elif "BA36" in info:
        BA36_crown_allcase_rel_info.append(info)
        i = case_info_crown.index(info)
        BA36_data = BA36_crown_allcase_rel.append(df_list_crown[i])

for info in case_info_fundus:
    if "BA21_22" in info:
        BA21_22_fundus_allcase_rel_info.append(info)
        i = case_info_fundus.index(info)
        BA21_22_data = BA21_22_fundus_allcase_rel.append(df_list_fundus[i])
    elif "BA20B_21" in info:
        BA20B_21_fundus_allcase_rel_info.append(info)
        i = case_info_fundus.index(info)
        BA20B_21_data = BA20B_21_fundus_allcase_rel.append(df_list_fundus[i])
    elif "BA20A_20B" in info:
            BA20A_20B_fundus_allcase_rel_info.append(info)
            i = case_info_fundus.index(info)
            BA20A_20B_data = BA20A_20B_fundus_allcase_rel.append(df_list_fundus[i])


#print("BA21_22_fundus_allcase_rel_info = ", BA21_22_fundus_allcase_rel_info)
#print("BA21_22_fundus_allcase_rel = ", BA21_22_fundus_allcase_rel)

#layer 1 values - all case
BA22_crown_allcase_rel_L1 = [i[0] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L1 = [i[0] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L1 = [i[0] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L1 = [i[0] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L1 = [i[0] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L1 = [i[0] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L1 = [i[0] for i in BA36_crown_allcase_rel]
#print("BA22_crown_allcase_rel_L1 = ", BA22_crown_allcase_rel_L1)
#print("BA22_crown_allcase_rel_info = ", BA22_crown_allcase_rel_info)

#layer 2 values - all case
BA22_crown_allcase_rel_L2 = [i[1] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L2 = [i[1] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L2 = [i[1] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L2 = [i[1] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L2 = [i[1] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L2 = [i[1] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L2 = [i[1] for i in BA36_crown_allcase_rel]

#layer 3 values - all case
BA22_crown_allcase_rel_L3 = [i[2] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L3 = [i[2] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L3 = [i[2] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L3 = [i[2] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L3 = [i[2] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L3 = [i[2] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L3 = [i[2] for i in BA36_crown_allcase_rel]

#layer 4 values - all case
BA22_crown_allcase_rel_L4 = [i[3] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L4 = [i[3] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L4 = [i[3] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L4 = [i[3] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L4 = [i[3] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L4 = [i[3] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L4 = [i[3] for i in BA36_crown_allcase_rel]

#layer 5 values - all case
BA22_crown_allcase_rel_L5 = [i[4] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L5 = [i[4] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L5 = [i[4] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L5 = [i[4] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L5 = [i[4] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L5 = [i[4] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L5 = [i[4] for i in BA36_crown_allcase_rel]

#layer 6 values - all case
BA22_crown_allcase_rel_L6 = [i[5] for i in BA22_crown_allcase_rel]
BA21_22_fundus_allcase_rel_L6 = [i[5] for i in BA21_22_fundus_allcase_rel]
BA21_crown_allcase_rel_L6 = [i[5] for i in BA21_crown_allcase_rel]
BA20B_21_fundus_allcase_rel_L6 = [i[5] for i in BA20B_21_fundus_allcase_rel]
BA20_all_crown_allcase_rel_L6 = [i[5] for i in BA20_all_crown_allcase_rel]
BA20A_20B_fundus_allcase_rel_L6 = [i[5] for i in BA20A_20B_fundus_allcase_rel]
BA36_crown_allcase_rel_L6 = [i[5] for i in BA36_crown_allcase_rel]

#lists
df_violin_list_L1 = [BA22_crown_allcase_rel_L1, BA21_22_fundus_allcase_rel_L1, BA21_crown_allcase_rel_L1, BA20B_21_fundus_allcase_rel_L1, BA20_all_crown_allcase_rel_L1, BA20A_20B_fundus_allcase_rel_L1, BA36_crown_allcase_rel_L1]

df_violin_list_L2 = [BA22_crown_allcase_rel_L2, BA21_22_fundus_allcase_rel_L2, BA21_crown_allcase_rel_L2, BA20B_21_fundus_allcase_rel_L2, BA20_all_crown_allcase_rel_L2, BA20A_20B_fundus_allcase_rel_L2, BA36_crown_allcase_rel_L2]

df_violin_list_L3 = [BA22_crown_allcase_rel_L3, BA21_22_fundus_allcase_rel_L3, BA21_crown_allcase_rel_L3, BA20B_21_fundus_allcase_rel_L3, BA20_all_crown_allcase_rel_L3, BA20A_20B_fundus_allcase_rel_L3, BA36_crown_allcase_rel_L3]

df_violin_list_L4 = [BA22_crown_allcase_rel_L4, BA21_22_fundus_allcase_rel_L4, BA21_crown_allcase_rel_L4, BA20B_21_fundus_allcase_rel_L4, BA20_all_crown_allcase_rel_L4, BA20A_20B_fundus_allcase_rel_L4, BA36_crown_allcase_rel_L4]

df_violin_list_L5 = [BA22_crown_allcase_rel_L5, BA21_22_fundus_allcase_rel_L5, BA21_crown_allcase_rel_L5, BA20B_21_fundus_allcase_rel_L5, BA20_all_crown_allcase_rel_L5, BA20A_20B_fundus_allcase_rel_L5, BA36_crown_allcase_rel_L5]

df_violin_list_L6 = [BA22_crown_allcase_rel_L6, BA21_22_fundus_allcase_rel_L6, BA21_crown_allcase_rel_L6, BA20B_21_fundus_allcase_rel_L6, BA20_all_crown_allcase_rel_L6, BA20A_20B_fundus_allcase_rel_L6, BA36_crown_allcase_rel_L6]
#print("df_violin_list_L1 = ", df_violin_list_L1)


#VIOLIN PLOT DATA
df_violin_info = [BA22_crown_allcase_rel_info, BA21_22_fundus_allcase_rel_info, BA21_crown_allcase_rel_info, BA20B_21_fundus_allcase_rel_info, BA20_all_crown_allcase_rel_info, BA20A_20B_fundus_allcase_rel_info, BA36_crown_allcase_rel_info]
#print("df_violin_info = ", df_violin_info)


#Layer 1
df_violin_L1 = pd.DataFrame(np.array([i for variable in df_violin_list_L1 for i in variable]), columns=['Layer1_rel_thick'])
#print("df_violin_L1 = ", df_violin_L1)

df_violin_case_info = df_violin_L1.insert(0, "Case_info", [i for case in df_violin_info for i in case])
#print(df_violin_L1)

#Layer 2
df_violin_L2 = pd.DataFrame(np.array([i for variable in df_violin_list_L2 for i in variable]), columns=['Layer2_rel_thick'])
#print("df_violin_L2 = ", df_violin_L2)

df_violin_case_info = df_violin_L2.insert(0, "Case_info", [i for case in df_violin_info for i in case])
#print(df_violin_L2)

#Layer 3
df_violin_L3 = pd.DataFrame(np.array([i for variable in df_violin_list_L3 for i in variable]), columns=['Layer3_rel_thick'])
#print("df_violin_L3 = ", df_violin_L3)

df_violin_case_info = df_violin_L3.insert(0, "Case_info", [i for case in df_violin_info for i in case])
#print(df_violin_L3)

#Layer 4
df_violin_L4 = pd.DataFrame(np.array([i for variable in df_violin_list_L4 for i in variable]), columns=['Layer4_rel_thick'])
#print("df_violin_L4 = ", df_violin_L4)

df_violin_case_info = df_violin_L4.insert(0, "Case_info", [i for case in df_violin_info for i in case])

#Layer 5
df_violin_L5 = pd.DataFrame(np.array([i for variable in df_violin_list_L5 for i in variable]), columns=['Layer5_rel_thick'])
#print("df_violin_L5 = ", df_violin_L5)

df_violin_case_info = df_violin_L5.insert(0, "Case_info", [i for case in df_violin_info for i in case])

#Layer 6
df_violin_L6 = pd.DataFrame(np.array([i for variable in df_violin_list_L6 for i in variable]), columns=['Layer6_rel_thick'])
#print("df_violin_L6 = ", df_violin_L6)

df_violin_case_info = df_violin_L6.insert(0, "Case_info", [i for case in df_violin_info for i in case])

#sys.exit()

df_violin_ind_var_info = []
for variable in df_violin_info:
    for i in variable:
        if "BA22" in i:
            df_violin_ind_var_info.append("BA22")
        elif "BA21_22" in i:
            df_violin_ind_var_info.append("BA21_22")
        elif "BA21" in i:
            df_violin_ind_var_info.append("BA21")
        elif "BA20B_21" in i:
            df_violin_ind_var_info.append("BA20B_21")
        elif "BA20_all" in i:
            df_violin_ind_var_info.append("BA20_all")
        elif "BA20A_20B" in i:
            df_violin_ind_var_info.append("BA20A_20B")
        elif "BA36" in i:
            df_violin_ind_var_info.append("BA36")
#print("df_violin_ind_var_info = ", df_violin_ind_var_info)

# covariate info
# sex info
case_female_lst = ["I27", "I30", "I32", "I33"]
case_male_lst = ["I25", "I31", "I34", "I40", "I42", "I44", "I47", "I49"]
df_violin_sex_info = []
for variable in df_violin_info:
    for i in variable:
        if i[:3] in case_female_lst:
            df_violin_sex_info.append("F")
        elif i[:3] in case_male_lst:
            df_violin_sex_info.append("M")

# BA covar input as number
df_violin_ba_num = []
for variable in df_violin_info:
    for i in variable:
        if "BA22" in i:
            df_violin_ba_num.append(22)
        elif "BA21_22" in i:
            df_violin_ba_num.append(2122)
        elif "BA21" in i:
            df_violin_ba_num.append(21)
        elif "BA20B_21" in i:
            df_violin_ba_num.append(2021)
        elif "BA20_all" in i:
            df_violin_ba_num.append(20)
        elif "BA20A_20B" in i:
            df_violin_ba_num.append(2020)
        elif "BA36" in i:
            df_violin_ba_num.append(36)

# dictionary with age and Braak and Braak coovariate info
case_age_diag_dict = {
'I25': [63, "NC"], 'I27': [86, "BBIII"], 'I30': [43, "NC"], 'I31': [80, "BBIII"],\
'I32': [45, "NC"], 'I33': [84, "BBI"], 'I34': [73, "BBI"], 'I40': [68, "BBI"],\
'I42': [58, "NC"], 'I44': [82, "BBII"], 'I47': [49, "NC"], 'I49': [67, "NC"] }

df_violin_age_info = []
df_violin_bb_info = []
for variable in df_violin_info:
    for i in variable:
        df_violin_age_info.append(case_age_diag_dict[i[:3]][0])
        df_violin_bb_info.append(case_age_diag_dict[i[:3]][1])


#Layer 1
df_violin_L1_BA_info = df_violin_L1.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L1.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L1.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L1.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L1.insert(6, "Diagnosis", [i for i in df_violin_bb_info])
# print(df_violin_L1)

# actual ancova happening here
layer1_ancova_sex = ancova(data=df_violin_L1, dv='Layer1_rel_thick', covar='BA_num', \
between='Sex')
layer1_ancova_age = ancova(data=df_violin_L1, dv='Layer1_rel_thick', covar='BA_num', \
between='Age')
layer1_ancova_diag = ancova(data=df_violin_L1, dv='Layer1_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer1 ANCOVA\n", layer1_ancova_sex, "\n", layer1_ancova_age, "\n", layer1_ancova_diag, "\n")

#Layer 2
df_violin_L2_BA_info = df_violin_L2.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L2.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L2.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L2.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L2.insert(6, "Diagnosis", [i for i in df_violin_bb_info])
# print(df_violin_L2)

# actual ancova happening here
layer2_ancova_sex = ancova(data=df_violin_L2, dv='Layer2_rel_thick', covar='BA_num', \
between='Sex')
layer2_ancova_age = ancova(data=df_violin_L2, dv='Layer2_rel_thick', covar='BA_num', \
between='Age')
layer2_ancova_diag = ancova(data=df_violin_L2, dv='Layer2_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer2 ANCOVA\n", layer2_ancova_sex, "\n", layer2_ancova_age, "\n", layer2_ancova_diag, "\n")

#Layer 3
df_violin_L3_BA_info = df_violin_L3.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L3.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L3.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L3.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L3.insert(6, "Diagnosis", [i for i in df_violin_bb_info])

# actual ancova happening here
layer3_ancova_sex = ancova(data=df_violin_L3, dv='Layer3_rel_thick', covar='BA_num', \
between='Sex')
layer3_ancova_age = ancova(data=df_violin_L3, dv='Layer3_rel_thick', covar='BA_num', \
between='Age')
layer3_ancova_diag = ancova(data=df_violin_L3, dv='Layer3_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer3 ANCOVA\n", layer3_ancova_sex, "\n", layer3_ancova_age, "\n", layer3_ancova_diag, "\n")

#Layer 4
df_violin_L4_BA_info = df_violin_L4.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L4.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L4.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L4.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L4.insert(6, "Diagnosis", [i for i in df_violin_bb_info])

# actual ancova happening here
layer4_ancova_sex = ancova(data=df_violin_L4, dv='Layer4_rel_thick', covar='BA_num', \
between='Sex')
layer4_ancova_age = ancova(data=df_violin_L4, dv='Layer4_rel_thick', covar='BA_num', \
between='Age')
layer4_ancova_diag = ancova(data=df_violin_L4, dv='Layer4_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer4 ANCOVA\n", layer4_ancova_sex, "\n", layer4_ancova_age, "\n", layer4_ancova_diag, "\n")

#Layer 5
df_violin_L5_BA_info = df_violin_L5.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L5.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L5.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L5.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L5.insert(6, "Diagnosis", [i for i in df_violin_bb_info])

# actual ancova happening here
layer5_ancova_sex = ancova(data=df_violin_L5, dv='Layer5_rel_thick', covar='BA_num', \
between='Sex')
layer5_ancova_age = ancova(data=df_violin_L5, dv='Layer5_rel_thick', covar='BA_num', \
between='Age')
layer5_ancova_diag = ancova(data=df_violin_L5, dv='Layer5_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer5 ANCOVA\n", layer5_ancova_sex, "\n", layer5_ancova_age, "\n", layer5_ancova_diag, "\n")

#Layer 6
df_violin_L6_BA_info = df_violin_L6.insert(2, "BA_info", [i for i in df_violin_ind_var_info])
df_violin_L6.insert(3, "Sex", [i for i in df_violin_sex_info])
df_violin_L6.insert(4, "BA_num", [i for i in df_violin_ba_num])
df_violin_L6.insert(5, "Age", [i for i in df_violin_age_info])
df_violin_L6.insert(6, "Diagnosis", [i for i in df_violin_bb_info])

# actual ancova happening here
layer6_ancova_sex = ancova(data=df_violin_L6, dv='Layer6_rel_thick', covar='BA_num', \
between='Sex')
layer6_ancova_age = ancova(data=df_violin_L6, dv='Layer6_rel_thick', covar='BA_num', \
between='Age')
layer6_ancova_diag = ancova(data=df_violin_L6, dv='Layer6_rel_thick', covar='BA_num', \
between='Diagnosis')
print("Layer6 ANCOVA\n", layer6_ancova_sex, "\n", layer6_ancova_age, "\n", layer6_ancova_diag, "\n")

df_violin_L1.to_excel(writer, index=False, sheet_name='df_violin_L1')
writer.save()


#VIOLIN PLOTS
#Layer 1
sns.violinplot(x="BA_info", y="Layer1_rel_thick", data=df_violin_L1, color='#C783B3')
plt.xticks(np.arange((len(df_violin_list_L1))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 1)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer1_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer1_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer1_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer1_long_dpi100.png')

plt.show()

#Layer 2
sns.violinplot(x="BA_info", y="Layer2_rel_thick", data=df_violin_L2, color='#DB7093')
plt.xticks(np.arange((len(df_violin_list_L2))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 2)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer2_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer2_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer2_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer2_long_dpi100.png')

plt.show()

#Layer 3
sns.violinplot(x="BA_info", y="Layer3_rel_thick", data=df_violin_L3, color='#993366')
plt.xticks(np.arange((len(df_violin_list_L3))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 3)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer3_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer3_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer3_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer3_long_dpi100.png')

plt.show()

#Layer 4
sns.violinplot(x="BA_info", y="Layer4_rel_thick", data=df_violin_L4, color='#900C3F')
plt.xticks(np.arange((len(df_violin_list_L4))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 4)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer4_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer4_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer4_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer4_long_dpi100.png')

plt.show()

#Layer 5
ax = sns.violinplot(x="BA_info", y="Layer5_rel_thick", data=df_violin_L5, color='#660033')
# lower opacity of the colour on the graph
for violin in ax.collections[::2]:
    violin.set_alpha(0.95)

plt.xticks(np.arange((len(df_violin_list_L5))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 5)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer5_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer5_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer5_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer5_long_dpi100.png')

plt.show()

#Layer 6
ax = sns.violinplot(x="BA_info", y="Layer6_rel_thick", data=df_violin_L6, color='#400120')
# lower opacity of the colour on the graph
for violin in ax.collections[::2]:
    violin.set_alpha(0.92)

# #use this to get a gradation of colour from darkest to lightest
# for violin, alpha in zip(ax.collections[::2], [0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65]) :
#     violin.set_alpha(alpha)
#sns.desaturate('#330019', 0.2)
plt.xticks(np.arange((len(df_violin_list_L6))), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=11, fontname="serif")
plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.ylabel("Relative thickness (Layer 6)", fontname="serif", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('BA_all_crown_fundus_violin_plot_layer6_long_dpi2000.png', dpi=2000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer6_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_violin_plot_layer6_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_violin_plot_layer6_long_dpi100.png')

plt.show()


# sys.exit()

#BOXPLOTS
#layer 1
plt.boxplot(df_violin_list_L1)
plt.xticks(np.arange(1, (len(df_violin_list_L1)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 1 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer1.png', dpi=1000)
plt.show()

#layer 2
plt.boxplot(df_violin_list_L2)
#plt.boxplot([BA22_L2_crown, BA21_22_L2_fundus, BA21_L2_crown, BA20B_21_L2_fundus, BA20_all_L2_crown, BA20A_20B_L2_fundus, BA36_L2_crown])
plt.xticks(np.arange(1, (len(df_violin_list_L2)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 2 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer2.png', dpi=1000)
plt.show()

#layer 3
plt.boxplot(df_violin_list_L3)
plt.xticks(np.arange(1, (len(df_violin_list_L3)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 3 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer3.png', dpi=1000)
plt.show()

#layer 4
plt.boxplot(df_violin_list_L4)
plt.xticks(np.arange(1, (len(df_violin_list_L4)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 4 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer4.png', dpi=1000)
plt.show()

#layer 5
plt.boxplot(df_violin_list_L5)
plt.xticks(np.arange(1, (len(df_violin_list_L5)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 5 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer5.png', dpi=1000)
plt.show()

#layer 6
plt.boxplot(df_violin_list_L6)
plt.xticks(np.arange(1, (len(df_violin_list_L6)+1)), ["BA22 \ncrown", "BA22_21 \nfundus", "BA21 \ncrown", "BA21_20 \nfundus", "BA20 \ncrown", "BA20_20 \nfundus", "BA36 \ncrown"], fontsize=7)
plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.title("Boxplots of relative layer thickness of layer 6 in all BAs", fontsize=10)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_boxplot_layer6.png', dpi=1000)
plt.show()


# MALE and FEMALE - same colour
#SEGMENTED BAR GRAPH

bar_LI = [BA22_Lall_crown_mean_female[0], BA22_Lall_crown_mean_male[0], BA21_Lall_crown_mean_female[0], BA21_Lall_crown_mean_male[0], BA20_all_Lall_crown_mean_female[0], BA20_all_Lall_crown_mean_male[0], BA36_Lall_crown_mean_female[0], BA36_Lall_crown_mean_male[0]]

bar_LII = [BA22_Lall_crown_mean_female[1], BA22_Lall_crown_mean_male[1], BA21_Lall_crown_mean_female[1], BA21_Lall_crown_mean_male[1], BA20_all_Lall_crown_mean_female[1], BA20_all_Lall_crown_mean_male[1], BA36_Lall_crown_mean_female[1], BA36_Lall_crown_mean_male[1]]

bar_LIII = [BA22_Lall_crown_mean_female[2], BA22_Lall_crown_mean_male[2], BA21_Lall_crown_mean_female[2], BA21_Lall_crown_mean_male[2], BA20_all_Lall_crown_mean_female[2], BA20_all_Lall_crown_mean_male[2], BA36_Lall_crown_mean_female[2], BA36_Lall_crown_mean_male[2]]

bar_LIV = [BA22_Lall_crown_mean_female[3], BA22_Lall_crown_mean_male[3], BA21_Lall_crown_mean_female[3], BA21_Lall_crown_mean_male[3], BA20_all_Lall_crown_mean_female[3], BA20_all_Lall_crown_mean_male[3], BA36_Lall_crown_mean_female[3], BA36_Lall_crown_mean_male[3]]

bar_LV = [BA22_Lall_crown_mean_female[4], BA22_Lall_crown_mean_male[4], BA21_Lall_crown_mean_female[4], BA21_Lall_crown_mean_male[4], BA20_all_Lall_crown_mean_female[4], BA20_all_Lall_crown_mean_male[4], BA36_Lall_crown_mean_female[4], BA36_Lall_crown_mean_male[4]]

bar_LVI = [BA22_Lall_crown_mean_female[5], BA22_Lall_crown_mean_male[5], BA21_Lall_crown_mean_female[5], BA21_Lall_crown_mean_male[5], BA20_all_Lall_crown_mean_female[5], BA20_all_Lall_crown_mean_male[5], BA36_Lall_crown_mean_female[5], BA36_Lall_crown_mean_male[5]]


barWidth = 0.65

ind = np.arange(len(bar_LI))

#bar height
r1 = bar_LVI
r2 = np.array(bar_LVI) + np.array(bar_LV)
r3 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV)
r4 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII)
r5 = np.array(bar_LVI) + np.array(bar_LV) + np.array(bar_LIV) + np.array(bar_LIII) + np.array(bar_LII)

plt.bar(ind, bar_LI, color='#5F9EA0', edgecolor='white', width=barWidth, label='Layer I', alpha=0.90, bottom=r5)
plt.bar(ind, bar_LII, color='#1BA7AC', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=r4)
plt.bar(ind, bar_LIII, color='#207979', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=r3)
plt.bar(ind, bar_LIV, color='#06697D', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2)
plt.bar(ind, bar_LV, color='#09414A', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=r1)
plt.bar(ind, bar_LVI, color='#001414', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)

bar_LVI = [BA22_Lall_crown_mean_female[5], BA22_Lall_crown_mean_male[5], BA21_Lall_crown_mean_female[5], BA21_Lall_crown_mean_male[5], BA20B_Lall_crown_mean_female[5], BA20B_Lall_crown_mean_male[5], BA20A_Lall_crown_mean_female[5], BA20A_Lall_crown_mean_male[5]]

plt.xlabel('Region', fontname="serif", fontsize=15, fontweight='bold')
plt.xticks(ind, ['BA22\ncrown\nfemale', 'BA22\ncrown\nmale', 'BA21\ncrown\nfemale', 'BA21\ncrown\nmale', 'BA20\ncrown\nfemale', 'BA20\ncrown\nmale', 'BA36\ncrown\nfemale', 'BA36\ncrown\nmale'], fontsize=11, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=15, fontweight='bold')
plt.yticks(np.arange(0, 1.6, 0.2)) #yaxis points
#plt.title('Segmented bar graph showing the laminar layers of the crown in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 7.2})
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_sex.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_sex_long_dpi1000.png', dpi=1000)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_sex_long_dpi300.png', dpi=300)
plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_samecolour_sex_long_dpi100.png')

plt.show()

# sys.exit()
# MALE and FEMALE - mixed group diff colour
#segmented bar graph

barWidth = 0.65

ind1 = 0
ind2 = 1
ind3 = 2
ind4 = 3
ind5 = 4
ind6 = 5
ind7 = 6
ind8 = 7


#bar height
#FEMALE
BA22_r1_female = BA22_Lall_crown_mean_female[5]
BA22_r2_female = np.array(BA22_Lall_crown_mean_female[5]) + np.array(BA22_Lall_crown_mean_female[4])
BA22_r3_female = np.array(BA22_Lall_crown_mean_female[5]) + np.array(BA22_Lall_crown_mean_female[4]) + np.array(BA22_Lall_crown_mean_female[3])
BA22_r4_female = np.array(BA22_Lall_crown_mean_female[5]) + np.array(BA22_Lall_crown_mean_female[4]) + np.array(BA22_Lall_crown_mean_female[3]) + np.array(BA22_Lall_crown_mean_female[2])
BA22_r5_female = np.array(BA22_Lall_crown_mean_female[5]) + np.array(BA22_Lall_crown_mean_female[4]) + np.array(BA22_Lall_crown_mean_female[3]) + np.array(BA22_Lall_crown_mean_female[2]) + np.array(BA22_Lall_crown_mean_female[1])

BA21_r1_female = BA21_Lall_crown_mean_female[5]
BA21_r2_female = np.array(BA21_Lall_crown_mean_female[5]) + np.array(BA21_Lall_crown_mean_female[4])
BA21_r3_female = np.array(BA21_Lall_crown_mean_female[5]) + np.array(BA21_Lall_crown_mean_female[4]) + np.array(BA21_Lall_crown_mean_female[3])
BA21_r4_female = np.array(BA21_Lall_crown_mean_female[5]) + np.array(BA21_Lall_crown_mean_female[4]) + np.array(BA21_Lall_crown_mean_female[3]) + np.array(BA21_Lall_crown_mean_female[2])
BA21_r5_female = np.array(BA21_Lall_crown_mean_female[5]) + np.array(BA21_Lall_crown_mean_female[4]) + np.array(BA21_Lall_crown_mean_female[3]) + np.array(BA21_Lall_crown_mean_female[2]) + np.array(BA21_Lall_crown_mean_female[1])

BA20B_r1_female = BA20B_Lall_crown_mean_female[5]
BA20B_r2_female = np.array(BA20B_Lall_crown_mean_female[5]) + np.array(BA20B_Lall_crown_mean_female[4])
BA20B_r3_female = np.array(BA20B_Lall_crown_mean_female[5]) + np.array(BA20B_Lall_crown_mean_female[4]) + np.array(BA20B_Lall_crown_mean_female[3])
BA20B_r4_female = np.array(BA20B_Lall_crown_mean_female[5]) + np.array(BA20B_Lall_crown_mean_female[4]) + np.array(BA20B_Lall_crown_mean_female[3]) + np.array(BA20B_Lall_crown_mean_female[2])
BA20B_r5_female = np.array(BA20B_Lall_crown_mean_female[5]) + np.array(BA20B_Lall_crown_mean_female[4]) + np.array(BA20B_Lall_crown_mean_female[3]) + np.array(BA20B_Lall_crown_mean_female[2]) + np.array(BA20B_Lall_crown_mean_female[1])

BA20A_r1_female = BA20A_Lall_crown_mean_female[5]
BA20A_r2_female = np.array(BA20A_Lall_crown_mean_female[5]) + np.array(BA20A_Lall_crown_mean_female[4])
BA20A_r3_female = np.array(BA20A_Lall_crown_mean_female[5]) + np.array(BA20A_Lall_crown_mean_female[4]) + np.array(BA20A_Lall_crown_mean_female[3])
BA20A_r4_female = np.array(BA20A_Lall_crown_mean_female[5]) + np.array(BA20A_Lall_crown_mean_female[4]) + np.array(BA20A_Lall_crown_mean_female[3]) + np.array(BA20A_Lall_crown_mean_female[2])
BA20A_r5_female = np.array(BA20A_Lall_crown_mean_female[5]) + np.array(BA20A_Lall_crown_mean_female[4]) + np.array(BA20A_Lall_crown_mean_female[3]) + np.array(BA20A_Lall_crown_mean_female[2]) + np.array(BA20A_Lall_crown_mean_female[1])


#MALE
BA22_r1_male = BA22_Lall_crown_mean_male[5]
BA22_r2_male = np.array(BA22_Lall_crown_mean_male[5]) + np.array(BA22_Lall_crown_mean_male[4])
BA22_r3_male = np.array(BA22_Lall_crown_mean_male[5]) + np.array(BA22_Lall_crown_mean_male[4]) + np.array(BA22_Lall_crown_mean_male[3])
BA22_r4_male = np.array(BA22_Lall_crown_mean_male[5]) + np.array(BA22_Lall_crown_mean_male[4]) + np.array(BA22_Lall_crown_mean_male[3]) + np.array(BA22_Lall_crown_mean_male[2])
BA22_r5_male = np.array(BA22_Lall_crown_mean[5]) + np.array(BA22_Lall_crown_mean[4]) + np.array(BA22_Lall_crown_mean[3]) + np.array(BA22_Lall_crown_mean[2]) + np.array(BA22_Lall_crown_mean[1])

BA21_r1_male = BA21_Lall_crown_mean_male[5]
BA21_r2_male = np.array(BA21_Lall_crown_mean_male[5]) + np.array(BA21_Lall_crown_mean_male[4])
BA21_r3_male = np.array(BA21_Lall_crown_mean_male[5]) + np.array(BA21_Lall_crown_mean_male[4]) + np.array(BA21_Lall_crown_mean_male[3])
BA21_r4_male = np.array(BA21_Lall_crown_mean_male[5]) + np.array(BA21_Lall_crown_mean_male[4]) + np.array(BA21_Lall_crown_mean_male[3]) + np.array(BA21_Lall_crown_mean_male[2])
BA21_r5_male = np.array(BA21_Lall_crown_mean_male[5]) + np.array(BA21_Lall_crown_mean_male[4]) + np.array(BA21_Lall_crown_mean_male[3]) + np.array(BA21_Lall_crown_mean_male[2]) + np.array(BA21_Lall_crown_mean_male[1])

BA20B_r1_male = BA20B_Lall_crown_mean_male[5]
BA20B_r2_male = np.array(BA20B_Lall_crown_mean_male[5]) + np.array(BA20B_Lall_crown_mean_male[4])
BA20B_r3_male = np.array(BA20B_Lall_crown_mean_male[5]) + np.array(BA20B_Lall_crown_mean_male[4]) + np.array(BA20B_Lall_crown_mean_male[3])
BA20B_r4_male = np.array(BA20B_Lall_crown_mean_male[5]) + np.array(BA20B_Lall_crown_mean_male[4]) + np.array(BA20B_Lall_crown_mean_male[3]) + np.array(BA20B_Lall_crown_mean_male[2])
BA20B_r5_male = np.array(BA20B_Lall_crown_mean_male[5]) + np.array(BA20B_Lall_crown_mean_male[4]) + np.array(BA20B_Lall_crown_mean_male[3]) + np.array(BA20B_Lall_crown_mean_male[2]) + np.array(BA20B_Lall_crown_mean_male[1])

BA20A_r1_male = BA20A_Lall_crown_mean_male[5]
BA20A_r2_male = np.array(BA20A_Lall_crown_mean_male[5]) + np.array(BA20A_Lall_crown_mean_male[4])
BA20A_r3_male = np.array(BA20A_Lall_crown_mean_male[5]) + np.array(BA20A_Lall_crown_mean_male[4]) + np.array(BA20A_Lall_crown_mean_male[3])
BA20A_r4_male = np.array(BA20A_Lall_crown_mean_male[5]) + np.array(BA20A_Lall_crown_mean_male[4]) + np.array(BA20A_Lall_crown_mean_male[3]) + np.array(BA20A_Lall_crown_mean_male[2])
BA20A_r5_male = np.array(BA20A_Lall_crown_mean_male[5]) + np.array(BA20A_Lall_crown_mean_male[4]) + np.array(BA20A_Lall_crown_mean_male[3]) + np.array(BA20A_Lall_crown_mean_male[2]) + np.array(BA20A_Lall_crown_mean_male[1])


#FEMALE
#Layer 1
plt.bar(ind1, BA22_Lall_crown_mean_female[0], color='#5F9EA0', edgecolor='white', width=barWidth, label='Layer I female', alpha=0.90, bottom=BA22_r5_female)
plt.bar(ind3, BA21_Lall_crown_mean_female[0], color='#5F9EA0', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r5_female)
plt.bar(ind5, BA20B_Lall_crown_mean_female[0], color='#5F9EA0', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r5_female)
plt.bar(ind7, BA20A_Lall_crown_mean_female[0], color='#5F9EA0', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r5_female)

#Layer 2
plt.bar(ind1, BA22_Lall_crown_mean_female[1], color='#1BA7AC', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=BA22_r4_female)
plt.bar(ind3, BA21_Lall_crown_mean_female[1], color='#1BA7AC', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r4_female)
plt.bar(ind5, BA20B_Lall_crown_mean_female[1], color='#1BA7AC', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r4_female)
plt.bar(ind7, BA20A_Lall_crown_mean_female[1], color='#1BA7AC', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r4_female)

#Layer3
plt.bar(ind1, BA22_Lall_crown_mean_female[2], color='#207979', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=BA22_r3_female)
plt.bar(ind3, BA21_Lall_crown_mean_female[2], color='#207979', edgecolor='white', width=barWidth, alpha=1, bottom=BA21_r3_female)
plt.bar(ind5, BA20B_Lall_crown_mean_female[2], color='#207979', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_r3_female)
plt.bar(ind7, BA20A_Lall_crown_mean_female[2], color='#207979', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_r3_female)

#Layer4
plt.bar(ind1, BA22_Lall_crown_mean_female[3], color='#06697D', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=BA22_r2_female)
plt.bar(ind3, BA21_Lall_crown_mean_female[3], color='#06697D', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r2_female)
plt.bar(ind5, BA20B_Lall_crown_mean_female[3], color='#06697D', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r2_female)
plt.bar(ind7, BA20A_Lall_crown_mean_female[3], color='#06697D', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r2_female)

#Layer 5
plt.bar(ind1, BA22_Lall_crown_mean_female[4], color='#09414A', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=BA22_r1_female)
plt.bar(ind3, BA21_Lall_crown_mean_female[4], color='#09414A', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r1_female)
plt.bar(ind5, BA20B_Lall_crown_mean_female[4], color='#09414A', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r1_female)
plt.bar(ind7, BA20A_Lall_crown_mean_female[4], color='#09414A', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r1_female)

#Layer 6
plt.bar(ind1, BA22_Lall_crown_mean_female[5], color='#001414', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)
plt.bar(ind3, BA21_Lall_crown_mean_female[5], color='#001414', edgecolor='white', width=barWidth, alpha=0.90)
plt.bar(ind5, BA20B_Lall_crown_mean_female[5], color='#001414', edgecolor='white', width=barWidth, alpha=0.90)
plt.bar(ind7, BA20A_Lall_crown_mean_female[5], color='#001414', edgecolor='white', width=barWidth, alpha=0.90)


#MALE
#Layer 1
plt.bar(ind2, BA22_Lall_crown_mean_male[0], color='#D07979', edgecolor='white', width=barWidth, label='Layer I male', alpha=1, bottom=BA22_r5_male) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[0], color='#D07979', edgecolor='white', width=barWidth, alpha=1, bottom=BA21_r5_male)
plt.bar(ind6, BA20B_Lall_crown_mean_male[0], color='#D07979', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_r5_male)
plt.bar(ind8, BA20A_Lall_crown_mean_male[0], color='#D07979', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_r5_male)

#Layer 2
plt.bar(ind2, BA22_Lall_crown_mean_male[1], color='#EC5959', edgecolor='white', width=barWidth, label='Layer II', alpha=0.95, bottom=BA22_r4_male) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[1], color='#EC5959', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA21_r4_male)
plt.bar(ind6, BA20B_Lall_crown_mean_male[1], color='#EC5959', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA20B_r4_male)
plt.bar(ind8, BA20A_Lall_crown_mean_male[1], color='#EC5959', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA20A_r4_male)

#Layer 3
plt.bar(ind2, BA22_Lall_crown_mean_male[2], color='#A43E3E', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=BA22_r3_male) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[2], color='#A43E3E', edgecolor='white', width=barWidth, alpha=1, bottom=BA21_r3_male)
plt.bar(ind6, BA20B_Lall_crown_mean_male[2], color='#A43E3E', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_r3_male)
plt.bar(ind8, BA20A_Lall_crown_mean_male[2], color='#A43E3E', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_r3_male)

#Layer 4
plt.bar(ind2, BA22_Lall_crown_mean_male[3], color='#C10303', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.95, bottom=BA22_r2_male) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[3], color='#C10303', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA21_r2_male)
plt.bar(ind6, BA20B_Lall_crown_mean_male[3], color='#C10303', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA20B_r2_male)
plt.bar(ind8, BA20A_Lall_crown_mean_male[3], color='#C10303', edgecolor='white', width=barWidth, alpha=0.95, bottom=BA20A_r2_male)

#Layer 5
plt.bar(ind2, BA22_Lall_crown_mean_male[4], color='#800000', edgecolor='white', width=barWidth, label='Layer V', alpha=1, bottom=BA22_r1_male) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[4], color='#800000', edgecolor='white', width=barWidth, alpha=1, bottom=BA21_r1_male)
plt.bar(ind6, BA20B_Lall_crown_mean_male[4], color='#800000', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_r1_male)
plt.bar(ind8, BA20A_Lall_crown_mean_male[4], color='#800000', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_r1_male)

#Layer 6
plt.bar(ind2, BA22_Lall_crown_mean_male[5], color='#400404', edgecolor='white', width=barWidth, label='Layer VI', alpha=1) #6BC3C3
plt.bar(ind4, BA21_Lall_crown_mean_male[5], color='#400404', edgecolor='white', width=barWidth, alpha=1)
plt.bar(ind6, BA20B_Lall_crown_mean_male[5], color='#400404', edgecolor='white', width=barWidth, alpha=1)
plt.bar(ind8, BA20A_Lall_crown_mean_male[5], color='#400404', edgecolor='white', width=barWidth, alpha=1)


plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks(np.arange(8), ['BA22\ncrown female', 'BA22\ncrown male', 'BA21\ncrown female', 'BA21\ncrown male', 'BA20l\ncrown female', 'BA20l\ncrown male', 'BA20m\ncrown female', 'BA20m\ncrown male'], fontsize=6, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.yticks(np.arange(0, 1.3, 0.2)) #yaxis points
plt.title('Segmented bar graph showing the laminar layers of the crown in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 4.5}, ncol=2)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_diffcolour_sex.png', dpi=1000)
plt.show()


#CROWN AND FUNDUS - mixed groups with different colours
#segmented bar graph

barWidth = 0.65

ind1 = 0
ind2 = 1
ind3 = 2
ind4 = 3
ind5 = 4
ind6 = 5
ind7 = 6
ind8 = 7
ind9 = 8
ind10 = 9

#bar height
#CROWN
BA22_r1 = BA22_Lall_crown_mean[5]
BA22_r2 = np.array(BA22_Lall_crown_mean[5]) + np.array(BA22_Lall_crown_mean[4])
BA22_r3 = np.array(BA22_Lall_crown_mean[5]) + np.array(BA22_Lall_crown_mean[4]) + np.array(BA22_Lall_crown_mean[3])
BA22_r4 = np.array(BA22_Lall_crown_mean[5]) + np.array(BA22_Lall_crown_mean[4]) + np.array(BA22_Lall_crown_mean[3]) + np.array(BA22_Lall_crown_mean[2])
BA22_r5 = np.array(BA22_Lall_crown_mean[5]) + np.array(BA22_Lall_crown_mean[4]) + np.array(BA22_Lall_crown_mean[3]) + np.array(BA22_Lall_crown_mean[2]) + np.array(BA22_Lall_crown_mean[1])

BA21_r1 = BA21_Lall_crown_mean[5]
BA21_r2 = np.array(BA21_Lall_crown_mean[5]) + np.array(BA21_Lall_crown_mean[4])
BA21_r3 = np.array(BA21_Lall_crown_mean[5]) + np.array(BA21_Lall_crown_mean[4]) + np.array(BA21_Lall_crown_mean[3])
BA21_r4 = np.array(BA21_Lall_crown_mean[5]) + np.array(BA21_Lall_crown_mean[4]) + np.array(BA21_Lall_crown_mean[3]) + np.array(BA21_Lall_crown_mean[2])
BA21_r5 = np.array(BA21_Lall_crown_mean[5]) + np.array(BA21_Lall_crown_mean[4]) + np.array(BA21_Lall_crown_mean[3]) + np.array(BA21_Lall_crown_mean[2]) + np.array(BA21_Lall_crown_mean[1])

BA20B_r1 = BA20B_Lall_crown_mean[5]
BA20B_r2 = np.array(BA20B_Lall_crown_mean[5]) + np.array(BA20B_Lall_crown_mean[4])
BA20B_r3 = np.array(BA20B_Lall_crown_mean[5]) + np.array(BA20B_Lall_crown_mean[4]) + np.array(BA20B_Lall_crown_mean[3])
BA20B_r4 = np.array(BA20B_Lall_crown_mean[5]) + np.array(BA20B_Lall_crown_mean[4]) + np.array(BA20B_Lall_crown_mean[3]) + np.array(BA20B_Lall_crown_mean[2])
BA20B_r5 = np.array(BA20B_Lall_crown_mean[5]) + np.array(BA20B_Lall_crown_mean[4]) + np.array(BA20B_Lall_crown_mean[3]) + np.array(BA20B_Lall_crown_mean[2]) + np.array(BA20B_Lall_crown_mean[1])

BA20A_r1 = BA20A_Lall_crown_mean[5]
BA20A_r2 = np.array(BA20A_Lall_crown_mean[5]) + np.array(BA20A_Lall_crown_mean[4])
BA20A_r3 = np.array(BA20A_Lall_crown_mean[5]) + np.array(BA20A_Lall_crown_mean[4]) + np.array(BA20A_Lall_crown_mean[3])
BA20A_r4 = np.array(BA20A_Lall_crown_mean[5]) + np.array(BA20A_Lall_crown_mean[4]) + np.array(BA20A_Lall_crown_mean[3]) + np.array(BA20A_Lall_crown_mean[2])
BA20A_r5 = np.array(BA20A_Lall_crown_mean[5]) + np.array(BA20A_Lall_crown_mean[4]) + np.array(BA20A_Lall_crown_mean[3]) + np.array(BA20A_Lall_crown_mean[2]) + np.array(BA20A_Lall_crown_mean[1])

BA20_all_r1 = BA20_all_Lall_crown_mean[5]
BA20_all_r2 = np.array(BA20_all_Lall_crown_mean[5]) + np.array(BA20_all_Lall_crown_mean[4])
BA20_all_r3 = np.array(BA20_all_Lall_crown_mean[5]) + np.array(BA20_all_Lall_crown_mean[4]) + np.array(BA20_all_Lall_crown_mean[3])
BA20_all_r4 = np.array(BA20_all_Lall_crown_mean[5]) + np.array(BA20_all_Lall_crown_mean[4]) + np.array(BA20_all_Lall_crown_mean[3]) + np.array(BA20_all_Lall_crown_mean[2])
BA20_all_r5 = np.array(BA20_all_Lall_crown_mean[5]) + np.array(BA20_all_Lall_crown_mean[4]) + np.array(BA20_all_Lall_crown_mean[3]) + np.array(BA20_all_Lall_crown_mean[2]) + np.array(BA20_all_Lall_crown_mean[1])

BA36_r1 = BA36_Lall_crown_mean[5]
BA36_r2 = np.array(BA36_Lall_crown_mean[5]) + np.array(BA36_Lall_crown_mean[4])
BA36_r3 = np.array(BA36_Lall_crown_mean[5]) + np.array(BA36_Lall_crown_mean[4]) + np.array(BA36_Lall_crown_mean[3])
BA36_r4 = np.array(BA36_Lall_crown_mean[5]) + np.array(BA36_Lall_crown_mean[4]) + np.array(BA36_Lall_crown_mean[3]) + np.array(BA36_Lall_crown_mean[2])
BA36_r5 = np.array(BA36_Lall_crown_mean[5]) + np.array(BA36_Lall_crown_mean[4]) + np.array(BA36_Lall_crown_mean[3]) + np.array(BA36_Lall_crown_mean[2]) + np.array(BA36_Lall_crown_mean[1])

#FUNDUS
BA21_22_r1 = BA21_22_fundus_mean[5]
BA21_22_r2 = np.array(BA21_22_fundus_mean[5]) + np.array(BA21_22_fundus_mean[4])
BA21_22_r3 = np.array(BA21_22_fundus_mean[5]) + np.array(BA21_22_fundus_mean[4]) + np.array(BA21_22_fundus_mean[3])
BA21_22_r4 = np.array(BA21_22_fundus_mean[5]) + np.array(BA21_22_fundus_mean[4]) + np.array(BA21_22_fundus_mean[3]) + np.array(BA21_22_fundus_mean[2])
BA21_22_r5 = np.array(BA21_22_fundus_mean[5]) + np.array(BA21_22_fundus_mean[4]) + np.array(BA21_22_fundus_mean[3]) + np.array(BA21_22_fundus_mean[2]) + np.array(BA21_22_fundus_mean[1])

BA20B_21_r1 = BA20B_21_fundus_mean[5]
BA20B_21_r2 = np.array(BA20B_21_fundus_mean[5]) + np.array(BA20B_21_fundus_mean[4])
BA20B_21_r3 = np.array(BA20B_21_fundus_mean[5]) + np.array(BA20B_21_fundus_mean[4]) + np.array(BA20B_21_fundus_mean[3])
BA20B_21_r4 = np.array(BA20B_21_fundus_mean[5]) + np.array(BA20B_21_fundus_mean[4]) + np.array(BA20B_21_fundus_mean[3]) + np.array(BA20B_21_fundus_mean[2])
BA20B_21_r5 = np.array(BA20B_21_fundus_mean[5]) + np.array(BA20B_21_fundus_mean[4]) + np.array(BA20B_21_fundus_mean[3]) + np.array(BA20B_21_fundus_mean[2]) + np.array(BA20B_21_fundus_mean[1])

BA20A_20B_r1 = BA20A_20B_fundus_mean[5]
BA20A_20B_r2 = np.array(BA20A_20B_fundus_mean[5]) + np.array(BA20A_20B_fundus_mean[4])
BA20A_20B_r3 = np.array(BA20A_20B_fundus_mean[5]) + np.array(BA20A_20B_fundus_mean[4]) + np.array(BA20A_20B_fundus_mean[3])
BA20A_20B_r4 = np.array(BA20A_20B_fundus_mean[5]) + np.array(BA20A_20B_fundus_mean[4]) + np.array(BA20A_20B_fundus_mean[3]) + np.array(BA20A_20B_fundus_mean[2])
BA20A_20B_r5 = np.array(BA20A_20B_fundus_mean[5]) + np.array(BA20A_20B_fundus_mean[4]) + np.array(BA20A_20B_fundus_mean[3]) + np.array(BA20A_20B_fundus_mean[2]) + np.array(BA20A_20B_fundus_mean[1])

BA20A_20A_r1 = BA20A_20A_fundus_mean[5]
BA20A_20A_r2 = np.array(BA20A_20A_fundus_mean[5]) + np.array(BA20A_20A_fundus_mean[4])
BA20A_20A_r3 = np.array(BA20A_20A_fundus_mean[5]) + np.array(BA20A_20A_fundus_mean[4]) + np.array(BA20A_20A_fundus_mean[3])
BA20A_20A_r4 = np.array(BA20A_20A_fundus_mean[5]) + np.array(BA20A_20A_fundus_mean[4]) + np.array(BA20A_20A_fundus_mean[3]) + np.array(BA20A_20A_fundus_mean[2])
BA20A_20A_r5 = np.array(BA20A_20A_fundus_mean[5]) + np.array(BA20A_20A_fundus_mean[4]) + np.array(BA20A_20A_fundus_mean[3]) + np.array(BA20A_20A_fundus_mean[2]) + np.array(BA20A_20A_fundus_mean[1])


#CROWN
#Layer 1
plt.bar(ind1, BA22_Lall_crown_mean[0], color='#C783B3', edgecolor='white', width=barWidth, label='Layer I crown', alpha=0.90, bottom=BA22_r5)
plt.bar(ind3, BA21_Lall_crown_mean[0], color='#C783B3', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r5)
plt.bar(ind5, BA20B_Lall_crown_mean[0], color='#C783B3', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r5)
plt.bar(ind7, BA20A_Lall_crown_mean[0], color='#C783B3', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r5)

#Layer 2
plt.bar(ind1, BA22_Lall_crown_mean[1], color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=BA22_r4)
plt.bar(ind3, BA21_Lall_crown_mean[1], color='#DB7093', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r4)
plt.bar(ind5, BA20B_Lall_crown_mean[1], color='#DB7093', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r4)
plt.bar(ind7, BA20A_Lall_crown_mean[1], color='#DB7093', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r4)

#Layer3
plt.bar(ind1, BA22_Lall_crown_mean[2], color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=0.90, bottom=BA22_r3)
plt.bar(ind3, BA21_Lall_crown_mean[2], color='#993366', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r3)
plt.bar(ind5, BA20B_Lall_crown_mean[2], color='#993366', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r3)
plt.bar(ind7, BA20A_Lall_crown_mean[2], color='#993366', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r3)

#Layer4
plt.bar(ind1, BA22_Lall_crown_mean[3], color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=BA22_r2)
plt.bar(ind3, BA21_Lall_crown_mean[3], color='#900C3F', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r2)
plt.bar(ind5, BA20B_Lall_crown_mean[3], color='#900C3F', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r2)
plt.bar(ind7, BA20A_Lall_crown_mean[3], color='#900C3F', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r2)

#Layer 5
plt.bar(ind1, BA22_Lall_crown_mean[4], color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=BA22_r1)
plt.bar(ind3, BA21_Lall_crown_mean[4], color='#660033', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA21_r1)
plt.bar(ind5, BA20B_Lall_crown_mean[4], color='#660033', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_r1)
plt.bar(ind7, BA20A_Lall_crown_mean[4], color='#660033', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_r1)

#Layer 6
plt.bar(ind1, BA22_Lall_crown_mean[5], color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)
plt.bar(ind3, BA21_Lall_crown_mean[5], color='#330019', edgecolor='white', width=barWidth, alpha=0.90)
plt.bar(ind5, BA20B_Lall_crown_mean[5], color='#330019', edgecolor='white', width=barWidth, alpha=0.90)
plt.bar(ind7, BA20A_Lall_crown_mean[5], color='#330019', edgecolor='white', width=barWidth, alpha=0.90)


#FUNDUS
#Layer 1
plt.bar(ind2, BA21_22_fundus_mean[0], color='#7F57A8', edgecolor='white', width=barWidth, label='Layer I fundus', alpha=0.86, bottom=BA21_22_r5) #6BC3C3
plt.bar(ind4, BA20B_21_fundus_mean[0], color='#7F57A8', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20B_21_r5)
plt.bar(ind6, BA20A_20B_fundus_mean[0], color='#7F57A8', edgecolor='white', width=barWidth, alpha=0.90, bottom=BA20A_20B_r5)

#Layer 2
plt.bar(ind2, BA21_22_fundus_mean[1], color='#8A2BE2', edgecolor='white', width=barWidth, label='Layer II', alpha=0.85, bottom=BA21_22_r4) #20B2AA
plt.bar(ind4, BA20B_21_fundus_mean[1], color='#8A2BE2', edgecolor='white', width=barWidth, alpha=0.85, bottom=BA20B_21_r4)
plt.bar(ind6, BA20A_20B_fundus_mean[1], color='#8A2BE2', edgecolor='white', width=barWidth, alpha=0.85, bottom=BA20A_20B_r4)

#Layer 3
plt.bar(ind2, BA21_22_fundus_mean[2], color='#5C3386', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=BA21_22_r3)
plt.bar(ind4, BA20B_21_fundus_mean[2], color='#5C3386', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_21_r3)
plt.bar(ind6, BA20A_20B_fundus_mean[2], color='#5C3386', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_20B_r3)

#Layer 4
plt.bar(ind2, BA21_22_fundus_mean[3], color='#510251', edgecolor='white', width=barWidth, label='Layer IV', alpha=1, bottom=BA21_22_r2) #1BA7AC    #396565 #5F9EA0
plt.bar(ind4, BA20B_21_fundus_mean[3], color='#510251', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_21_r2)
plt.bar(ind6, BA20A_20B_fundus_mean[3], color='#510251', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_20B_r2)

#Layer 5
plt.bar(ind2, BA21_22_fundus_mean[4], color='#2B0352', edgecolor='white', width=barWidth, label='Layer V', alpha=1, bottom=BA21_22_r1) #074D4D
plt.bar(ind4, BA20B_21_fundus_mean[4], color='#2B0352', edgecolor='white', width=barWidth, alpha=1, bottom=BA20B_21_r1)
plt.bar(ind6, BA20A_20B_fundus_mean[4], color='#2B0352', edgecolor='white', width=barWidth, alpha=1, bottom=BA20A_20B_r1)

#Layer 6
plt.bar(ind2, BA21_22_fundus_mean[5], color='#1B0235', edgecolor='white', width=barWidth, label='Layer VI', alpha=1) #012626 #002E2E #002424
plt.bar(ind4, BA20B_21_fundus_mean[5], color='#1B0235', edgecolor='white', width=barWidth, alpha=1)
plt.bar(ind6, BA20A_20B_fundus_mean[5], color='#1B0235', edgecolor='white', width=barWidth, alpha=1)


plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks(np.arange(7), ['BA22\ncrown', 'BA21_22\nfundus', 'BA21\ncrown', 'BA20l_21\nfundus', 'BA20l\ncrown', 'BA20m_20l\nfundus', 'BA20m\ncrown'], fontsize=6, fontname="serif")
plt.ylabel("Relative layer thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.yticks(np.arange(0, 1.3, 0.2)) #yaxis points
plt.title('Segmented bar graph showing the laminar layers of the crown and fundus in the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 4.5}, ncol=2)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_seg_chart_mixed_group_diffcolour.png', dpi=400)
plt.show()








#CROWN AND FUNDUS - separated groups with different colours
#segmented bar graph

bar_LI_crown = [BA22_Lall_crown_mean[0], BA21_Lall_crown_mean[0], BA20B_Lall_crown_mean[0], BA20A_Lall_crown_mean[0], BA20_all_Lall_crown_mean[0], BA36_Lall_crown_mean[0]]

bar_LII_crown = [BA22_Lall_crown_mean[1], BA21_Lall_crown_mean[1], BA20B_Lall_crown_mean[1], BA20A_Lall_crown_mean[1], BA20_all_Lall_crown_mean[1], BA36_Lall_crown_mean[1]]

bar_LIII_crown = [BA22_Lall_crown_mean[2], BA21_Lall_crown_mean[2], BA20B_Lall_crown_mean[2], BA20A_Lall_crown_mean[2], BA20_all_Lall_crown_mean[2], BA36_Lall_crown_mean[2]]

bar_LIV_crown = [BA22_Lall_crown_mean[3], BA21_Lall_crown_mean[3], BA20B_Lall_crown_mean[3], BA20A_Lall_crown_mean[3], BA20_all_Lall_crown_mean[3], BA36_Lall_crown_mean[3]]

bar_LV_crown = [BA22_Lall_crown_mean[4], BA21_Lall_crown_mean[4], BA20B_Lall_crown_mean[4], BA20A_Lall_crown_mean[4], BA20_all_Lall_crown_mean[4], BA36_Lall_crown_mean[4]]

bar_LVI_crown = [BA22_Lall_crown_mean[5], BA21_Lall_crown_mean[5], BA20B_Lall_crown_mean[5], BA20A_Lall_crown_mean[5], BA20_all_Lall_crown_mean[5], BA36_Lall_crown_mean[5]]
#print(bar_LV)

bar_LI_fundus = [BA21_22_fundus_mean[0], BA20B_21_fundus_mean[0], BA20A_20B_fundus_mean[0],
BA20A_20A_fundus_mean[0]]

bar_LII_fundus = [BA21_22_fundus_mean[1], BA20B_21_fundus_mean[1], BA20A_20B_fundus_mean[1],
BA20A_20A_fundus_mean[1]]

bar_LIII_fundus = [BA21_22_fundus_mean[2], BA20B_21_fundus_mean[2], BA20A_20B_fundus_mean[2],
BA20A_20A_fundus_mean[2]]

bar_LIV_fundus = [BA21_22_fundus_mean[3], BA20B_21_fundus_mean[3], BA20A_20B_fundus_mean[3],
BA20A_20A_fundus_mean[3]]

bar_LV_fundus = [BA21_22_fundus_mean[4], BA20B_21_fundus_mean[4], BA20A_20B_fundus_mean[4],
BA20A_20A_fundus_mean[4]]

bar_LVI_fundus = [BA21_22_fundus_mean[5], BA20B_21_fundus_mean[5], BA20A_20B_fundus_mean[5],
BA20A_20A_fundus_mean[5]]


barWidth = 0.5
ind_crown = np.arange(len(bar_LI_crown))
ind_fundus = np.arange(len(bar_LI_fundus)) + len(bar_LI_crown)


#bar height
r1 = bar_LVI_crown
r2 = np.array(bar_LVI_crown) + np.array(bar_LV_crown)
r3 = np.array(bar_LVI_crown) + np.array(bar_LV_crown) + np.array(bar_LIV_crown)
r4 = np.array(bar_LVI_crown) + np.array(bar_LV_crown) + np.array(bar_LIV_crown) + np.array(bar_LIII_crown)
r5 = np.array(bar_LVI_crown) + np.array(bar_LV_crown) + np.array(bar_LIV_crown) + np.array(bar_LIII_crown) + np.array(bar_LII_crown)

r6 = bar_LVI_fundus
r7 = np.array(bar_LVI_fundus) + np.array(bar_LV_fundus)
r8 = np.array(bar_LVI_fundus) + np.array(bar_LV_fundus) + np.array(bar_LIV_fundus)
r9 = np.array(bar_LVI_fundus) + np.array(bar_LV_fundus) + np.array(bar_LIV_fundus) + np.array(bar_LIII_fundus)
r10 = np.array(bar_LVI_fundus) + np.array(bar_LV_fundus) + np.array(bar_LIV_fundus) + np.array(bar_LIII_fundus) + np.array(bar_LII_fundus)


plt.bar(ind_crown, bar_LI_crown, color='#C783B3', edgecolor='white', width=barWidth, label='Layer I crown', alpha=0.90, bottom=r5)
plt.bar(ind_crown, bar_LII_crown, color='#DB7093', edgecolor='white', width=barWidth, label='Layer II', alpha=0.90, bottom=r4)
plt.bar(ind_crown, bar_LIII_crown, color='#993366', edgecolor='white', width=barWidth, label='Layer III', alpha=0.90, bottom=r3)
plt.bar(ind_crown, bar_LIV_crown, color='#900C3F', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r2)
plt.bar(ind_crown, bar_LV_crown, color='#660033', edgecolor='white', width=barWidth, label='Layer V', alpha=0.90, bottom=r1)
plt.bar(ind_crown, bar_LVI_crown, color='#330019', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90)

plt.bar(ind_fundus, bar_LI_fundus, color='#DC7373', edgecolor='white', width=barWidth, label='Layer I fundus', bottom=r10)
plt.bar(ind_fundus, bar_LII_fundus, color='#EC5959', edgecolor='white', width=barWidth, label='Layer II', alpha=1, bottom=r9) #F74242 #F73636
plt.bar(ind_fundus, bar_LIII_fundus, color='#A43E3E', edgecolor='white', width=barWidth, label='Layer III', alpha=1, bottom=r8)
plt.bar(ind_fundus, bar_LIV_fundus, color='#C10303', edgecolor='white', width=barWidth, label='Layer IV', alpha=0.90, bottom=r7)
plt.bar(ind_fundus, bar_LV_fundus, color='#800000', edgecolor='white', width=barWidth, label='Layer V', alpha=0.95, bottom=r6)
plt.bar(ind_fundus, bar_LVI_fundus, color='#400404', edgecolor='white', width=barWidth, label='Layer VI', alpha=0.90) #330000


plt.xlabel('Region', fontname="serif", fontsize=8, fontweight='bold')
plt.xticks(np.concatenate([ind_crown, ind_fundus]), ['BA22', 'BA21', 'BA20B', 'BA20A', 'BA20_all', 'BA36', 'BA21_22', 'BA20B_21', 'BA20A_20B', 'BA20A_20A'], fontsize=6, fontname="serif")
plt.ylabel("Relative cortical thickness", fontname="serif", fontsize=8, fontweight='bold')
plt.yticks(np.arange(0, 1.3, 0.2)) #yaxis points
plt.title('Segmented bar graph showing the laminar layers of the crown and fundus of the TNC', fontname="serif", fontsize=8)
plt.legend(loc='upper right', fontsize=8.25, prop={'size': 4.6}, ncol=2)
plt.tight_layout()
#plt.savefig('BA_all_crown_fundus_seg_chart_separated_group.png', dpi=400)
plt.show()
