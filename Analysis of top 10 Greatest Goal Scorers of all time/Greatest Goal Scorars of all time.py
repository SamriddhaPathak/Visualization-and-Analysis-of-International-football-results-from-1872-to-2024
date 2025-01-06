import matplotlib.pyplot as plt
import pandas as pd 
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('Data(file_format_CSV)\Goalscorers.csv')

Goal_Scorers_Data = data['scorer'].dropna().replace('Cristiano Ronaldo', 'Cr.Ronaldo').replace('Robert Lewandowski', 'Lewandowski')                
Goal_Scorers_Data_count = Counter(Goal_Scorers_Data)

Top_Scorers = Goal_Scorers_Data_count.most_common(10)
Top_players = []
Top_scores = []
for items in Top_Scorers:
    Top_players.append(items[0])
    Top_scores.append(items[1])
    
Top_players.reverse()
Top_scores.reverse()
plt.figure(figsize=(20, 15))
plt.barh(Top_players, Top_scores, color='skyblue')
plt.ylabel('Players')
plt.xlabel('Number of Goals Scored')
plt.title('Top 10 Goal Scorers of All Time')
plt.show()
