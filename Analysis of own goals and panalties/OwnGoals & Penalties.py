import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

plt.style.use("fivethirtyeight") 

data = pd.read_csv("Data(file_format_CSV)\Goalscorers.csv")
OwnGoalsData = np.array(data["own_goal"], dtype = str)
Penaltydata = np.array(data["penalty"], dtype = str)

list_OwnGoalsData = dict(Counter(OwnGoalsData))
list_PenaltyData = dict(Counter(Penaltydata))

new_list_OwnGoalsData_check = ['Scored goals', 'Own goals']
new_list_OwnGoalsData_popn = []

for items in list_OwnGoalsData:
    new_list_OwnGoalsData_popn.append(list_OwnGoalsData.get(items))
    
print (new_list_OwnGoalsData_popn)
    
new_list_PenaltyData_check = ['Non Penalty goals', 'Penalty goals']
new_list_PenaltyData_popn = []

for items in list_PenaltyData:
    new_list_PenaltyData_popn.append(list_PenaltyData.get(items))
    
explode = [0, 0.1]

fig, axs = plt.subplots(1, 2, figsize=(22,15))
axs[0].pie(new_list_OwnGoalsData_popn, labels = new_list_OwnGoalsData_check, explode = explode, autopct = '%1.1f%%')
axs[0].legend(loc = 'lower left')
axs[0].set_title('Own goals VS scored goals (1872 to 2024)')

axs[1].pie(new_list_PenaltyData_popn, labels = new_list_PenaltyData_check, explode = explode, autopct = '%1.1f%%')
axs[1].legend(loc = 'lower right')
axs[1].set_title('Penalty goals VS Non Penalty goals (1872 to 2024)')

plt.tight_layout()
plt.show()

