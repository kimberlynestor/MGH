
"""
name: thick_funcs
Author: Kimberly Nestor
Use:
This script is part of the TNC laminar thickness project and uses the output
thickness data from the laplace equation to do statistical analyses and data
visualization. These are the functions called in the main program.
"""
import glob, os
import pandas as pd
import numpy as np


#FUNCTIONS

#Use:
# This function will import the data of 3 (in some instances 2 and 1) slices, remove the data from the lines that don't go from pial surface to white matter boundary aka junk lines. It does this by finding the derivatives of every laplace line and then thresholding so that only the mostly start part of the line remains. The function then averages the r data points (slices) and returns relative numbers

# Inputs: case - "I25"; BA - "BA21"; area - "crown" or "fundus"

# Outputs: a list with 6 items that coorespond to the averaged thickness of each laminar layer i.e. 6lauers
def import_clean_data_avg(case, BA, area):
    if area == "crown":
        data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/**'
    elif area == "fundus":
        data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/**'
    elif area == "sulcus":
        data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/sulcus/**'
    filename_list = []
    for filename in glob.glob(data_files, recursive=True):
        if os.path.isfile(filename):
            if filename.endswith("profile_all_long.csv"):
                if case in filename and BA in filename:
                    if "I25_block4" in filename:
                        continue
                    elif "I33_block2_slice85_fundus_BA20B_21" in filename:
                        continue
                    elif "I33_block2_slice85_fundus_BA21_22" in filename:
                        continue
                    else:
                        filename_list.append(filename)
                    # print("filename_list = ", filename_list)
    #sys.exit()
    layer1_allslice = []
    layer2_allslice = []
    layer3_allslice = []
    layer4_allslice = []
    layer5_allslice = []
    layer6_allslice = []
    for filename in filename_list:
        filename = pd.read_csv(filename)

        #print(filename['Layer 1'])
        print(filename)

        layer1_all_df = filename['Layer 1']
        layer2_all_df = filename['Layer 2']
        layer3_all_df = filename['Layer 3']
        layer4_all_df = filename['Layer 4']
        layer5_all_df = filename['Layer 5']
        layer6_all_df = filename['Layer 6']

        #make a list from a column in the pandas dataframe
        def list_make(layer):
            new_list = []
            for number in layer:
                new_list.append(number)
            return new_list

        layer1_all = list_make(layer1_all_df)
        layer2_all = list_make(layer2_all_df)
        layer3_all = list_make(layer3_all_df)
        layer4_all = list_make(layer4_all_df)
        layer5_all = list_make(layer5_all_df)
        layer6_all = list_make(layer6_all_df)
        # print("layer1_all = ", layer1_all)
        #finds derivatives
        layer1_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer1_all[1:], layer1_all)]
        layer2_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer2_all[1:], layer2_all)]
        layer3_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer3_all[1:], layer3_all)]
        layer4_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer4_all[1:], layer4_all)]
        layer5_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer5_all[1:], layer5_all)]
        layer6_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer6_all[1:], layer6_all)]
        # print("layer1_slope = ", layer1_slope)
        # print("layer2_slope = ", layer2_slope)
        # print("layer4_slope = ", layer4_slope)


        #Finds threshold values from derivatives
        layer1_slope_range = [layer1_slope.index(i) for i in layer1_slope if -0.015 < i < 0.025 if i != 0] #0.02 is the threshold used for the slope, this can be adjusted depending on the slope of the data
        layer1_slope_threshold = [layer1_slope_range[0], layer1_slope_range[-1]]

        layer2_slope_range = [layer2_slope.index(i) for i in layer2_slope if -0.015 < i < 0.025 if i != 0]
        layer2_slope_threshold = [layer2_slope_range[0], layer2_slope_range[-1]]

        layer3_slope_range = [layer3_slope.index(i) for i in layer3_slope if -0.015 < i < 0.025 if i != 0]
        layer3_slope_threshold = [layer3_slope_range[0], layer3_slope_range[-1]]

        layer4_slope_range = [layer4_slope.index(i) for i in layer4_slope if -0.015 < i < 0.025 if i != 0]
        layer4_slope_threshold = [layer4_slope_range[0], layer4_slope_range[-1]]

        layer5_slope_range = [layer5_slope.index(i) for i in layer5_slope if -0.015 < i < 0.025 if i != 0]
        layer5_slope_threshold = [layer5_slope_range[0], layer5_slope_range[-1]]

        layer6_slope_range = [layer6_slope.index(i) for i in layer6_slope if -0.015 < i < 0.025 if i != 0]
        layer6_slope_threshold = [layer6_slope_range[0], layer6_slope_range[-1]]


        #all the start values for the 6 layers
        start_all = [min(layer1_slope_range), min(layer2_slope_range), min(layer3_slope_range), min(layer4_slope_range), min(layer5_slope_range), min(layer6_slope_range)]
        #print("start_all = ", start_all)

        #all the stop values for the 6 layers
        stop_all = [max(layer1_slope_range), max(layer2_slope_range), max(layer3_slope_range), max(layer4_slope_range), max(layer5_slope_range), max(layer6_slope_range)]
        #print("stop_all = ", stop_all)

        #stop value is determined for all 6 slices
        start = max(start_all)
        stop = min(stop_all)
        print("start = ", start)
        print("stop = ", stop)

        layer1 = layer1_all[start:stop]
        layer2 = layer2_all[start:stop]
        layer3 = layer3_all[start:stop]
        layer4 = layer4_all[start:stop]
        layer5 = layer5_all[start:stop]
        layer6 = layer6_all[start:stop]
        # print("layer1 = ", layer1)
        [layer1_allslice.append(i) for i in layer1]
        [layer2_allslice.append(i) for i in layer2]
        [layer3_allslice.append(i) for i in layer3]
        [layer4_allslice.append(i) for i in layer4]
        [layer5_allslice.append(i) for i in layer5]
        [layer6_allslice.append(i) for i in layer6]
    #print("layer1_allslice = ", layer1_allslice)

    #mean of all three data points
    layer1_mean = (np.mean((layer1_allslice)))
    #print("layer1_mean = ", layer1_mean)
    layer2_mean = (np.mean((layer2_allslice)))
    layer3_mean = (np.mean((layer3_allslice)))
    layer4_mean = (np.mean((layer4_allslice)))
    layer5_mean = (np.mean((layer5_allslice)))
    layer6_mean = (np.mean((layer6_allslice)))
    Lall_mean_list = [layer1_mean, layer2_mean, layer3_mean, layer4_mean, layer5_mean, layer6_mean]
    return Lall_mean_list
    #sum_all_meanL = sum(Lall)
    #relative_num = [(layer1_mean/sum_all_meanL), (layer2_mean/sum_all_meanL), (layer3_mean/sum_all_meanL), (layer4_mean/sum_all_meanL), (layer5_mean/sum_all_meanL), (layer6_mean/sum_all_meanL)]
    #return relative_num

#this is the same as above, but will average BA20A and BA20B into one BA20.
def BA20_all_clean_data_avg(case, BA20A, BA20B):
    data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/**'

    def list_make(layer):
            new_list = []
            for number in layer:
                new_list.append(number)
            return new_list

    filename_list_BA20A = []
    filename_list_BA20B = []
    if BA20A is None:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all_long.csv"):
                    if case in filename and BA20B in filename:
                        if "I25_block4" in filename:
                            continue
                        else:
                            filename_list_BA20B.append(filename)
                            # print("filename_list_BA20A = ", filename_list_BA20A)
                            # sys.exit()
        layer1_allslice = []
        layer2_allslice = []
        layer3_allslice = []
        layer4_allslice = []
        layer5_allslice = []
        layer6_allslice = []
        for filename in filename_list_BA20B:
            filename = pd.read_csv(filename)
            # print(filename['Layer 1'])
            #sys.exit()
            layer1_all_df = filename['Layer 1']
            layer2_all_df = filename['Layer 2']
            layer3_all_df = filename['Layer 3']
            layer4_all_df = filename['Layer 4']
            layer5_all_df = filename['Layer 5']
            layer6_all_df = filename['Layer 6']

            layer1_all = list_make(layer1_all_df)
            layer2_all = list_make(layer2_all_df)
            layer3_all = list_make(layer3_all_df)
            layer4_all = list_make(layer4_all_df)
            layer5_all = list_make(layer5_all_df)
            layer6_all = list_make(layer6_all_df)

            #finds derivatives
            layer1_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer1_all[1:], layer1_all)]
            layer2_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer2_all[1:], layer2_all)]
            layer3_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer3_all[1:], layer3_all)]
            layer4_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer4_all[1:], layer4_all)]
            layer5_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer5_all[1:], layer5_all)]
            layer6_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer6_all[1:], layer6_all)]

            #Finds threshold values from derivatives
            layer1_slope_range = [layer1_slope.index(i) for i in layer1_slope if -0.015 < i < 0.025 if i != 0] #0.02 is the threshold used for the slope, this can be adjusted depending on the slope of the data
            layer1_slope_threshold = [layer1_slope_range[0], layer1_slope_range[-1]]

            layer2_slope_range = [layer2_slope.index(i) for i in layer2_slope if -0.015 < i < 0.025 if i != 0]
            layer2_slope_threshold = [layer2_slope_range[0], layer2_slope_range[-1]]

            layer3_slope_range = [layer3_slope.index(i) for i in layer3_slope if -0.015 < i < 0.025 if i != 0]
            layer3_slope_threshold = [layer3_slope_range[0], layer3_slope_range[-1]]

            layer4_slope_range = [layer4_slope.index(i) for i in layer4_slope if -0.015 < i < 0.025 if i != 0]
            layer4_slope_threshold = [layer4_slope_range[0], layer4_slope_range[-1]]

            layer5_slope_range = [layer5_slope.index(i) for i in layer5_slope if -0.015 < i < 0.025 if i != 0]
            layer5_slope_threshold = [layer5_slope_range[0], layer5_slope_range[-1]]

            layer6_slope_range = [layer6_slope.index(i) for i in layer6_slope if -0.015 < i < 0.025 if i != 0]
            layer6_slope_threshold = [layer6_slope_range[0], layer6_slope_range[-1]]

            #all the start values for the 6 layers
            start_all = [min(layer1_slope_range), min(layer2_slope_range), min(layer3_slope_range), min(layer4_slope_range), min(layer5_slope_range), min(layer6_slope_range)]
            #print("start_all = ", start_all)

            #all the stop values for the 6 layers
            stop_all = [max(layer1_slope_range), max(layer2_slope_range), max(layer3_slope_range), max(layer4_slope_range), max(layer5_slope_range), max(layer6_slope_range)]
            #print("stop_all = ", stop_all)

            #stop value is determined for all 6 slices
            start = max(start_all)
            stop = min(stop_all)
            #print("start = ", start)
            #print("stop = ", stop)

            layer1 = layer1_all[start:stop]
            layer2 = layer2_all[start:stop]
            layer3 = layer3_all[start:stop]
            layer4 = layer4_all[start:stop]
            layer5 = layer5_all[start:stop]
            layer6 = layer6_all[start:stop]
            #print("layer1 = ", layer1)

            [layer1_allslice.append(i) for i in layer1]
            [layer2_allslice.append(i) for i in layer2]
            [layer3_allslice.append(i) for i in layer3]
            [layer4_allslice.append(i) for i in layer4]
            [layer5_allslice.append(i) for i in layer5]
            [layer6_allslice.append(i) for i in layer6]
        #print("layer1_allslice = ", layer1_allslice)

        #mean of all three data points
        layer1_mean = (np.mean((layer1_allslice)))
        layer2_mean = (np.mean((layer2_allslice)))
        layer3_mean = (np.mean((layer3_allslice)))
        layer4_mean = (np.mean((layer4_allslice)))
        layer5_mean = (np.mean((layer5_allslice)))
        layer6_mean = (np.mean((layer6_allslice)))
        Lall_mean_list = [layer1_mean, layer2_mean, layer3_mean, layer4_mean, layer5_mean, layer6_mean]
        return Lall_mean_list
        #sum_all_meanL = sum(Lall)
        #relative_num = [(layer1_mean/sum_all_meanL), (layer2_mean/sum_all_meanL), (layer3_mean/sum_all_meanL), (layer4_mean/sum_all_meanL), (layer5_mean/sum_all_meanL), (layer6_mean/sum_all_meanL)]
        #return relative_num
    elif BA20B is None:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all_long.csv"):
                    if case in filename and BA20A in filename:
                        if "I25_block4" in filename:
                            continue
                        else:
                            filename_list_BA20A.append(filename)
        layer1_allslice = []
        layer2_allslice = []
        layer3_allslice = []
        layer4_allslice = []
        layer5_allslice = []
        layer6_allslice = []
        for filename in filename_list_BA20A:
            filename = pd.read_csv(filename)
            #print(filename['Layer 1'])

            layer1_all_df = filename['Layer 1']
            layer2_all_df = filename['Layer 2']
            layer3_all_df = filename['Layer 3']
            layer4_all_df = filename['Layer 4']
            layer5_all_df = filename['Layer 5']
            layer6_all_df = filename['Layer 6']

            layer1_all = list_make(layer1_all_df)
            layer2_all = list_make(layer2_all_df)
            layer3_all = list_make(layer3_all_df)
            layer4_all = list_make(layer4_all_df)
            layer5_all = list_make(layer5_all_df)
            layer6_all = list_make(layer6_all_df)

            #finds derivatives
            layer1_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer1_all[1:], layer1_all)]
            layer2_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer2_all[1:], layer2_all)]
            layer3_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer3_all[1:], layer3_all)]
            layer4_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer4_all[1:], layer4_all)]
            layer5_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer5_all[1:], layer5_all)]
            layer6_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer6_all[1:], layer6_all)]

            #Finds threshold values from derivatives
            layer1_slope_range = [layer1_slope.index(i) for i in layer1_slope if -0.015 < i < 0.025 if i != 0] #0.02 is the threshold used for the slope, this can be adjusted depending on the slope of the data
            layer1_slope_threshold = [layer1_slope_range[0], layer1_slope_range[-1]]

            layer2_slope_range = [layer2_slope.index(i) for i in layer2_slope if -0.015 < i < 0.025 if i != 0]
            layer2_slope_threshold = [layer2_slope_range[0], layer2_slope_range[-1]]

            layer3_slope_range = [layer3_slope.index(i) for i in layer3_slope if -0.015 < i < 0.025 if i != 0]
            layer3_slope_threshold = [layer3_slope_range[0], layer3_slope_range[-1]]

            layer4_slope_range = [layer4_slope.index(i) for i in layer4_slope if -0.015 < i < 0.025 if i != 0]
            layer4_slope_threshold = [layer4_slope_range[0], layer4_slope_range[-1]]

            layer5_slope_range = [layer5_slope.index(i) for i in layer5_slope if -0.015 < i < 0.025 if i != 0]
            layer5_slope_threshold = [layer5_slope_range[0], layer5_slope_range[-1]]

            layer6_slope_range = [layer6_slope.index(i) for i in layer6_slope if -0.015 < i < 0.025 if i != 0]
            layer6_slope_threshold = [layer6_slope_range[0], layer6_slope_range[-1]]

            #all the start values for the 6 layers
            start_all = [min(layer1_slope_range), min(layer2_slope_range), min(layer3_slope_range), min(layer4_slope_range), min(layer5_slope_range), min(layer6_slope_range)]
            #print("start_all = ", start_all)

            #all the stop values for the 6 layers
            stop_all = [max(layer1_slope_range), max(layer2_slope_range), max(layer3_slope_range), max(layer4_slope_range), max(layer5_slope_range), max(layer6_slope_range)]
            #print("stop_all = ", stop_all)

            #stop value is determined for all 6 slices
            start = max(start_all)
            stop = min(stop_all)
            #print("start = ", start)
            #print("stop = ", stop)

            layer1 = layer1_all[start:stop]
            layer2 = layer2_all[start:stop]
            layer3 = layer3_all[start:stop]
            layer4 = layer4_all[start:stop]
            layer5 = layer5_all[start:stop]
            layer6 = layer6_all[start:stop]
            #print("layer1 = ", layer1)

            [layer1_allslice.append(i) for i in layer1]
            [layer2_allslice.append(i) for i in layer2]
            [layer3_allslice.append(i) for i in layer3]
            [layer4_allslice.append(i) for i in layer4]
            [layer5_allslice.append(i) for i in layer5]
            [layer6_allslice.append(i) for i in layer6]
        #print("layer1_allslice = ", layer1_allslice)

        #mean of all three data points
        layer1_mean = (np.mean((layer1_allslice)))
        layer2_mean = (np.mean((layer2_allslice)))
        layer3_mean = (np.mean((layer3_allslice)))
        layer4_mean = (np.mean((layer4_allslice)))
        layer5_mean = (np.mean((layer5_allslice)))
        layer6_mean = (np.mean((layer6_allslice)))
        Lall_mean_list = [layer1_mean, layer2_mean, layer3_mean, layer4_mean, layer5_mean, layer6_mean]
        return Lall_mean_list
        #sum_all_meanL = sum(Lall)
        #relative_num = [(layer1_mean/sum_all_meanL), (layer2_mean/sum_all_meanL), (layer3_mean/sum_all_meanL), (layer4_mean/sum_all_meanL), (layer5_mean/sum_all_meanL), (layer6_mean/sum_all_meanL)]
        #return relative_num
    else:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all_long.csv"):
                    if case in filename and BA20A in filename:
                        if "I25_block4" in filename:
                            continue
                        else:
                            filename_list_BA20A.append(filename)
                    elif case in filename and BA20B in filename:
                        if "I25_block4" in filename:
                            continue
                        else:
                            filename_list_BA20B.append(filename)
        layer1_allslice_BA20A = []
        layer2_allslice_BA20A = []
        layer3_allslice_BA20A = []
        layer4_allslice_BA20A = []
        layer5_allslice_BA20A = []
        layer6_allslice_BA20A = []

        layer1_allslice_BA20B = []
        layer2_allslice_BA20B = []
        layer3_allslice_BA20B = []
        layer4_allslice_BA20B = []
        layer5_allslice_BA20B = []
        layer6_allslice_BA20B = []
        for filename in filename_list_BA20A:
            filename = pd.read_csv(filename)
            #print(filename['Layer 1'])

            layer1_all_df = filename['Layer 1']
            layer2_all_df = filename['Layer 2']
            layer3_all_df = filename['Layer 3']
            layer4_all_df = filename['Layer 4']
            layer5_all_df = filename['Layer 5']
            layer6_all_df = filename['Layer 6']

            layer1_all = list_make(layer1_all_df)
            layer2_all = list_make(layer2_all_df)
            layer3_all = list_make(layer3_all_df)
            layer4_all = list_make(layer4_all_df)
            layer5_all = list_make(layer5_all_df)
            layer6_all = list_make(layer6_all_df)
            #print("layer1_all = ", layer1_all)

            #finds derivatives
            layer1_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer1_all[1:], layer1_all)]
            layer2_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer2_all[1:], layer2_all)]
            layer3_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer3_all[1:], layer3_all)]
            layer4_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer4_all[1:], layer4_all)]
            layer5_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer5_all[1:], layer5_all)]
            layer6_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer6_all[1:], layer6_all)]
            #print("layer1_slope = ", layer1_slope)

            #Finds threshold values from derivatives
            layer1_slope_range = [layer1_slope.index(i) for i in layer1_slope if -0.015 < i < 0.025 if i != 0] #0.02 is the threshold used for the slope, this can be adjusted depending on the slope of the data
            layer1_slope_threshold = [layer1_slope_range[0], layer1_slope_range[-1]]

            layer2_slope_range = [layer2_slope.index(i) for i in layer2_slope if -0.015 < i < 0.025 if i != 0]
            layer2_slope_threshold = [layer2_slope_range[0], layer2_slope_range[-1]]

            layer3_slope_range = [layer3_slope.index(i) for i in layer3_slope if -0.015 < i < 0.025 if i != 0]
            layer3_slope_threshold = [layer3_slope_range[0], layer3_slope_range[-1]]

            layer4_slope_range = [layer4_slope.index(i) for i in layer4_slope if -0.015 < i < 0.025 if i != 0]
            layer4_slope_threshold = [layer4_slope_range[0], layer4_slope_range[-1]]

            layer5_slope_range = [layer5_slope.index(i) for i in layer5_slope if -0.015 < i < 0.025 if i != 0]
            layer5_slope_threshold = [layer5_slope_range[0], layer5_slope_range[-1]]

            layer6_slope_range = [layer6_slope.index(i) for i in layer6_slope if -0.015 < i < 0.025 if i != 0]
            layer6_slope_threshold = [layer6_slope_range[0], layer6_slope_range[-1]]
            #print("layer1_slope_range = ", layer1_slope_range)
            #print("layer1_slope_threshold = ", layer1_slope_threshold)

            #all the start values for the 6 layers
            start_all = [min(layer1_slope_range), min(layer2_slope_range), min(layer3_slope_range), min(layer4_slope_range), min(layer5_slope_range), min(layer6_slope_range)]
            #print("start_all = ", start_all)

            #all the stop values for the 6 layers
            stop_all = [max(layer1_slope_range), max(layer2_slope_range), max(layer3_slope_range), max(layer4_slope_range), max(layer5_slope_range), max(layer6_slope_range)]
            #print("stop_all = ", stop_all)

            #stop value is determined for all 6 slices
            start = max(start_all)
            stop = min(stop_all)
            #print("start = ", start)
            #print("stop = ", stop)

            layer1 = layer1_all[start:stop]
            layer2 = layer2_all[start:stop]
            layer3 = layer3_all[start:stop]
            layer4 = layer4_all[start:stop]
            layer5 = layer5_all[start:stop]
            layer6 = layer6_all[start:stop]
            #print("layer1 = ", layer1)

            [layer1_allslice_BA20A.append(i) for i in layer1]
            [layer2_allslice_BA20A.append(i) for i in layer2]
            [layer3_allslice_BA20A.append(i) for i in layer3]
            [layer4_allslice_BA20A.append(i) for i in layer4]
            [layer5_allslice_BA20A.append(i) for i in layer5]
            [layer6_allslice_BA20A.append(i) for i in layer6]
        #print("layer1_allslice = ", layer1_allslice)
        for filename in filename_list_BA20B:
            filename = pd.read_csv(filename)
            #print(filename['Layer 1'])

            layer1_all_df = filename['Layer 1']
            layer2_all_df = filename['Layer 2']
            layer3_all_df = filename['Layer 3']
            layer4_all_df = filename['Layer 4']
            layer5_all_df = filename['Layer 5']
            layer6_all_df = filename['Layer 6']

            layer1_all = list_make(layer1_all_df)
            layer2_all = list_make(layer2_all_df)
            layer3_all = list_make(layer3_all_df)
            layer4_all = list_make(layer4_all_df)
            layer5_all = list_make(layer5_all_df)
            layer6_all = list_make(layer6_all_df)
            #print("layer1_all = ", layer1_all)

            #finds derivatives
            layer1_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer1_all[1:], layer1_all)]
            layer2_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer2_all[1:], layer2_all)]
            layer3_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer3_all[1:], layer3_all)]
            layer4_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer4_all[1:], layer4_all)]
            layer5_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer5_all[1:], layer5_all)]
            layer6_slope = [(ypoint2 - ypoint1) for ypoint1, ypoint2 in zip(layer6_all[1:], layer6_all)]
            #print("layer1_slope = ", layer1_slope)

            #Finds threshold values from derivatives
            layer1_slope_range = [layer1_slope.index(i) for i in layer1_slope if -0.015 < i < 0.025 if i != 0] #0.02 is the threshold used for the slope, this can be adjusted depending on the slope of the data
            layer1_slope_threshold = [layer1_slope_range[0], layer1_slope_range[-1]]

            layer2_slope_range = [layer2_slope.index(i) for i in layer2_slope if -0.015 < i < 0.025 if i != 0]
            layer2_slope_threshold = [layer2_slope_range[0], layer2_slope_range[-1]]

            layer3_slope_range = [layer3_slope.index(i) for i in layer3_slope if -0.015 < i < 0.025 if i != 0]
            layer3_slope_threshold = [layer3_slope_range[0], layer3_slope_range[-1]]

            layer4_slope_range = [layer4_slope.index(i) for i in layer4_slope if -0.015 < i < 0.025 if i != 0]
            layer4_slope_threshold = [layer4_slope_range[0], layer4_slope_range[-1]]

            layer5_slope_range = [layer5_slope.index(i) for i in layer5_slope if -0.015 < i < 0.025 if i != 0]
            layer5_slope_threshold = [layer5_slope_range[0], layer5_slope_range[-1]]

            layer6_slope_range = [layer6_slope.index(i) for i in layer6_slope if -0.015 < i < 0.025 if i != 0]
            layer6_slope_threshold = [layer6_slope_range[0], layer6_slope_range[-1]]
            #print("layer1_slope_range = ", layer1_slope_range)
            #print("layer1_slope_threshold = ", layer1_slope_threshold)

            #all the start values for the 6 layers
            start_all = [min(layer1_slope_range), min(layer2_slope_range), min(layer3_slope_range), min(layer4_slope_range), min(layer5_slope_range), min(layer6_slope_range)]
            #print("start_all = ", start_all)

            #all the stop values for the 6 layers
            stop_all = [max(layer1_slope_range), max(layer2_slope_range), max(layer3_slope_range), max(layer4_slope_range), max(layer5_slope_range), max(layer6_slope_range)]
            #print("stop_all = ", stop_all)

            #stop value is determined for all 6 slices
            start = max(start_all)
            stop = min(stop_all)
            #print("start = ", start)
            #print("stop = ", stop)

            layer1 = layer1_all[start:stop]
            layer2 = layer2_all[start:stop]
            layer3 = layer3_all[start:stop]
            layer4 = layer4_all[start:stop]
            layer5 = layer5_all[start:stop]
            layer6 = layer6_all[start:stop]
            #print("layer1 = ", layer1)

            [layer1_allslice_BA20B.append(i) for i in layer1]
            [layer2_allslice_BA20B.append(i) for i in layer2]
            [layer3_allslice_BA20B.append(i) for i in layer3]
            [layer4_allslice_BA20B.append(i) for i in layer4]
            [layer5_allslice_BA20B.append(i) for i in layer5]
            [layer6_allslice_BA20B.append(i) for i in layer6]


        #mean of all three data points
        layer1_BA20A_mean = (np.mean((layer1_allslice_BA20A)))
        layer2_BA20A_mean = (np.mean((layer2_allslice_BA20A)))
        layer3_BA20A_mean = (np.mean((layer3_allslice_BA20A)))
        layer4_BA20A_mean = (np.mean((layer4_allslice_BA20A)))
        layer5_BA20A_mean = (np.mean((layer5_allslice_BA20A)))
        layer6_BA20A_mean = (np.mean((layer6_allslice_BA20A)))

        layer1_BA20B_mean = (np.mean((layer1_allslice_BA20B)))
        layer2_BA20B_mean = (np.mean((layer2_allslice_BA20B)))
        layer3_BA20B_mean = (np.mean((layer3_allslice_BA20B)))
        layer4_BA20B_mean = (np.mean((layer4_allslice_BA20B)))
        layer5_BA20B_mean = (np.mean((layer5_allslice_BA20B)))
        layer6_BA20B_mean = (np.mean((layer6_allslice_BA20B)))

        Lall_BA20A_mean = [layer1_BA20A_mean, layer2_BA20A_mean, layer3_BA20A_mean, layer4_BA20A_mean, layer5_BA20A_mean, layer6_BA20A_mean]

        Lall_BA20B_mean = [layer1_BA20B_mean, layer2_BA20B_mean, layer3_BA20B_mean, layer4_BA20B_mean, layer5_BA20B_mean, layer6_BA20B_mean]

        Lall_BA20_all_clean_data_mean = np.mean(np.array([Lall_BA20A_mean, Lall_BA20B_mean]), axis=0)
    return Lall_BA20_all_clean_data_mean
        #sum_all_meanL = sum(Lall_BA20_all_clean_data_mean)
        #relative_num = [(Lall_BA20_all_clean_data_mean[0]/sum_all_meanL), (Lall_BA20_all_clean_data_mean[1]/sum_all_meanL), (Lall_BA20_all_clean_data_mean[2]/sum_all_meanL), (Lall_BA20_all_clean_data_mean[3]/sum_all_meanL), (Lall_BA20_all_clean_data_mean[4]/sum_all_meanL), (Lall_BA20_all_clean_data_mean[5]/sum_all_meanL)]
    #return relative_num

#Use:
#This function is an older precurser to the above functions and only reads data files, compile slices into a dataframe and then average all laplace lines for all slices and turn into relative numbers and return layers 1-6 in a list
def import_data_relative(case, BA, area):
    if area == "crown":
        data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/**'
    elif area == "fundus":
        data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/fundus/**'
    filename_list = []
    for filename in glob.glob(data_files, recursive=True):
        if os.path.isfile(filename):
            if filename.endswith("profile_all.xls"):
                if case in filename and BA in filename:
                    filename_list.append(filename)
    layer1 = [pd.read_excel(i, usecols=[1]) for i in filename_list]
    layer2 = [pd.read_excel(i, usecols=[2]) for i in filename_list]
    layer3 = [pd.read_excel(i, usecols=[3]) for i in filename_list]
    layer4 = [pd.read_excel(i, usecols=[4]) for i in filename_list]
    layer5 = [pd.read_excel(i, usecols=[5]) for i in filename_list]
    layer5 = [pd.read_excel(i, usecols=[5]) for i in filename_list]
    layer6 = [pd.read_excel(i, usecols=[6]) for i in filename_list]
    layer1_mean = (np.mean((layer1)[0]))[0]
    layer2_mean = (np.mean((layer2)[0]))[0]
    layer3_mean = (np.mean((layer3)[0]))[0]
    layer4_mean = (np.mean((layer4)[0]))[0]
    layer5_mean = (np.mean((layer5)[0]))[0]
    layer6_mean = (np.mean((layer6)[0]))[0]
    Lall = [layer1_mean, layer2_mean, layer3_mean, layer4_mean, layer5_mean, layer6_mean]
    sum_all_meanL = sum(Lall)
    relative_num = [(layer1_mean/sum_all_meanL), (layer2_mean/sum_all_meanL), (layer3_mean/sum_all_meanL), (layer4_mean/sum_all_meanL), (layer5_mean/sum_all_meanL), (layer6_mean/sum_all_meanL)]
    return relative_num

#older precurse - average data from BA20A and BA20B and make relative numbers and return layers 1-6 in a list
def BA20_all_import_data_rel(case, BA20A, BA20B):
    data_files = '/autofs/space/asterion_001/users/kn751/tnc_laminar_project/laminar_thickness/crown/**'
    filename_list_BA20A = []
    filename_list_BA20B = []
    if BA20A is None:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all.xls"):
                    if case in filename and BA20B in filename:
                        filename_list_BA20B.append(filename)
        layer1_BA20B = [pd.read_excel(i, usecols=[1]) for i in filename_list_BA20A]
        layer2_BA20B = [pd.read_excel(i, usecols=[2]) for i in filename_list_BA20A]
        layer3_BA20B = [pd.read_excel(i, usecols=[3]) for i in filename_list_BA20A]
        layer4_BA20B = [pd.read_excel(i, usecols=[4]) for i in filename_list_BA20A]
        layer5_BA20B = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer5_BA20B = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer6_BA20B = [pd.read_excel(i, usecols=[6]) for i in filename_list_BA20A]
        layer1_BA20B_mean = (np.mean((layer1_BA20B)[0]))[0]
        layer2_BA20B_mean = (np.mean((layer2_BA20B)[0]))[0]
        layer3_BA20B_mean = (np.mean((layer3_BA20B)[0]))[0]
        layer4_BA20B_mean = (np.mean((layer4_BA20B)[0]))[0]
        layer5_BA20B_mean = (np.mean((layer5_BA20B)[0]))[0]
        layer6_BA20B_mean = (np.mean((layer6_BA20B)[0]))[0]
        Lall_BA20B_mean = [layer1_BA20B_mean, layer2_BA20B_mean, layer3_BA20B_mean, layer4_BA20B_mean, layer5_BA20B_mean, layer6_BA20B_mean]
        Lall_BA20_all_clean_data_avg_mean = Lall_BA20B_mean
        sum_all_meanL = sum(Lall_BA20_all_clean_data_avg_mean)
        relative_num = [(Lall_BA20_all_clean_data_avg_mean[0]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[1]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[2]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[3]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[4]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[5]/sum_all_meanL)]
    elif BA20B is None:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all.xls"):
                    if case in filename and BA20A in filename:
                        filename_list_BA20A.append(filename)
        layer1_BA20A = [pd.read_excel(i, usecols=[1]) for i in filename_list_BA20A]
        layer2_BA20A = [pd.read_excel(i, usecols=[2]) for i in filename_list_BA20A]
        layer3_BA20A = [pd.read_excel(i, usecols=[3]) for i in filename_list_BA20A]
        layer4_BA20A = [pd.read_excel(i, usecols=[4]) for i in filename_list_BA20A]
        layer5_BA20A = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer5_BA20A = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer6_BA20A = [pd.read_excel(i, usecols=[6]) for i in filename_list_BA20A]
        layer1_BA20A_mean = (np.mean((layer1_BA20A)[0]))[0]
        layer2_BA20A_mean = (np.mean((layer2_BA20A)[0]))[0]
        layer3_BA20A_mean = (np.mean((layer3_BA20A)[0]))[0]
        layer4_BA20A_mean = (np.mean((layer4_BA20A)[0]))[0]
        layer5_BA20A_mean = (np.mean((layer5_BA20A)[0]))[0]
        layer6_BA20A_mean = (np.mean((layer6_BA20A)[0]))[0]
        Lall_BA20A_mean = [layer1_BA20A_mean, layer2_BA20A_mean, layer3_BA20A_mean, layer4_BA20A_mean, layer5_BA20A_mean, layer6_BA20A_mean]
        Lall_BA20_all_clean_data_avg_mean = Lall_BA20A_mean
        sum_all_meanL = sum(Lall_BA20_all_clean_data_avg_mean)
        relative_num = [(Lall_BA20_all_clean_data_avg_mean[0]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[1]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[2]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[3]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[4]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[5]/sum_all_meanL)]
    else:
        for filename in glob.glob(data_files, recursive=True):
            if os.path.isfile(filename):
                if filename.endswith("profile_all.xls"):
                    if case in filename and BA20A in filename:
                        filename_list_BA20A.append(filename)
                    elif case in filename and BA20B in filename:
                        filename_list_BA20B.append(filename)
        #return filename_list_BA20A, filename_list_BA20B
        layer1_BA20A = [pd.read_excel(i, usecols=[1]) for i in filename_list_BA20A]
        layer2_BA20A = [pd.read_excel(i, usecols=[2]) for i in filename_list_BA20A]
        layer3_BA20A = [pd.read_excel(i, usecols=[3]) for i in filename_list_BA20A]
        layer4_BA20A = [pd.read_excel(i, usecols=[4]) for i in filename_list_BA20A]
        layer5_BA20A = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer5_BA20A = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20A]
        layer6_BA20A = [pd.read_excel(i, usecols=[6]) for i in filename_list_BA20A]
        layer1_BA20B = [pd.read_excel(i, usecols=[1]) for i in filename_list_BA20B]
        layer2_BA20B = [pd.read_excel(i, usecols=[2]) for i in filename_list_BA20B]
        layer3_BA20B = [pd.read_excel(i, usecols=[3]) for i in filename_list_BA20B]
        layer4_BA20B = [pd.read_excel(i, usecols=[4]) for i in filename_list_BA20B]
        layer5_BA20B = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20B]
        layer5_BA20B = [pd.read_excel(i, usecols=[5]) for i in filename_list_BA20B]
        layer6_BA20B = [pd.read_excel(i, usecols=[6]) for i in filename_list_BA20B]
        layer1_BA20A_mean = (np.mean((layer1_BA20A)[0]))[0]
        layer2_BA20A_mean = (np.mean((layer2_BA20A)[0]))[0]
        layer3_BA20A_mean = (np.mean((layer3_BA20A)[0]))[0]
        layer4_BA20A_mean = (np.mean((layer4_BA20A)[0]))[0]
        layer5_BA20A_mean = (np.mean((layer5_BA20A)[0]))[0]
        layer6_BA20A_mean = (np.mean((layer6_BA20A)[0]))[0]
        layer1_BA20B_mean = (np.mean((layer1_BA20B)[0]))[0]
        layer2_BA20B_mean = (np.mean((layer2_BA20B)[0]))[0]
        layer3_BA20B_mean = (np.mean((layer3_BA20B)[0]))[0]
        layer4_BA20B_mean = (np.mean((layer4_BA20B)[0]))[0]
        layer5_BA20B_mean = (np.mean((layer5_BA20B)[0]))[0]
        layer6_BA20B_mean = (np.mean((layer6_BA20B)[0]))[0]
        Lall_BA20A_mean = [layer1_BA20A_mean, layer2_BA20A_mean, layer3_BA20A_mean, layer4_BA20A_mean, layer5_BA20A_mean, layer6_BA20A_mean]
        Lall_BA20B_mean = [layer1_BA20B_mean, layer2_BA20B_mean, layer3_BA20B_mean, layer4_BA20B_mean, layer5_BA20B_mean, layer6_BA20B_mean]
        Lall_BA20_all_clean_data_avg_mean = np.mean(np.array([Lall_BA20A_mean, Lall_BA20B_mean]), axis=0)
        sum_all_meanL = sum(Lall_BA20_all_clean_data_avg_mean)
        relative_num = [(Lall_BA20_all_clean_data_avg_mean[0]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[1]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[2]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[3]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[4]/sum_all_meanL), (Lall_BA20_all_clean_data_avg_mean[5]/sum_all_meanL)]
    return relative_num

#Use:
#This function just returns one layer thickness from a list of 6 items.

#Inputs:
# BA_variable - can be a single BA, but I input a list of lists including all cases of one BA
# layer - layer e.g. "L1"
# Outputs: a list of e.g. all of Layer 1 data for BA20A from all cases

def get_ind_layer(BA_variable, layer):
    ind_layer = []
    for list in BA_variable:
        if layer == "L1":
            ind_layer.append(list[0])
            #print(ind_layer)
        elif layer == "L2":
            ind_layer.append(list[1])
        elif layer == "L3":
            ind_layer.append(list[2])
        elif layer == "L4":
            ind_layer.append(list[3])
        elif layer == "L5":
            ind_layer.append(list[4])
        elif layer == "L6":
            ind_layer.append(list[5])
    return ind_layer

#Use - This functions takes the input of a list of averaged data and returns a list of relative data. Specifically a list of 6 values.
def make_relative(Lall_mean_list):
    sum_all_meanL = sum(Lall_mean_list)
    relative_num = [(Lall_mean_list[0]/sum_all_meanL), (Lall_mean_list[1]/sum_all_meanL), (Lall_mean_list[2]/sum_all_meanL), (Lall_mean_list[3]/sum_all_meanL), (Lall_mean_list[4]/sum_all_meanL), (Lall_mean_list[5]/sum_all_meanL)]
    return relative_num


if __name__ == "__main__":

    I42_BA20B_21_avg_Lall_fundus = import_clean_data_avg("I42", "BA20B_21", "fundus")
    print("I42_BA20B_21_avg_Lall_fundus = ", I42_BA20B_21_avg_Lall_fundus)

#sys.exit()
