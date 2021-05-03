"""
Name: Kimberly Nestor
Date: 10/28/2020
Description: Makes a graph simulting percentage change of Bok's equivolue theory.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy as np


# age demog information
age_lst = [63, 86, 43, 80, 45, 84, 73, 68, 58, 82, 49, 67]
mean_age = np.mean(age_lst)
min_age = min(age_lst)
max_age = max(age_lst)
std_age = np.std(age_lst)

# print("""
# mean_age = {}
# min_age = {}
# max_age = {}
# std_age = {}
# """.format(mean_age, min_age, max_age, std_age))
# sys.exit()

# positive percentage change
LAY_ONE_CHANGE = 250
LAY_TWO_CHANGE = 250
LAY_THREE_CHANGE = 250

# negative percentage change
LAY_FOUR_CHANGE = -250
LAY_FIVE_CHANGE = -250
LAY_SIX_CHANGE = -250

lay_lst = [LAY_ONE_CHANGE, LAY_TWO_CHANGE, LAY_THREE_CHANGE, LAY_FOUR_CHANGE, \
LAY_FIVE_CHANGE, LAY_SIX_CHANGE]


#PERCENTAGE CHANGE GRAPH - crown and fundus

bars = lay_lst

#bar position on graph
barWidth = 0.6

r1 = np.arange(len(bars))


plt.bar(r1, bars, color='#964000', edgecolor='white', width=barWidth, alpha=1)
# plt.bar(r1, bars, color='#662d15', edgecolor='white', width=barWidth, alpha=1)
# plt.bar(r1, bars, color='#4d2210', edgecolor='white', width=barWidth, alpha=1)


plt.axhline(y=0, color='#6F6F70', linestyle='solid', linewidth=1)


plt.xticks([r + 0 for r in range(len(bars))] , ['LI','LII', 'LIII', 'LIV', 'LV', 'LVI'], fontsize=13, fontname="serif")
plt.yticks([]) #yaxis points
plt.ylabel('Simulated percentage change thickness', fontname="serif", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('equi_sim_per_change_dpi1000.png', dpi=1000)
plt.savefig('equi_sim_per_change_dpi300.png', dpi=300)
plt.savefig('equi_sim_per_change_dpi100.png')


plt.show()



#
