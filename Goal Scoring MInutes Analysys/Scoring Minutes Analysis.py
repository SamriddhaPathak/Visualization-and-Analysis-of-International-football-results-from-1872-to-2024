import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv("Data(file_format_CSV)\Goalscorers.csv")
Scoring_Minutes_Data= list((data['minute'].dropna().fillna("No Goals")))

Count_Scoring_Minutes = Counter(Scoring_Minutes_Data)

Top_Scoring_minutes = Count_Scoring_Minutes.most_common(4)
# print (Top_Scoring_minutes)

Scoring_Minutes = [str(items[0]) for items in Top_Scoring_minutes]
No_of_Goals = [items[1] for items in Top_Scoring_minutes]

# print (Scoring_Minutes , No_of_Goals)
fig, axs = plt.subplots(1,2,figsize=(18, 12))
explode = [0.04,0,0,0]

axs[0].pie(No_of_Goals, labels = Scoring_Minutes, explode = explode, autopct = "%1.1f%%")
axs[0].legend(loc = 'lower left')
axs[0].set_title('Top 4 Scoring Minutes of All Time(1872 - 2024)\nPie Chart')

Scoring_Minutes.reverse()
No_of_Goals.reverse()

axs[1].barh(Scoring_Minutes, No_of_Goals , color = 'skyblue')
axs[1].set_title('Top 4 Scoring Minutes of All Time (1872 - 2024)\nBar Chart')
axs[1].set_xlabel("Number of Goals")
axs[1].set_ylabel("Time of Goal")

plt.show()
