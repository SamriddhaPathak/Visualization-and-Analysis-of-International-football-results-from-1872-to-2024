import matplotlib.pyplot as plt
import pandas as pd 
from collections import Counter

plt.style.use('fivethirtyeight')
data = pd.read_csv('Data(file_format_CSV)\Goalscorers.csv')

home_team = data['home_team']
away_team = data['away_team']

count_nations = Counter(home_team)
count_nations.update(away_team)

Top3_count_nations = count_nations.most_common(4)

countries = [items[0] for items in Top3_count_nations]
scores = [items[1] for items in Top3_count_nations]

fig, axs = plt.subplots(1,2, figsize=(12,24))
explode = [0.06, 0, 0, 0]
axs[0].pie(scores, labels = countries, explode = explode, autopct = "%1.1f%%", shadow = True)
axs[0].legend(loc='upper left')
axs[0].set_title('Top 4 Goal scoring Countries of all Time\nPie Chart')

countries.reverse()
scores.reverse()
axs[1].barh(countries, scores)
axs[1].set_xlabel('No of Goals')
axs[1].set_title('Top 4 Goal scoring Countries of all Time\nBar Chart')

plt.show() 
