# Import necessary libraries(:..:)
import matplotlib.pyplot as plt  # For creating visualizations
import pandas as pd  # For handling data in tabular format   
import numpy as np  # For numerical operations
from collections import Counter  # For counting occurrences of elements

# Set a visual style for the plots
plt.style.use("fivethirtyeight")   

# Load the dataset containing goal data
data = pd.read_csv("Data(file_format_CSV)\Goalscorers.csv")

# Extract the 'own_goal' column and convert it into a NumPy array of strings
OwnGoalsData = np.array(data["own_goal"], dtype=str)

# Extract the 'penalty' column and convert it into a NumPy array of strings
Penaltydata = np.array(data["penalty"], dtype=str)

# Count the occurrences of each unique value in 'own_goal' and 'penalty' columns
list_OwnGoalsData = dict(Counter(OwnGoalsData))
list_PenaltyData = dict(Counter(Penaltydata))
 
# Define labels for the pie chart representing own goals vs. scored goals
new_list_OwnGoalsData_check = ['Scored goals', 'Own goals']
 
# Create a list to store the count of each label 
new_list_OwnGoalsData_popn = []
for items in list_OwnGoalsData:
    # Append the counts of each type (e.g., scored goals, own goals)
    new_list_OwnGoalsData_popn.append(list_OwnGoalsData.get(items))
    
# Print the counts for own goals and scored goals for debugging purposes
print(new_list_OwnGoalsData_popn)

# Define labels for the pie chart representing penalty goals vs. non-penalty goals
new_list_PenaltyData_check = ['Non Penalty goals', 'Penalty goals']

# Create a list to store the count of each label
new_list_PenaltyData_popn = []
for items in list_PenaltyData:
    # Append the counts of each type (e.g., non-penalty goals, penalty goals)
    new_list_PenaltyData_popn.append(list_PenaltyData.get(items))
    
# Define the 'explode' parameter to highlight certain sections of the pie chart
# The second section (e.g., 'Own goals' or 'Penalty goals') will be slightly separated
explode = [0, 0.1]

# Create a figure with two subplots to compare the two pie charts
fig, axs = plt.subplots(1, 2, figsize=(22, 15))

# Plot the pie chart for own goals vs. scored goals
axs[0].pie(new_list_OwnGoalsData_popn, 
           labels=new_list_OwnGoalsData_check, 
           explode=explode, 
           autopct='%1.1f%%')  # Show percentages
axs[0].legend(loc='lower left')  # Add a legend in the lower-left corner
axs[0].set_title('Own goals VS scored goals (1872 to 2024)')  # Add a title to the chart

# Plot the pie chart for penalty goals vs. non-penalty goals
axs[1].pie(new_list_PenaltyData_popn, 
           labels=new_list_PenaltyData_check, 
           explode=explode, 
           autopct='%1.1f%%')  # Show percentages
axs[1].legend(loc='lower right')  # Add a legend in the lower-right corner
axs[1].set_title('Penalty goals VS Non Penalty goals (1872 to 2024)')  # Add a title to the chart

# Adjust the layout to prevent overlapping of elements
plt.tight_layout()

# Display the plots
plt.show()
